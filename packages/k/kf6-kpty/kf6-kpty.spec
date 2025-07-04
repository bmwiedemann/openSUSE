#
# spec file for package kf6-kpty
#
# Copyright (c) 2025 SUSE LLC
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

%define rname kpty
# Full KF6 version (e.g. 6.15.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kpty
Version:        6.15.0
Release:        0
Summary:        Primitives to interface with pseudo terminal devices
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%package -n libKF6Pty6
Summary:        Interfacing with pseudo terminal devices
Requires:       kf6-kpty >= %{version}

%description -n libKF6Pty6
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%package devel
Summary:        Development files for kpty, a pseudo terminal device interface
Requires:       libKF6Pty6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%lang_package -n libKF6Pty6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kpty6

%ldconfig_scriptlets -n libKF6Pty6

%files
%{_kf6_debugdir}/kpty.categories

%files -n libKF6Pty6
%license LICENSES/*
%{_kf6_libdir}/libKF6Pty.so.*

%files devel
%{_kf6_includedir}/KPty/
%{_kf6_cmakedir}/KF6Pty/
%{_kf6_libdir}/libKF6Pty.so

%files -n libKF6Pty6-lang -f kpty6.lang

%changelog
