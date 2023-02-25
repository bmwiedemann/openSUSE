#
# spec file for package libcbor-doc
#
# Copyright (c) 2023 SUSE LLC
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


%define socurrent  0
%define sorevision 10
%define soage      2
%define lname   libcbor%{socurrent}_%{sorevision}
%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "doc"
# in 15sp4/sp5, the doc fails to build with an assert in sphinx
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} <= 150500
%define build_man 0
%else
%define build_man 1
%endif
%else
%define build_man 0
%endif

%if "%{flavor}" == "doc"
Name:           libcbor-doc
%else
Name:           libcbor
%endif
Version:        0.10.2
Release:        0
Summary:        Library for parsing Concise Binary Object Representation (CBOR)
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/PJK/libcbor
Source0:        https://github.com/PJK/libcbor/archive/v%{version}.tar.gz
Source1:        libcbor.3
%if %{build_man}
BuildRequires:  doxygen
BuildRequires:  python3-Sphinx
BuildRequires:  python3-breathe
%else
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcmocka-devel
BuildRequires:  ninja
%endif

%description
libcbor is a C99 library for parsing and generating CBOR (RFC 7049),
a general-purpose schema-less binary data format.

It supports flexible memory management, UTF-8, streams & incremental
processing, and has a layered architecture.

%package -n %{lname}
Summary:        Library for parsing Concise Binary Object Representation (CBOR)
Group:          System/Libraries

%description -n %{lname}
libcbor is a C99 library for parsing and generating CBOR (RFC 7049),
a general-purpose schema-less binary data format.

It supports flexible memory management, UTF-8, streams & incremental
processing, and has a layered architecture.

%package        devel
Summary:        Development files for libcbor
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libcbor is a C library for parsing and generating CBOR.
The libcbor-devel contains libraries and header files for libcbor.

%prep
%autosetup -n libcbor-%{version}
sed -i 's|${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/pkgconfig|${CMAKE_INSTALL_LIBDIR}/pkgconfig|' src/CMakeLists.txt

%build
export CFLAGS="%(echo %{optflags}) -Wno-return-type"
export CXXFLAGS="$CFLAGS"
%if %{build_man}
%make_build -C doc man
%else

%define __builder ninja
%cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_TESTS=ON
%cmake_build
%endif

%install
%if "%{flavor}" == "doc"

mkdir -p %{buildroot}%{_mandir}/man3
%if %{build_man}
cp doc/build/man/*.3 %{buildroot}%{_mandir}/man3
%else
cp %{SOURCE1} %{buildroot}%{_mandir}/man3
%endif

%else

%cmake_install
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if "%{flavor}" == "doc"
%files
%doc CHANGELOG.md README.md
%{_mandir}/*/*

%else

%files -n %{lname}
%license LICENSE.md
%{_libdir}/libcbor.so.%{socurrent}.%{sorevision}
%{_libdir}/libcbor.so.%{socurrent}.%{sorevision}.%{soage}

%files devel
%{_includedir}/cbor.h
%dir %{_includedir}/cbor
%{_includedir}/cbor/*.h
%dir %{_includedir}/cbor/internal
%{_includedir}/cbor/internal/*.h
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc
%endif

%changelog
