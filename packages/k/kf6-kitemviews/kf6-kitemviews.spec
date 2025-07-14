#
# spec file for package kf6-kitemviews
#
# Copyright (c) 2025 SUSE LLC
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

%define rname kitemviews
# Full KF6 version (e.g. 6.16.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kitemviews
Version:        6.16.0
Release:        0
Summary:        Set of item views extending the Qt model-view framework
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists.

%package -n libKF6ItemViews6
Summary:        Set of item views extending the Qt model-view framework
Requires:       kf6-kitemviews >= %{version}

%description -n libKF6ItemViews6
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists.

%package devel
Summary:        Set of item views extending the Qt model-view framework
Requires:       libKF6ItemViews6 = %{version}

%description devel
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists. Development files.

%lang_package -n libKF6ItemViews6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kitemviews6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6ItemViews6

%files
%{_kf6_debugdir}/kitemviews.categories

%files -n libKF6ItemViews6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6ItemViews.so.*

%files devel
%{_kf6_includedir}/KItemViews/
%{_kf6_cmakedir}/KF6ItemViews/
%{_kf6_libdir}/libKF6ItemViews.so
%{_kf6_plugindir}/designer/kitemviews6widgets.so

%files -n libKF6ItemViews6-lang -f kitemviews6.lang

%changelog
