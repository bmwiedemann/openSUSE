#
# spec file for package kf6-kbookmarks
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname kbookmarks
# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kbookmarks
Version:        6.21.0
Release:        0
Summary:        Framework for manipulating bookmarks in XBEL format
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package -n libKF6Bookmarks6
Summary:        Framework for manipulating bookmarks in XBEL format
Requires:       kf6-kbookmarks >= %{version}

%description -n libKF6Bookmarks6
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package -n libKF6BookmarksWidgets6
Summary:        Framework for manipulating bookmarks in XBEL format
Requires:       kf6-kbookmarks >= %{version}

%description -n libKF6BookmarksWidgets6
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package devel
Summary:        Development files for kbookmarks, a XBEL format bookmark manipulation framework
Requires:       libKF6Bookmarks6 = %{version}
Requires:       libKF6BookmarksWidgets6 = %{version}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description devel
Development files for kbookmarks, a framework for accessing and
manipulating bookmarks using the XBEL format

%lang_package -n libKF6Bookmarks6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kbookmarks6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6Bookmarks6
%ldconfig_scriptlets -n libKF6BookmarksWidgets6

%files
%{_kf6_debugdir}/kbookmarks.categories
%{_kf6_debugdir}/kbookmarks.renamecategories
%{_kf6_debugdir}/kbookmarkswidgets.categories

%files -n libKF6Bookmarks6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Bookmarks.so.*

%files -n libKF6BookmarksWidgets6
%{_kf6_libdir}/libKF6BookmarksWidgets.so.*

%files devel
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/libKF6BookmarksWidgets.so
%{_kf6_cmakedir}/KF6Bookmarks/
%{_kf6_includedir}/KBookmarks/
%{_kf6_includedir}/KBookmarksWidgets/

%files -n libKF6Bookmarks6-lang -f kbookmarks6.lang

%changelog
