#
# spec file for package mobipocket
#
# Copyright (c) 2023 SUSE LLC
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


%define rname kdegraphics-mobipocket
%define lname libqmobipocket
%define sover 2

%bcond_without released
Name:           mobipocket
Version:        22.12.3
Release:        0
Summary:        E-book plugin and library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)

%description
Mobipocket E-book support for Okular.

%package -n %{lname}%{sover}
Summary:        E-book plugin and library
Provides:       mobipocket = %{version}
Obsoletes:      mobipocket < %{version}

%description -n %{lname}%{sover}
Mobipocket E-book plugin and library.

%package devel
Summary:        E-book plugin and library
Requires:       %{lname}%{sover} = %{version}

%description devel
Mobipocket E-book plugin and library.

This package provides development files for mobipocket
library

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n %{lname}%{sover}

%files -n %{lname}%{sover}
%license COPYING
%{_kf5_libdir}/libqmobipocket.so.*

%files devel
%{_includedir}/qmobipocket/
%{_kf5_cmakedir}/QMobipocket/
%{_kf5_libdir}/libqmobipocket.so

%changelog
