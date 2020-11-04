#
# spec file for package plasma5-workspace
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%{!?_fillupdir: %global _fillupdir %{_localstatedir}/adm/fillup-templates}

%define kf5_version 5.58.0

%bcond_without lang
Name:           plasma5-workspace
# Full Plasma 5 version (e.g. 5.9.1)
%{!?_plasma5_bugfix: %global _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.1 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Version:        5.20.2
Release:        0
%global _plasma5_bugfix 5.20.1
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-workspace-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-workspace-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
# PATCHES 501-??? are PATCH-FIX-OPENSUSE
Patch501:       0001-Use-qdbus-qt5.patch
Patch502:       0001-Ignore-default-sddm-face-icons.patch
Patch503:       0001-Set-GTK_BACKEND-x11-in-a-wayland-session.patch
# PATCH-FEATURE-OPENSUSE
Patch506:       0001-Revert-No-icons-on-the-desktop-by-default.patch
BuildRequires:  breeze5-icons
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformHeaders-devel >= 5.4.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(AppStreamQt) >= 0.10.4
BuildRequires:  cmake(KDED) >= %{kf5_version}
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5ActivitiesStats) >= %{kf5_version}
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IdleTime) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(KF5NetworkManagerQt) >= %{kf5_version}
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5NotifyConfig) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5People) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5PlasmaQuick)
BuildRequires:  cmake(KF5Prison) >= %{kf5_version}
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(KF5Screen) >= 5.0.93
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(KF5Su) >= %{kf5_version}
BuildRequires:  cmake(KF5SysGuard) >= %{_plasma5_version}
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlRpcClient)
BuildRequires:  cmake(KScreenLocker) >= %{_plasma5_version}
BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Phonon4Qt5) >= 4.6.60
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.1.0
#!BuildIgnore:  kdialog
BuildRequires:  cmake(KWinDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Gui) >= 5.4.0
BuildRequires:  cmake(Qt5Network) >= 5.4.0
BuildRequires:  cmake(Qt5Qml) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.4.0
BuildRequires:  cmake(Qt5Script) >= 5.4.0
BuildRequires:  cmake(Qt5Sql) >= 5.4.0
BuildRequires:  cmake(Qt5Svg) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  cmake(ScreenSaverDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(dbusmenu-qt5)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libgps)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
%endif
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-libs = %{version}-%{release}
# contains default style, cursors, etc
Requires:       breeze >= %{_plasma5_version}
# battery applet
Requires:       drkonqi5 >= %{_plasma5_version}
# dialog/platformtheme/etc
Requires:       frameworkintegration-plugin
Requires:       kactivitymanagerd
# used within startup
Requires:       kde-cli-tools5 >= %{_plasma5_version}
Requires:       kded
Requires:       kdelibs4support
Requires:       kglobalaccel5 >= %{_plasma5_version}
Requires:       kinit
Requires:       kquickcharts
Requires:       kscreen5 >= %{_plasma5_version}
Requires:       kscreenlocker >= %{_plasma5_version}
Requires:       kwin5 >= %{_plasma5_version}
Requires:       libkscreen2-plugin >= %{_plasma5_version}
Requires:       libqt5-qdbus
Requires:       libqt5-qtpaths
# heavily used by plasma
Requires:       libqt5-qtquickcontrols
# needed by krunner
Requires:       milou5 >= %{_plasma5_version}
# boo#912317
Requires:       gmenudbusmenuproxy >= %{_plasma5_version}
Recommends:     oxygen5-sounds >= %{_plasma5_version}
Requires:       solid-imports
# Used by KCMs
Requires:       knewstuff-imports
# Used by the user feedback KCM
Requires:       kuserfeedback-imports
Requires:       xembedsniproxy >= %{_plasma5_version}
# startkde and startplasma call these
Requires:       awk
Requires:       xprop
Requires:       xrdb
Requires:       xsetroot
# hardcode versions of plasma-framework-components and plasma-framework-private packages, as upstream doesn't keep backwards compability there
%requires_ge    plasma-framework-components
%requires_ge    plasma-framework
Recommends:     %{name}-lang
Recommends:     kio-extras5
# The lockscreen has a button to open a virtual keyboard
Recommends:     libqt5-qtvirtualkeyboard
# notifications...
Recommends:     phonon4qt5-backend
# people should be able to adjust desktop
Recommends:     systemsettings5
Conflicts:      kdebase4-workspace < 5.3.0
# Some files have been moved from kio-extras5 to plasma5-workspace in 5.4. This should prevent a possible file conflict. (boo#944656)
Conflicts:      kio-extras5 < 15.08.0
# plasmashell implements the dbus interface org.freedesktop.Notifications directly
Provides:       %{name}-branding = %{_plasma5_bugfix}
Provides:       %{name}-branding-upstream = %{version}
Provides:       dbus(org.freedesktop.Notifications)
Obsoletes:      %{name}-branding-upstream < %{version}

