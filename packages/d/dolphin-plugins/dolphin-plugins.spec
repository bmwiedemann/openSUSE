#
# spec file for package dolphin-plugins
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
Name:           dolphin-plugins
Version:        22.12.0
Release:        0
Summary:        Version control plugins for Dolphin
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(DolphinVcs)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     dolphin >= %{_kapp_version}

%description
Dolphin file manager specific version control plugins that:
- Show the version state of a file by an emblem + color
- Provide a context menu with version control specific actions

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%dir %{_kf5_plugindir}/dolphin
%dir %{_kf5_plugindir}/dolphin/vcs
%{_kf5_appstreamdir}/org.kde.dolphin-plugins.metainfo.xml
%{_kf5_configkcfgdir}/fileviewgitpluginsettings.kcfg
%{_kf5_configkcfgdir}/fileviewhgpluginsettings.kcfg
%{_kf5_configkcfgdir}/fileviewsvnpluginsettings.kcfg
%{_kf5_plugindir}/dolphin/vcs/fileviewbazaarplugin.so
%{_kf5_plugindir}/dolphin/vcs/fileviewdropboxplugin.so
%{_kf5_plugindir}/dolphin/vcs/fileviewgitplugin.so
%{_kf5_plugindir}/dolphin/vcs/fileviewhgplugin.so
%{_kf5_plugindir}/dolphin/vcs/fileviewsvnplugin.so
%{_kf5_plugindir}/kf5/kfileitemaction/mountisoaction.so

%files lang -f %{name}.lang

%changelog
