#
# spec file for package solid
#
# Copyright (c) 2020 SUSE LLC
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


%define lname   libKF5Solid5
%define _tar_path 5.75
%bcond_without lang
Name:           solid
Version:        5.75.0
Release:        0
Summary:        KDE Desktop hardware abstraction
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  bison
BuildRequires:  extra-cmake-modules >= %{_tar_path}
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
BuildRequires:  pkgconfig(libudev)
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.12.0
%endif

%description
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package -n %{lname}
Summary:        KDE Desktop hardware abstraction
Group:          System/GUI/KDE
Recommends:     %{lname}-lang = %{version}
Recommends:     %{name}-imports = %{version}
Recommends:     %{name}-tools = %{version}
Recommends:     media-player-info
Recommends:     udisks2
Obsoletes:      libKF5Solid4

%description -n %{lname}
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package tools
Summary:        KDE Desktop hardware abstraction
Group:          System/GUI/KDE

%description tools
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.
CLI utilities.

%package imports
Summary:        KDE Desktop hardware abstraction
Group:          System/GUI/KDE

%description imports
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.
QML imports.

%package devel
Summary:        KDE Desktop hardware abstraction: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.12.0

%description devel
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.
Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -DWITH_NEW_SOLID_JOB=ON -DWITH_NEW_POWER_ASYNC_API=ON -DWITH_NEW_POWER_ASYNC_FREEDESKTOP=ON -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%{_kf5_debugdir}/solid.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Solid.so.*

%files tools
%license LICENSES/*
%{_kf5_bindir}/solid-hardware5
%{_kf5_bindir}/solid-power

%files imports
%license LICENSES/*
%{_kf5_qmldir}/

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Solid/
%{_kf5_libdir}/libKF5Solid.so
%{_kf5_mkspecsdir}/qt_Solid.pri

%changelog
