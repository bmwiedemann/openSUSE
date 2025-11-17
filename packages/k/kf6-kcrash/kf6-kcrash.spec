#
# spec file for package kf6-kcrash
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

%define rname kcrash
# Full KF6 version (e.g. 6.20.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kcrash
Version:        6.20.0
Release:        0
Summary:        An application crash handler
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

%description
KCrash provides support for intercepting and handling application crashes.

%package -n libKF6Crash6
Summary:        An application crash handler
Requires:       kf6-kcrash >= %{version}
Recommends:     drkonqi6

%description -n libKF6Crash6
KCrash provides support for intercepting and handling application crashes.

%package devel
Summary:        Build environment for the KCrash application crash handler
Requires:       libKF6Crash6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
KCrash provides support for intercepting and handling application crashes.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Crash6

%files
%{_kf6_debugdir}/kcrash.categories
%{_kf6_debugdir}/kcrash.renamecategories

%files -n libKF6Crash6
%license LICENSES/*
%doc README*
%{_kf6_libdir}/libKF6Crash.so.*

%files devel
%{_kf6_cmakedir}/KF6Crash/
%{_kf6_includedir}/KCrash/
%{_kf6_libdir}/libKF6Crash.so

%changelog
