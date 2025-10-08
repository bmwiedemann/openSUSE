#
# spec file for package PackageKit-Qt
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


%global pkqt_flavor @BUILD_FLAVOR@%{nil}
%if "%{pkqt_flavor}" == ""
%define pkg_suffix -Qt
ExclusiveArch:  do_not_build
%endif
%if "%{pkqt_flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -Qt6
%define pkqt   packagekitqt6
%endif
%define major 2
Name:           PackageKit%{?pkg_suffix}
Version:        1.1.4
Release:        0
Summary:        Simple software installation management software
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://github.com/hughsie/PackageKit-Qt
Source:         https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz#/PackageKit-Qt-%{version}.tar.gz
# PATCH-FIX-UPSTREAM boo#1103678
Patch0:         0001-Fix-PackageKit-not-emitting-network-state-changed-signal.patch
# PATCH-FIX-UPSTREAM kde#508235
Patch1:         0001-offline-Ensure-the-enum-is-registered.patch
BuildRequires:  PackageKit-devel >= %{version}
BuildRequires:  cmake
BuildRequires:  pkgconfig
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
%endif

%description
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package -n lib%{pkqt}-%{major}
Summary:        Simple software installation management software
Group:          System/Libraries

%description -n lib%{pkqt}-%{major}
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package -n %{pkqt}-devel
Summary:        Simple software installation management software
Group:          Development/Libraries/C and C++
Requires:       lib%{pkqt}-%{major} = %{version}

%description -n %{pkqt}-devel
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%prep
%autosetup -p1 -n PackageKit-Qt-%{version}

%build
%if 0%{?qt6}
%cmake_qt6
%{qt6_build}
%endif

%install
%if 0%{?qt6}
%qt6_install
%endif

%check
%ctest

%ldconfig_scriptlets -n lib%{pkqt}-%{major}

%files -n lib%{pkqt}-%{major}
%license COPYING
%doc NEWS AUTHORS README.md
%{_libdir}/libpackagekitqt?.so.*

%files -n %{pkqt}-devel
%doc TODO MAINTAINERS
%{_libdir}/libpackagekitqt?.so
%{_libdir}/cmake/packagekitqt?/
%{_libdir}/pkgconfig/packagekitqt?.pc
%{_includedir}/PackageKitQt

%changelog
