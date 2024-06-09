#
# spec file for package kf6-breeze-icons
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


%define qt6_version 6.6.0

%define rname breeze-icons
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-breeze-icons
Version:        6.3.0
Release:        0
Summary:        Breeze icon theme
License:        LGPL-3.0-only
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  libxml2-tools
# Skip 24px icons generation (saves ~30MB and installs dangling symlinks)
# BuildRequires:  python3 python3-lxml
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
Provides:       breeze5-icons = %{version}
Obsoletes:      breeze5-icons < %{version}

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%package -n libKF6BreezeIcons6
Summary:        Breeze icon theme - icon library

%description -n libKF6BreezeIcons6
Breeze-icons is a freedesktop.org compatible icon theme.
This package provides a library containing icons, resources, and functions
to use them. It is meant to be used for self contained deployments.

%package rcc
Summary:        Breeze icon theme - rcc file
Provides:       breeze5-icons-rcc = %{version}
Obsoletes:      breeze5-icons-rcc < %{version}

%description rcc
Breeze-icons is a freedesktop.org compatible icon theme.
This contains the Breeze (non-dark) icons in a QResource file, used by Kexi.

%package devel
Summary:        CMake config files for kf6-breeze-icons
Requires:       kf6-breeze-icons = %{version}
Requires:       libKF6BreezeIcons6 = %{version}

%description devel
This package provides CMake config files for projects that wish to ensure
the Breeze icons are available at build time.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%define _lto_cflags %{nil}

# kexi needs the icons resource
%cmake_kf6 \
  -DBINARY_ICONS_RESOURCE:BOOL=TRUE \
  -DWITH_ICON_GENERATION:BOOL=FALSE

%kf6_build

%install
%kf6_install

# yast2-theme uses these, but it got renamed in 5.55.0
ln -s yast-software-group.svg %{buildroot}%{_kf6_iconsdir}/breeze/preferences/32/yast-software.svg

%fdupes %{buildroot}%{_kf6_iconsdir}

%icon_theme_cache_create_ghost breeze
%icon_theme_cache_create_ghost breeze-dark

%ldconfig_scriptlets -n libKF6BreezeIcons6

%files
%license COPYING*
%ghost %{_kf6_iconsdir}/breeze/icon-theme.cache
%ghost %{_kf6_iconsdir}/breeze-dark/icon-theme.cache
%exclude %{_kf6_iconsdir}/breeze/breeze-icons.rcc
%exclude %{_kf6_iconsdir}/breeze-dark/breeze-icons-dark.rcc
%{_kf6_iconsdir}/breeze/
%{_kf6_iconsdir}/breeze-dark/

%files -n libKF6BreezeIcons6
%{_kf6_libdir}/libKF6BreezeIcons.so.*

%files rcc
%dir %{_kf6_iconsdir}/breeze
# Kexi does not need the -dark variant.
%{_kf6_iconsdir}/breeze/breeze-icons.rcc

%files devel
%{_kf6_cmakedir}/KF6BreezeIcons/
%{_kf6_includedir}/BreezeIcons/
%{_kf6_libdir}/libKF6BreezeIcons.so

%changelog
