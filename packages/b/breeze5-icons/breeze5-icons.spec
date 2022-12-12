#
# spec file for package breeze5-icons
#
# Copyright (c) 2021 SUSE LLC
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           breeze5-icons
Version:        5.101.0
Release:        0
Summary:        Breeze icon theme
License:        LGPL-3.0-only
URL:            https://www.kde.org
Source:         breeze-icons-%{version}.tar.xz
%if %{with released}
Source1:        breeze-icons-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  python3
BuildRequires:  python3-lxml
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildArch:      noarch

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%package rcc
Summary:        Breeze icon theme - rcc file

%description rcc
Breeze-icons is a freedesktop.org compatible icon theme.
This contains the Breeze (non-dark) icons in a QResource file, used by Kexi.

%prep
%autosetup -p1 -n breeze-icons-%{version}

%build
# For some reason Kexi only wants to use breeze-icons.rcc and not the icons directory,
# so build it just for that.
%cmake_kf5 -d build -- -DBINARY_ICONS_RESOURCE=ON
%cmake_build

%install
%kf5_makeinstall -C build

# yast2-theme uses these, but it got renamed in 5.55.0
ln -s yast-software-group.svg %{buildroot}%{_kf5_iconsdir}/breeze/preferences/32/yast-software.svg
# FIXME: No longer there, but should be present anyway due to breeze-dark inheriting breeze
# Remove after testing
# ln -s yast-software-group.svg %%{buildroot}%%{_kf5_iconsdir}/breeze-dark/preferences/32/yast-software.svg

%fdupes %{buildroot}%{_kf5_iconsdir}

%icon_theme_cache_create_ghost breeze
%icon_theme_cache_create_ghost breeze-dark

%post
%icon_theme_cache_post breeze
%icon_theme_cache_post breeze-dark

%files
%license COPYING*
%ghost %{_kf5_iconsdir}/breeze/icon-theme.cache
%ghost %{_kf5_iconsdir}/breeze-dark/icon-theme.cache
%exclude %{_kf5_iconsdir}/breeze/breeze-icons.rcc
%exclude %{_kf5_iconsdir}/breeze-dark/breeze-icons-dark.rcc
%{_kf5_iconsdir}/breeze/
%{_kf5_iconsdir}/breeze-dark/

%files rcc
%dir %{_kf5_iconsdir}/breeze
# Kexi does not need the -dark variant.
%{_kf5_iconsdir}/breeze/breeze-icons.rcc

%changelog
