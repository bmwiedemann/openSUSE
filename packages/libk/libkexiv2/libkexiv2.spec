#
# spec file for package libkexiv2
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


%define rname  libkexiv2
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define kf6_version 6.19.0
%define qt6_version 6.9.0
%define library_name libKExiv2Qt6
%define so_suffix -0
%else
ExclusiveArch: do_not_build
%endif
%bcond_without released
Name:           libkexiv2%{?pkg_suffix}
Version:        25.12.0
Release:        0
Summary:        Library to manipulate picture meta data
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2) >= 0.25
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
%endif

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.

%package -n %{library_name}%{so_suffix}
Summary:        Library to manipulate picture meta data
Requires:       %{name} >= %{version}

%description -n %{library_name}%{so_suffix}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.

%package devel
Summary:        Build environment for libkexiv2
Requires:       %{library_name}%{so_suffix} = %{version}

%description devel
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE
%kf6_build
%endif

%install
%if 0%{?qt6}
%kf6_install
%endif

%ldconfig_scriptlets -n %{library_name}%{so_suffix}

%files
%if 0%{?qt6}
%{_kf6_debugdir}/libkexiv2.categories
%endif

%files -n %{library_name}%{so_suffix}
%license LICENSES/*
%doc README
%{_libdir}/%{library_name}.so.*

%files devel
%if 0%{?qt6}
%{_kf6_cmakedir}/KExiv2Qt6/
%{_includedir}/KExiv2Qt6/
%endif
%{_libdir}/%{library_name}.so

%changelog
