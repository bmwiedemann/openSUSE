#
# spec file for package plasma6-pa
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-pa
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-pa
Version:        6.1.1
Release:        0
Summary:        The Plasma6 Volume Manager
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6PulseAudioQt)
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       (pulseaudio-module-x11 or pipewire-pulseaudio)
# boo#1092871
Recommends:     (pulseaudio-module-gsettings if pulseaudio)
Supplements:    (plasma6-desktop and (pulseaudio or pipewire-pulseaudio))
Provides:       plasma5-pa = %{version}
Obsoletes:      plasma5-pa < %{version}
Obsoletes:      plasma5-pa-lang < %{version}
%if 0%{?suse_version} > 1500
Suggests:       pipewire-pulseaudio
%else
Suggests:       pulseaudio-module-x11
%endif

%description
A volume manager plasmoid superseding kmix.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %{_kf6_htmldir}/en/kcontrol/
%{_kf6_applicationsdir}/kcm_pulseaudio.desktop
%{_kf6_appstreamdir}/org.kde.plasma.volume.appdata.xml
%{_kf6_libdir}/libplasma-volume.so.*
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.volume/
%{_kf6_plugindir}/kf6/kded/audioshortcutsservice.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_pulseaudio.so
%dir %{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qmldir}/org/kde/plasma/private/volume/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol

%changelog
