#
# spec file for package tellico
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


Name:           tellico
Version:        3.3.3
Release:        0
Summary:        A Collection Manager
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://tellico-project.org/
Source0:        https://tellico-project.org/files/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libcdio-devel
BuildRequires:  libcsv-devel
BuildRequires:  libexempi-devel
BuildRequires:  libkcddb-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libv4l-devel
BuildRequires:  libxslt-devel
BuildRequires:  libyaz-devel
BuildRequires:  pkgconfig
BuildRequires:  taglib-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Sane)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang = %{version}

%description
Tellico is an application for organizing your collections. It provides
default templates for books, bibliographies, videos, music, video games, coins,
stamps, trading cards, comic books, and wines.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 "-DENABLE_WEBCAM=true" -d build
%cmake_build

%install
%kf5_makeinstall -C build

%suse_update_desktop_file -r org.kde.%{name} Qt KDE Office Database

%find_lang %{name}
%{kf5_find_htmldocs}

%{kf5_post_install}

%fdupes -s %{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_kf5_applicationsdir}/org.kde.tellico.desktop
%dir %{_kf5_appsdir}/kconf_update
%{_kf5_appsdir}/kconf_update/tellico*
%{_kf5_appsdir}/tellico/
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.tellico.appdata.xml
%{_kf5_bindir}/tellico
%config %{_kf5_configdir}/tellico*
%dir %{_kf5_configkcfgdir}
%{_kf5_configkcfgdir}/tellico_config.kcfg
%doc %{_kf5_htmldir}/en/tellico/
%{_kf5_iconsdir}/hicolor/*/apps/tellico.png
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-tellico.png
%{_kf5_kxmlguidir}/tellico/
%{_datadir}/mime/packages/tellico.xml

%files lang -f %{name}.lang

%changelog
