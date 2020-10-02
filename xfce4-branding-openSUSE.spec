#
# spec file for package xfce4-branding-openSUSE
#
# Copyright (c) 2020 SUSE LLC
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


%define libxfce4ui_gtk2_libname libxfce4ui-1-0
%define libxfce4ui_gtk3_libname libxfce4ui-2-0
%define libexo_libname          libexo-1-0

%define xfce4_panel_version     %(rpm -q --queryformat '%%{VERSION}' xfce4-panel)
%define xfce4_session_version   %(rpm -q --queryformat '%%{VERSION}' xfce4-session)
%define xfce4_settings_version  %(rpm -q --queryformat '%%{VERSION}' xfce4-settings)
%define xfdesktop_version       %(rpm -q --queryformat '%%{VERSION}' xfdesktop)
%define libgarcon_version       %(rpm -q --queryformat '%%{VERSION}' libgarcon-data)
%define libxfce4ui_version      %(rpm -q --queryformat '%%{VERSION}' %{libxfce4ui_gtk3_libname})
%define xfce4_notifyd_version   %(rpm -q --queryformat '%%{VERSION}' xfce4-notifyd)
%define exo_version             %(rpm -q --queryformat '%%{VERSION}' %{libexo_libname})
%define xfwm4_version           %(rpm -q --queryformat '%%{VERSION}' xfwm4)
%define xfce4_power_manager_version %(rpm -q --queryformat '%%{VERSION}' xfce4-power-manager)
%define thunar_volman_version   %(rpm -q --queryformat '%%{VERSION}' thunar-volman)

Name:           xfce4-branding-openSUSE
Version:        4.14+20200311
Release:        0
Summary:        openSUSE Branding of the Xfce Desktop Environment
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://github.com/openSUSE/xfce4-branding-openSUSE/tree/4.14
Source0:        %{name}-%{version}.tar.xz
Source1:        openSUSE-xfce-icon-theme.tar.bz2
BuildRequires:  %{libexo_libname}
BuildRequires:  %{libxfce4ui_gtk2_libname}
BuildRequires:  %{libxfce4ui_gtk3_libname}
BuildRequires:  fdupes
BuildRequires:  libgarcon-data
BuildRequires:  wallpaper-branding
# owns %%{_datadir}/applications/xfce-mimeapps.list symlink target
Requires:       libgio-2_0-0
# for regenerating xfce-mimeapps.list
BuildRequires:  desktop-file-utils
BuildRequires:  elementary-xfce-icon-theme
BuildRequires:  gtk2-metatheme-greybird-geeko
BuildRequires:  gtk3-metatheme-greybird-geeko
BuildRequires:  hack-fonts
BuildRequires:  metatheme-greybird-geeko-common
BuildRequires:  noto-coloremoji-fonts
BuildRequires:  noto-sans-fonts
BuildRequires:  thunar-volman
BuildRequires:  xfce4-notifyd
BuildRequires:  xfce4-panel
BuildRequires:  xfce4-power-manager
BuildRequires:  xfce4-session
BuildRequires:  xfce4-settings
BuildRequires:  xfdesktop
BuildRequires:  xfwm4
BuildRequires:  xfwm4-branding-upstream
BuildArch:      noarch

%description
This package provides the openSUSE look and feel for the Xfce desktop environment.

%package -n openSUSE-xfce-icon-theme
Summary:        openSUSE Xfce Default Icon Theme
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Requires:       adwaita-icon-theme
Requires:       elementary-xfce-icon-theme

%description -n openSUSE-xfce-icon-theme
This is the openSUSE Xfce Default Icon Theme.

%package -n xfce4-panel-branding-openSUSE
Summary:        openSUSE Branding of xfce4-panel
# uses xfce4-panel-plugin-mixer
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Recommends:     pavucontrol
Recommends:     xfce4-panel-plugin-pulseaudio
Recommends:     xfce4-panel-plugin-power-manager
# require. Because without this, many things (package-update-indicator...) will not work well, it's not really optional.
Requires:       xfce4-panel-plugin-statusnotifier
Requires:       xfce4-panel-plugin-whiskermenu
Conflicts:      otherproviders(xfce4-panel-branding)
Provides:       xfce4-panel-branding = %{xfce4_panel_version}
Supplements:    packageand(xfce4-panel:branding-openSUSE)

%description -n xfce4-panel-branding-openSUSE
This package provides the openSUSE look and feel for the Xfce Panel.

