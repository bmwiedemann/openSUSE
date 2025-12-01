#
# spec file for package lightdm-kde-greeter
#
# Copyright (c) 2025 SUSE LLC
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


%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE91}
Name:           lightdm-kde-greeter
Version:        6.0.5
Release:        0
Summary:        LightDM KDE Greeter
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://invent.kde.org/plasma/lightdm-kde-greeter
Source0:        %{name}-%{version}.tar.xz
Source91:       filter-requires.sh
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
Requires:       %{name}-branding = %{version}
Requires:       lightdm
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-lang
Provides:       lightdm-greeter = %{version}
# ?????
#equires:       qt6qmlimport(ConnectionEnum.1)

%description
This package provides a KDE-based LightDM greeter engine.
This is a fork of KDE4-based LightDM greeter engine for KDE6.

%package        branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/X11/Displaymanagers
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description    branding-upstream
This package provides the upstream look and feel for %{name}.

%lang_package

%prep
%autosetup -p1
sed -i 's/^#\(Background\)/\1/' greeter/%{name}.conf.in
sed -i 's/^\(BackgroundFillMode\).*/\1=2/' greeter/%{name}.conf.in

%build
%cmake_kf6 \
    -DGREETER_IMAGES_DIR="%{_sharedstatedir}/lightdm/%{name}/images" \
    -DDATA_INSTALL_DIR="%{_kf6_sharedir}" \
    -DGREETER_DEFAULT_WALLPAPER="%{_datadir}/wallpapers/openSUSEdefault/contents/images/default.png"
%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

install -d -m 755 %{buildroot}%{_kf6_sysconfdir}/alternatives/
touch %{buildroot}%{_kf6_sysconfdir}/alternatives/lightdm-default-greeter.desktop

ln -s %{_kf6_sysconfdir}/alternatives/lightdm-default-greeter.desktop \
    %{buildroot}%{_kf6_sharedir}/xgreeters/lightdm-default-greeter.desktop

%post
%{_kf6_sbindir}/update-alternatives --install \
    %{_kf6_sharedir}/xgreeters/lightdm-default-greeter.desktop \
    lightdm-default-greeter.desktop \
    %{_kf6_sharedir}/xgreeters/%{name}.desktop \
    20

%postun
if [ "$1" = 0 ]; then
    %{_kf6_sbindir}/update-alternatives --remove lightdm-default-greeter.desktop \
        %{_kf6_sharedir}/xgreeters/%{name}.desktop
fi

%files
%doc README.md
%{_kf6_sharedir}/%{name}
%{_kf6_bindir}/%{name}-rootimage
%{_kf6_bindir}/%{name}-wifikeeper
%{_userunitdir}/%{name}-wifikeeper.service
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_lightdm.so
%{_kf6_libexecdir}/kauth/kcmlightdmhelper
%{_kf6_sbindir}/%{name}
%{_kf6_sharedir}/applications/kcm_lightdm.desktop
%{_kf6_dbuspolicydir}/org.kde.kcontrol.kcmlightdm.conf
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmlightdm.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmlightdm.policy
%dir %{_kf6_sharedir}/xgreeters
%{_kf6_sharedir}/xgreeters/lightdm-default-greeter.desktop
%{_kf6_sharedir}/xgreeters/%{name}.desktop
%ghost %{_kf6_sysconfdir}/alternatives/lightdm-default-greeter.desktop
%license COPYING.GPL3 LICENSES/*.txt

%files branding-upstream
%dir %{_kf6_sysconfdir}/lightdm
%config(noreplace) %{_kf6_sysconfdir}/lightdm/%{name}.conf

%files lang -f %{name}.lang

%changelog
