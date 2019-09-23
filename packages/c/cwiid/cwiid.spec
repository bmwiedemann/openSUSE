#
# spec file for package cwiid
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{!?py_ver:          %global py_ver          %(python -c "import sys; v=sys.version_info[:2]; print '%%d.%%d'%%v" 2>/dev/null)}
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define sover      1
Name:           cwiid
Version:        0.6.00+131.gfadf11e
Release:        0
Summary:        Library to access Wiimotes
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://abstrakraft.org/cwiid/
Source:         %{name}-%{version}.tar.xz
Source2:        baselibs.conf
Patch0:         0001-Fix-program-ldflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bluez-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.0.0

%description
Library to access Wiimotes.

%package -n libcwiid%{sover}
Summary:        Library to access Wiimotes
Group:          System/Libraries

%description -n libcwiid%{sover}
Library to access Wiimotes.

%package -n libcwiid-devel
Summary:        Library to access Wiimotes
Group:          Development/Libraries/C and C++
Requires:       bluez-devel
Requires:       libcwiid%{sover} = %{version}

%description -n libcwiid-devel
API and library to access Wiimotes.

%package -n wminput
Summary:        Linux Event Driver for the Wiimote
Group:          Hardware/Joystick
Requires:       libcwiid%{sover} = %{version}

%description -n wminput
wminput is an Linux event, mouse, and joystick driver for the wiimote using the
uinput system.

It supports assigning key/button symbols to buttons on the wiimote, nunchuk,
and classic controller, and axes symbols to wiimote axes including direction
pads, "analog" sticks, and "analog" shoulder buttons.

Furthermore, it provides a plugin interface through which more advanced
functionality can be implemented, such as accelerometer and ir calculations.

Plugins can provide button-type events and axes.

%package -n wmgui
Summary:        Graphical User Interface to the Wiimote
Group:          Hardware/Joystick
Requires:       libcwiid%{sover} = %{version}

%description -n wmgui
Graphical user interface for the capabilities of libcwiid, a Wiimote access
library.

%package -n lswm
Summary:        List Wiimote Devices
Group:          Hardware/Joystick
Requires:       libcwiid%{sover} = %{version}

%description -n lswm
lswm is a command-line utility to list Wiimote devices.

%package -n python-cwiid
Summary:        Python Module to Access Wiimotes
Group:          Development/Libraries/Python
Requires:       libcwiid%{sover} = %{version}

%description -n python-cwiid
Python wrapper module around the libcwiid library, to
access Wiimote devices.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
%configure \
    --disable-ldconfig
make %{?_smp_mflags}

%install
%make_install
rm "%{buildroot}%{_libdir}"/lib*.a
rm -rf "%{buildroot}%{_datadir}/doc"

chmod 0644 "%{buildroot}%{_includedir}"/*.h
chmod 0644 "%{buildroot}%{_sysconfdir}"/cwiid/wminput/*

rm doc/Makefile*

%post   -n libcwiid%{sover} -p /sbin/ldconfig
%postun -n libcwiid%{sover} -p /sbin/ldconfig

%files -n lswm
%defattr(-,root,root)
%{_bindir}/lswm

%files -n wmgui
%defattr(-,root,root)
%{_bindir}/wmgui
%{_mandir}/man1/wmgui.1%{ext_man}

%files -n wminput
%defattr(-,root,root)
%doc doc/wminput.list
%doc wminput/README
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_sysconfdir}/cwiid/wminput
%config %{_sysconfdir}/cwiid/wminput/*
%{_bindir}/wminput
%dir %{_libdir}/cwiid
%dir %{_libdir}/cwiid/plugins
%{_libdir}/cwiid/plugins/*.so
%{_mandir}/man1/wminput.1%{ext_man}

%files -n libcwiid-devel
%defattr(-,root,root)
%{_includedir}/cwiid.h
%{_libdir}/libcwiid.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n libcwiid%{sover}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/Xmodmap
%dir %{_sysconfdir}/cwiid
%dir %{_libdir}/cwiid
%dir %{_libdir}/cwiid/plugins
%{_libdir}/libcwiid.so.%{sover}
%{_libdir}/libcwiid.so.%{sover}.*

%files -n python-cwiid
%defattr(-,root,root)
%{python_sitearch}/cwiid.so
%if 0%{?suse_version} >= 1100
%{python_sitearch}/cwiid-0.6.00-py%{py_ver}.egg-info
%endif

%changelog
