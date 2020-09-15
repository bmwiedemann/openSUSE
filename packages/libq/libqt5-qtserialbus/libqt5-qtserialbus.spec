#
# spec file for package libqt5-qtserialbus
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


%define qt5_snapshot 0

Name:           libqt5-qtserialbus
Version:        5.15.1
Release:        0
Summary:        Qt 5 Serial Bus Addon
License:        LGPL-3.0-only OR GPL-2.0-or-later
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtserialbus-everywhere-src-5.15.1
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5DBus-devel >= %{version}
BuildRequires:  libQt5Network-devel >= %{version}
BuildRequires:  libQt5Widgets-devel >= %{version}
BuildRequires:  libqt5-qtserialport-devel >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Qt Serial Bus API provides classes and functions to access the
various industrial serial buses and protocols, such as CAN, ModBus,
and others.

%prep
%autosetup -n %{tar_version}

%package -n libQt5SerialBus5
Summary:        Qt 5 Serial Bus Addon
Group:          Development/Libraries/X11

%description -n libQt5SerialBus5
The Qt Serial Bus API provides classes and functions to access the
various industrial serial buses and protocols, such as CAN, ModBus,
and others.

This package contains base tools, like string, xml, and network
handling.

%package devel
Summary:        Development files for the Qt5 SerialBus library
Group:          Development/Libraries/X11
Requires:       libQt5SerialBus5 = %{version}

%description devel
You need this package if you want to compile programs with qtserialbus.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 SerialBus library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}

%description private-headers-devel
This package provides private headers of libqt5-qtserialbus that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 Serial Port examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtserialbus module.

%post -n libQt5SerialBus5 -p /sbin/ldconfig

%postun -n libQt5SerialBus5 -p /sbin/ldconfig

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

fdupes -s %{buildroot}%{prefix}

%files
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_bindir}/*
%{_libqt5_plugindir}/

%files -n libQt5SerialBus5
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5SerialBus.so.*

%files private-headers-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*
%{_libqt5_libdir}/cmake/Qt5SerialBus
%{_libqt5_libdir}/libQt5SerialBus.prl
%{_libqt5_libdir}/libQt5SerialBus.so
%{_libqt5_libdir}/pkgconfig/Qt5SerialBus.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_serialbus*.pri

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
