#
# spec file for package kdeconnect-kde
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without released
Name:           kdeconnect-kde
Version:        23.04.1
Release:        0
Summary:        Integration of Android with Linux desktops
License:        GPL-2.0-or-later
URL:            https://community.kde.org/KDEConnect
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source100:      kdeconnect-kde.SuSEfirewall
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(KF5PeopleVCard)
BuildRequires:  cmake(KF5PulseAudioQt)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(wayland-protocols)
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols2
Requires:       plasma-framework-components
# kdeconnect-openssh-8.8.patch needs https://github.com/libfuse/sshfs/pull/269,
# which is so far only on the way to TW.
Requires:       sshfs >= 3.7.2
Recommends:     kpeoplevcard
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
Summary:        ZSH completion for %{name}
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

for translation_file in kdeconnect-{app,cli,core,fileitemaction,indicator,interfaces,kcm,kded,kio,nautilus-extension,plugins,settings,sms,urlhandler} plasma_applet_org.kde.kdeconnect; do
    %find_lang $translation_file %{name}.lang
done
%kf5_find_htmldocs

%if 0%{?suse_version} < 1550
# susefirewall config file
install -D -m 0644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif

%suse_update_desktop_file %{buildroot}%{_kf5_applicationsdir}/org.kde.kdeconnect.app.desktop Network RemoteAccess
%suse_update_desktop_file %{buildroot}%{_kf5_applicationsdir}/org.kde.kdeconnect.nonplasma.desktop Network RemoteAccess
%suse_update_desktop_file %{buildroot}%{_kf5_applicationsdir}/org.kde.kdeconnect_open.desktop Network RemoteAccess

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
%if 0%{?suse_version} < 1550
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif
%dir %{_datadir}/Thunar
%dir %{_datadir}/contractor
%dir %{_datadir}/deepin
%dir %{_datadir}/deepin/dde-file-manager
%dir %{_datadir}/deepin/dde-file-manager/oem-menuextensions
%dir %{_datadir}/nautilus-python
%dir %{_kf5_sharedir}/kdeconnect
%{_datadir}/Thunar/sendto/
%{_datadir}/contractor/kdeconnect.contract
%{_datadir}/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop
%{_datadir}/nautilus-python/extensions/
%{_kf5_applicationsdir}/*.desktop
%{_kf5_appstreamdir}/org.kde.kdeconnect.appdata.xml
%{_kf5_appstreamdir}/org.kde.kdeconnect.metainfo.xml
%{_kf5_bindir}/kdeconnect-app
%{_kf5_bindir}/kdeconnect-cli
%{_kf5_bindir}/kdeconnect-handler
%{_kf5_bindir}/kdeconnect-indicator
%{_kf5_bindir}/kdeconnect-settings
%{_kf5_bindir}/kdeconnect-sms
%{_kf5_configdir}/autostart/org.kde.kdeconnect.daemon.desktop
%{_kf5_debugdir}/kdeconnect-kde.categories
%{_kf5_htmldir}/en/kdeconnect/
%{_kf5_iconsdir}/hicolor/*/apps/kdeconnect*
%{_kf5_iconsdir}/hicolor/*/status/*.svg
%{_kf5_libdir}/libkdeconnect*.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kdeconnect.service
%{_kf5_sharedir}/kdeconnect/kdeconnect_findthisdevice_config.qml
%{_kf5_sharedir}/kdeconnect/kdeconnect_pausemusic_config.qml
%{_kf5_sharedir}/kdeconnect/kdeconnect_runcommand_config.qml
%{_kf5_sharedir}/kdeconnect/kdeconnect_sendnotifications_config.qml
%{_kf5_sharedir}/kdeconnect/kdeconnect_share_config.qml
%{_kf5_sharedir}/kdeconnect/kdeconnect_clipboard_config.qml
%{_kf5_sharedir}/plasma/
%{_libexecdir}/kdeconnectd

%files lang -f %{name}.lang

%changelog
