#
# spec file for package kmbox
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


%bcond_without released
%define libname libKPim5Mbox5
Name:           kmbox
Version:        23.04.0
Release:        0
Summary:        KDE PIM Libraries: Mailbox functionality
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test)
Conflicts:      libKF5MBox5 < %{version}

%description
This package contains the basic packages for KDE PIM applications.

%package -n %{libname}
Summary:        KDE PIM Libraries: Mailbox functionality
%requires_eq    kmbox

%description  -n %{libname}
This package provides the mailbox functionality for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       %{libname} = %{version}
Requires:       cmake(KPim5Mime)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n %{libname}
%{_kf5_libdir}/libKPim5Mbox.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KMbox/
%{_kf5_cmakedir}/KF5Mbox/
%{_kf5_cmakedir}/KPim5Mbox/
%{_kf5_libdir}/libKPim5Mbox.so
%{_kf5_mkspecsdir}/qt_KMbox.pri

%changelog
