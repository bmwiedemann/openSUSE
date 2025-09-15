#
# spec file for package avr-libc
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define into_sysroot 1
%define doc_vers 2.2.0
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
Version:        2.2.1
Release:        0
Summary:        The C Runtime Library for AVR Microcontrollers
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://savannah.nongnu.org/projects/avr-libc
Source:         https://github.com/avrdudes/avr-libc/releases/download/%{name}-2_2_1-release/%{name}-%{version}.tar.bz2
Source1:        https://github.com/avrdudes/avr-libc/releases/download/%{name}-2_2_1-release/%{name}-%{version}.tar.bz2.sig
Source4:        https://avrdudes.github.io/avr-libc/%{name}-user-manual-%{doc_vers}.tar.bz2
Source6:        https://avrdudes.github.io/avr-libc/%{name}-user-manual-%{doc_vers}.pdf
# from http://pgp.mit.edu/pks/lookup?op=vindex&search=0x7E9EADC3030D34EB (Joerg Wunsch)
Source8:        %{name}.keyring
# from ?? - poor man's logic analyzer by 'jw'
Source9:        logicp-1.02.tgz
Source100:      %{name}-rpmlintrc
Patch0:         0001-Return-files-missed-in-the-release-tarball.patch
Patch1:         0002-dox_latex_header.tex-Add-to-EXTRA_DIST-969-1023.patch
Patch2:         0003-dox-api-Makefile.am-EXTRA_DIST-Add-filter-dox.sh-avr.patch
# required for ./bootstrap
BuildRequires:  autoconf
# required for ./bootstrap
BuildRequires:  automake
BuildRequires:  cross-avr-binutils
BuildRequires:  cross-avr-gcc%{gcc_version}-bootstrap
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  ghostscript
# required for autosetup -S git
BuildRequires:  git
BuildRequires:  netpbm
# required for ./bootstrap
BuildRequires:  python3
BuildRequires:  transfig
Recommends:     avr-example
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# does not depend on host arch. bnc#233520
BuildArch:      noarch

%description
The C runtime library for the AVR family of microcontrollers for use
with the GNU toolset (cross-avr-binutils, cross-avr-gcc, uisp, etc.).

%prep
# -S git is a workaround for:
# File avr-libc-logo-large.png: git binary diffs are not supported.
%autosetup -a4 -b9 -S git
cp -a %{SOURCE6} .

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# required for 0002-dox_latex_header.tex-Add-to-EXTRA_DIST-969-1023.patch
#          and 0003-dox-api-Makefile.am-EXTRA_DIST-Add-filter-dox.sh-avr.patch
./bootstrap
CC="avr-gcc-%{gcc_version}" ./configure --prefix=%{PREFIX} --host=avr --mandir=%{PREFIX}/man
make %{?_smp_mflags} CC="avr-gcc-%{gcc_version} -pipe" CCAS="avr-gcc-%{gcc_version} -pipe"
# dox-html target builds man pages
make %{?_smp_mflags} CC="avr-gcc-%{gcc_version}" -C doc/api dox-html

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
make -C doc/api DESTDIR=%{buildroot} install-dox-man %{?_smp_mflags}

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pr AUTHORS LICENSE NEWS README.md *.pdf %{buildroot}%{_docdir}/%{name}
cp -pr %{name}-user-manual-%{doc_vers} %{buildroot}%{_docdir}/%{name}/user-manual-%{doc_vers}
ln -s %{_docdir}/%{name}/user-manual-%{doc_vers} %{buildroot}/%{PREFIX}/share/doc/%{name}-%{version}/user-manual
ln -s %{PREFIX}/share/doc/%{name}-%{version}/examples %{buildroot}%{_docdir}/%{name}
cat >> %{buildroot}%{_docdir}/%{name}/user-manual.html <<EOF
<head><meta http-equiv="Refresh" content="0; user-manual-%{doc_vers}/index.html"></head>
<a href="user-manual-%{doc_vers}/pages.html">user-manual-%{doc_vers}/index.html</a>
EOF

mv %{buildroot}/%{PREFIX}/avr/* %{buildroot}/%{PREFIX}/
rm -Rf %{buildroot}/%{PREFIX}/avr

# do not run brp-strip-debug on our avr-elf objects.
export NO_BRP_STRIP_DEBUG=true

%fdupes %{buildroot}/%{PREFIX}
%fdupes -s %{buildroot}%{_docdir}/%{name}

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
