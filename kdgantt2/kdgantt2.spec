#
# spec file for package kdgantt2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kdgantt2
Version:        16.08.3
Release:        0
Summary:        Gantt chart library
License:        GPL-2.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0

%description
This library implements Gantt chart drawing functionality. It allows
to easily embed the Gantt charts into the application as long as it
is capable of drawing QWidget or QGraphicsView objects.

This package is part of the KDE PIM module.

%prep
%setup -q

%build
%cmake_kf5 -d build

%make_jobs

%install
%kf5_makeinstall -C build

%package -n libKF5KDGantt2-5
Summary:        Gantt chart library for kdepim
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       kdgantt2 = %{version}

%description -n libKF5KDGantt2-5
This library implements Gantt chart drawing functionality. It allows
to easily embed the Gantt charts into the application as long as it
is capable of drawing QWidget or QGraphicsView objects.

%post  -n libKF5KDGantt2-5 -p /sbin/ldconfig
%postun -n libKF5KDGantt2-5 -p /sbin/ldconfig

%package devel
Summary:        Development package for kdgantt2
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5KDGantt2-5 = %{version}

%description devel
The development package for the kdgantt2 libraries.

%files devel
%license COPYING*
%{_includedir}/KF5/KDGantt2/
%{_includedir}/KF5/kdgantt2/
%{_includedir}/KF5/kdgantt2_version.h
%{_libdir}/cmake/KF5KDGantt2/
%{_libdir}/libKF5KDGantt2.so
%{_libdir}/qt5/mkspecs/modules/qt_KDGantt2.pri

%files
%license COPYING*
%{_kf5_debugdir}/kdgantt2.categories

%files -n libKF5KDGantt2-5
%license COPYING*
%{_libdir}/libKF5KDGantt2.so.*

%changelog
