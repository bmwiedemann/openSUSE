#
# spec file for package kpty
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


%define lname   libKF5Pty5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kpty
Version:        5.75.0
Release:        0
Summary:        Primitives to interface with pseudo terminal devices
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
BuildRequires:  utempter-devel
BuildRequires:  cmake(KF5CoreAddons) >= %{_tar_path}
BuildRequires:  cmake(KF5I18n) >= %{_tar_path}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0

%description
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%package -n %{lname}
Summary:        Interfacing with pseudo terminal devices
Group:          System/GUI/KDE
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%package devel
Summary:        Development files for kpty, a pseudo terminal device interface
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5CoreAddons) >= %{_tar_path}
Requires:       cmake(Qt5Core) >= 5.12.0

%description devel
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Pty.so.*
%{_kf5_debugdir}/kpty.categories

%files devel
%license LICENSES/*
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*.h
%{_kf5_includedir}/*/
%{_kf5_libdir}/cmake/KF5Pty/
%{_kf5_libdir}/libKF5Pty.so
%{_kf5_mkspecsdir}/qt_KPty.pri

%changelog
