#
# spec file for package kompare
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kompare
Version:        24.12.0
Release:        0
Summary:        File Comparator
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kompare
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KompareDiff2) >= 6
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       kompare5 = %{version}
Obsoletes:      kompare5 < %{version}

%description
Tool to visualize changes between two versions of a file.

%package devel
Summary:        Development files for the File Comparator
Requires:       kompare = %{version}

%description devel
Development files for the File Comparator package

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.kompare.desktop
%{_kf6_appstreamdir}/org.kde.kompare.appdata.xml
%{_kf6_bindir}/kompare
%{_kf6_debugdir}/kompare.categories
%{_kf6_iconsdir}/hicolor/*/*/kompare.*
%{_kf6_libdir}/libkomparedialogpages.so.*
%{_kf6_libdir}/libkompareinterface.so.*
%{_kf6_plugindir}/kf6/parts/komparenavtreepart.so
%{_kf6_plugindir}/kf6/parts/komparepart.so
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/kompare.desktop

%files devel
%{_includedir}/kompare/
%{_kf6_libdir}/libkompareinterface.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
