#
# spec file for package kproperty
#
# Copyright (c) 2024 SUSE LLC
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


%define sover 4
Name:           kproperty
Version:        3.2.0
Release:        0
Summary:        Property editing framework with editor widget
License:        LGPL-2.0-only
Group:          Productivity/Office/Other
URL:            https://community.kde.org/KProperty
Source0:        https://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         fix-build-with-gcc48.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)

%description
A property editing framework with editor widget similar to what is known from Qt Designer

%package -n libKPropertyCore3-%{sover}
Summary:        Core library for the Property editing framework
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKPropertyCore3-%{sover}
The Core library for the property editing framework with editor widget similar to what is known from Qt Designer

%package -n libKPropertyWidgets3-%{sover}
Summary:        Editor Widget library for the property editing framework
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKPropertyWidgets3-%{sover}
The editor widget library for the property editing framework similar to what is known from Qt Designer

%package devel
Summary:        Development package for kproperty
Group:          Development/Libraries/KDE
Requires:       libKPropertyCore3-%{sover} = %{version}
Requires:       libKPropertyWidgets3-%{sover} = %{version}

%description devel
Development package for the property editing Framework

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%find_lang %{name} %{name}.lang --all-name --with-qt

# The pkgconfig files contain incorrect stuff
rm %{buildroot}%{_kf5_libdir}/pkgconfig/KProperty*.pc

%post -n libKPropertyCore3-%{sover} -p /sbin/ldconfig
%postun -n libKPropertyCore3-%{sover} -p /sbin/ldconfig

%files -n libKPropertyCore3-%{sover}
%{_kf5_libdir}/libKPropertyCore3.so.*

%post -n libKPropertyWidgets3-%{sover} -p /sbin/ldconfig
%postun -n libKPropertyWidgets3-%{sover} -p /sbin/ldconfig

%files
%{_kf5_sharedir}/kproperty3/

%files -n libKPropertyWidgets3-%{sover}
%license COPYING.*
%{_kf5_libdir}/libKPropertyWidgets3.so.*

%files devel
%license COPYING*
%{_includedir}/KPropertyCore3/
%{_includedir}/KPropertyWidgets3/
%{_kf5_cmakedir}/KPropertyCore3/
%{_kf5_cmakedir}/KPropertyWidgets3/
%{_kf5_libdir}/libKPropertyCore3.so
%{_kf5_libdir}/libKPropertyWidgets3.so

%files lang -f %{name}.lang

%changelog
