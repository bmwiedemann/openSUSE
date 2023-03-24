#
# spec file for package xmrig
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


Name:           xmrig
Version:        6.19.1
Release:        0
Summary:        XMR mining application
License:        GPL-3.0-only
URL:            https://xmrig.com/
Source0:        %{name}-%{version}.tar.gz
Source1:        xmrig.service
#PATCH-FIX-SUSE correct-opencl-file.patch nopeinomicon@posteo.net -- Sets correct location/name for libOpenCL.so.1 used for OpenCL mode
Patch1:         correct-opencl-file.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libuv-devel
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Recommends:     libOpenCL1
%{?systemd_ordering}

%description
Open source CPU/GPU XMR cryptocurrency miner.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake -Wno-dev
%cmake_build

%install
install -D -m 0755 build/xmrig %{buildroot}%{_bindir}/xmrig
install -D -m 0644 src/config.json %{buildroot}%{_sysconfdir}/xmrig/xmrig.conf
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xmrig@.service

%files
%doc README.md CHANGELOG.md scripts
%license LICENSE
%dir %{_sysconfdir}/xmrig
%config %{_sysconfdir}/xmrig/xmrig.conf
%{_bindir}/xmrig
%{_unitdir}/xmrig@.service

%changelog
