#
# spec file for package foma
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname	libfoma0
Name:           foma
Version:        0.9.18+git20180511.bad2f09
Release:        0
Summary:        Finite-state compiler and C library
License:        Apache-2.0
Group:          Productivity/Text/Utilities
URL:            https://fomafst.github.io/
# Source must be from git tarball has different license than git, no idea why
Source0:        foma-%{version}.tar.xz
Patch0:         foma-harden-build.patch
Patch1:         foma-fix-sizeof.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(zlib)

%description
Foma is a compiler, programming language, and C library for constructing
finite-state automata and transducers for various uses. It has specific
support for many natural language processing applications such as producing
morphological analyzers. Although NLP applications are probably the main
use of foma, it is sufficiently generic to use for a large number of purposes.

%package -n %{libname}
Summary:        Finite-state C library
Group:          System/Libraries

%description -n %{libname}
The library contains efficient implementations of all classical
automata/transducer algorithms: determinization, minimization,
epsilon-removal, composition, boolean operations. Also, more
advanced construction methods are available: context restriction,
quotients, first-order regular logic, transducers from replacement
rules, etc.

%package devel
Summary:        Finite-state C library development files and headers
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Finite-state C library development files and headers for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p2
%patch1 -p2
sed -i '/^CFLAGS/c\CFLAGS = %{optflags} -Wl,--as-needed -D_GNU_SOURCE -std=c99 -fvisibility=hidden -fPIC' Makefile
sed -i '/^LDFLAGS/c\LDFLAGS = -lreadline -lz -lreadline -fpic' Makefile
sed -i '/^FLOOKUPLDFLAGS/c\FLOOKUPLDFLAGS = libfoma.a -lz -fpic' Makefile

%build
# hand written Makefile that gets to be quite PITA
make -j1

%install
%make_install \
	prefix=%{buildroot}%{_prefix} \
	libdir=%{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libdir}/*.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/cgflookup
%{_bindir}/flookup
%{_bindir}/foma

%files devel
%{_includedir}/fomalib.h
%{_includedir}/fomalibconf.h
%{_libdir}/libfoma.so

%files -n %{libname}
%license COPYING
%{_libdir}/libfoma.so.*

%changelog
