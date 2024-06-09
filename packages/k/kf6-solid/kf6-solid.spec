#
# spec file for package kf6-solid
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


%define qt6_version 6.6.0

%define rname solid
%bcond_without released
Name:           kf6-solid
Version:        6.3.0
Release:        0
Summary:        KDE Desktop hardware abstraction
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mount)

%description
Solid is a device integration framework. It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package tools
Summary:        KDE Desktop hardware abstraction

%description tools
Solid is a device integration framework. It provides a way of querying and
interacting with hardware independently of the underlying operating system.
CLI utilities.

%package -n libKF6Solid6
Summary:        KDE Desktop hardware abstraction
Requires:       kf6-solid >= %{version}
Recommends:     kf6-solid-tools = %{version}
Recommends:     media-player-info
Recommends:     udisks2

%description -n libKF6Solid6
Solid is a device integration framework. It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package devel
Summary:        KDE Desktop hardware abstraction: Build Environment
Requires:       libKF6Solid6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Solid is a device integration framework. It provides a way of querying and
interacting with hardware independently of the underlying operating system.
Development files.

%lang_package -n libKF6Solid6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE \

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang solid6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6Solid6

%files -n libKF6Solid6-lang -f solid6.lang

%files
%{_kf6_debugdir}/solid.categories
%{_kf6_debugdir}/solid.renamecategories

%files tools
%{_kf6_bindir}/solid-hardware6

%files -n libKF6Solid6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Solid.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Solid.*
%{_kf6_includedir}/Solid/
%{_kf6_cmakedir}/KF6Solid/
%{_kf6_libdir}/libKF6Solid.so

%changelog
