#
# spec file for package plasma5-desktop
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


%define kf5_version 5.58.0

%global have_ibus_dict_emoji_pkg (0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200)

%bcond_without lang
Name:           plasma5-desktop
Version:        5.19.0
Release:        0
# Full Plasma 5 version (e.g. 5.9.3)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.3 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         plasma-desktop-%{version}.tar.xz
%if %{with lang}
Source1:        plasma-desktop-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Use-themed-user-face-icon-in-kickoff.patch
BuildRequires:  extra-cmake-modules >= 1.8.0
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  libtag-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(AppStreamQt) >= 0.10.4
BuildRequires:  cmake(KDED) >= %{kf5_version}
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5ActivitiesStats) >= %{kf5_version}
BuildRequires:  cmake(KF5Attica) >= %{kf5_version}
BuildRequires:  cmake(KF5Auth) >= %{kf5_version}
BuildRequires:  cmake(KF5Baloo) >= %{kf5_version}
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5NewStuffQuick) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5NotifyConfig) >= %{kf5_version}
BuildRequires:  cmake(KF5People) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5PlasmaQuick) >= %{kf5_version}
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KRunnerAppDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(KSMServerDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(KWinDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma5_bugfix}
BuildRequires:  cmake(LibTaskManager) >= %{_plasma5_version}
BuildRequires:  cmake(Phonon4Qt5) >= 4.6.60
BuildRequires:  cmake(Qt5Concurrent) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Qml) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.4.0
BuildRequires:  cmake(Qt5Sql) >= 5.4.0
BuildRequires:  cmake(Qt5Svg) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  cmake(ScreenSaverDBusInterface) >= %{_plasma5_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xorg-evdev)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xorg-synaptics)
%ifarch %arm aarch64
BuildRequires:  pkgconfig(glesv2)
%else
BuildRequires:  pkgconfig(gl)
%endif
#BuildRequires:  pkgconfig(xrender)
BuildRequires:  breeze5-icons
BuildRequires:  xkeyboard-config
# Includes some plugins for kpackage needed during build
BuildRequires:  plasma5-workspace >= %{_plasma5_bugfix}
Requires:       %{name}-branding = %{version}
Requires:       libqt5-qtgraphicaleffects
Requires:       plasma5-workspace >= %{_plasma5_bugfix}
# hardcode versions of plasma-framework-componets and plasma-framework-private packages, as upstream doesn't keep backwards compability there
%requires_ge plasma-framework-components
%requires_ge plasma-framework-private
Requires:       kde-user-manager
# Various KCMs use it
Requires:       kinfocenter5
Requires:       kirigami2
Requires:       kmenuedit5
Requires:       ksysguard5
# Needed for sensors
Requires:       libksysguard5-imports
# kcm_style does DBus calls to the KDED module.
# However, that depends on xsettingsd and gio, so
# let the Supplements in kde-gtk-config5 handle it.
# Requires:       kde-gtk-config5 >= %{_plasma5_version}
# needed for the ActivityManager
Requires:       kactivities5-imports
# Needed for several KCMs
Requires:       knewstuff-imports
Conflicts:      kactivities5 < 5.20.0
Recommends:     plasma5-addons
Recommends:     %{name}-emojier
Provides:       kdebase4-workspace = 5.3.0
Obsoletes:      kdebase4-workspace < 5.3.0
Provides:       kcm-touchpad = %{version}
Obsoletes:      kcm-touchpad < %{version}
Provides:       kdebase4-workspace-plasma-calendar = %{version}
Obsoletes:      kdebase4-workspace-plasma-calendar < %{version}
Provides:       kdebase4-workspace-plasma-engine-akonadi = %{version}
Obsoletes:      kdebase4-workspace-plasma-engine-akonadi < %{version}
Conflicts:      kio-extras5 <= 5.3.2
Provides:       kcm-touchpad5 = %{version}
Obsoletes:      kcm-touchpad5 < %{version}
# libinput configuration is lacking in comparision
Recommends:     xf86-input-synaptics
Provides:       %{name}-branding = %{version}
Provides:       %{name}-branding-upstream = %{version}
Obsoletes:      %{name}-branding-upstream < %{version}
Provides:       plasma5-addons-kimpanel = %{version}
Obsoletes:      plasma5-addons-kimpanel < %{version}
Provides:       %{name}-kimpanel = %{version}
Obsoletes:      %{name}-kimpanel < %{version}
Obsoletes:      synaptiks

%description
This package contains the basic packages for a Plasma workspace.

%package emojier
Summary:        Selection window for emoji text input
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
# Other color fonts don't really work that well
Recommends:     noto-coloremoji-fonts
%if %{have_ibus_dict_emoji_pkg}
Requires:       ibus-dict-emoji
%endif

%description emojier
Press Meta+. to open an emoji selection window.

%lang_package

%prep
%autosetup -p1 -n plasma-desktop-%{version}

# Workaround for boo#1038368
sed -i"" "s/Name=Desktop/Name=Desktop Containment/g" containments/desktop/package/metadata.desktop

%build
%if !%{have_ibus_dict_emoji_pkg}
  # Reference the local copy (see the comment in the install section)
  sed -i"" 's#ibus/dicts/#plasma/ibus-emoji-dicts/#g' applets/kimpanel/backend/ibus/emojier/emojier.cpp
%endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

  # Copy the icon for kcolorschemeeditor.desktop
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/preferences
  if [ -f %{_kf5_iconsdir}/breeze/apps/32/preferences-desktop-color.svg ]; then
      cp %{_kf5_iconsdir}/breeze/apps/32/preferences-desktop-color.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
  else
      cp %{_kf5_iconsdir}/breeze/preferences/32/preferences-desktop-color.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/preferences/
  fi

  # remove empty/invalid appstream xml files. kpackagetool5 generates invalid files sometimes...
  # remove this once kpackagetool5 is fixed
  find %{buildroot}%{_kf5_appstreamdir} -type f -size 0 -print -delete

%if !%{have_ibus_dict_emoji_pkg}
  # The emojier needs .dict files from ibus, which are part of the ibus package.
  # That's a huge dep tree and is also known to break things such as keyboard layout selection.
  # So until that is fixed (boo#1161584) install the files as part of the package.
  mkdir -p %{buildroot}%{_kf5_sharedir}/plasma/ibus-emoji-dicts/
  cp %{_datadir}/ibus/dicts/emoji-*.dict %{buildroot}%{_kf5_sharedir}/plasma/ibus-emoji-dicts/
%endif

  # no devel files needed here
  rm -rfv %{buildroot}%{_kf5_sharedir}/dbus-1/interfaces/
  %fdupes %{buildroot}/%{_prefix}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/kcmkeys.categories
%{_kf5_dbuspolicydir}/org.kde.fontinst.conf
%{_kf5_dbuspolicydir}/org.kde.kcontrol.kcmclock.conf
%{_kf5_knsrcfilesdir}/colorschemes.knsrc
%{_kf5_knsrcfilesdir}/emoticons.knsrc
%{_kf5_knsrcfilesdir}/icons.knsrc
%{_kf5_knsrcfilesdir}/kfontinst.knsrc
%{_kf5_knsrcfilesdir}/plasma-themes.knsrc
%{_kf5_knsrcfilesdir}/lookandfeel.knsrc
%{_kf5_knsrcfilesdir}/xcursor.knsrc
%{_kf5_knsrcfilesdir}/ksplash.knsrc
%{_kf5_knsrcfilesdir}/gtk2_themes.knsrc
%{_kf5_knsrcfilesdir}/gtk3_themes.knsrc
%{_kf5_bindir}/kaccess
%{_kf5_bindir}/kapplymousetheme
%{_kf5_bindir}/kfontinst
%{_kf5_bindir}/kfontview
%{_kf5_bindir}/knetattach
%{_kf5_bindir}/krdb
%{_kf5_bindir}/kcm-touchpad-list-devices
%{_kf5_bindir}/solid-action-desktop-gen
%{_kf5_bindir}/lookandfeeltool
%{_kf5_bindir}/kcolorschemeeditor
%{_kf5_bindir}/tastenbrett
%{_kf5_configdir}/autostart/kaccess.desktop
%{_kf5_libdir}/kconf_update_bin/krdb_clearlibrarypath
%{_kf5_libdir}/libexec/
%{_kf5_libdir}/libkdeinit5_kaccess.so
%exclude %{_kf5_libdir}/libkfontinst.so
%{_kf5_libdir}/libkfontinst.so.*
%exclude %{_kf5_libdir}/libkfontinstui.so
%{_kf5_libdir}/libkfontinstui.so.*
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_applicationsdir}/org.kde.kfontview.desktop
%{_kf5_applicationsdir}/org.kde.knetattach.desktop
%{_kf5_applicationsdir}/org.kde.kcolorschemeeditor.desktop
%{_kf5_sharedir}/dbus-1/services/org.kde.fontinst.service
%{_kf5_sharedir}/dbus-1/system-services/org.kde.fontinst.service
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.fontinst.policy
%{_kf5_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %{_kf5_htmldir}/en/*/
%dir %{_kf5_iconsdir}/hicolor/*/
%dir %{_kf5_iconsdir}/hicolor/*/*/
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_configkcfgdir}/
%{_kf5_sharedir}/kcm_componentchooser/
%{_kf5_sharedir}/kcmkeys/
%{_kf5_sharedir}/kcmsolidactions/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kcontrol/
%{_kf5_sharedir}/kdisplay/
%{_kf5_sharedir}/kfontinst/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_sharedir}/kpackage/
%{_kf5_sharedir}/kcmmouse/
%{_kf5_sharedir}/kcmkeyboard/
%{_kf5_notifydir}/
%{_kf5_sharedir}/konqsidebartng/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_datadir}/
%{_kf5_sharedir}/solid/
%exclude %{_kf5_plasmadir}/ibus-emoji-dicts/
%{_kf5_plasmadir}/
%{_kf5_appstreamdir}/
%{_kf5_libdir}/libexec/kimpanel-ibus-panel
%{_kf5_qmldir}/org/kde/plasma/private/kimpanel/
%{_kf5_servicesdir}/*kimpanel*
%{_kf5_plasmadir}/services/kimpanel.operations
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.kimpanel/
%{_kf5_plugindir}/plasma/dataengine/plasma_engine_kimpanel.so

%files emojier
%{_kf5_bindir}/ibus-ui-emojier-plasma
%{_kf5_applicationsdir}/org.kde.plasma.emojier.desktop
%dir %{_kf5_sharedir}/kglobalaccel
%{_kf5_sharedir}/kglobalaccel/org.kde.plasma.emojier.desktop
%if !%{have_ibus_dict_emoji_pkg}
%{_kf5_plasmadir}/ibus-emoji-dicts/
%endif

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
