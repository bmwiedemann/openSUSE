#
# spec file for package foma
#
# Copyright (c) 2024 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define libname	libfoma0
Name:           foma
Version:        0.10.0+git22
Release:        0
Summary:        Finite-state compiler and C library
License:        Apache-2.0
URL:            https://fomafst.github.io/
Source:         foma-%version.tar.xz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(zlib)

%description
Foma is a compiler, programming language, and C library for constructing
finite-state automata and transducers for various uses. It has specific support
for many natural language processing applications such as producing
morphological analyzers. Although NLP applications are probably the main use of
foma, it is sufficiently generic to use for a large number of purposes.

%package -n %{libname}
Summary:        Finite-state C library

%description -n %{libname}
The library contains efficient implementations of all classical
automata/transducer algorithms: determinization, minimization, epsilon-removal,
composition, boolean operations. Also, more advanced construction methods are
available: context restriction, quotients, first-order regular logic,
transducers from replacement rules, etc.

%package devel
Summary:        Finite-state C library development files and headers
Requires:       %{libname} = %{version}

%description devel
Finite-state C library development files and headers for %{name}.

%prep
%autosetup -p1

%build
pushd foma/
%cmake
%cmake_build
popd

%install
pushd foma/
%cmake_install
popd
find "%buildroot" -type f -name "*.a" -print -delete

%ldconfig_scriptlets -n %libname

%files
%{_bindir}/cgflookup
%{_bindir}/flookup
%{_bindir}/foma

%files devel
%{_includedir}/fomalib.h
%{_includedir}/fomalibconf.h
%{_libdir}/libfoma.so
%{_libdir}/pkgconfig/libfoma.pc

%files -n %{libname}
%license foma/COPYING
%{_libdir}/libfoma.so.*

%changelog
