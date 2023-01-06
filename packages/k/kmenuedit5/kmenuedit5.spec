#
# spec file for package kmenuedit5
#
# Copyright (c) 2023 SUSE LLC
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
Name:           kmenuedit5
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Provides the interface and basic tools for the KDE workspace
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/kmenuedit-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kmenuedit-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KHotKeysDBusInterface) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Xml)
Recommends:     %{name}-lang
Conflicts:      kdebase4-workspace < 5.3.0

%description
Provides the interface and basic tools for the KDE workspace.

%lang_package

%prep
%setup -q -n kmenuedit-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif
  %fdupes -s %{buildroot}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_bindir}/kmenuedit
%{_kf5_applicationsdir}/org.kde.kmenuedit.desktop
%{_kf5_appstreamdir}/org.kde.kmenuedit.appdata.xml
%{_kf5_sharedir}/icons/hicolor/*/*/*.*
%{_kf5_sharedir}/kmenuedit/
%{_kf5_sharedir}/kxmlgui5/
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%{_kf5_htmldir}/en/kmenuedit/
%{_kf5_debugdir}/kmenuedit.categories
%dir %{_kf5_libdir}/kconf_update_bin
%{_kf5_libdir}/kconf_update_bin/kmenuedit_globalaccel

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
