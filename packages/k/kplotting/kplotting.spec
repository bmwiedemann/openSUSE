#
# spec file for package kplotting
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


%define lname   libKF5Plotting5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           kplotting
Version:        5.75.0
Release:        0
Summary:        KDE Data plotting library
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_tar_path}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0

%description
KPlotWidget is a QWidget-derived class that provides a virtual base
class for data plotting. The idea behind KPlotWidget is that a
developer only has to specify information in "data units", i.e. the
natural units of the data being plotted. KPlotWidget automatically
converts everything to screen pixel units.

%package -n %{lname}
Summary:        KDE Data plotting library
Group:          System/GUI/KDE
%requires_ge    libQt5Widgets5

%description -n %{lname}
KPlotWidget is a QWidget-derived class that provides a virtual base
class for data plotting. The idea behind KPlotWidget is that a
developer only has to specify information in "data units", i.e. the
natural units of the data being plotted. KPlotWidget automatically
converts everything to screen pixel units.

%package devel
Summary:        Build environment for the KDE data plotting library
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Widgets) >= 5.12.0

%description devel
Development files for KPlotWidget, which is a QWidget-derived class
that provides a virtual base class for data plotting.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Plotting.so.*

%files devel
%license LICENSES/*
%dir %{_kf5_plugindir}/designer
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Plotting/
%{_kf5_libdir}/libKF5Plotting.so
%{_kf5_mkspecsdir}/qt_KPlotting.pri
%{_kf5_plugindir}/designer/kplotting5widgets.so

%changelog
