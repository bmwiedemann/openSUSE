#
# spec file for package kleopatra
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
Name:           kleopatra
Version:        19.08.3
Release:        0
Summary:        KDE Key Manager
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kmime-devel
BuildRequires:  knotifications-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkleo-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.6.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Obsoletes:      kleopatra5 < %{version}
Provides:       kleopatra5 = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Kleopatra is a Key Manager for KDE.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%suse_update_desktop_file org.kde.kleopatra      Utility Security

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/kleopatra.categories
%{_kf5_debugdir}/kleopatra.renamecategories
%dir %{_kf5_appstreamdir}
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%doc %lang(en) %{_kf5_htmldir}/en/kleopatra/
%doc %lang(en) %{_kf5_htmldir}/en/kwatchgnupg/
%{_kf5_applicationsdir}/kleopatra_import.desktop
%{_kf5_applicationsdir}/org.kde.kleopatra.desktop
%{_kf5_appstreamdir}/org.kde.kleopatra.appdata.xml
%{_kf5_bindir}/kleopatra
%{_kf5_bindir}/kwatchgnupg
%{_kf5_iconsdir}/hicolor/*/apps/kleopatra.png
%{_kf5_libdir}/libkleopatraclientcore.so*
%{_kf5_libdir}/libkleopatraclientgui.so*
%{_kf5_plugindir}/kcm_kleopatra.so
%{_kf5_servicesdir}/kleopatra_*.desktop
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kleopatra/
%{_kf5_sharedir}/kwatchgnupg/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
