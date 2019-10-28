#
# spec file for package libkmahjongg
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkmahjongg
Version:        19.08.2
Release:        0
Summary:        General Data for KDE Games
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains data which is required by KDE games.

%package -n libKF5KMahjongglib5
Summary:        Library for Mahjongg tiles
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
Requires:       libkmahjongg

%description -n libKF5KMahjongglib5
This package contains the library for Mahjongg tiles.

%package devel
Summary:        Library for Mahjongg tiles: Build Environment
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5KMahjongglib5 = %{version}
Obsoletes:      %{name}-kf5-devel < %{version}
Provides:       %{name}-kf5-devel = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop games that uses Mahjongg tiles.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif
%fdupes -s %{buildroot}

%post -n libKF5KMahjongglib5 -p /sbin/ldconfig
%postun -n libKF5KMahjongglib5 -p /sbin/ldconfig

%files
%license COPYING*
%doc README
%{_kf5_debugdir}/libkmahjongg.categories
%{_kf5_sharedir}/kmahjongglib/

%files -n libKF5KMahjongglib5
%license COPYING*
%doc README
%{_kf5_libdir}/libKF5KMahjongglib.so.*

%files devel
%license COPYING*
%doc README
%{_kf5_includedir}/KF5KMahjongg/
%{_kf5_libdir}/libKF5KMahjongglib.so
%{_kf5_cmakedir}/KF5KMahjongglib

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
