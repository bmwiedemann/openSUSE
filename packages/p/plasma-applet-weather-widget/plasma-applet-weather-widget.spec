#
# spec file for package plasma-applet-weather-widget
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/.
#

%define lang_name plasma_applet_org.kde.weatherWidget

Name:           plasma-applet-weather-widget
Version:        1.6.10
Release:        0
Summary:        Plasma 5 widget for displaying weather information
License:        GPL-2.0-only
Group:          System/GUI/KDE
Url:            https://github.com/kotelnik/plasma-applet-weather-widget
Source:         https://github.com/kotelnik/plasma-applet-weather-widget/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtxmlpatterns-imports

%lang_package

%description
Plasma 5 widget for displaying weather information.

%prep
%setup -q -n %{name}-%{version}

%build
# Fix locale code for translation.
mv translations/po/%{lang_name}_hu_HU.po \
   translations/po/%{lang_name}_hu.po

%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%find_lang %{lang_name} %{name}.lang
%fdupes %{buildroot}

%files
%license LICENSE
%{_kf5_appstreamdir}/org.kde.weatherWidget.appdata.xml
%dir %{_kf5_plasmadir}/plasmoids
%{_kf5_plasmadir}/plasmoids/org.kde.weatherWidget
%{_kf5_qmldir}/org/kde/private/weatherWidget
%{_kf5_servicesdir}/plasma-applet-org.kde.weatherWidget.desktop

%files lang -f %{name}.lang

%changelog