%package -n xfce4-session-branding-openSUSE
Summary:        openSUSE Branding of xfce4-session
# owns %%{_datadir}/applications/xfce-mimeapps.list symlink target
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Requires:       libgio-2_0-0
# for regenerating xfce-mimeapps.list
Requires:       desktop-file-utils
Requires:       elementary-xfce-icon-theme
Requires:       gtk2-metatheme-greybird-geeko
Requires:       gtk3-metatheme-greybird-geeko
Requires:       metatheme-greybird-geeko-common
Requires:       thunar-volman
Conflicts:      otherproviders(xfce4-session-branding)
Provides:       xfce4-session-branding = %{xfce4_session_version}
Supplements:    packageand(xfce4-session:branding-openSUSE)

%description -n xfce4-session-branding-openSUSE
This package provides the openSUSE look and feel for the Xfce Session Manager.

%package -n xfce4-settings-branding-openSUSE
Summary:        openSUSE Branding of xfce4-settings
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Requires:       desktop-data-openSUSE
Requires:       elementary-xfce-icon-theme
Requires:       gtk2-metatheme-adwaita
Requires:       gtk2-metatheme-greybird-geeko
Requires:       gtk3-metatheme-adwaita
Requires:       gtk3-metatheme-greybird-geeko
Requires:       hack-fonts
Requires:       metatheme-greybird-geeko-common
Requires:       noto-coloremoji-fonts
Requires:       noto-sans-fonts
Requires:       openSUSE-xfce-icon-theme
Recommends:     noto-sans-cjk-fonts
Conflicts:      otherproviders(xfce4-settings-branding)
Provides:       xfce4-settings-branding = %{xfce4_settings_version}
Supplements:    packageand(xfce4-settings:branding-openSUSE)

%description -n xfce4-settings-branding-openSUSE
This package provides the openSUSE look and feel for Xfce.

%package -n xfdesktop-branding-openSUSE
Summary:        openSUSE Branding of xfdesktop
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Requires:       desktop-data-openSUSE
Requires:       wallpaper-branding
Conflicts:      otherproviders(xfdesktop-branding)
Provides:       xfce4-desktop-branding-openSUSE = %{xfdesktop_version}
Provides:       xfdesktop-branding = %{xfdesktop_version}
Obsoletes:      xfce4-desktop-branding-openSUSE < %{xfdesktop_version}
Supplements:    packageand(xfdesktop:branding-openSUSE)

%description -n xfdesktop-branding-openSUSE
This package provides the openSUSE look and feel for the Xfce Desktop Manager.

%package -n libgarcon-branding-openSUSE
Summary:        openSUSE Branding of libgarcon
License:        CC-BY-SA-3.0 AND GPL-2.0-only
Group:          System/GUI/XFCE
Requires:       desktop-data-openSUSE
Requires:       wallpaper-branding
# xfce-applications.menu requires xfce-settings-manager.menu
Requires:       xfce4-settings-branding-openSUSE = %{version}
# the menu references xfce4-about.desktop
Requires:       libxfce4ui-tools
Conflicts:      otherproviders(libgarcon-branding)
Provides:       libgarcon-branding = %{libgarcon_version}
Supplements:    packageand(libgarcon-data:branding-openSUSE)

%description -n libgarcon-branding-openSUSE
This package provides the openSUSE look and feel for Garcon.

%package -n libxfce4ui-branding-openSUSE
Summary:        openSUSE Branding of libxfce4ui
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Conflicts:      otherproviders(libxfce4ui-branding)
Provides:       libxfce4ui-branding = %{libxfce4ui_version}
Supplements:    packageand(%{libxfce4ui_gtk2_libname}:branding-openSUSE)
Supplements:    packageand(%{libxfce4ui_gtk3_libname}:branding-openSUSE)

%description -n libxfce4ui-branding-openSUSE
This package provides the openSUSE look and feel for the libxfce4ui library.

%package -n xfce4-notifyd-branding-openSUSE
Summary:        openSUSE Branding of xfce4-notifyd
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Conflicts:      otherproviders(xfce4-notifyd-branding)
Provides:       xfce4-notifyd-branding = %{xfce4_notifyd_version}
Supplements:    packageand(xfce4-notifyd:branding-openSUSE)

%description -n xfce4-notifyd-branding-openSUSE
This package provides the openSUSE look and feel for the Xfce Notification Daemon.

