#
# spec file for package khelpcenter
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           khelpcenter
Version:        24.05.2
Release:        0
Summary:        KDE Documentation Application
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/khelpcenter
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libxapian-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libxml-2.0)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64
# khelpcenter uses some images and stylesheets from kdoctools (boo#1011094)
Requires:       kf6-kdoctools >= %{kf6_version}
Conflicts:      kdebase4-runtime < 17.04.1
Provides:       suse_help_viewer
Provides:       khelpcenter5 = %{version}
Obsoletes:      khelpcenter5 < %{version}
Obsoletes:      khelpcenter5-lang < %{version}

%description
Application to show KDE Applications' documentation.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.khelpcenter Documentation Viewer

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.khelpcenter.desktop
%{_kf6_appstreamdir}/org.kde.khelpcenter.metainfo.xml
%{_kf6_bindir}/khelpcenter
%{_kf6_configkcfgdir}/khelpcenter.kcfg
%{_kf6_debugdir}/khelpcenter.categories
%{_kf6_sharedir}/dbus-1/services/org.kde.khelpcenter.service
%{_kf6_sharedir}/khelpcenter/
%{_libexecdir}/khc_mansearch.pl
%{_libexecdir}/khc_xapianindexer
%{_libexecdir}/khc_xapiansearch

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
