#
# spec file for package libcbor
#
# Copyright (c) 2020 SUSE LLC
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
%define sorevision 8
%define soage      0

%define lname   libcbor%{socurrent}_%{sorevision}

Name:           libcbor
Version:        0.8.0
Release:        0
Summary:        Library for parsing Concise Binary Object Representation (CBOR)
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://libcbor.org
Source0:        https://github.com/PJK/libcbor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libcmocka-devel
BuildRequires:  ninja
BuildRequires:  python3-Sphinx
BuildRequires:  python3-breathe
BuildRequires:  valgrind

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
%autosetup
sed -i 's|${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/pkgconfig|${CMAKE_INSTALL_LIBDIR}/pkgconfig|' src/CMakeLists.txt

%build
make %{?_smp_mflags} -C doc man

%define __builder ninja
%cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_TESTS=ON
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_mandir}/man1
cp doc/build/man/* %{buildroot}%{_mandir}/man1

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_mandir}/*/*
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

%changelog