%package -n exo-branding-openSUSE
Summary:        openSUSE Branding of exo
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Conflicts:      otherproviders(exo-branding)
Conflicts:      otherproviders(%{libexo_libname}-branding)
Provides:       %{libexo_libname}-branding-openSUSE  = %{version}
Provides:       exo-branding = %{exo_version}
Obsoletes:      %{libexo_libname}-branding-openSUSE <= %{version}
Supplements:    packageand(%{libexo_libname}:branding-openSUSE)
Supplements:    packageand(libexo-2-0:branding-openSUSE)

%description -n exo-branding-openSUSE
This package provides the openSUSE look and feel for the exo library.

%package -n xfwm4-branding-openSUSE
Summary:        openSUSE Branding of xfwm4
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Requires:       noto-sans-fonts
Conflicts:      otherproviders(xfwm4-branding)
Provides:       xfwm4-branding = %{xfwm4_version}
Supplements:    packageand(xfwm4:branding-openSUSE)

%description -n xfwm4-branding-openSUSE
This package provides the openSUSE look and feel for the xfwm4 window manager.

%package -n xfce4-power-manager-branding-openSUSE
Summary:        openSUSE Branding of xfce4-power-manager
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Conflicts:      otherproviders(xfce4-power-manager-branding)
Provides:       xfce4-power-manager-branding = %{xfce4_power_manager_version}
Supplements:    packageand(xfce4-power-manager:branding-openSUSE)

%description -n xfce4-power-manager-branding-openSUSE
This package provides the openSUSE look and feel for the Xfce Power Manager.

%package -n thunar-volman-branding-openSUSE
Summary:        openSUSE Branding of thunar-volman
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later
Group:          System/GUI/XFCE
Conflicts:      otherproviders(thunar-volman-branding)
Provides:       thunar-volman-branding = %{thunar_volman_version}
Supplements:    packageand(thunar-volman:branding-openSUSE)

%description -n thunar-volman-branding-openSUSE
This package provides the openSUSE look and feel for the Thunar Volume Manager.

%prep
%setup -q -n %{name}-%{version} -a1

%build

%install
# find overlay directory with the highest version less or equal to
# %%suse_version
for dir in [[:digit:]]*; do
    if [ ! -d "${dir}" ]; then
        continue
    elif [ "${dir}" -le "0%{?suse_version}" ]; then
        if [ -z "${overlay_version}" ] ||\
                [ "${dir}" -gt "${overlay_version}" ]; then
            overlay_version="${dir}"
        fi
    fi
done
for dir in base "${overlay_version}"; do
    if [ -d "${dir}" ]; then
    (
        cd $dir
        find . -depth -print | cpio -puvd %{buildroot}
    )
    fi
done
(
    cd openSUSE-xfce-icon-theme
    find openSUSE-Xfce -depth -print | cpio -puvd %{buildroot}%{_datadir}/icons
)

%fdupes %{buildroot}%{_datadir}/icons/openSUSE-Xfce

%icon_theme_cache_create_ghost openSUSE-Xfce

%post -n openSUSE-xfce-icon-theme
%icon_theme_cache_post openSUSE-Xfce

%files -n openSUSE-xfce-icon-theme
%license openSUSE-xfce-icon-theme/{COPYING,LICENSES}
%{_datadir}/icons/openSUSE-Xfce
%ghost %{_datadir}/icons/openSUSE-Xfce/icon-theme.cache

%files -n xfce4-panel-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/whiskermenu
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/whiskermenu/defaults.rc
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
%{_datadir}/pixmaps/xfce4-suse.png
%{_datadir}/pixmaps/xfce4-opensuse-white.svg
%{_datadir}/icons/hicolor/*

%files -n xfce4-session-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%config %{_sysconfdir}/xfce_defaults.conf
%dir %{_datadir}/applications
%{_datadir}/applications/xfce-mimeapps.list

%files -n xfce4-settings-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/xfce-settings-manager.menu

%files -n xfdesktop-branding-openSUSE
%license COPYING
%dir %{_datadir}/wallpapers/xfce
%{_datadir}/wallpapers/xfce/default.wallpaper

%files -n libgarcon-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/menus
%dir %{_datadir}/desktop-directories
%config %{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_datadir}/desktop-directories/YaST.directory

%files -n libxfce4ui-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%files -n xfce4-notifyd-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-notifyd.xml
%{_datadir}/themes/openSUSE-Xfce

%files -n exo-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%config %{_sysconfdir}/xdg/xfce4/helpers.rc

%files -n xfwm4-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml

%files -n xfce4-power-manager-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml

%files -n thunar-volman-branding-openSUSE
%license COPYING
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/thunar-volman.xml

%changelog
