#
# spec file for package libksane-kf5
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


%define kf5_version 5.90.0
%define qt5_version 5.15.2

%define rname libksane

%bcond_without released
Name:           libksane-kf5
Version:        24.05.1
Release:        0
Summary:        KDE scanning library
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source0:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KSaneCore) >= 24.02.2
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

%description
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%package -n libKF5Sane6
Summary:        KDE scan library
Requires:       libksane-icons
Recommends:     libksane-lang = %{version}

%description -n libKF5Sane6
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%package devel
Summary:        Development files for the KDE scanning library
Requires:       libKF5Sane6 = %{version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}
# libksane-devel is now the KF6/Qt6 based one
Provides:       libksane-devel = 23.08.4
Obsoletes:      libksane-devel <= 23.08.4

%description devel
This package contains a library to add scan support to KDE
applications.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

# Only one translation package for both flavors
rm -r %{buildroot}%{_datadir}/locale

%ldconfig_scriptlets -n libKF5Sane6

%files -n libKF5Sane6
%license COPYING*
%{_kf5_libdir}/libKF5Sane.so.*
# Icons are already packaged in libksane-icons
%exclude %{_kf5_iconsdir}/

%files devel
%{_kf5_cmakedir}/KF5Sane/
%{_kf5_includedir}/KSane/
%{_kf5_libdir}/libKF5Sane.so

%changelog
