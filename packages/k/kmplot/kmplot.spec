#
# spec file for package kmplot
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
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kmplot
Version:        22.12.1
Release:        0
Summary:        Mathematical Function Plotter
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kmplot
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Mathematical function plotter by KDE.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%doc %lang(en) %{_kf5_htmldir}/en/kmplot
%{_kf5_applicationsdir}/org.kde.kmplot.desktop
%{_kf5_appstreamdir}/org.kde.kmplot.appdata.xml
%{_kf5_bindir}/kmplot
%{_kf5_configkcfgdir}/kmplot.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kmplot.*.xml
%{_kf5_iconsdir}/hicolor/*/apps/kmplot.*
%{_kf5_kxmlguidir}/kmplot/
%{_kf5_plugindir}/kf5/parts/kmplotpart.so
%{_kf5_servicesdir}/kmplot_part.desktop
%{_mandir}/*/kmplot.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