%description
This package contains the basic packages for a Plasma workspace.

%package libs
Summary:        The KDE Plasma Workspace Components
Group:          Development/Libraries/KDE
%requires_ge    kio
%requires_ge    kservice
%requires_ge    libKF5Activities5
%requires_ge    libKF5CoreAddons5
%requires_ge    libKF5I18n5
%requires_ge    libKF5WindowSystem5
%requires_ge    libQt5Core5
%requires_ge    libQt5DBus5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Widgets5
%requires_ge    libQt5X11Extras5
%requires_ge    libksysguard5
%requires_ge    plasma-framework

%description libs
This package contains the basic packages for a KDE Plasma 5 workspace.

%package -n xembedsniproxy
Summary:        XEmbed SNI Proxy
Group:          System/GUI/KDE
Provides:       xembed-sni-proxy = %{version}
Obsoletes:      xembed-sni-proxy < %{version}

%description -n xembedsniproxy
This package provides a proxy translating XEmbed for SNI trays.
Can also be used by standalone tray apps.

%package -n gmenudbusmenuproxy
Summary:        GMenu to DBusMenu Proxy
Group:          System/GUI/KDE
Recommends:     (unity-gtk2-module if libgtk-2_0-0)
Recommends:     (unity-gtk3-module if libgtk-3-0)

%description -n gmenudbusmenuproxy
This package provides a proxy translating GMenu (GTK Menu) to DBusMenu (the
standard), useful for global menu implementations.

%package devel
Summary:        The KDE Plasma Workspace Components
Group:          Development/Libraries/KDE
Requires:       %{name}-libs = %{version}-%{release}
Requires:       cmake(KF5SysGuard) >= %{_plasma5_version}
Requires:       cmake(KF5Wayland) >= %{kf5_version}
Requires:       cmake(Qt5Core) >= 5.4.0
Requires:       cmake(Qt5Gui) >= 5.4.0
Requires:       cmake(Qt5Quick) >= 5.4.0
Conflicts:      kapptemplate <= 16.03.80
Conflicts:      kdebase4-workspace-devel
Provides:       plasma-workspace5-devel = %{version}
Obsoletes:      plasma-workspace5-devel < %{version}

%description devel
This package contains the basic packages for a KDE Plasma 5 workspace.
Development files.

%package -n plasma5-session
Summary:        KDE Plasma 5 X11 Session
Group:          System/GUI/KDE
Requires:       breeze >= %{_plasma5_bugfix}
Requires:       breeze5-decoration >= %{_plasma5_bugfix}
Requires:       khotkeys5 >= %{_plasma5_bugfix}
Requires:       kwin5 >= %{_plasma5_bugfix}
Requires:       libkscreen2-plugin >= %{_plasma5_bugfix}
Requires:       plasma5-desktop >= %{_plasma5_bugfix}
Requires:       plasma5-workspace >= %{_plasma5_bugfix}
Requires:       polkit-kde-agent-5 >= %{_plasma5_bugfix}
Requires:       powerdevil5 >= %{_plasma5_bugfix}
Requires:       systemsettings5 >= %{_plasma5_bugfix}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(pre):  %{_bindir}/cut
Requires(pre):  %{_bindir}/grep
Requires(pre):  %{_bindir}/sed
# Pulls in NetworkManager, some don't use it
Recommends:     plasma-nm5 >= %{_plasma5_bugfix}
# needed for displaying the handbooks of KDE applications in a Plasma5 session (boo#980068)
Recommends:     khelpcenter5
Provides:       kdebase4-session = %{version}
Obsoletes:      kdebase4-session < %{version}
BuildArch:      noarch

%description -n plasma5-session
This package contains the startup scripts necessary to start a KDE
Plasma 5 session with X11 from a display manager.

