#
# spec file for package kalendar
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


%global __requires_exclude qt6qmlimport\\((org\\.kde\\.merkuro|org\\.kde\\.raven).*

%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1
%define plasma6_version 5.27.80

%bcond_without released
Name:           merkuro
Version:        24.05.1
Release:        0
Summary:        Calendar Application
License:        GPL-3.0-only
URL:            https://apps.kde.org/merkuro.calendar
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementQuick) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailCommon) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MimeTreeParserCore) >= %{kpim6_version}
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(gpgme)
Requires:       kalendarac
Requires:       kdepim-addons
Requires:       kdepim-runtime
# No automatic qmlimport requires for embedded resources :-/
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Provides:       kalendar = %{version}
Obsoletes:      kalendar < %{version}
# merkuro has a runtime dependency on QtWebEngine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Calendar application using Akonadi to sync with external services (NextCloud, GMail, ...).

%package plasmoid
Summary:        Plasma widget to view address book contacts
Supplements:    (merkuro and plasma6-workspace)
Requires:       merkuro = %{version}
Provides:       kalendar-plasmoid = %{version}
Obsoletes:      kalendar-plasmoid < %{version}

%description plasmoid
This package provides a Plasma widget to view address book contacts.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*

%{_kf6_applicationsdir}/org.kde.merkuro.calendar.desktop
%{_kf6_applicationsdir}/org.kde.merkuro.contact.desktop
%{_kf6_applicationsdir}/org.kde.merkuro.mail.desktop
%{_kf6_appstreamdir}/org.kde.merkuro.calendar.metainfo.xml
%{_kf6_appstreamdir}/org.kde.merkuro.contact.metainfo.xml
%{_kf6_appstreamdir}/org.kde.merkuro.mail.metainfo.xml
%{_kf6_bindir}/merkuro-calendar
%{_kf6_bindir}/merkuro-contact
%{_kf6_bindir}/merkuro-mail
%{_kf6_debugdir}/akonadi.quick.categories
%{_kf6_debugdir}/merkuro.categories
%{_kf6_debugdir}/merkuro.contact.categories
%{_kf6_iconsdir}/hicolor/*/apps/org.kde.merkuro.*.png
%{_kf6_qmldir}/org/kde/akonadi/
%{_kf6_qmldir}/org/kde/merkuro/

%files plasmoid
%dir %{_kf6_plasmadir}/plasmoids
%{_kf6_appstreamdir}/org.kde.merkuro.contact.appdata.xml
%{_kf6_plasmadir}/plasmoids/org.kde.merkuro.contact

%files lang -f %{name}.lang

%changelog
