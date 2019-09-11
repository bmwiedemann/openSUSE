#
# spec file for package libqt5-qtlocation
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define qt5_snapshot 0

%define libname libQt5Positioning5

Name:           libqt5-qtlocation
Version:        5.13.0
Release:        0
Summary:        Qt 5 Location Library
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtlocation-everywhere-src-5.13.0
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  libicu-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
# needed for free, used to tune build parallelism
BuildRequires:  procps

%description
The Qt Location API facilitates creating mapping solutions using
the data available from some contemporary location services.

%prep
%setup -q -n qtlocation-everywhere-src-%{real_version}

%package -n %libname
Summary:        Qt 5 Positioning Library
Group:          Development/Libraries/X11

%description -n %libname
The Qt Positioning API gives developers the ability to determine a
position by using a variety of possible sources, including satellite,
WiFi, text file, and so on. That information can then be used to, for
example, determine a position on a map. In addition, satellite
information can be retrieved and area-based monitoring be performed.

%package -n libQt5Location5
Summary:        Qt 5 Location Library
Group:          Development/Libraries/X11

%description -n libQt5Location5
The Qt Location API facilitates creating mapping solutions using
the data available from some contemporary location services.
Using Qt Location, one can

 * access and present map data,
 * support touch gesture on a specific area of the map,
 * query for a specific geographical location and route,
 * add additional layers on top, such as polylines and circles,
 * and search for places and related images.
 
%package -n libQt5PositioningQuick5
Summary:        Qt5 Positioning Library for Qt Quick
Group:          System/Libraries

%description -n libQt5PositioningQuick5
This library contains glue code for using the Qt Location module in Qt Quick
applications.

%package devel
Summary:        Development files for the Qt5 Location Library
Group:          Development/Libraries/X11
Requires:       %libname = %{version}
Requires:       libQt5Location5 = %{version}
Requires:       libQt5PositioningQuick5 = %{version}

%description devel
The Qt Location API facilitates creating mapping solutions using
the data available from some contemporary location services.

This subpackage contains the header files for developing
applications that want to make use of the Qt Location libraries.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 Location Library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
Requires:       libqt5-qtbase-private-headers-devel >= %{version}
Requires:       libqt5-qtdeclarative-private-headers-devel

%description private-headers-devel
This package provides private headers of libqt5-qtlocation that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 location examples
Group:          Documentation/Other
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtlocation module.

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%post -n libQt5Location5 -p /sbin/ldconfig

%postun -n libQt5Location5 -p /sbin/ldconfig

%post -n libQt5PositioningQuick5 -p /sbin/ldconfig

%postun -n libQt5PositioningQuick5 -p /sbin/ldconfig

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%if 0%{?suse_version} < 1330
%qmake5 QMAKE_CC=gcc-7 QMAKE_CXX=g++-7 CONFIG+=c++14
%else
%qmake5
%endif

# do not eat all memory (logic from chromium specfile)
jobs="%{?jobs:%{jobs}}"
echo "Available memory:"
cat /proc/meminfo
echo "System limits:"
ulimit -a
if test -n "$jobs" -a "$jobs" -gt 1 ; then
    mem_per_process=900000
    max_mem=$(awk '/MemTotal/ { print $2 }' /proc/meminfo)
    max_jobs="$(($max_mem / $mem_per_process))"
    test "$jobs" -gt "$max_jobs" && jobs="$max_jobs" && echo "Warning: Reducing number of jobs to $max_jobs because of memory limits"
    test "$jobs" -le 0 && jobs=1 && echo "Warning: Do not use the parallel build at all becuse of memory limits"
fi

%__make -j$jobs VERBOSE=1

%install
%qmake5_install
find %{buildroot}/%{_libdir} -type f -name '*.la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libdir}/pkgconfig -type f -name '*.pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} +
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%fdupes %{buildroot}%{_libqt5_examplesdir}/

%files -n %libname
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5Positioning.so.*
%dir %{_libqt5_plugindir}/position
%{_libqt5_plugindir}/position/libqtposition_geoclue.so
%{_libqt5_plugindir}/position/libqtposition_geoclue2.so
%{_libqt5_plugindir}/position/libqtposition_positionpoll.so

%files -n libQt5Location5
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5Location.so.*
%{_libqt5_plugindir}/geoservices/
%{_libqt5_archdatadir}/qml/QtLocation/
%dir %{_libqt5_archdatadir}/qml/Qt/
%dir %{_libqt5_archdatadir}/qml/Qt/labs/
%{_libqt5_archdatadir}/qml/Qt/labs/location/

%files -n libQt5PositioningQuick5
%license LICENSE.*
%{_libqt5_libdir}/libQt5PositioningQuick.so.*
%{_libqt5_archdatadir}/qml/QtPositioning

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtPositioning/%{so_version}
%{_libqt5_includedir}/QtLocation/%{so_version}
%{_libqt5_includedir}/QtPositioningQuick/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtPositioning/%{so_version}
%exclude %{_libqt5_includedir}/QtLocation/%{so_version}
%exclude %{_libqt5_includedir}/QtPositioningQuick/%{so_version}
%{_libqt5_includedir}/QtPositioning
%{_libqt5_includedir}/QtLocation
%{_libqt5_includedir}/QtPositioningQuick
%{_libqt5_libdir}/cmake/Qt5Positioning
%{_libqt5_libdir}/cmake/Qt5Location
%{_libqt5_libdir}/cmake/Qt5PositioningQuick
%{_libqt5_libdir}/libQt5Positioning.prl
%{_libqt5_libdir}/libQt5Location.prl
%{_libqt5_libdir}/libQt5PositioningQuick.prl
%{_libqt5_libdir}/libQt5Positioning.so
%{_libqt5_libdir}/libQt5Location.so
%{_libqt5_libdir}/libQt5PositioningQuick.so
%{_libqt5_libdir}/pkgconfig/Qt5Positioning.pc
%{_libqt5_libdir}/pkgconfig/Qt5Location.pc
%{_libqt5_libdir}/pkgconfig/Qt5PositioningQuick.pc
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_*.pri

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
