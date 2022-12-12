#
# spec file for package kjs
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


%define sonum   5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kjs
Version:        5.101.0
Release:        0
Summary:        KDE Javascript engine
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
BuildRequires:  pcre-devel
BuildRequires:  perl
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0

%description
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package -n libKF5JS%{sonum}
Summary:        KDE Javascript engine

%description -n libKF5JS%{sonum}
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package -n libKF5JSApi%{sonum}
Summary:        KDE Javascript engine
%requires_ge    libKF5JS5
%requires_ge    libQt5Core5

%description -n libKF5JSApi%{sonum}
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package devel
Summary:        KDE Javascript engine: Build Environment
Requires:       extra-cmake-modules
Requires:       libKF5JS%{sonum} = %{version}
Requires:       libKF5JSApi%{sonum} = %{version}
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript. Development files.

%lang_package -n %{name}-devel

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
  chmod +x %{buildroot}%{_kf5_datadir}/kjs/create_hash_table
%fdupes %{buildroot}

%find_lang %{name} --with-man --all-name

%post -n libKF5JS%{sonum} -p /sbin/ldconfig
%postun -n libKF5JS%{sonum} -p /sbin/ldconfig
%post -n libKF5JSApi%{sonum} -p /sbin/ldconfig
%postun -n libKF5JSApi%{sonum} -p /sbin/ldconfig

%files devel-lang -f %{name}.lang

%files -n libKF5JS%{sonum}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5JS.so.*

%files -n libKF5JSApi%{sonum}
%{_kf5_libdir}/libKF5JSApi.so.*

%files devel
%{_kf5_bindir}/kjs5
%{_kf5_libdir}/libKF5JS.so
%{_kf5_libdir}/libKF5JSApi.so
%{_kf5_libdir}/cmake/KF5JS/
%{_kf5_includedir}/
%{_kf5_datadir}/kjs/
%{_kf5_mkspecsdir}/qt_KJSApi.pri
%{_kf5_mkspecsdir}/qt_KJS.pri
%doc %lang(en) %{_kf5_mandir}/*/kjs5.*

%changelog
