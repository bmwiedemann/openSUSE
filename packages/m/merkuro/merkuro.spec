#
# spec file for package kalendar
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


%global __requires_exclude qmlimport\\((org\\.kde\\.merkuro\\.1|org\\.kde\\.raven).*
%define kf5_version 5.105.0
%bcond_without released
Name:           merkuro
Version:        23.08.0
Release:        0
Summary:        Calendar Application
License:        GPL-3.0-only
URL:            https://apps.kde.org/merkuro.calendar
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KPim5PimCommonAkonadi)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5EventViews)
BuildRequires:  cmake(KPim5MailCommon)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  pkgconfig(gpgme)
Requires:       kalendarac
Requires:       kdepim-addons
Requires:       kdepim-runtime
# No automatic qmlimport requires for embedded resources :-/
Requires:       kirigami2 >= %{kf5_version}
Requires:       qt5qmlimport(QtGraphicalEffects.1)
Requires:       qt5qmlimport(QtLocation.5)
Requires:       qt5qmlimport(QtQuick.Dialogs.1)
Requires:       qt5qmlimport(org.kde.kitemmodels.1)
Provides:       kalendar = %{version}
Obsoletes:      kalendar < %{version}
# Got vendored for now
# Requires:       qt5qmlimport(org.kde.kirigamiaddons.treeview.1)
# kalendar has a runtime dependency on QtWebEngine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64

%description
Calendar application using Akonadi to sync with external services (NextCloud, GMail, ...).

%package plasmoid
Summary:        Plasma widget to view address book contacts
Supplements:    (%{name} and plasma5-workspace)
Requires:       %{name} = %{version}
Provides:       kalendar-plasmoid = %{version}
Obsoletes:      kalendar-plasmoid < %{version}

%description plasmoid
This package provides a Plasma widget to view address book contacts.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} == 1500
  export CXX=g++-10
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%files
%license LICENSES/*
%dir %{_kf5_qmldir}/org/kde/merkuro/
%{_kf5_applicationsdir}/org.kde.merkuro.contact.desktop
%{_kf5_applicationsdir}/org.kde.merkuro.mail.desktop
%{_kf5_applicationsdir}/org.kde.merkuro.calendar.desktop
%{_kf5_bindir}/merkuro-mail
%{_kf5_bindir}/merkuro-calendar
%{_kf5_bindir}/merkuro-contact
%{_kf5_debugdir}/akonadi.quick.categories
%{_kf5_debugdir}/merkuro.categories
%{_kf5_debugdir}/merkuro.contact.categories
%{_kf5_iconsdir}/hicolor/*/apps/org.kde.merkuro.*.png
%{_kf5_qmldir}/org/kde/akonadi/
%{_kf5_qmldir}/org/kde/merkuro/contact/
%{_kf5_qmldir}/org/kde/merkuro/calendar/
%{_kf5_qmldir}/org/kde/merkuro/mail/
%{_kf5_qmldir}/org/kde/merkuro/components/
%{_kf5_appstreamdir}/org.kde.merkuro.calendar.metainfo.xml
%{_kf5_appstreamdir}/org.kde.merkuro.mail.metainfo.xml
%{_kf5_appstreamdir}/org.kde.merkuro.contact.metainfo.xml

%files plasmoid
%dir %{_kf5_plasmadir}/plasmoids
%{_kf5_appstreamdir}/org.kde.merkuro.contact.appdata.xml
%{_kf5_plasmadir}/plasmoids/org.kde.merkuro.contact

%files lang -f %{name}.lang

%changelog