%package -n plasma5-session-wayland
Summary:        KDE Plasma 5 Wayland Session
Group:          System/GUI/KDE
Requires:       kwayland-integration >= %{_plasma5_bugfix}
Requires:       libqt5-qtwayland
Requires:       plasma5-session >= %{version}
Requires:       xf86-input-libinput
Requires:       xorg-x11-server-wayland
# For screen sharing and window thumbnails in plasmashell
Requires:       pipewire

%description -n plasma5-session-wayland
This package contains the startup scripts necessary to start a KDE
Plasma 5 session with Wayland from a display manager.

%lang_package

%prep
%autosetup -p1 -n plasma-workspace-%{version}

%build
  %cmake_kf5 -d build -- -DKDE_DEFAULT_HOME=.kde4 -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build

  %if %{with lang}
    %{kf5_find_lang}
    %{kf5_find_htmldocs}
  %endif

  %suse_update_desktop_file -r %{buildroot}%{_kf5_applicationsdir}/org.kde.klipper.desktop System TrayIcon
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/48x48/apps/
  cp %{_kf5_iconsdir}/breeze/apps/48/klipper.svg %{buildroot}%{_kf5_iconsdir}/hicolor/48x48/apps/

  # Copy the icon for org.kde.kcolorschemeeditor.desktop
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/32x32/apps/
  cp %{_kf5_iconsdir}/breeze/preferences/32/preferences-desktop-color.svg %{buildroot}%{_kf5_iconsdir}/hicolor/32x32/apps/

  # Rename upstream session file to oS location
  mv %{buildroot}%{_kf5_sharedir}/xsessions/{plasma,plasma5}.desktop

  # Install compatibility symlink
  ln -s %{_kf5_sharedir}/xsessions/plasma5.desktop %{buildroot}%{_kf5_sharedir}/xsessions/kde-plasma.desktop

  # Install custom "full wayland" session
  pushd %{buildroot}%{_kf5_sharedir}/wayland-sessions/
  sed '/^Name/d;s/^Exec=/Exec=env GDK_BACKEND=wayland QT_QPA_PLATFORM=wayland /' plasmawayland.desktop > plasmafullwayland.desktop
  echo 'Name=Plasma (Full Wayland)' >> plasmafullwayland.desktop
  popd

  mkdir -p %{buildroot}%{_sysconfdir}/alternatives
  touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
  ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

# To work around boo#1175025. Can't use symlinks either, kpackage doesn't like them.
%if 0%{?suse_version} < 1550
  %fdupes %{buildroot}/%{_prefix}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post -n plasma5-session
# Reset the DEFAULT_WM value for KDE upgrade compatibility
if [ -f %{_sysconfdir}/sysconfig/windowmanager ]; then
    OLD_DEFAULTWM=`grep "DEFAULT_WM" %{_sysconfdir}/sysconfig/windowmanager | cut -d '=' -f 2 | cut -d '"' -f 2`
fi

if [ -f %{_fillupdir}/sysconfig.windowmanager ]; then
    TEMPLATE_DEFAULTWM=`grep "DEFAULT_WM" %{_fillupdir}/sysconfig.windowmanager | cut -d '=' -f 2 | cut -d '"' -f 2`
fi

# Check the old DEFAULT_WM and whether current DEFAULT_WM exists
if [ "$OLD_DEFAULTWM" = "startkde4" ] || [ "$OLD_DEFAULTWM" = "startkde" ] || [ "$OLD_DEFAULTWM" = "kde4" ]; then
    if [ -n "$TEMPLATE_DEFAULTWM" ] && [ "$OLD_DEFAULTWM" != "$TEMPLATE_DEFAULTWM" ]; then
        sed -i -e "s/^DEFAULT_WM=['\"]\?kde.*/DEFAULT_WM=\"${TEMPLATE_DEFAULTWM}\"/g" %{_sysconfdir}/sysconfig/windowmanager
    fi
fi

%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/plasma5.desktop 25

