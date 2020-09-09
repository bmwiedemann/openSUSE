#
# spec file for package rocs
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           rocs
Version:        20.08.1
Release:        0
Summary:        Graph Theory IDE
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Mathematics
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 1.7.0
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5ScriptTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XmlPatterns)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Rocs is a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.

Rocs has a scripting module, done in Qt Script, which interacts with
the drawn graph and every change in the graph with the script is
reflected on the drawn one.

%package -n librocsgraphtheory0
Summary:        ROCS Graph Theory IDE main component library
Group:          System/Libraries

%description -n librocsgraphtheory0
Rocs is a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.

Rocs has a scripting module, done in Qt Script, which interacts with
the drawn graph and every change in the graph with the script is
reflected on the drawn one.

%package devel
Summary:        Development files for Rocs
Group:          Development/Libraries/KDE
Requires:       librocsgraphtheory0 = %{version}

%description devel
This package provides development files and headers needed
to build software using Rocs.

%lang_package

%prep
%setup -q

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.%{name} Math
%fdupes -s %{buildroot}

%post -n librocsgraphtheory0 -p /sbin/ldconfig
%postun -n librocsgraphtheory0 -p /sbin/ldconfig

%files
%license COPYING*
%doc ChangeLog README.md
%doc %lang(en) %{_kf5_htmldir}/en/rocs/
%dir %{_kf5_appstreamdir}
%{_kf5_applicationsdir}/org.kde.rocs.desktop
%{_kf5_appstreamdir}/org.kde.rocs.appdata.xml
%{_kf5_bindir}/rocs
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/
%{_kf5_plugindir}/
%{_kf5_sharedir}/rocs/

%files devel
%license COPYING*
%doc TESTING.md
%{_kf5_prefix}/include/rocs/
%{_kf5_libdir}/librocsgraphtheory.so

%files -n librocsgraphtheory0
%license COPYING*
%{_kf5_libdir}/librocsgraphtheory.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
