#
# spec file for package kdesvn
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


Name:           kdesvn
Version:        2.1.0
Release:        0
Summary:        KDE Subversion Client
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://userbase.kde.org/Kdesvn
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kbookmarks-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  knotifications-devel
BuildRequires:  kparts-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
# needed for the database
Requires:       libQt5Sql5-sqlite
Provides:       kde4-kdesvn = %{version}
Obsoletes:      kde4-kdesvn < %{version}
Obsoletes:      libsvnqt7 < %{version}

%description
kdesvn is a GUI client for subversion repositories.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %suse_update_desktop_file -G "SVN Client" org.kde.kdesvn Development RevisionControl
  %find_lang %{name} --all-name --with-man
  %kf5_find_htmldocs
  %fdupes -s %{buildroot}%{_datadir}

%files -f %{name}.lang
%license COPYING COPYING.OpenSSL
%doc AUTHORS ChangeLog
%dir %{_kf5_iconsdir}/hicolor/96x96
%dir %{_kf5_iconsdir}/hicolor/96x96/actions
%dir %{_kf5_iconsdir}/hicolor/96x96/places
%doc %lang(en) %{_kf5_htmldir}/en/kdesvn/
%doc %lang(en) %{_kf5_mandir}/man1/kdesvn.1%{?ext_man}
%doc %lang(en) %{_kf5_mandir}/man1/kdesvnaskpass.1%{?ext_man}
%{_kf5_applicationsdir}/org.kde.kdesvn.desktop
%{_kf5_appstreamdir}/org.kde.kdesvn.appdata.xml
%{_kf5_bindir}/kdesvn
%{_kf5_bindir}/kdesvnaskpass
%{_kf5_configkcfgdir}/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.kdesvnd.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kdesvn/
%{_kf5_plugindir}/kdesvnpart.so
%{_kf5_plugindir}/kf5/kded/kdesvnd.so
%{_kf5_plugindir}/kio_ksvn.so
%{_kf5_servicesdir}/*.desktop
%{_kf5_servicesdir}/*.protocol
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_sharedir}/dbus-1/services/org.kde.kdesvnd.service
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kdesvn/

%changelog
