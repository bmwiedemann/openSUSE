#
# spec file for package lxqt-menu-data
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


%global debug_package %{nil}
Name:           lxqt-menu-data
Version:        2.2.0
Release:        0
Summary:        Menu files for LXQt Panel, Configuration Center and PCManFM-Qt
License:        LGPL-2.1-or-later
URL:            https://github.com/lxqt/lxqt-menu-data
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch1:         001-lxqt-applications-menu-2.0.0.patch
BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools)
BuildArch:      noarch

%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration Center
and PCManFM-Qt/libfm-qt.

%package devel
Summary:        Tools for building lxqt-panel, lxqt-config, libfm-qt
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description devel
This package provides several tools needed to build other components
maintained by the LXQt project.

%prep
%autosetup -p1
sed -i 's/\(Icon=\).*/\1applications-utilities/' ./menu/desktop-directories/lxqt-utility.directory.in

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/lxqt-*.menu
%dir %{_datadir}/desktop-directories/
%{_datadir}/desktop-directories/lxqt-*.directory
%license LICENSE

%files devel
%{_datadir}/cmake/%{name}/

%changelog
