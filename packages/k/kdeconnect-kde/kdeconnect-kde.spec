#
# spec file for package kdeconnect-kde
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdeconnect-kde
Version:        24.05.2
Release:        0
Summary:        Integration of Android with Linux desktops
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kdeconnect
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source100:      kdeconnect-kde.SuSEfirewall
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami2) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11
BuildRequires:  cmake(KF6ModemManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6People) >= %{kf6_version}
# BuildRequires:  cmake(KF6PeopleVCard)
BuildRequires:  cmake(KF6PulseAudioQt)
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Bluetooth) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xtst)
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kpeople-imports >= %{kf6_version}
Requires:       kf6-qqc2-desktop-style >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
Requires:       sshfs >= 3.7.2
# TODO Not packaged yet
# Recommends:     kpeoplevcard
Conflicts:      kdeconnect-kde4

%description
A package for integration of Android with Linux desktops.

Current feature list:
- Clipboard share: copy from or to your desktop
- Notifications sync (4.3+): Read your Android notifications
- Multimedia remote control: Use your phone as a remote control
- WiFi connection: no USB wire or Bluetooth needed
- RSA Encryption: your information is safe

Please note you will need to install KDE Connect on Android for this app to work:
https://play.google.com/store/apps/details?id=org.kde.kdeconnect_tp or
https://f-droid.org/en/packages/org.kde.kdeconnect_tp/

