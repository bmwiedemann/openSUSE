#
# spec file for package pcc
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Guido Berhoerster.
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

%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

Name:           pcc
Version:        1.0.0
Release:        0
Summary:        Portable and Fast C Compiler
License:        BSD-4-Clause
Group:          Development/Languages/C and C++
Url:            http://pcc.ludd.ltu.se/
Source0:        pcc-%{version}.tar.bz2
Source1:        pcc-libs-%{version}.tar.bz2
Source100:      pcc-rpmlintrc
Patch0:         pcc-1.0.0-fix-missing-headers.patch
Patch1:         pcc-1.0.0-do-not-hardcode-cflags.patch
Patch2:         pcc-1.0.0-fix-ctor-dtor-not-emitted.patch
Patch3:         pcc-1.0.0-disable-stack-protector.patch
Patch4:         pcc-1.0.0-fix-undefined-expressions.patch
Patch5:         pcc-1.0.0-do-not-include-user-hostname.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
# PPC support is broken: http://thread.gmane.org/gmane.comp.compilers.pcc/2391
# ARM support is broken: armv7l is not (yet) supported by pcc-libs
ExclusiveArch:  %ix86 x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Portable C Compiler is a C99 compiler which aims to be small, simple, fast
and understandable. It is based on the original Portable C Compiler written by
S. C. Johnson in the late 70's although large parts of the codebase have been
rewritten.

%prep
%setup -q -a1
cd pcc-libs-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
cd ..
%patch4 -p1
%patch5 -p1

%build
cd pcc-libs-%{version}
%configure --libexecdir=%{_libexecdir}/%{name}
# there is a race condition breaking parallel build
make 
cd ..
autoreconf -fi
%configure \
    --libexecdir=%{_libexecdir}/%{name} \
    --enable-tls
# there is a race condition breaking parallel build
make

%install
cd pcc-libs-%{version}
%makeinstall strip=no
cd ..
%makeinstall strip=no

# avoid conflicts with gcc
ln -s %{_libexecdir}/%{name}/cpp \
    %{buildroot}%{_bindir}/pcc-cpp
mv %{buildroot}%{_mandir}/man1/cpp.1 %{buildroot}%{_mandir}/man1/pcc-cpp.1
%fdupes %{buildroot}%{_libdir}/pcc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/pcc
%{_bindir}/pcc-cpp
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/ccom
%{_libexecdir}/%{name}/cpp
%{_libdir}/%{name}
%attr(644,root,root) %{_mandir}/man1/ccom.1*
%attr(644,root,root) %{_mandir}/man1/pcc-cpp.1*
%attr(644,root,root) %{_mandir}/man1/pcc.1*

%changelog
