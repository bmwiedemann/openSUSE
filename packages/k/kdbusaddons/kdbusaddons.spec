#
# spec file for package kdbusaddons
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


%define lname   libKF5DBusAddons5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdbusaddons
Version:        5.101.0
Release:        0
Summary:        Convenience classes for QtDBus
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
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package -n %{lname}
Summary:        Convenience classes for QtDBus
%requires_ge    libQt5DBus5
Recommends:     %{name}-tools = %{version}

%description -n %{lname}
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package tools
Summary:        Convenience classes for QtDBus: CLI tools

%description tools
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Aditional CLI tools.

%package devel
Summary:        Convenience classes for QtDBus: Build Environment
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5DBus) >= 5.15.0

%description devel
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kdbusaddons5 --with-qt --without-mo

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f kdbusaddons5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5DBusAddons.so.*

%files tools
%{_kf5_bindir}/kquitapp5

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5DBusAddons/
%{_kf5_libdir}/libKF5DBusAddons.so
%{_kf5_mkspecsdir}/qt_KDBusAddons.pri

%changelog
