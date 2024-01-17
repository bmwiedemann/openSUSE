#
# spec file for package lightly
#
# Copyright (c) 2022 SUSE LLC
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


%define kf5_ver 5.66.0
Name:           lightly
Version:        0.4.1
Release:        0
Summary:        A modern style for qt applications
License:        GPL-2.0-or-later
URL:            https://github.com/Luwx/Lightly
Source0:        https://github.com/Luwx/Lightly/archive/v%{version}.tar.gz#/Lightly-%{version}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  frameworkintegration-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_ver}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_ver}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_ver}
BuildRequires:  cmake(KF5I18n) >= %{kf5_ver}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_ver}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_ver}
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Requires:       %{name}-decoration
Requires:       %{name}-style
Requires:       breeze5-cursors
Requires:       breeze5-icons

%description
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

%package        decoration
Summary:        Lightly kdecoration theme

%description    decoration
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

This package contains the kdecoration theme of Lightly.

%package        style
Summary:        Lightly kstyle theme and color schemes
Requires:       kconf_update5

%description    style
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

This package contains the kstyle theme and color schemes of Lightly.

%package -n     liblightlycommon5-5
Summary:        Lightly support code

%description -n liblightlycommon5-5
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

This package contains the support code of Lightly.

%prep
%autosetup -n Lightly-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%post   -p /sbin/ldconfig -n liblightlycommon5-5
%postun -p /sbin/ldconfig -n liblightlycommon5-5

%files
%license COPYING
%doc README.md

%files decoration
%license COPYING
%dir %{_kf5_plugindir}
%dir %{_kf5_plugindir}/org.kde.kdecoration2/
%{_kf5_plugindir}/org.kde.kdecoration2/lightlydecoration.so
%dir %{_kf5_servicesdir}
%{_kf5_servicesdir}/lightlydecorationconfig.desktop

%files style
%license COPYING
%dir %{_kf5_sharedir}/color-schemes/
%{_kf5_sharedir}/color-schemes/Lightly.colors
%{_kf5_libdir}/kconf_update_bin/
%{_kf5_sharedir}/kconf_update/
%dir %{_kf5_plugindir}
%{_kf5_plugindir}/kstyle_lightly_config.so
%dir %{_kf5_plugindir}/styles/
%{_kf5_plugindir}/styles/lightly.so
%dir %{_kf5_sharedir}/kstyle/
%dir %{_kf5_sharedir}/kstyle/themes
%{_kf5_sharedir}/kstyle/themes/lightly.themerc
%dir %{_kf5_servicesdir}
%{_kf5_servicesdir}/lightlystyleconfig.desktop
%{_kf5_cmakedir}/Lightly/

%files -n liblightlycommon5-5
%license COPYING
%{_libdir}/liblightlycommon5.so.*

%changelog
