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
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdbusaddons
Version:        5.82.0
Release:        0
Summary:        Convenience classes for QtDBus
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
%endif

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package -n %{lname}
Summary:        Convenience classes for QtDBus
Group:          System/GUI/KDE
%requires_ge    libQt5DBus5
Recommends:     %{lname}-lang = %{version}
Recommends:     %{name}-tools = %{version}

%description -n %{lname}
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package tools
Summary:        Convenience classes for QtDBus: CLI tools
Group:          Development/Tools/Debuggers

%description tools
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Aditional CLI tools.

%package devel
Summary:        Convenience classes for QtDBus: Build Environment
Group:          Development/Libraries/KDE
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

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5DBusAddons.so.*

%files tools
%{_kf5_bindir}/kquitapp5

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5DBusAddons/
%{_kf5_libdir}/libKF5DBusAddons.so
%{_kf5_mkspecsdir}/qt_KDBusAddons.pri

%changelog