%postun -n plasma5-session
[ -f %{_datadir}/xsessions/plasma5.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/plasma5.desktop

%files libs
%license COPYING*
%{_kf5_libdir}/libkworkspace5.so.*
%{_kf5_libdir}/libplasma-geolocation-interface.so.*
%{_kf5_libdir}/libtaskmanager.so.*
%{_kf5_libdir}/libweather_ion.so.*
%{_kf5_libdir}/libcolorcorrect.so.*
%{_kf5_libdir}/libnotificationmanager.so.*

%files
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kcolorschemeeditor.desktop
%{_kf5_applicationsdir}/org.kde.kfontview.desktop
%{_kf5_bindir}/kcminit
%{_kf5_bindir}/kcminit_startup
%{_kf5_bindir}/kfontinst
%{_kf5_bindir}/kfontview
%{_kf5_bindir}/klipper
%{_kf5_bindir}/krunner
%{_kf5_bindir}/ksmserver
%{_kf5_bindir}/ksplashqml
%{_kf5_bindir}/plasmashell
%{_kf5_bindir}/plasmawindowed
%{_kf5_bindir}/systemmonitor
%{_kf5_bindir}/plasma_waitforname
%{_kf5_bindir}/plasma_session
%{_kf5_bindir}/startplasma-wayland
%{_kf5_bindir}/startplasma-x11
%{_kf5_bindir}/plasma-shutdown
%{_kf5_bindir}/kde-systemd-start-condition
%{_kf5_bindir}/lookandfeeltool
%{_kf5_bindir}/kcolorschemeeditor
%{_kf5_bindir}/krdb
%{_kf5_configdir}/autostart/org.kde.plasmashell.desktop
%{_kf5_configdir}/autostart/klipper.desktop
%{_kf5_configkcfgdir}/
%{_kf5_knsrcfilesdir}/colorschemes.knsrc
%{_kf5_knsrcfilesdir}/gtk_themes.knsrc
%{_kf5_knsrcfilesdir}/kfontinst.knsrc
%{_kf5_knsrcfilesdir}/icons.knsrc
%{_kf5_knsrcfilesdir}/lookandfeel.knsrc
%{_kf5_knsrcfilesdir}/plasma-themes.knsrc
%{_kf5_knsrcfilesdir}/plasmoids.knsrc
%{_kf5_knsrcfilesdir}/wallpaper.knsrc
%{_kf5_knsrcfilesdir}/wallpaperplugin.knsrc
%{_kf5_knsrcfilesdir}/xcursor.knsrc

%config %{_kf5_configdir}/taskmanagerrulesrc
%config %{_kf5_configdir}/plasmanotifyrc
%dir %{_kf5_libdir}/libexec
%{_kf5_libdir}/libexec/ksmserver-logout-greeter
%{_kf5_libdir}/libexec/plasma-changeicons
%{_kf5_libdir}/libkdeinit5_kcminit.so
%{_kf5_libdir}/libkdeinit5_kcminit_startup.so
%{_kf5_libdir}/libkdeinit5_klipper.so
%{_kf5_libdir}/kconf_update_bin/krunnerplugins
%{_kf5_libdir}/kconf_update_bin/krunnerglobalshortcuts
%{_kf5_libdir}/libexec/baloorunner
%{_kf5_libdir}/libexec/plasma-sourceenv.sh
%{_kf5_libdir}/libexec/startplasma-waylandsession
%{_kf5_libdir}/libexec/plasma-dbus-run-session-if-needed
%{_kf5_libdir}/kconf_update_bin/krdb_clearlibrarypath
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_applicationsdir}/org.kde.klipper.desktop
%{_kf5_applicationsdir}/org.kde.plasmashell.desktop
%{_kf5_applicationsdir}/org.kde.systemmonitor.desktop
%{_kf5_applicationsdir}/plasma-windowed.desktop
%{_kf5_configkcfgdir}/freespacenotifier.kcfg
%{_kf5_configkcfgdir}/iconssettingsbase.kcfg
%{_kf5_configkcfgdir}/feedbacksettings.kcfg
%dir %{_kf5_sharedir}/krunner/
%dir %{_kf5_sharedir}/krunner/dbusplugins/
%{_kf5_sharedir}/kcontrol/
%{_kf5_sharedir}/kdisplay/
%{_kf5_sharedir}/kpackage/
%{_kf5_sharedir}/kfontinst/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_sharedir}/dbus-1/services/org.kde.fontinst.service
%{_kf5_sharedir}/dbus-1/system-services/org.kde.fontinst.service
%{_kf5_sharedir}/dbus-1/services/org.kde.LogoutPrompt.service
%{_kf5_sharedir}/dbus-1/services/org.kde.baloorunner.service
%{_kf5_sharedir}/dbus-1/services/org.kde.krunner.service
%{_kf5_sharedir}/dbus-1/services/org.kde.plasma.Notifications.service
%{_kf5_sharedir}/dbus-1/services/org.kde.KSplash.service
%{_kf5_sharedir}/dbus-1/services/org.kde.Shutdown.service
%{_kf5_sharedir}/dbus-1/system.d/org.kde.fontinst.conf
%{_kf5_sharedir}/desktop-directories/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/polkit-1/actions/org.kde.fontinst.policy
%{_kf5_sharedir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_kf5_sharedir}/konqsidebartng/

