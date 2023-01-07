#
# spec file for package kmime
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


%define kf5_version 5.99.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kmime
Version:        22.12.1
Release:        0
Summary:        KDE PIM libraries MIME support
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(Qt5Test)

%description
This package contains the basic packages for KDE PIM applications.

%package -n libKF5Mime5
Summary:        KDE PIM libraries MIME Support
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5Mime5
This package provides MIME support for KDE PIM applications

%package devel
Summary:        Build environment for the KDE PIM MIME libraries
Requires:       libKF5Mime5 = %{version}
Requires:       cmake(KF5Codecs)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n kmime-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5Mime5 -p /sbin/ldconfig
%postun -n libKF5Mime5 -p /sbin/ldconfig

%files -n libKF5Mime5
%license LICENSES/*
%{_kf5_libdir}/libKF5Mime.so.*
%{_kf5_debugdir}/kmime.categories

%files devel
%{_kf5_cmakedir}/KF5Mime/
%{_kf5_includedir}/KMime/
%{_kf5_libdir}/libKF5Mime.so
%{_kf5_mkspecsdir}/qt_KMime.pri

%files lang -f %{name}.lang

%changelog
