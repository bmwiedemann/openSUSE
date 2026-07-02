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


%define kf6_version 6.19.0
%define qt6_version 6.9.0

%define rname  libkdcraw

%bcond_without released
Name:           libkdcraw
Version:        26.04.3
Release:        0
Summary:        Shared library interface around dcraw
License:        LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libraw) >= 0.18.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}

%description
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%package -n libkdcraw-qt6
Summary:        Shared library interface around dcraw

%description -n libkdcraw-qt6
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%package -n libKDcrawQt6-5
Summary:        Shared library interface around dcraw
Requires:       libkdcraw-qt6 = %{version}

%description -n libKDcrawQt6-5
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%package devel
Summary:        Shared library interface around dcraw
Requires:       libKDcrawQt6-5 = %{version}

%description devel
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKDcrawQt6-5

%files -n libkdcraw-qt6
%{_kf6_debugdir}/libkdcraw.categories

%files -n libKDcrawQt6-5
%license LICENSES/*
%{_libdir}/libKDcrawQt6.so.*

%files devel
%doc README
%{_kf6_cmakedir}/KDcrawQt6/
%{_includedir}/KDcrawQt6/
%{_libdir}/libKDcrawQt6.so

%changelog
