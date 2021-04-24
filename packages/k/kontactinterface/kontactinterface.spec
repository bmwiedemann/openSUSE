#
# spec file for package kontactinterface
#
# Copyright (c) 2021 SUSE LLC
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


%define kf5_version 5.79.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kontactinterface
Version:        21.04.0
Release:        0
Summary:        KDE PIM Libraries: Interface to Contacts
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
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

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKF5KontactInterface5
Summary:        KDE PIM Libraries: Interface to Contacts
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5KontactInterface5
This package provides the interface to contacts for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       libKF5KontactInterface5 = %{version}
Requires:       cmake(KF5Parts) >= %{kf5_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=OFF -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5KontactInterface5 -p /sbin/ldconfig
%postun -n libKF5KontactInterface5 -p /sbin/ldconfig

%files -n libKF5KontactInterface5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5KontactInterface.so.*
%{_kf5_servicetypesdir}/kontactplugin.desktop

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KF5KontactInterface/
%{_kf5_includedir}/KontactInterface/
%{_kf5_includedir}/kontactinterface_version.h
%{_kf5_libdir}/libKF5KontactInterface.so
%{_kf5_mkspecsdir}/qt_KontactInterface.pri

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
