#
# spec file for package akregator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akregator
Version:        19.08.2
Release:        0
Summary:        RSS Feed Reader
License:        GPL-2.0-or-later
Group:          Productivity/Networking/News/Utilities
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-mime-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  grantlee5-devel
BuildRequires:  grantleetheme-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kontactinterface-devel
BuildRequires:  kparts-devel
BuildRequires:  kpimtextedit-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdepim-devel >= %{_kapp_version}
BuildRequires:  libkleo
BuildRequires:  messagelib-devel
BuildRequires:  pimcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  syndication-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.7.0
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Quick) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.7.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.7.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.7.0
Provides:       akregator5 = %{version}
Obsoletes:      akregator5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
# Needed for 42.3
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
%if 0%{?sle_version} < 120300
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc7-c++
%endif
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Akregator is a news feed reader. It enables you to follow news sites,
blogs and other RSS/Atom-enabled websites without the need to
manually check for updates using a web browser. Akregator is designed
for convenient reading of hundreds of news sources. It comes with
Konqueror integration for adding news feeds and with an internal
browser for news reading.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%if 0%{?suse_version} < 1330
  # It does not build with the default compiler (GCC 4.8) on Leap 42.x
  %if 0%{?sle_version} < 120300
    export CC=gcc-6
    export CXX=g++-6
  %else
    export CC=gcc-7
    export CXX=g++-7
  %endif
%endif
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%make_jobs

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
%{_kf5_plugindir}/kontact_akregatorplugin.so
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
