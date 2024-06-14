#
# spec file for package kleopatra
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           kleopatra
Version:        24.05.1
Release:        0
Summary:        Certificate manager and GUI for OpenPGP and CMS cryptography
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kleopatra
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libgpgmepp-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkleo) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MimeTreeParserWidgets) >= %{kpim6_version}
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(libassuan)
Requires:       dirmngr
Requires:       gpg2
Recommends:     paperkey
Obsoletes:      kleopatra5 < %{version}
Provides:       kleopatra5 = %{version}

%description
Kleopatra is a certificate manager and GUI for OpenPGP and CMS cryptography.

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
%doc %lang(en) %{_kf6_htmldir}/en/kleopatra/
%doc %lang(en) %{_kf6_htmldir}/en/kwatchgnupg/
%{_kf6_applicationsdir}/kleopatra_import.desktop
%{_kf6_applicationsdir}/org.kde.kleopatra.desktop
%{_kf6_applicationsdir}/org.kde.kwatchgnupg.desktop
%{_kf6_appstreamdir}/org.kde.kleopatra.appdata.xml
%{_kf6_bindir}/kleopatra
%{_kf6_bindir}/kwatchgnupg
%{_kf6_debugdir}/kleopatra.categories
%{_kf6_debugdir}/kleopatra.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/kleopatra.png
%{_kf6_iconsdir}/hicolor/*/apps/kwatchgnupg.png
%{_kf6_libdir}/libkleopatraclientcore.so.*
%{_kf6_libdir}/libkleopatraclientgui.so.*
%dir %{_kf6_plugindir}/pim6/
%dir %{_kf6_plugindir}/pim6/kcms
%dir %{_kf6_plugindir}/pim6/kcms/kleopatra
%{_kf6_plugindir}/pim6/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
%{_kf6_sharedir}/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
%{_kf6_sharedir}/kio/servicemenus/kleopatra_signencryptfiles.desktop
%{_kf6_sharedir}/kio/servicemenus/kleopatra_signencryptfolders.desktop
%{_kf6_sharedir}/kleopatra/
%{_kf6_sharedir}/kwatchgnupg/
%{_kf6_sharedir}/mime/packages/application-vnd-kde-kleopatra.xml
%{_kf6_sharedir}/mime/packages/kleopatra-mime.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kleopatra/
%exclude %{_kf6_htmldir}/en/kwatchgnupg/

%changelog
