#
# spec file for package libksane
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
Name:           libksane
Version:        24.05.2
Release:        0
Summary:        KDE scanning library
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KSaneCore6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%package -n libKSaneWidgets6
Summary:        KDE scan library
Requires:       libksane-icons
Recommends:     libksane-lang = %{version}

%description -n libKSaneWidgets6
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%package -n libksane-icons
Summary:        Icons required by libksane library
Conflicts:      libKF5Sane5 <= 23.08.5

%description -n libksane-icons
Icons required by libksane library.

%package devel
Summary:        Development files for the KDE scanning library
Requires:       libKSaneWidgets6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
This package contains a library to add scan support to KDE applications.

%lang_package -n libKSaneWidgets6

%package -n libksane-lang
Summary:        Translations for libKSaneWidgets6 and libKF5Sane6
Supplements:    libKF5Sane6 = %{version}
Supplements:    libKSaneWidgets6 = %{version}
Provides:       libksane-lang-all = %{version}
# Briefly existed in the devel project
Obsoletes:      libKF5Sane6-lang
Obsoletes:      libKSaneWidgets6-lang
BuildArch:      noarch

%description -n libksane-lang
Provides translations for packages libKSaneWidgets6 and libKF5Sane6.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKSaneWidgets6

%files -n libksane-icons
%{_kf6_iconsdir}/hicolor/16x16/actions/black-white.png
%{_kf6_iconsdir}/hicolor/16x16/actions/color.png
%{_kf6_iconsdir}/hicolor/16x16/actions/gray-scale.png

%files -n libKSaneWidgets6
%license LICENSES/*
%{_kf6_libdir}/libKSaneWidgets6.so.*

%files devel
%{_kf6_cmakedir}/KSaneWidgets6/
%{_includedir}/KSaneWidgets6/
%{_kf6_libdir}/libKSaneWidgets6.so

%files -n libksane-lang -f %{name}.lang

%changelog
