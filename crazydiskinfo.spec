#
# spec file for package crazydiskinfo
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


Name:           crazydiskinfo
Version:        1.1.0
Release:        0
Summary:        An interactive TUI S.M.A.R.T viewer
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/otakuto/crazydiskinfo
#Git-Clone:     https://github.com/otakuto/crazydiskinfo.git
Source:         https://github.com/otakuto/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         crazydiskinfo-obey-cflags.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libatasmart-devel
BuildRequires:  ncurses-devel

%description
CrazyDiskInfo is an interactive TUI S.M.A.R.T viewer.
It offers the following features:

 * An UI similar to CrystalDiskInfo.
 * Health and temperature checking algorithms based on CrystalDiskInfo.

%prep
%autosetup -p1

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%{_sbindir}/crazydiskinfo

%changelog
