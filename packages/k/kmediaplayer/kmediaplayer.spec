#
# spec file for package kmediaplayer
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


%define lname   libKF5MediaPlayer5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           kmediaplayer
Version:        5.101.0
Release:        0
Summary:        Interface for media player KParts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Parts) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files.

%package -n %{lname}
Summary:        Interface for media player KParts
Obsoletes:      libKF5MediaPlayer4

%description -n %{lname}
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files.

%package devel
Summary:        Interface for media player KParts: Build Environment
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5I18n) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Parts) >= %{_kf5_bugfix_version}

%description devel
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files. Development files.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%{_kf5_libdir}/libKF5MediaPlayer.so.*
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kmediaplayer-engine.desktop
%{_kf5_servicetypesdir}/kmediaplayer-player.desktop

%files devel
%{_kf5_libdir}/libKF5MediaPlayer.so
%{_kf5_libdir}/cmake/KF5MediaPlayer/
%{_kf5_includedir}/KMediaPlayer/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KMediaPlayer.xml

%changelog
