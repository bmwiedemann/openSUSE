#
# spec file for package lxqt-build-tools-qt5
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
Name:           lxqt-build-tools-qt5
Version:        0.13.0
Release:        0
Summary:        Core build tools for LXQt
License:        BSD-3-Clause
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz.asc
BuildRequires:  cmake >= 3.5.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildArch:      noarch

%description
This package provides several tools needed to build LXQt itself as well as other components maintained by the LXQt project.

%package devel
Summary:        Tools for building lxqt
Requires:       cmake(Qt5Core)
Conflicts:      lxqt-build-tools-devel

%description devel
This package provides several tools needed to build compatibility for Qt5 applications within LXQt 2.0


%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc AUTHORS CHANGELOG README.md
%license BSD-3-Clause
%{_datadir}/cmake/
%{_bindir}/lxqt-transupdate

%changelog
