#
# spec file for package breeze5-icons
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _tar_path 5.63
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           breeze5-icons
Version:        5.63.0
Release:        0
Summary:        Breeze icon theme
License:        LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/breeze-icons-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/breeze-icons-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE oxygen.diff -- inherit from oxygen
Patch0:         oxygen.diff
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  cmake(Qt5Core) >= 5.11.0
BuildRequires:  cmake(Qt5Test) >= 5.11.0
Requires:       oxygen5-icon-theme
BuildArch:      noarch

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%prep
%setup -q -n breeze-icons-%{version}
%patch0 -p1

%build
  %cmake_kf5 -d build -- -DBINARY_ICONS_RESOURCE=ON
  %make_jobs

%install
  %kf5_makeinstall -C build

  # yast2-theme uses these, but it got renamed in 5.55.0
  ln -s yast-software-group.svg %{buildroot}%{_kf5_iconsdir}/breeze/preferences/32/yast-software.svg
  ln -s yast-software-group.svg %{buildroot}%{_kf5_iconsdir}/breeze-dark/preferences/32/yast-software.svg

  %fdupes -s %{buildroot}%{_kf5_iconsdir}

  %icon_theme_cache_create_ghost breeze
  %icon_theme_cache_create_ghost breeze-dark

%post
%icon_theme_cache_post breeze
%icon_theme_cache_post breeze-dark

%files
%license COPYING*
%ghost %{_kf5_iconsdir}/breeze/icon-theme.cache
%ghost %{_kf5_iconsdir}/breeze-dark/icon-theme.cache
%{_kf5_iconsdir}/breeze/
%{_kf5_iconsdir}/breeze-dark/

%changelog
