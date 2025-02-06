#
# spec file for package opencl-cpp-headers
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Aaron Puchert.
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


Name:           opencl-cpp-headers
Version:        2024.10.24
Release:        0
Summary:        OpenCL C++ headers
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.khronos.org/registry/OpenCL/
Source:         https://github.com/KhronosGroup/OpenCL-CLHPP/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  findutils
BuildRequires:  gcc-c++
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(OpenCL-Headers)
%else
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
%endif
Requires:       opencl-headers
Conflicts:      opencl-headers-1_2
BuildArch:      noarch

%description
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides the official C++ headers for OpenCL, which are wrappers
around the C headers.

%prep
%autosetup -n OpenCL-CLHPP-%{version}

%build
# Fix line endings
find -type f -exec dos2unix {} \;

%cmake -DBUILD_DOCS=OFF -DBUILD_EXAMPLES=OFF -DBUILD_TESTING=OFF

%cmake_build

%install
%cmake_install

%files
%dir %{_includedir}/CL
%{_includedir}/CL/cl2.hpp
%{_includedir}/CL/opencl.hpp
%{_datadir}/cmake/OpenCLHeadersCpp/
%{_datadir}/pkgconfig/OpenCL-CLHPP.pc

%changelog
