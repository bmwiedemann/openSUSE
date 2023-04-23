#
# spec file for package kmime
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


%define kf5_version 5.103.0
%bcond_without released
%define libname libKPim5Mime5
Name:           kmime
Version:        23.04.0
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
Conflicts:      libKF5Mime5 < %{version}

%description
This package contains the basic packages for KDE PIM applications.

%package -n %{libname}
Summary:        KDE PIM libraries MIME Support
%requires_eq    %{name}
# Renamed
Obsoletes:      kmime-lang <= 23.04.0

%description  -n %{libname}
This package provides MIME support for KDE PIM applications

%package devel
Summary:        Build environment for the KDE PIM MIME libraries
Requires:       %{libname} = %{version}
Requires:       cmake(KF5Codecs)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n %{libname}

%prep
%autosetup -p1 -n kmime-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSES/*
%{_kf5_debugdir}/kmime.categories

%files -n %{libname}
%{_kf5_libdir}/libKPim5Mime.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KMime/
%{_kf5_cmakedir}/KF5Mime/
%{_kf5_cmakedir}/KPim5Mime/
%{_kf5_libdir}/libKPim5Mime.so
%{_kf5_mkspecsdir}/qt_KMime.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
