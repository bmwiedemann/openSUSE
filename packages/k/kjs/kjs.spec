#
# spec file for package kjs
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
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kjs
Version:        5.75.0
Release:        0
Summary:        KDE Javascript engine
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pcre-devel
BuildRequires:  perl
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0

%description
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package -n libKF5JS%{sonum}
Summary:        KDE Javascript engine
Group:          System/GUI/KDE

%description -n libKF5JS%{sonum}
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package -n libKF5JSApi%{sonum}
Summary:        KDE Javascript engine
Group:          System/GUI/KDE
%requires_ge    libKF5JS5
%requires_ge    libQt5Core5

%description -n libKF5JSApi%{sonum}
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package devel
Summary:        KDE Javascript engine: Build Environment
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules
Requires:       libKF5JS%{sonum} = %{version}
Requires:       libKF5JSApi%{sonum} = %{version}
Requires:       cmake(Qt5Core) >= 5.12.0
%if %{with lang}
Recommends:     %{name}-devel-lang = %{version}
%endif

%description devel
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript. Development files.

%lang_package -n %{name}-devel

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  chmod +x %{buildroot}%{_kf5_datadir}/kjs/create_hash_table
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%endif

%post -n libKF5JS%{sonum} -p /sbin/ldconfig
%postun -n libKF5JS%{sonum} -p /sbin/ldconfig
%post -n libKF5JSApi%{sonum} -p /sbin/ldconfig
%postun -n libKF5JSApi%{sonum} -p /sbin/ldconfig

%if %{with lang}
%files devel-lang -f %{name}.lang
%endif

%files -n libKF5JS%{sonum}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5JS.so.*

%files -n libKF5JSApi%{sonum}
%license COPYING*
%doc README*
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
