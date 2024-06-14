#
# spec file for package rocs
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


%bcond_without released
Name:           rocs
Version:        24.05.1
Release:        0
Summary:        Graph Theory IDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/rocs
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5ScriptTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XmlPatterns)
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
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%fdupes -s %{buildroot}

%ldconfig_scriptlets -n librocsgraphtheory0

%files
%license LICENSES/*
%doc ChangeLog README.md
%doc %lang(en) %{_kf5_htmldir}/en/rocs/
%{_kf5_applicationsdir}/org.kde.rocs.desktop
%{_kf5_appstreamdir}/org.kde.rocs.appdata.xml
%{_kf5_bindir}/rocs
%{_kf5_configkcfgdir}/rocs.kcfg
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_plugindir}/rocs/
%{_kf5_sharedir}/rocs/

%files -n librocsgraphtheory0
%{_kf5_libdir}/librocsgraphtheory.so.*

%files devel
%doc TESTING.md
%{_kf5_prefix}/include/rocs/
%{_kf5_libdir}/librocsgraphtheory.so

%files lang -f %{name}.lang

%changelog
