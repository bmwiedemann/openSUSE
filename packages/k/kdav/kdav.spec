#
# spec file for package kdav
#
# Copyright (c) 2020 SUSE LLC
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


%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without  lang
Name:           kdav
Version:        5.74.0
Release:        0
Summary:        DAV protocol implementation
License:        LGPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5XmlPatterns)
Recommends:     %{name}-lang

%description
kdav is a library providing a KJob-based implementation of DAV protocols such as
CardDAV, WebDAV, and CalDAV.

%package -n libKF5DAV5
Summary:        Core library for kdav
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5DAV5
kdav is a library providing a KJob-based implementation of DAV protocols such as
CardDAV, WebDAV, and CalDAV.

%package devel
Summary:        Development package for kdav
Group:          Development/Libraries/KDE
Requires:       libKF5DAV5 = %{version}

%description devel
This package contains development files needed to use kdav in other applications.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5DAV5 -p /sbin/ldconfig
%postun -n libKF5DAV5 -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README.md
%{_kf5_debugdir}/kdav.categories
%{_kf5_debugdir}/kdav.renamecategories

%files -n libKF5DAV5
%license LICENSES/*
%doc README.md
%{_kf5_libdir}/libKF5DAV.so.5
%{_kf5_libdir}/libKF5DAV.so.5.*

%files devel
%license LICENSES/*
%doc README.md
%{_includedir}/KF5/
%{_kf5_libdir}/cmake/KF5DAV/
%{_kf5_libdir}/libKF5DAV.so
%{_kf5_mkspecsdir}/qt_kdav.pri

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
