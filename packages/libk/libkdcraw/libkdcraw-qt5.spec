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


%define kf5_version 5.91.0
%define qt5_version 5.15.0

%define rname  libkdcraw

%bcond_without released
Name:           libkdcraw-qt5
Version:        25.12.3
Release:        0
Summary:        Shared library interface around dcraw
License:        LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libraw) >= 0.18.0
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
Provides:       libkdcraw = %{version}
Obsoletes:      libkdcraw < %{version}
Provides:       libkdcraw-kf5 = %{version}
Obsoletes:      libkdcraw-kf5 < %{version}

%description
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%package -n libKF5Dcraw5
Summary:        Shared library interface around dcraw
Requires:       libkdcraw-qt5 = %{version}

%description -n libKF5Dcraw5
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%package devel
Summary:        Shared library interface around dcraw
Requires:       libKF5Dcraw5 = %{version}
Provides:       libkdcraw-devel = %{version}
Obsoletes:      libkdcraw-devel < %{version}
Provides:       libkdcraw-kf5-devel = %{version}
Obsoletes:      libkdcraw-kf5-devel < %{version}

%description devel
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n libKF5Dcraw5

%files
%{_kf5_debugdir}/libkdcraw.categories

%files -n libKF5Dcraw5
%license LICENSES/*
%{_libdir}/libKF5KDcraw.so.*

%files devel
%doc README
%{_kf5_cmakedir}/KF5KDcraw/
%{_kf5_includedir}/KDCRAW/
%{_libdir}/libKF5KDcraw.so

%changelog
