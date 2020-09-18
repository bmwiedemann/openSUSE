#
# spec file for package attica-qt5
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


%define sonum   5
%define rname attica
%define _libname KF5Attica
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           attica-qt5
Version:        5.74.0
Release:        0
Summary:        Open Collaboration Service client library
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Network) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0

%description
Attica is a library to access Open Collaboration Service servers.

%package -n lib%{_libname}%{sonum}
Summary:        Open Collaboration Service client library - development files
Group:          System/GUI/KDE
Requires:       %{name} >= %{_kf5_bugfix_version}
%requires_ge    libQt5Core5
%requires_ge    libQt5Network5

%description -n lib%{_libname}%{sonum}
Attica is a library to access Open Collaboration Service servers.

%package -n attica-qt5-devel
Summary:        Open Collaboration Service client library - development files
Group:          Development/Libraries/C and C++
Requires:       lib%{_libname}%{sonum} = %{version}
Requires:       cmake(Qt5Core) >= 5.12.0
Requires:       cmake(Qt5Network) >= 5.12.0
Requires:       cmake(Qt5Widgets) >= 5.12.0

%description -n attica-qt5-devel
Development files for attica, Attica a library to access Open Collaboration Service servers.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%post -n lib%{_libname}%{sonum} -p /sbin/ldconfig
%postun -n lib%{_libname}%{sonum} -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/attica.categories
%{_kf5_debugdir}/attica.renamecategories

%files -n lib%{_libname}%{sonum}
%license LICENSES/*
%doc README*
%{_libqt5_libdir}/lib%{_libname}*.so.*

%files -n attica-qt5-devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Attica/
%{_kf5_mkspecsdir}/qt_Attica.pri
%{_libqt5_libdir}/lib%{_libname}*.so
%{_libqt5_libdir}/pkgconfig/libKF5Attica.pc

%changelog
