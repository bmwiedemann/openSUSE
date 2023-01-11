#
# spec file for package libqt5-qtserialport
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


%define qt5_snapshot 1
%define libname libQt5SerialPort5
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtserialport-everywhere-src-%{version}
Name:           libqt5-qtserialport
Version:        5.15.8+kde0
Release:        0
Summary:        Qt 5 Serial Port Addon
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{real_version}
BuildRequires:  libqt5-qtbase-devel >= %{real_version}
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libudev)
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt Serial Port provides the basic functionality, which includes
configuring, I/O operations, getting and setting the control signals
of the RS-232 pinouts. This module does not support terminal features
(echo, CR/LF control, text mode, timeouts/delays, or poinout signal
change notification).

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 Serial Port Addon
Group:          Development/Libraries/X11
%requires_ge    libQt5Core5

%description -n %{libname}
Qt Serial Port provides the basic functionality, which includes
configuring, I/O operations, getting and setting the control signals
of the RS-232 pinouts. This module does not support terminal features
(echo, CR/LF control, text mode, timeouts/delays, or poinout signal
change notification).

%package devel
Summary:        Development files for the Qt5 SerialPort library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Provides:       libQt5SerialPort-devel = %{version}
Obsoletes:      libQt5SerialPort-devel < %{version}

%description devel
You need this package if you want to compile programs with qtserialport.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 SerialPort library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{real_version}
Provides:       libQt5SerialPort-private-headers-devel = %{version}
Obsoletes:      libQt5SerialPort-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtserialport that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 Serial Port examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtserialport module.

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

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5SerialPort.so.*

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*
%{_libqt5_libdir}/cmake/Qt5SerialPort
%{_libqt5_libdir}/libQt5SerialPort.prl
%{_libqt5_libdir}/libQt5SerialPort.so
%{_libqt5_libdir}/pkgconfig/Qt5SerialPort.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_serialport*.pri

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
