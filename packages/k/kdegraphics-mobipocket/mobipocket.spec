#
# spec file for package mobipocket
#
# Copyright (c) 2024 SUSE LLC
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


%define qt5_version 5.15.2

%define rname kdegraphics-mobipocket

%bcond_without released
Name:           mobipocket
Version:        24.05.2
Release:        0
Summary:        E-book plugin and library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}

%description
Mobipocket E-book support for Okular.

%package -n libqmobipocket2
Summary:        E-book plugin and library
Provides:       mobipocket = %{version}
Obsoletes:      mobipocket < %{version}

%description -n libqmobipocket2
Mobipocket E-book library.

%package devel
Summary:        E-book plugin and library
Requires:       libqmobipocket2 = %{version}

%description devel
Mobipocket E-book plugin and library.

This package provides development files for mobipocket library.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n libqmobipocket2

%files -n libqmobipocket2
%license COPYING
%{_kf5_libdir}/libqmobipocket.so.*

%files devel
%{_includedir}/QMobipocket/
%{_kf5_cmakedir}/QMobipocket/
%{_kf5_libdir}/libqmobipocket.so

%changelog
