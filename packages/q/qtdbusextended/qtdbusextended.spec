#
# spec file for package qtdbusextended
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

%define sover             1
%define libqt5_includedir %{_includedir}/qt5
%define libqt5_archdatadir   %{_libdir}/qt5

Name:           qtdbusextended
Summary:        Extended DBus for Qt
Version:        0.0.3
Release:        0
License:        LGPL-2.1+
URL:            https://github.com/nemomobile/qtdbusextended
Source:         https://github.com/nemomobile/qtdbusextended/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)

%description
Qt provides several classes for DBus communication.

Extended DBus for Qt provides the following main additional features to the
QDBusAbstractInterface class:

    DBus provides a Properties Interface which specifies a PropertiesChanged
    signal whose reception is not implemented in the properties bridge by
    QtDBus. Extended DBus for Qt provides it.
    
    The DBus Properties Interface also specifies a GetAll method not implemented
    in the standard QtDBus. Extended DBus for Qt provides it.
    
    QtDBus properties mechanism is completely synchronous. Extended DBus for Qt
    provides an additional asynchronous alternative.
    
    An alternative and very simple cache mechanism is also implemented in
    Extended DBus for Qt so the DBus traffic is reduced to the minimum.


%package -n libdbusextended-qt5-%{sover}
Summary:        Qtdbusextended libraries
Group:          System/Libraries

%description -n libdbusextended-qt5-%{sover}
This package contains the libraries for qtdbusextended

%package devel
Summary:        Development package for qtdbusextended
Requires:       libdbusextended-qt5-%{sover} = %{version}-%{release}

%description devel
Header files and libraries for qtdbusextended.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
%make_build

%install
%qmake5_install

%post -n libdbusextended-qt5-%{sover} -p /sbin/ldconfig
%postun -n libdbusextended-qt5-%{sover} -p /sbin/ldconfig

%files -n libdbusextended-qt5-%{sover}
%defattr(-,root,root)
%{_libdir}/libdbusextended-qt5.so.*

%files devel
%defattr(-,root,root)
%doc README.md
%license COPYING
%{libqt5_includedir}/DBusExtended
%{_libdir}/pkgconfig/dbusextended-qt5.pc
%{_libdir}/libdbusextended-qt5.so
%{_libqt5_archdatadir}/mkspecs/features/dbusextended-qt5.prf

%changelog
