#
# spec file for package opencl-cpp-headers
#
# Copyright (c) 2017 Aaron Puchert.
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


Name:           opencl-cpp-headers
Version:        2.0.10
Release:        0
Summary:        OpenCL C++ headers
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://www.khronos.org/registry/OpenCL/
Source:         https://github.com/KhronosGroup/OpenCL-CLHPP/archive/v%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  findutils
BuildRequires:  python
Conflicts:      opencl-headers-1_2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       opencl-headers

%description
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides the official C++ headers for OpenCL, which are wrappers
around the C headers.

%prep
%setup -q -n OpenCL-CLHPP-%{version}

%build
# Fix line endings
find -type f -print0 | xargs -0 dos2unix

# Build cl.hpp from input_cl.hpp
./gen_cl_hpp.py

%install
install -d -m 0755 %{buildroot}%{_includedir}/CL
install -p -m 0644 cl.hpp %{buildroot}%{_includedir}/CL
install -p -m 0644 input_cl2.hpp %{buildroot}%{_includedir}/CL/cl2.hpp

%files
%defattr(-,root,root)
%dir %{_includedir}/CL
%{_includedir}/CL/*.hpp

%changelog
