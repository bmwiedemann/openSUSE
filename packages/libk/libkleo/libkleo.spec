#
# spec file for package libkleo
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
Name:           libkleo
Version:        24.05.1
Release:        0
Summary:        Base package of Kleopatra, a key manager by KDE
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_headers-devel
BuildRequires:  libgpgmepp-devel >= 1.16.0
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(QGpgmeQt6) >= 1.16.0
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
libkleo is a library used by KDE PIM applications to handle cryptographic key
and certificate management.

%package -n libKPim6libkleo6
Summary:        LibKleo library for kdepim
Requires:       libkleo = %{version}

%description -n libKPim6libkleo6
This package contains the libkleo library, a library used by KDE PIM
applications to handle cryptographic key and certificate management.

%package devel
Summary:        Development package for libkleo
Requires:       libKPim6libkleo6 = %{version}
Requires:       libgpgmepp-devel >= 1.16.0
Requires:       cmake(QGpgmeQt6) >= 1.16.0

%description devel
The development package for the libkleo libraries.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6libkleo6

%files
%config %{_kf6_configdir}/libkleopatrarc
%{_kf6_debugdir}/libkleo.categories
%{_kf6_debugdir}/libkleo.renamecategories
%{_kf6_sharedir}/libkleopatra/

%files -n libKPim6libkleo6
%license LICENSES/*
%{_kf6_libdir}/libKPim6Libkleo.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Libkleo.*
%{_includedir}/KPim6/Libkleo/
%{_kf6_cmakedir}/KPim6Libkleo/
%{_kf6_libdir}/libKPim6Libkleo.so

%files lang -f %{name}.lang

%changelog
