#
# spec file for package kgamma6
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

%define rname kgamma

%bcond_without released
Name:           kgamma6
Version:        6.1.1
Release:        0
Summary:        Display gamma configuration
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
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
Provides:       kgamma = %{version}
Obsoletes:      kgamma < %{version}
Provides:       kgamma5 = %{version}
Obsoletes:      kgamma5 < %{version}
Obsoletes:      kgamma5-lang < %{version}

%description
This package contains a KDE system settings module to configure display
gamma.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/*
%{_kf6_applicationsdir}/kcm_kgamma.desktop
%dir %{_kf6_plugindir}/plasma/kcminit
%{_kf6_plugindir}/plasma/kcminit/kcm_kgamma_init.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kgamma.so
%{_kf6_sharedir}/kgamma/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
