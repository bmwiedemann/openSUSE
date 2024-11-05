#
# spec file for package mfgtools
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


Name:           mfgtools
Version:        1.5.191.0
Release:        0
Summary:        Freescale/NXP I.MX Chip image deploy tools
License:        BSD-3-Clause
Group:          System/Management
URL:            https://github.com/NXPmicro/mfgtools.git
Source0:        %{name}-%{version}.tar
Patch0:         mfgtools-gcc13.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libzip-devel
BuildRequires:  libzstd-devel
BuildRequires:  pkg-config
BuildRequires:  tinyxml2-devel
BuildRequires:  zlib-devel

%description
Freescale/NXP I.MX Chip image deploy tools. This package holds the evolution of MFGTools (aka MFGTools v3), which is called the UUU (Universal Update Utility).

%prep
%autosetup -p1

%build
echo uuu_%{version} > .tarball-version
cmake .
make

%install
mkdir -p %{buildroot}%{_bindir}
install uuu/uuu %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/uuu

%changelog
