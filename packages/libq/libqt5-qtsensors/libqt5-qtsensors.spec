#
# spec file for package libqt5-qtsensors
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


# Internal QML imports of examples
%global __requires_exclude qmlimport\\((Explorer|Grue).*

%define qt5_snapshot 1
%define libname libQt5Sensors5
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtsensors-everywhere-src-%{version}
Name:           libqt5-qtsensors
Version:        5.15.8+kde0
Release:        0
Summary:        Qt 5 Sensors library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{real_version}
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= %{real_version}
BuildRequires:  pkgconfig(Qt5DBus) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Qml) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{real_version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces. The Qt Sensors API also provides a motion gesture
recognition API for devices.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 Sensors library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          System/Libraries
%requires_ge    libQt5Core5
# Make sure that on "non-container" systems the daemon for the iio-sensor-proxy
# plugin is installed.
Requires:       (iio-sensor-proxy if systemd)

%description -n %{libname}
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces. The Qt Sensors API also provides a motion gesture
recognition API for devices.

%package -n %{libname}-imports
Summary:        QML imports for the Qt 5 Sensors library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          System/Libraries
%requires_ge    libQtQuick5
Supplements:    (%{libname} and libQtQuick5)
# imports splited with 5.4.1
Conflicts:      %{libname} < 5.4.1

%description -n %{libname}-imports
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package devel
Summary:        Development files for the Qt 5 Sensors library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Provides:       libQt5Sensors-devel = %{version}
Obsoletes:      libQt5Sensors-devel < %{version}

%description devel
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces.

This subpackage contains the header files for developing
applications that want to make use of libQt5Sensors5.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 Sensors library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{real_version}
Provides:       libQt5Sensors-private-headers-devel = %{version}
Obsoletes:      libQt5Sensors-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtsensors that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 sensors examples
License:        BSD-3-Clause
Group:          Documentation/Other
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtsensors module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%fdupes -s %{buildroot}%{_libqt5_examplesdir}

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5Sensors.so.*
%{_libqt5_plugindir}/sensors
%{_libqt5_plugindir}/sensorgestures

%files -n %{libname}-imports
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtSensors/

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtSensors/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtSensors/%{so_version}
%{_libqt5_includedir}/QtSensors
%{_libqt5_libdir}/cmake/Qt5Sensors
%{_libqt5_libdir}/libQt5Sensors.prl
%{_libqt5_libdir}/libQt5Sensors.so
%{_libqt5_libdir}/pkgconfig/Qt5Sensors.pc
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_*.pri

%files examples
%defattr(-,root,root,755)
%{_libqt5_examplesdir}/

%changelog
