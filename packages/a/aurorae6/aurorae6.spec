#
# spec file for package plasma6-aurorae
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define rname aurorae
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           aurorae6
Version:        6.6.1
Release:        0
Summary:        Themeable window decoration for KWin
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDecoration3) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Aurorae is a themeable window decoration for KWin.

It supports theme files consisting of several SVG files for decoration and
buttons. Themes can be installed and selected directly in the configuration
module of KWin decorations.

%package devel
Summary:        Themeable window decoration for KWin
Requires:       aurorae6 = %{version}

%description devel
Aurorae is a themeable window decoration for KWin.

It supports theme files consisting of several SVG files for decoration and
buttons. Themes can be installed and selected directly in the configuration
module of KWin decorations.

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
%doc README
%{_kf6_knsrcfilesdir}/aurorae.knsrc
%dir %{_kf6_plugindir}/org.kde.kdecoration3
%{_kf6_plugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.so
%{_kf6_plugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.v2.so
%dir %{_kf6_plugindir}/org.kde.kdecoration3.kcm
%{_kf6_plugindir}/org.kde.kdecoration3.kcm/kcm_auroraedecoration.so
%dir %{_kf6_qmldir}/org/kde/kwin
%dir %{_kf6_qmldir}/org/kde/kwin/decoration
%{_kf6_qmldir}/org/kde/kwin/decoration/*
%dir %{_kf6_qmldir}/org/kde/kwin/decorations
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/
%dir %{_kf6_sharedir}/kwin
%{_kf6_sharedir}/kwin/aurorae/
%dir %{_kf6_sharedir}/kwin/decorations
%{_kf6_sharedir}/kwin/decorations/kwin4_decoration_qml_plastik/
%{_libexecdir}/plasma-apply-aurorae

%files devel
%{_kf6_cmakedir}/Aurorae/

%files lang -f %{name}.lang

%changelog
