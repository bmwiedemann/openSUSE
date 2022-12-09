#
# spec file for package libksane
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


%define _so 5
%define lname libKF5Sane
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libksane
Version:        22.12.0
Release:        0
Summary:        KDE scanning library
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  sane-backends-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KSaneCore)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%package devel
Summary:        Development files for the KDE scanning library
Requires:       %{lname}%{_so} = %{version}
Requires:       pkgconfig
Requires:       sane-backends-devel
Requires:       cmake(KF5Wallet)
Requires:       cmake(KF5WidgetsAddons)
Requires:       cmake(Qt5Widgets)
Obsoletes:      libksane-kf5-devel < %{version}
Provides:       libksane-kf5-devel = %{version}

%description devel
This package contains a library to add scan support to KDE
applications.

%package -n %{lname}%{_so}
Summary:        KDE scan library
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n %{lname}%{_so}
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n %{lname}%{_so} -p /sbin/ldconfig
%postun -n %{lname}%{_so} -p /sbin/ldconfig

%files -n %{lname}%{_so}
%license COPYING*
%{_kf5_iconsdir}/hicolor/*/actions/black-white.png
%{_kf5_iconsdir}/hicolor/*/actions/color.png
%{_kf5_iconsdir}/hicolor/*/actions/gray-scale.png
%{_kf5_libdir}/%{lname}.so.*

%files devel
%{_kf5_cmakedir}/KF5Sane/
%{_kf5_includedir}/KSane/
%{_kf5_includedir}/ksane_version.h
%{_kf5_libdir}/%{lname}.so

%files lang -f %{name}.lang

%changelog
