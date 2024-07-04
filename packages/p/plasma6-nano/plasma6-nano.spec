#
# spec file for package plasma6-nano
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


%global __requires_exclude qt6qmlimport\\(org\\.kde\\.plasma\\.private\\.nanoshell.*

%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-nano

%bcond_without released
Name:           plasma6-nano
Version:        6.1.2
Release:        0
# Full Plasma 6 version (e.g. 5.9.3)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Minimal Plasma shell for embedded devices
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
Requires:       plasma6-workspace >= %{_plasma6_bugfix}
# hardcode versions of plasma6-framework-components, as upstream doesn't keep backwards compability there
%requires_ge    plasma6-framework-components
# Part of the default applet selection
# TODO remove? there's no such package
# Recommends:     plasma-mycroft
Recommends:     plasma6-nm
Provides:       plasma5-nano = %{version}
Obsoletes:      plasma5-nano < %{version}
Obsoletes:      plasma5-nano-lang < %{version}

%description
A minimal plasma shell package intended for embedded devices

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%{_kf6_appstreamdir}/org.kde.plasma.nano.desktoptoolbox.appdata.xml
%dir %{_kf6_plasmadir}/packages/
%{_kf6_plasmadir}/packages/org.kde.plasma.nano.desktoptoolbox/
%dir %{_kf6_plasmadir}/shells
%{_kf6_plasmadir}/shells/org.kde.plasma.nano/
%dir %{_kf6_qmldir}/org/kde/plasma/
%dir %{_kf6_qmldir}/org/kde/plasma/private/
%{_kf6_qmldir}/org/kde/plasma/private/nanoshell/

%files lang -f %{name}.lang

%changelog
