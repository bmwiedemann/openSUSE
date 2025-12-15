#
# spec file for package rocs
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define kf6_version 6.19.0
%define qt6_version 6.9.0

%bcond_without released
Name:           rocs
Version:        25.12.0
Release:        0
Summary:        Graph Theory IDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/rocs
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextTemplate) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Rocs is a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.

Rocs has a scripting module, done in Qt Script, which interacts with
the drawn graph and every change in the graph with the script is
reflected on the drawn one.

%package -n librocsgraphtheory0
Summary:        ROCS Graph Theory IDE main component library

%description -n librocsgraphtheory0
Rocs is a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.

Rocs has a scripting module, done in Qt Script, which interacts with
the drawn graph and every change in the graph with the script is
reflected on the drawn one.

%package devel
Summary:        Development files for Rocs
Requires:       librocsgraphtheory0 = %{version}

%description devel
This package provides development files and headers needed
to build software using Rocs.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name --with-html

%fdupes %{buildroot}

%ldconfig_scriptlets -n librocsgraphtheory0

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/rocs/
%{_kf6_applicationsdir}/org.kde.rocs.desktop
%{_kf6_appstreamdir}/org.kde.rocs.appdata.xml
%{_kf6_bindir}/rocs
%{_kf6_configkcfgdir}/rocs.kcfg
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_plugindir}/rocs/
%{_kf6_sharedir}/rocs/

%files -n librocsgraphtheory0
%{_kf6_libdir}/librocsgraphtheory.so.*

%files devel
%doc TESTING.md
%{_includedir}/rocs/
%{_kf6_libdir}/librocsgraphtheory.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/rocs/

%changelog
