#
# spec file for package lxqt2-build-tools
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

%define _name lxqt-build-tools
Name:           lxqt2-build-tools
Version:        2.0.0
Release:        0
Summary:        Core build tools for LXQt
License:        BSD-3-Clause
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz.asc
BuildRequires:  cmake >= 3.5.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= 6.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildArch:      noarch

%description
This package provides several tools needed to build LXQt itself as well as other components maintained by the LXQt project.

%package devel
Summary:        Tools for building lxqt
Requires:       cmake(Qt6Core)

%description devel
This package provides several tools needed to build LXQt itself as well as other components maintained by the LXQt project.

These tools used to be spread over the repositories of various other components and were summarized to ease dependency management. So far many components, in particular [liblxqt](https://github.com/lxde/liblxqt), were representing a build dependency without being needed themselves but only because their repository was providing a subset of the tools which are now summarized here. So the use of this repository will reduce superfluous and bloated dependencies.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%files devel
%doc AUTHORS CHANGELOG README.md
%license BSD-3-Clause
%{_datadir}/cmake/
%{_bindir}/lxqt2-transupdate

%changelog
