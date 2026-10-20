#
# spec file for package xpumanager
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           xpumanager
Version:        2.3.0
Release:        0
Summary:        Intel data center GPU monitoring utility
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/intel/xpumanager
Source0:        https://github.com/intel/xpumanager/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  grpc-devel
BuildRequires:  igsc >= 1.2.0
BuildRequires:  igsc-devel
BuildRequires:  intel-metee-devel
BuildRequires:  meson
BuildRequires:  openSUSE-release
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(CLI11)
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(level-zero)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(libudev)
# The tools already need libze_loader.so.1, which suggests requiring a
# particular back-end at the rpm level is moot
#Requires:       libze_intel_gpu1

%description
Intel XPU Manager is a tool for monitoring and managing Intel Data
Center GPUs. It is supposed to improve device utilization. The XPU
System Management Interface (XPU-SMI) is a command line interface to
manage GPUs.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%fdupes %{buildroot}/%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/xpu-smi
%dir %{_datadir}/xpum
%dir %{_datadir}/xpum/resources
%dir %{_datadir}/xpum/resources/config
%{_datadir}/xpum/resources/config/device_thresholds.json
%{_datadir}/xpum/resources/config/pci.conf
%{_datadir}/xpum/resources/config/pci.ids

%changelog
