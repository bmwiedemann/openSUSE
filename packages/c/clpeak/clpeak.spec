#
# spec file for package clpeak
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2015-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           clpeak
Version:        1.1.1
Release:        0
Summary:        Find peak OpenCL capacities like bandwidth & compute
License:        SUSE-Public-Domain
Group:          System/Benchmark
URL:            https://github.com/krrishnarraj/clpeak
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(gl)

%description
A tool which profiles OpenCL devices to find their peak capacities like
bandwidth & compute.

%prep
%autosetup

%build
%cmake \
  -Wno-dev
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/%{name}

%check
%ctest

%files
%license LICENSE
%doc README.md results
%{_bindir}/%{name}

%changelog
