#
# spec file for package libkleo
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkleo
Version:        22.12.1
Release:        0
Summary:        Base package of Kleopatra, a key manager by KDE
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qt5Widgets)

%description
libkleo is a library used by KDE PIM applications to handle cryptographic key
and certificate management.

%package -n libKF5Libkleo5
Summary:        LibKleo library for kdepim
License:        LGPL-2.1-or-later
Requires:       libkleo = %{version}

%description -n libKF5Libkleo5
This package contains the libkleo library, a library used by KDE PIM
applications to handle cryptographic key and certificate management.

%package devel
Summary:        Development package for libkleo
License:        LGPL-2.1-or-later
Requires:       libKF5Libkleo5 = %{version}
Requires:       libgpgmepp-devel
Requires:       cmake(QGpgme)

%description devel
The development package for the libkleo libraries.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5Libkleo5 -p /sbin/ldconfig
%postun -n libKF5Libkleo5 -p /sbin/ldconfig

%files
%config %{_kf5_configdir}/libkleopatrarc
%{_kf5_debugdir}/libkleo.categories
%{_kf5_debugdir}/libkleo.renamecategories
%{_kf5_sharedir}/libkleopatra/

%files -n libKF5Libkleo5
%license LICENSES/*
%{_kf5_libdir}/libKF5Libkleo.so.*

%files devel
%{_kf5_cmakedir}/KF5Libkleo/
%{_kf5_includedir}/Libkleo/
%{_kf5_libdir}/libKF5Libkleo.so
%{_kf5_mkspecsdir}/qt_Libkleo.pri

%files lang -f %{name}.lang

%changelog
