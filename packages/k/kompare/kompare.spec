#
# spec file for package kompare
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
Name:           kompare
Version:        22.12.1
Release:        0
Summary:        File Comparator
License:        GPL-2.0-only AND GFDL-1.2-only
URL:            https://apps.kde.org/kompare
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(LibKompareDiff2)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Tool to visualize changes between two versions of a file.

%package devel
Summary:        Development files for the File Comparator
Requires:       %{name} = %{version}

%description devel
Development files for the File Comparator package

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

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.kompare Utility TextEditor

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/*/
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%dir %{_kf5_sharedir}/kio
%dir %{_kf5_sharedir}/kio/servicemenus
%{_kf5_applicationsdir}/org.kde.kompare.desktop
%{_kf5_appstreamdir}/org.kde.kompare.appdata.xml
%{_kf5_bindir}/kompare
%{_kf5_debugdir}/kompare.categories
%{_kf5_iconsdir}/hicolor/*/*/kompare.*
%{_kf5_libdir}/libkomparedialogpages.so.*
%{_kf5_libdir}/libkompareinterface.so.*
%{_kf5_plugindir}/kf5/parts/kompare*part.so
%{_kf5_sharedir}/kio/servicemenus/kompare.desktop

%files devel
%{_kf5_prefix}/include/kompare/
%{_kf5_libdir}/libkompareinterface.so

%files lang -f %{name}.lang

%changelog
