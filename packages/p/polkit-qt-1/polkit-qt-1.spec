#
# spec file for package polkit-qt-1
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == "%{nil}"
%define pkg_suffix -qt
ExclusiveArch:  do-not-build
%endif
%if "%flavor" == "qt5"
%define pkg_suffix -qt5
%define qt5 1
%define qt5_version 5.5.0
%endif
%if "%flavor" == "qt6"
%define pkg_suffix -qt6
%define qt6 1
%define qt6_version 6.5.0
%endif

%bcond_without released
%define rname polkit-qt-1
Name:           polkit%{pkg_suffix}-1
Version:        0.200.0
Release:        0
Summary:        PolicyKit Library Qt Bindings
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/polkit-qt-1/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/polkit-qt-1/%{rname}-%{version}.tar.xz.sig
Source2:        %{rname}.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
%if 0%{?qt5}
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
%endif
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
%endif

%description
Polkit-qt-1 aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit%{pkg_suffix}-1-1
Summary:        PolicyKit Library Qt Bindings

%description -n libpolkit%{pkg_suffix}-1-1
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit%{pkg_suffix}-1-devel
Summary:        PolicyKit Library Qt Bindings
Requires:       libpolkit%{pkg_suffix}-1-1 = %{version}
Requires:       polkit-devel

%description -n libpolkit%{pkg_suffix}-1-devel
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%prep
%autosetup -n %{rname}-%{version}

%build
%if 0%{?qt5}
%cmake_kf5 -d build
%cmake_build
%endif

%if 0%{?qt6}
%cmake_kf6 -DQT_MAJOR_VERSION:STRING=6
%kf6_build
%endif

%install
%if 0%{?qt5}
%kf5_makeinstall -C build
%endif

%if 0%{?qt6}
%kf6_install
%endif

%ldconfig_scriptlets -n libpolkit%{pkg_suffix}-1-1

%files -n libpolkit%{pkg_suffix}-1-1
%license LICENSES/*
%doc README
%if 0%{?qt5}
%{_kf5_libdir}/libpolkit-qt5-gui-1.so.*
%{_kf5_libdir}/libpolkit-qt5-core-1.so.*
%{_kf5_libdir}/libpolkit-qt5-agent-1.so.*
%endif
%if 0%{?qt6}
%{_kf6_libdir}/libpolkit-qt6-gui-1.so.*
%{_kf6_libdir}/libpolkit-qt6-core-1.so.*
%{_kf6_libdir}/libpolkit-qt6-agent-1.so.*
%endif

%files -n libpolkit%{pkg_suffix}-1-devel
%{_includedir}/polkit%{pkg_suffix}-1/
%if 0%{?qt5}
%{_kf5_libdir}/pkgconfig/polkit-qt5-*.pc
%{_kf5_libdir}/libpolkit-qt5-gui-1.so
%{_kf5_libdir}/libpolkit-qt5-core-1.so
%{_kf5_libdir}/libpolkit-qt5-agent-1.so
%{_kf5_libdir}/cmake/PolkitQt5-1/
%endif
%if 0%{?qt6}
%{_kf6_pkgconfigdir}/polkit-qt6-*.pc
%{_kf6_libdir}/libpolkit-qt6-gui-1.so
%{_kf6_libdir}/libpolkit-qt6-core-1.so
%{_kf6_libdir}/libpolkit-qt6-agent-1.so
%{_kf6_libdir}/cmake/PolkitQt6-1/
%endif

%changelog
