#
# spec file for package kitemviews
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


%define lname   libKF5ItemViews5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kitemviews
Version:        5.116.0
Release:        0
Summary:        Set of item views extending the Qt model-view framework
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiPlugin) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

%description
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists.

%package -n %{lname}
Summary:        Set of item views extending the Qt model-view framework
%requires_ge    libQt5Widgets5

%description -n %{lname}
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists.

%package devel
Summary:        Set of item views extending the Qt model-view framework
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}

%description devel
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kitemviews5 --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f kitemviews5.lang

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5ItemViews.so.*
%{_kf5_debugdir}/kitemviews.categories

%files devel
%dir %{_kf5_plugindir}/designer
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5ItemViews/
%{_kf5_libdir}/libKF5ItemViews.so
%{_kf5_mkspecsdir}/qt_KItemViews.pri
%{_kf5_plugindir}/designer/kitemviews5widgets.so

%changelog
