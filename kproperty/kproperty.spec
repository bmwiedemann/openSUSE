#
# spec file for package kproperty
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang

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
%setup -q
%patch0 -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
  %kf5_makeinstall -C build
  %find_lang %{name} %{name}.lang --all-name --with-qt

%post -n libKPropertyCore3-%{sover} -p /sbin/ldconfig
%postun -n libKPropertyCore3-%{sover} -p /sbin/ldconfig

%files -n libKPropertyCore3-%{sover}
%{_libdir}/libKPropertyCore3.so.*

%post -n libKPropertyWidgets3-%{sover} -p /sbin/ldconfig
%postun -n libKPropertyWidgets3-%{sover} -p /sbin/ldconfig

%files -n libKPropertyWidgets3-%{sover}
%license COPYING.*
%{_libdir}/libKPropertyWidgets3.so.*

%files devel
%license COPYING*
%{_includedir}/KPropertyCore3/
%{_includedir}/KPropertyWidgets3/
%{_libdir}/libKPropertyWidgets3.so
%{_libdir}/libKPropertyCore3.so
%{_libdir}/cmake/KPropertyCore3/
%{_libdir}/cmake/KPropertyWidgets3/
%{_libdir}/pkgconfig/KProperty*.pc

%files
%{_datadir}/kproperty3/

%files lang -f %{name}.lang

%changelog