%package zsh-completion
Summary:        ZSH completion for kdeconnect-kde
Requires:       kdeconnect-kde = %{version}
Supplements:    (kdeconnect-kde and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for kdeconnect-kde.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

# Remove unused static lib
rm %{buildroot}%{_kf6_libdir}/libkdeconnectinterfaces.a

%if 0%{?suse_version} < 1550
# susefirewall config file
install -D -m 0644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/kdeconnect-kde
%endif

%suse_update_desktop_file %{buildroot}%{_kf6_applicationsdir}/org.kde.kdeconnect.app.desktop RemoteAccess
%suse_update_desktop_file %{buildroot}%{_kf6_applicationsdir}/org.kde.kdeconnect.nonplasma.desktop RemoteAccess

%pre
# migrate old kdeconnect-kde service
# XXX: can be removed after some time, the author would suggest after 2023-06-15 has passed
if grep -q kdeconnect-kde /etc/firewalld/zones/*.xml 2>/dev/null; then
    echo "Migrating 'kdeconnect-kde' firewalld service to identical 'kdeconnect' shipped with firewalld."
    sed -i 's/<service name="kdeconnect-kde"\/>/<service name="kdeconnect"\/>/' /etc/firewalld/zones/*.xml
    if firewall-cmd -q --state; then
        firewall-cmd --reload
    fi
fi
true
# migrate kdeconnect-kde end

%post
%ldconfig
%if 0%{?is_opensuse}
if [ $1 -eq 1 ]; then # inital/first package install
    if [ -x %{_bindir}/firewall-cmd ]; then
        echo 'Adding kdeconnect service to default and home firewalld zones'
        if firewall-cmd -q --state; then
            firewall-cmd -q --add-service=kdeconnect
            firewall-cmd -q --add-service=kdeconnect --zone=home
            firewall-cmd -q --runtime-to-permanent
        else
            firewall-offline-cmd -q --add-service=kdeconnect
            firewall-offline-cmd -q --add-service=kdeconnect --zone=home
        fi
    fi
fi
true
%endif

%postun
%ldconfig
%if 0%{?is_opensuse}
if [ $1 -eq 0 ]; then # last/final package removal
    if [ -x %{_bindir}/firewall-cmd ]; then
        echo 'Removing kdeconnect service from default and home firewalld zones'
        if firewall-cmd -q --state; then
            firewall-cmd -q --remove-service=kdeconnect
            firewall-cmd -q --remove-service=kdeconnect --zone=home
            firewall-cmd -q --runtime-to-permanent
        else
            firewall-offline-cmd -q --remove-service=kdeconnect
            firewall-offline-cmd -q --remove-service-from-zone=kdeconnect --zone=home
        fi
    fi
fi
true
%endif

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kdeconnect

%files
%license LICENSES/*
%doc README*
%doc %lang(en) %{_kf6_htmldir}/en/kdeconnect*/
%if 0%{?suse_version} < 1550
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/kdeconnect-kde
%endif
%{_kf6_applicationsdir}/kcm_kdeconnect.desktop
%{_kf6_applicationsdir}/org.kde.kdeconnect-settings.desktop
%{_kf6_applicationsdir}/org.kde.kdeconnect.app.desktop
%{_kf6_applicationsdir}/org.kde.kdeconnect.daemon.desktop
%{_kf6_applicationsdir}/org.kde.kdeconnect.handler.desktop
%{_kf6_applicationsdir}/org.kde.kdeconnect.nonplasma.desktop
%{_kf6_applicationsdir}/org.kde.kdeconnect.sms.desktop
%{_kf6_appstreamdir}/org.kde.kdeconnect.appdata.xml
%{_kf6_appstreamdir}/org.kde.kdeconnect.metainfo.xml
%{_kf6_bindir}/kdeconnect-app
%{_kf6_bindir}/kdeconnect-cli
%{_kf6_bindir}/kdeconnect-handler
%{_kf6_bindir}/kdeconnect-indicator
%{_kf6_bindir}/kdeconnect-settings
%{_kf6_bindir}/kdeconnect-sms
%{_kf6_bindir}/kdeconnectd
%{_kf6_configdir}/autostart/org.kde.kdeconnect.daemon.desktop
%{_kf6_debugdir}/kdeconnect-kde.categories
%{_kf6_iconsdir}/hicolor/*/apps/kdeconnect*.svg
%{_kf6_iconsdir}/hicolor/*/status/*.svg
%{_kf6_libdir}/libkdeconnectcore.so.*
%{_kf6_libdir}/libkdeconnectpluginkcm.so.*
%{_kf6_notificationsdir}/kdeconnect.notifyrc
%{_kf6_plasmadir}/plasmoids/org.kde.kdeconnect/
%{_kf6_plugindir}/kdeconnect/
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/kdeconnectfileitemaction.so
%{_kf6_plugindir}/kf6/kio/kdeconnect.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kdeconnect.so
%{_kf6_qmldir}/org/kde/kdeconnect/
%dir %{_kf6_sharedir}/contractor
%{_kf6_sharedir}/contractor/kdeconnect.contract
%{_kf6_sharedir}/dbus-1/services/org.kde.kdeconnect.service
%dir %{_kf6_sharedir}/deepin
%dir %{_kf6_sharedir}/deepin/dde-file-manager
%dir %{_kf6_sharedir}/deepin/dde-file-manager/oem-menuextensions
%{_kf6_sharedir}/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop
%{_kf6_sharedir}/kdeconnect
%{_kf6_sharedir}/kdeconnect/kdeconnect_clipboard_config.qml
%{_kf6_sharedir}/kdeconnect/kdeconnect_findthisdevice_config.qml
%{_kf6_sharedir}/kdeconnect/kdeconnect_pausemusic_config.qml
%{_kf6_sharedir}/kdeconnect/kdeconnect_runcommand_config.qml
%{_kf6_sharedir}/kdeconnect/kdeconnect_sendnotifications_config.qml
%{_kf6_sharedir}/kdeconnect/kdeconnect_share_config.qml
%dir %{_kf6_sharedir}/nautilus-python
%dir %{_kf6_sharedir}/nautilus-python/extensions/
%{_kf6_sharedir}/nautilus-python/extensions/kdeconnect-share.py
%dir %{_kf6_sharedir}/Thunar
%dir %{_kf6_sharedir}/Thunar/sendto
%{_kf6_sharedir}/Thunar/sendto/kdeconnect-thunar.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kdeconnect*/

%changelog
