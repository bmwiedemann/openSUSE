#
# spec file for package libkvkontakte
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define so_ver 2

Name:           libkvkontakte
Version:        5.0.0
Release:        0
Summary:        Library for asynchronous interaction with vkontakte.ru social network
License:        GPL-2.0+
Group:          System/Libraries
Url:            https://community.kde.org/LibKVkontakte
Source0:        http://download.kde.org/stable/libkvkontakte/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdewebkit-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libkvkontakte is a KDE C++ library for asynchronous interaction with
vkontakte.ru social network via its open API.

%package devel
Summary:        Development file for libkvkontakte
Group:          Development/Libraries/C and C++
Requires:       libKF5Vkontakte%{so_ver} = %{version}

%description devel
This package contains development file for libkvkontakte.

%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Requires:       libKF5Vkontakte%{so_ver} = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:%{name})
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%package -n libKF5Vkontakte%{so_ver}
Summary:        Library for asynchronous interaction with vkontakte.ru social network
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n libKF5Vkontakte%{so_ver}
libkvkontakte is a KDE C++ library for asynchronous interaction with
vkontakte.ru social network via its open API.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%find_lang %{name}

%post -n libKF5Vkontakte%{so_ver} -p /sbin/ldconfig

%postun -n libKF5Vkontakte%{so_ver} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc COPYING* NEWS README
%{_kf5_includedir}/Vkontakte/
%{_kf5_includedir}/kf5vkontakte_version.h
%{_kf5_libdir}/libKF5Vkontakte.so
%{_kf5_libdir}/cmake/KF5Vkontakte/

%files -n libKF5Vkontakte%{so_ver}
%defattr(-,root,root,-)
%doc COPYING COPYING.LGPL-2 COPYING.LIB
%{_kf5_libdir}/libKF5Vkontakte.so.*

%files lang -f %{name}.lang

%changelog
