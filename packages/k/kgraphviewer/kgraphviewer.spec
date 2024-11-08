#
# spec file for package kgraphviewer
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


%define kf6_version 6.3.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kgraphviewer
Version:        24.08.3
Release:        0
Summary:        Graphviz dot graph file viewer
License:        GPL-2.0-only
URL:            https://apps.kde.org/kgraphviewer
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  boost-devel
BuildRequires:  graphviz-devel >= 2.30
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       graphviz

%description
KGraphViewer is a Graphviz dot graph file viewer, aimed to replace the other
outdated Graphviz tools. Graphs are commonly used in scientific domains and
particularly in computer science.

%package -n libkgraphviewer0
Summary:        Graphviz dot graph file viewer

%description -n libkgraphviewer0
KGraphViewer is a Graphviz dot graph file viewer, aimed to replace the other
outdated Graphviz tools. Graphs are commonly used in scientific domains and
particularly in computer science.

This package install the kgraphviewer library.

%package -n kgraphviewer-devel
Summary:        Development files for kgraphviewer
Requires:       kgraphviewer = %{version}
Requires:       libkgraphviewer0 = %{version}

%description -n kgraphviewer-devel
Development files for kgraphviewer.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kgraphviewer --with-html kgraphviewer.lang

%ldconfig_scriptlets -n libkgraphviewer0

%files
%license COPYING COPYING.DOC
%doc AUTHORS
%doc %lang(en) %{_kf6_htmldir}/en/kgraphviewer
%{_kf6_applicationsdir}/org.kde.kgraphviewer.desktop
%{_kf6_appstreamdir}/org.kde.kgraphviewer.appdata.xml
%{_kf6_bindir}/kgraphviewer
%{_kf6_configkcfgdir}/kgraphviewer_partsettings.kcfg
%{_kf6_configkcfgdir}/kgraphviewersettings.kcfg
%{_kf6_debugdir}/kgraphviewer.categories
%{_kf6_iconsdir}/hicolor/*/apps/kgraphviewer.png
%{_kf6_plugindir}/kf6/parts/kgraphviewerpart.so

%files -n libkgraphviewer0
%{_kf6_libdir}/libkgraphviewer.so.*

%files -n kgraphviewer-devel
%{_includedir}/kgraphviewer/
%{_kf6_cmakedir}/KGraphViewerPart/
%{_kf6_libdir}/libkgraphviewer.so

%files lang -f kgraphviewer.lang
%exclude %{_kf6_htmldir}/en/kgraphviewer

%changelog
