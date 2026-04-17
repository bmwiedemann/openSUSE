#
# spec file for package libkdcraw
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define rname  libkdcraw
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define kf6_version 6.19.0
%define qt6_version 6.9.0
%define library_name libKDcrawQt6
%define so_suffix -5
%else
ExclusiveArch:  do_not_build
%endif
%bcond_without released
Name:           libkdcraw%{?pkg_suffix}
Version:        26.04.0
Release:        0
Summary:        Shared library interface around dcraw
License:        LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libraw) >= 0.18.0
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
%endif

%description
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.  The library documentation is available on header
files.

This library is used by kipi-plugins, digiKam and others kipi host
programs.

%package -n %{library_name}%{so_suffix}
Summary:        Shared library interface around dcraw
Requires:       %{name} >= %{version}

%description -n %{library_name}%{so_suffix}
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.  The library documentation is available on header
files.

This library is used by kipi-plugins, digiKam and others kipi host
programs.

%package devel
Summary:        Shared library interface around dcraw
Requires:       %{library_name}%{so_suffix} = %{version}

%description devel
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.  The library documentation is available on header
files.

This library is used by kipi-plugins, digiKam and others kipi host
programs.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_kf6
%kf6_build
%endif

%install
%if 0%{?qt6}
%kf6_install
%endif

%ldconfig_scriptlets -n %{library_name}%{so_suffix}

%files
%if 0%{?qt6}
%{_kf6_debugdir}/libkdcraw.categories
%endif

%files -n %{library_name}%{so_suffix}
%license LICENSES/*
%{_libdir}/%{library_name}.so.*

%files devel
%doc README
%if 0%{?qt6}
%{_kf6_cmakedir}/KDcrawQt6/
%{_includedir}/KDcrawQt6/
%endif
%{_libdir}/%{library_name}.so

%changelog
