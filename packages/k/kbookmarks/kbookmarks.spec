#
# spec file for package kbookmarks
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


%define lname   libKF5Bookmarks5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kbookmarks
Version:        5.101.0
Release:        0
Summary:        Framework for manipulating bookmarks in XBEL format
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
Requires:       cmake(Qt5DBus) >= 5.15.0
Requires:       cmake(Qt5Widgets) >= 5.15.0
Requires:       cmake(Qt5Xml) >= 5.15.0

%description
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package -n %{lname}
Summary:        Framework for manipulating bookmarks in XBEL format

%description -n %{lname}
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package devel
Summary:        Development files for kbookmarks, a XBEL format bookmark manipulation framework
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Widgets) >= 5.15.0
Requires:       cmake(Qt5Xml) >= 5.15.0

%description devel
Development files for kbookmarks, a framework for accessing and
manipulating bookmarks using the XBEL format

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kbookmarks5 --with-qt --without-mo

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f kbookmarks5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5Bookmarks.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5Bookmarks.so
%{_kf5_libdir}/cmake/KF5Bookmarks/
%{_kf5_includedir}/KBookmarks/
%{_kf5_mkspecsdir}/qt_KBookmarks.pri

%changelog
