#
# spec file for package kcachegrind
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
Name:           kcachegrind
Version:        22.12.1
Release:        0
Summary:        Frontend for Cachegrind
License:        GPL-2.0-only AND BSD-4-Clause AND GFDL-1.2-only
URL:            https://apps.kde.org/kcachegrind
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)

%description
KCachegrind is a frontend for cachegrind.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
%cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name --with-qt
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kcachegrind Development Profiling

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/kcachegrind/
%{_kf5_applicationsdir}/org.kde.kcachegrind.desktop
%{_kf5_appstreamdir}/org.kde.kcachegrind.appdata.xml
%{_kf5_bindir}/dprof2calltree
%{_kf5_bindir}/hotshot2calltree
%{_kf5_bindir}/kcachegrind
%{_kf5_bindir}/memprof2calltree
%{_kf5_bindir}/op2calltree
%{_kf5_bindir}/pprof2calltree
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_sharedir}/kcachegrind/

%files lang -f %{name}.lang

%changelog
