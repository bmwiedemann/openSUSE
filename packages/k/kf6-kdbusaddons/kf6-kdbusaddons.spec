#
# spec file for package kf6-kdbusaddons
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname kdbusaddons
# Full KF6 version (e.g. 6.20.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kdbusaddons
Version:        6.20.0
Release:        0
Summary:        Convenience classes for QtDBus
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package -n libKF6DBusAddons6
Summary:        Convenience classes for QtDBus
Requires:       kf6-kdbusaddons = %{version}
Recommends:     kf6-kdbusaddons-tools = %{version}

%description -n libKF6DBusAddons6
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package tools
Summary:        Convenience classes for QtDBus: CLI tools

%description tools
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Aditional CLI tools.

%package devel
Summary:        Convenience classes for QtDBus: Build Environment
Requires:       kf6-extra-cmake-modules
Requires:       libKF6DBusAddons6 = %{version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}

%description devel
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Development files.

%lang_package -n libKF6DBusAddons6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kdbusaddons6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6DBusAddons6

%files
%{_kf6_debugdir}/kdbusaddons.categories
%{_kf6_debugdir}/kdbusaddons.renamecategories

%files -n libKF6DBusAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6DBusAddons.so.*

%files tools
%{_kf6_bindir}/kquitapp6

%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_cmakedir}/KF6DBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so

%files -n libKF6DBusAddons6-lang -f kdbusaddons6.lang

%changelog
