#
# spec file for package dolphin-plugins
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
Name:           dolphin-plugins
Version:        24.05.1
Release:        0
Summary:        Version control plugins for Dolphin
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(DolphinVcs) >= 24.02.0
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Recommends:     dolphin

%description
Dolphin file manager specific version control plugins that:
- Show the version state of a file by an emblem + color
- Provide a context menu with version control specific actions
- Provide context menu actions to mount ISO disk images

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif

%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_appstreamdir}/org.kde.dolphin-plugins.metainfo.xml
%{_kf6_configkcfgdir}/fileviewgitpluginsettings.kcfg
%{_kf6_configkcfgdir}/fileviewhgpluginsettings.kcfg
%{_kf6_configkcfgdir}/fileviewsvnpluginsettings.kcfg
%dir %{_kf6_plugindir}/dolphin
%dir %{_kf6_plugindir}/dolphin/vcs
%{_kf6_plugindir}/dolphin/vcs/fileviewbazaarplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewdropboxplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewgitplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewhgplugin.so
%{_kf6_plugindir}/dolphin/vcs/fileviewsvnplugin.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/makefileactions.so
%{_kf6_plugindir}/kf6/kfileitemaction/mountisoaction.so

%files lang -f %{name}.lang

%changelog