%dir %{_kf5_htmldir}
%dir %lang(en) %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/klipper/
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/
%doc %lang(en) %{_kf5_htmldir}/en/PolicyKit-kde/
%{_kf5_notifydir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%dir %{_kf5_sharedir}/kglobalaccel
%{_kf5_sharedir}/kglobalaccel/krunner.desktop
%{_kf5_sharedir}/ksplash/
%{_kf5_sharedir}/kstyle/
%{_kf5_plasmadir}/
%{_kf5_sharedir}/solid/
%{_kf5_sharedir}/kio_desktop/
%{_kf5_iconsdir}/hicolor/32x32/apps/preferences-desktop-color.svg
%{_kf5_iconsdir}/hicolor/48x48/apps/klipper.svg
%{_kf5_iconsdir}/hicolor/*/mimetypes/fonts-package.png
%{_kf5_iconsdir}/hicolor/*/apps/kfontview.png
%{_kf5_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz

%{_kf5_appstreamdir}/
%dir %{_kf5_sharedir}/sddm
%dir %{_kf5_sharedir}/sddm/themes
%{_kf5_sharedir}/sddm/themes/breeze/
%{_kf5_debugdir}/*.categories
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_sharedir}/kpackage/kcms/kcm_translations
%{_kf5_sharedir}/kpackage/kcms/kcm_feedback
%{_kf5_sharedir}/kpackage/kcms/kcm5_icons
%{_kf5_sharedir}/kpackage/kcms/kcm_desktoptheme
%dir %{_kf5_libdir}/libexec/kauth
%{_kf5_libdir}/libexec/kauth/fontinst
%{_kf5_libdir}/libexec/kauth/fontinst_helper
%{_kf5_libdir}/libexec/kauth/fontinst_x11
%{_kf5_libdir}/libexec/kfontprint
%exclude %{_kf5_libdir}/libkfontinst.so
%{_kf5_libdir}/libkfontinst.so.*
%exclude %{_kf5_libdir}/libkfontinstui.so
%{_kf5_libdir}/libkfontinstui.so.*

%files -n xembedsniproxy
%license COPYING*
%{_kf5_bindir}/xembedsniproxy
%{_kf5_configdir}/autostart/xembedsniproxy.desktop

%files -n gmenudbusmenuproxy
%license COPYING*
%{_kf5_bindir}/gmenudbusmenuproxy
%{_kf5_configdir}/autostart/gmenudbusmenuproxy.desktop

%files devel
%license COPYING*
%{_kf5_prefix}/include/kworkspace5/
%{_kf5_prefix}/include/plasma/
%{_kf5_prefix}/include/taskmanager/
%{_kf5_prefix}/include/notificationmanager/
%{_kf5_prefix}/include/colorcorrect/
%{_kf5_libdir}/cmake/KRunnerAppDBusInterface/
%{_kf5_libdir}/cmake/KSMServerDBusInterface/
%{_kf5_libdir}/cmake/LibKWorkspace/
%{_kf5_libdir}/cmake/LibTaskManager/
%{_kf5_libdir}/cmake/LibColorCorrect/
%{_kf5_libdir}/cmake/LibNotificationManager/
%{_kf5_libdir}/libkworkspace5.so
%{_kf5_libdir}/libplasma-geolocation-interface.so
%{_kf5_libdir}/libtaskmanager.so
%{_kf5_libdir}/libweather_ion.so
%{_kf5_libdir}/libcolorcorrect.so
%{_kf5_libdir}/libnotificationmanager.so
%{_kf5_sharedir}/kdevappwizard/
%{_kf5_sharedir}/dbus-1/interfaces/

%files -n plasma5-session
%license COPYING*
%{_kf5_sharedir}/xsessions/plasma5.desktop
%{_kf5_sharedir}/xsessions/kde-plasma.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_kf5_sharedir}/xsessions/default.desktop

%files -n plasma5-session-wayland
%license COPYING*
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/plasmawayland.desktop
%{_datadir}/wayland-sessions/plasmafullwayland.desktop

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
