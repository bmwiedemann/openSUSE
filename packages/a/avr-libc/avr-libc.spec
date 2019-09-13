#
# spec file for package avr-libc
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define into_sysroot 1
%define doc_vers %{version}
%if %{into_sysroot}
%define PREFIX /usr/avr/sys-root
%else
# FIXME:
# okay, FHS 2.2, if you forbid the obvious choices, can you also suggest a better place?
# avr-libc: "/usr/avr/{include,lib,...}" is not allowed anymore in FHS 2.2
# avr-libc: "/usr/local/avr/{include,lib,...}" is not allowed anymore in FHS 2.2
%define PREFIX %{_prefix}
%define PREFIX %{_prefix}/local
%endif

%{!?gcc_version: %define gcc_version 7}

Name:           avr-libc
Version:        2.0.0
Release:        0
Summary:        The C Runtime Library for AVR Microcontrollers
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://savannah.nongnu.org/projects/avr-libc
Source:         http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        http://savannah.nongnu.org/download/%{name}/%{name}-manpages-%{doc_vers}.tar.bz2
Source3:        http://savannah.nongnu.org/download/%{name}/%{name}-manpages-%{doc_vers}.tar.bz2.sig
Source4:        http://savannah.nongnu.org/download/%{name}/%{name}-user-manual-%{doc_vers}.tar.bz2
Source5:        http://savannah.nongnu.org/download/%{name}/%{name}-user-manual-%{doc_vers}.tar.bz2.sig
Source6:        http://savannah.nongnu.org/download/%{name}/%{name}-user-manual-%{doc_vers}.pdf.bz2
Source7:        http://savannah.nongnu.org/download/%{name}/%{name}-user-manual-%{doc_vers}.pdf.bz2.sig
Source8:        %{name}.keyring
Source9:        logicp-1.02.tgz
Source100:      %{name}-rpmlintrc
BuildRequires:  cross-avr-binutils
BuildRequires:  cross-avr-gcc%{gcc_version}-bootstrap
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  netpbm
Recommends:     avr-example
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# does not depend on host arch. bnc#233520
BuildArch:      noarch
%if 0%{?suse_version} < 1100
BuildRequires:  libgmp3
BuildRequires:  libmpfr1
%endif

%description
The C runtime library for the AVR family of microcontrollers for use
with the GNU toolset (cross-avr-binutils, cross-avr-gcc, uisp, etc.).

%prep
%setup -q -a2 -a4 -b9
cp -a %{SOURCE6} .
bunzip2 %{name}-user-manual-%{doc_vers}.pdf.bz2

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./configure --prefix=%{PREFIX} --host=avr
make %{?_smp_mflags} CC="avr-gcc -pipe" CCAS="avr-gcc -pipe"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pr AUTHORS ChangeLog* LICENSE NEWS README *.pdf %{buildroot}%{_docdir}/%{name}
cp -pr %{name}-user-manual-%{doc_vers} %{buildroot}%{_docdir}/%{name}/user-manual-%{doc_vers}
ln -s %{_docdir}/%{name}/user-manual-%{doc_vers} %{buildroot}/%{PREFIX}/share/doc/%{name}-%{version}/user-manual
ln -s %{PREFIX}/share/doc/%{name}-%{version}/examples %{buildroot}%{_docdir}/%{name}
cat >> %{buildroot}%{_docdir}/%{name}/user-manual.html <<EOF
<head><meta http-equiv="Refresh" content="0; user-manual-%{doc_vers}/index.html"></head>
<a href="user-manual-%{doc_vers}/pages.html">user-manual-%{doc_vers}/index.html</a>
EOF

mv %{buildroot}/%{PREFIX}/avr/* %{buildroot}/%{PREFIX}/
rm -Rf %{buildroot}/%{PREFIX}/avr

mkdir -p %{buildroot}/%{PREFIX}/
cp -pr man %{buildroot}/%{PREFIX}/.

# do not run brp-strip-debug on our avr-elf objects.
export NO_BRP_STRIP_DEBUG=true

%fdupes %{buildroot}

%check
### selftest ###
cd ../logicp*
## how do we tell the linker that crt*.o is at a nonstandard location?
ln -s $RPM_BUILD_ROOT%PREFIX/lib/crtatt*.o .
ln -s $RPM_BUILD_ROOT%PREFIX/lib/avrtiny/crtatt*.o .
ln -s $RPM_BUILD_ROOT%PREFIX/lib/avr?/crtatm*.o .
make test CFLAGS="-Wall -g -Os -mint8 -I$RPM_BUILD_ROOT%PREFIX/include/ -L$RPM_BUILD_ROOT%PREFIX/lib/avr4" CPU=mega8 || true
make test CFLAGS="-Wall -g -Os -mint8 -I$RPM_BUILD_ROOT%PREFIX/include/ -L$RPM_BUILD_ROOT%PREFIX/lib/avr4" CPU=mega48 || true
make test CFLAGS="-Wall -g -Os -mint8 -I$RPM_BUILD_ROOT%PREFIX/include/ -L$RPM_BUILD_ROOT%PREFIX/lib/avr4" CPU=mega644 || true
make test CFLAGS="-Wall -g -Os -mint8 -I$RPM_BUILD_ROOT%PREFIX/include/ -L$RPM_BUILD_ROOT%PREFIX/lib"      CPU=tiny2313 || true
make test CFLAGS="-Wall -g -Os -mint8 -I$RPM_BUILD_ROOT%PREFIX/include/ -L$RPM_BUILD_ROOT%PREFIX/lib"      CPU=tiny4313 || true

%files
%defattr (-, root, root)
%doc %{_docdir}/%{name}
%if %{into_sysroot}
%dir %{PREFIX}
%{PREFIX}/*
%else
%{_prefix}/*
%endif
# %%doc /usr/share/man/man?/*.*

%changelog
