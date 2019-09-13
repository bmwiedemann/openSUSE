#
# spec file for package systemsettings5
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


%bcond_without lang
Name:           systemsettings5
Version:        5.16.5
Release:        0
Summary:        KDE's control center
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/systemsettings-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/systemsettings-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE install_administration_category.diff -- install System Administration category, needed at least for YaST KCM
Patch0:         install_administration_category.diff
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  kirigami2-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
Requires:       kirigami2 >= 2.1
Recommends:     %{name}-lang

%description
Provides KDE's control center modules.

%package devel
Summary:        KDE's control center
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Conflicts:      kdebase4-workspace-devel

%description devel
Provides KDE's control center modules. Development files.

%lang_package
%prep
%setup -q -n systemsettings-%{version}
%autopatch -p1

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif
  %suse_update_desktop_file  kdesystemsettings X-SuSE-core

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_bindir}/systemsettings5
%{_kf5_libdir}/libsystemsettingsview.so.*
%{_kf5_plugindir}/
%{_kf5_applicationsdir}/*.desktop
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %{_kf5_htmldir}/en/*/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/systemsettings/
%{_kf5_sharedir}/kxmlgui5/
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/genericqml
%{_kf5_sharedir}/kpackage/genericqml/org.kde.systemsettings.sidebar
%{_kf5_debugdir}/*.categories
%{_kf5_appstreamdir}/org.kde.systemsettings.metainfo.xml

%files devel
%{_kf5_libdir}/libsystemsettingsview.so
%{_includedir}/*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
