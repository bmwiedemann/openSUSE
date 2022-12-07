#
# spec file for package libcerf
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Christoph Junghans <junghans@votca.org>
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


Name:           libcerf
Version:        2.2
Release:        0
Summary:        A library that complex error functions
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://jugit.fz-juelich.de/mlz/libcerf
Source0:        https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix_return.patch fix return value in one function
Patch1:         fix_return.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig

%description
libcerf is a self-contained numeric library that provides an efficient and
accurate implementation of complex error functions, along with Dawson,
Faddeeva, and Voigt functions.

%package -n libcerf2
Summary:        A library that provides complex error functions
Group:          Development/Libraries/C and C++

%description -n libcerf2
libcerf is a self-contained numeric library that provides an efficient and
accurate implementation of complex error functions, along with Dawson,
Faddeeva, and Voigt functions.

%package devel
Summary:        Development headers and libraries for libcerf
Group:          Development/Libraries/C and C++
Requires:       libcerf2 = %{version}-%{release}

%description devel
libcerf is a self-contained numeric library that provides an efficient and
accurate implementation of complex error functions, along with Dawson,
Faddeeva, and Voigt functions.

This package contains development headers and libraries for libcerf

%prep
%setup -q -n %{name}-v%{version}
%patch1
# Force cmake to use the paths passed at configure time
sed -i -e 's|lib/pkgconfig/|%{_lib}/pkgconfig/|' CMakeLists.txt
sed -i -e 's|DESTINATION lib|DESTINATION %{_lib}|' lib/CMakeLists.txt
sed -i -e 's|${prefix}/lib|@LIB_INSTALL_DIR@|' libcerf.pc.in

%build
%cmake -DCMAKE_SKIP_RPATH=OFF
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/cerf/* %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_prefix}

%post -n libcerf2 -p /sbin/ldconfig
%postun -n libcerf2 -p /sbin/ldconfig

%check
%ctest

%files -n libcerf2
%license LICENSE
%{_libdir}/libcerf.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libcerf.so
%{_libdir}/pkgconfig/libcerf.pc
%{_mandir}/man3/*
%{_docdir}/%{name}
%{_libdir}/cmake/cerf

%changelog
