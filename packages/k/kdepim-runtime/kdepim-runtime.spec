#
# spec file for package kdepim-runtime
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
%define kpim6_version 6.1.2

%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150500
%bcond_without etebase
%endif

%bcond_without released
Name:           kdepim-runtime
Version:        24.05.2
Release:        0
Summary:        Akonadi resources for PIM applications
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libboost_system-devel
%if %{with etebase}
BuildRequires:  libetebase-devel
%endif
BuildRequires:  libkolabxml-devel >= 1.1
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6DAV) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiNotes) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GAPI) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IMAP) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6LdapWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mbox) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Recommends:     kalendarac
Requires:       akonadi
Requires:       akonadi-plugin-calendar
Requires:       akonadi-plugin-contacts
Requires:       akonadi-plugin-mime
Provides:       kio-pimlibs = %{version}
Obsoletes:      kdepim4-runtime < %{version}
Obsoletes:      kio-pimlibs < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This package contains the Akonadi resources, agents and plugins needed to
use PIM applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.akonadi_contacts_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_davgroupware_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_ews_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_google_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_imap_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_kolab_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_openxchange_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_vcard_resource.desktop
%{_kf6_applicationsdir}/org.kde.akonadi_vcarddir_resource.desktop
%{_kf6_bindir}/akonadi_*
%{_kf6_bindir}/gidmigrator
%{_kf6_dbusinterfacesdir}/org.kde.Akonadi.Maildir.Settings.xml
%{_kf6_dbusinterfacesdir}/org.kde.Akonadi.MixedMaildir.Settings.xml
%{_kf6_debugdir}/kdepim-runtime.categories
%{_kf6_debugdir}/kdepim-runtime.renamecategories
%if %{with etebase}
%{_kf6_iconsdir}/hicolor/*/apps/akonadi-etesync.png
%endif
%{_kf6_iconsdir}/hicolor/*/apps/akonadi-ews.png
%{_kf6_iconsdir}/hicolor/*/apps/ox.png
%{_kf6_libdir}/*
%{_kf6_notificationsdir}/akonadi_*.notifyrc
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/akonadi
%dir %{_kf6_plugindir}/pim6/akonadi/config
%{_kf6_plugindir}/pim6/akonadi/config/*.so
%dir %{_kf6_plugindir}/pim6/kcms
%dir %{_kf6_plugindir}/pim6/kcms/kaddressbook/
%dir %{_kf6_plugindir}/pim6/mailtransport
%{_kf6_plugindir}/pim6/mailtransport/mailtransport_akonadiplugin.so
%{_kf6_sharedir}/akonadi/
%{_kf6_sharedir}/mime/packages/kdepim-mime.xml

%files lang -f %{name}.lang

%changelog
