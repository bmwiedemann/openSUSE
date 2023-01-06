#
# spec file for package plasma5-nano
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


%define kf5_version 5.98.0

%bcond_without released
Name:           plasma5-nano
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.9.3)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.3 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plasma Nano
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-nano-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-nano-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
# Includes some plugins for kpackage needed during build
BuildRequires:  plasma5-workspace >= %{_plasma5_bugfix}
Requires:       kdeclarative-components
Requires:       kirigami2
Requires:       libqt5-qtgraphicaleffects
Requires:       plasma5-workspace >= %{_plasma5_bugfix}
# hardcode versions of plasma-framework-components and plasma-framework-private packages, as upstream doesn't keep backwards compability there
%requires_ge plasma-framework-components
%requires_ge plasma-framework-private
# Part of the default applet selection
Recommends:     plasma-mycroft
Recommends:     plasma-nm5

%description
A minimal plasma shell package intended for embedded devices

%lang_package

%prep
%autosetup -p1 -n plasma-nano-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%files
%license LICENSES/*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/plasma/
%dir %{_kf5_qmldir}/org/kde/plasma/private/
%{_kf5_qmldir}/org/kde/plasma/private/nanoshell/
%{_kf5_appstreamdir}/org.kde.plasma.nano.desktoptoolbox.appdata.xml
%dir %{_kf5_plasmadir}/packages/
%{_kf5_plasmadir}/packages/org.kde.plasma.nano.desktoptoolbox/
%dir %{_kf5_plasmadir}/shells
%{_kf5_plasmadir}/shells/org.kde.plasma.nano/
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.nano.desktop
%{_kf5_servicesdir}/plasma-package-org.kde.plasma.nano.desktoptoolbox.desktop

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
