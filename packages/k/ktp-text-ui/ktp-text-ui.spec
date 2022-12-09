#
# spec file for package ktp-text-ui
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           ktp-text-ui
Version:        22.12.0
Release:        0
Summary:        Telepathy chat handler by KDE
License:        GPL-2.0-or-later
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  ktp-icons
BuildRequires:  telepathy-logger-qt5-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KTp)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5WebEngine)
# Explicitely require logger, otherwise the ui would crash
Requires:       telepathy-logger
Obsoletes:      %{name}-devel
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
Includes KDE's implementation of the Telepathy chat handler,
a chat plasmoid, and a chat log viewer application.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%fdupes %{buildroot}

mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
cp %{_kf5_iconsdir}/breeze/apps/48/kde-im-log-viewer.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/

%files
%license COPYING*
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/ktp-log-viewer
%{_kf5_iconsdir}/hicolor/scalable/apps/kde-im-log-viewer.svg
%{_kf5_kxmlguidir}/ktp-text-ui/
%{_kf5_libdir}/libktpchat.so*
%{_kf5_libdir}/libktpimagesharer.so*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.TextUi.service
%{_kf5_sharedir}/ktelepathy/
%{_kf5_sharedir}/ktp-log-viewer/
%{_kf5_sharedir}/telepathy/
%{_libexecdir}/ktp-adiumxtra-protocol-handler
%{_libexecdir}/ktp-text-ui

%files lang -f %{name}.lang

%changelog
