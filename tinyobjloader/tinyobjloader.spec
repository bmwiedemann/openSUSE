#
# spec file for package tinyobjloader
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
%define lname   libtinyobjloader%{sover}
Name:           tinyobjloader
Version:        1.0.6
Release:        0
Summary:        Wavefront .obj file loader
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/syoyo/tinyobjloader
Source:         https://github.com/syoyo/tinyobjloader/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         tinyobjloader-fix-cmake-path.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
A single-file Wavefront .obj loader written in C++.
It can parse over 10M polygons with moderate memory and time.

%package -n %{lname}
Summary:        Wavefront .obj file loader
Group:          System/Libraries

%description -n %{lname}
A single-file Wavefront .obj loader written in C++.
It can parse over 10M polygons with moderate memory and time.

%package devel
Summary:        Development files for tinyobjloader
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
A single-file Wavefront .obj file loader written in C++.
No dependency except for C++ STL. It can parse over 10M polygons with
moderate memory and time.

This subpackage contains libraries and header files for developing
applications that want to make use of tinyobjloader.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DTINYOBJLOADER_COMPILATION_SHARED=ON
%make_jobs

%install
%cmake_install
rm -f %{buildroot}/%{_datadir}/doc/tinyobjloader/LICENSE

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc README.md
%{_libdir}/libtinyobjloader.so.%{sover}*

%files devel
%{_includedir}/tiny_obj_loader.h
%{_libdir}/libtinyobjloader.so
%{_libdir}/pkgconfig/tinyobjloader.pc
%{_libdir}/cmake/tinyobjloader-*.cmake

%changelog
