#
# spec file for package akregator
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akregator
Version:        20.08.1
Release:        0
Summary:        RSS Feed Reader
License:        GPL-2.0-or-later
Group:          Productivity/Networking/News/Utilities
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  libkleo
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent) >= 5.7.0
BuildRequires:  cmake(Qt5Gui) >= 5.7.0
BuildRequires:  cmake(Qt5Network) >= 5.7.0
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml) >= 5.7.0
BuildRequires:  cmake(Qt5Quick) >= 5.7.0
BuildRequires:  cmake(Qt5Test) >= 5.7.0
BuildRequires:  cmake(Qt5WebEngine) >= 5.7.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.7.0
BuildRequires:  cmake(Qt5Widgets) >= 5.7.0
Provides:       akregator5 = %{version}
Obsoletes:      akregator5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Akregator is a news feed reader. It enables you to follow news sites,
blogs and other RSS/Atom-enabled websites without the need to
manually check for updates using a web browser. Akregator is designed
for convenient reading of hundreds of news sources. It comes with
Konqueror integration for adding news feeds and with an internal
browser for news reading.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
rm %{buildroot}%{_kf5_libdir}/*.so
%suse_update_desktop_file -r org.kde.akregator       Network  RSS-News

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB COPYING.DOC
%doc README
%dir %{_kf5_appstreamdir}/
%{_kf5_debugdir}/akregator.categories
%{_kf5_debugdir}/akregator.renamecategories
%{_kf5_applicationsdir}/org.kde.akregator.desktop
%{_kf5_appstreamdir}/org.kde.akregator.appdata.xml
%{_kf5_bindir}/akregator*
%{_kf5_configkcfgdir}/akregator.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.akregator.part.xml
%doc %lang(en) %{_kf5_htmldir}/en/akregator/
%{_kf5_iconsdir}/hicolor/*/apps/akregator*.png
%{_kf5_iconsdir}/hicolor/scalable/apps/akregator.svg
%{_kf5_libdir}/libakregatorinterfaces.so*
%{_kf5_libdir}/libakregatorprivate.so.*
%{_kf5_notifydir}/akregator.notifyrc
%{_kf5_plugindir}/akregator*.so
%dir %{_kf5_plugindir}/kontact5/
%{_kf5_plugindir}/kontact5/kontact_akregatorplugin.so
%{_kf5_servicesdir}/akregator_*.desktop
%{_kf5_servicesdir}/feed.protocol
%{_kf5_servicesdir}/kontact/
%{_kf5_servicetypesdir}/akregator_plugin.desktop
%{_kf5_sharedir}/akregator/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kontact/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
