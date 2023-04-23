#
# spec file for package kontactinterface
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


%define kf5_version 5.99.0
%bcond_without released
Name:           kontactinterface
Version:        23.04.0
Release:        0
Summary:        KDE PIM Libraries: Interface to Contacts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5Parts) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5X11Extras)

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKPim5KontactInterface5
Summary:        KDE PIM Libraries: Interface to Contacts
Provides:       %{name} = %{version}
# Renamed
Obsoletes:      kontactinterface-lang <= 23.04.0

%description  -n libKPim5KontactInterface5
This package provides the interface to contacts for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKPim5KontactInterface5 = %{version}
Requires:       cmake(KF5Parts) >= %{kf5_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n libKPim5KontactInterface5

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang libKPim5KontactInterface5 --with-man --all-name

%ldconfig_scriptlets -n libKPim5KontactInterface5

%files -n libKPim5KontactInterface5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKPim5KontactInterface.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KontactInterface/
%{_kf5_cmakedir}/KF5KontactInterface/
%{_kf5_cmakedir}/KPim5KontactInterface/
%{_kf5_libdir}/libKPim5KontactInterface.so
%{_kf5_mkspecsdir}/qt_KontactInterface.pri

%files -n libKPim5KontactInterface5-lang -f libKPim5KontactInterface5.lang

%changelog
