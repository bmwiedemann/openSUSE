#
# spec file for package gpsd
#
# Copyright (c) 2023 SUSE LLC
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


%define         sover 30
%define         libgps libgps%{sover}
%define         libQgps libQgpsmm%{sover}
%define         _udevdir %(pkg-config --variable udevdir udev)
%bcond_without python2
Name:           gpsd
Version:        3.25
Release:        0
Summary:        Service daemon for mediating access to a GPS
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            https://gpsd.gitlab.io/gpsd/
Source0:        https://download-mirror.savannah.gnu.org/releases/gpsd/%{name}-%{version}.tar.xz
Source1:        rules.gpsd
Source2:        udev.gpsd
Source3:        sysconfig.gpsd
Source98:       https://download-mirror.savannah.gnu.org/releases/gpsd/%{name}-%{version}.tar.xz.sig
Source99:       %{name}.keyring
Patch0:         harden_gpsd.service.patch
Patch1:         harden_gpsdctl@.service.patch
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pyserial
BuildRequires:  scons >= 2.3.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libusb-1.0)
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(udev)
Requires:       udev
Requires(pre):  %fillup_prereq
Requires(pre):  coreutils
%{?systemd_requires}
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
BuildRequires:  pps-tools-devel
%endif

%description
gpsd is a service daemon that mediates access to a GPS sensor connected
to the host computer by serial or USB interface, making its data on the
location/course/velocity of the sensor available to be queried on TCP
port 2947 of the host computer.  With gpsd, multiple GPS client
applications (such as navigational and wardriving software) can share
access to a GPS without contention or loss of data.  Also, gpsd
responds to queries with a format that is substantially easier to parse
than NMEA 0183.  A client library is provided for applications.

After installing this RPM, gpsd will automatically connect to USB GPSes
when they are plugged in and requires no configuration.  For serial
GPSes, you will need to start gpsd by hand.  Once connected, the daemon
automatically discovers the correct baudrate, stop bits, and protocol.
The daemon will be quiescent when there are no clients asking for
location information, and copes gracefully when the GPS is unplugged
and replugged.

%package devel
Summary:        Client libraries in C and Python for talking to a running gpsd or GPS
Group:          Development/Libraries/C and C++
Requires:       %{libQgps}
Requires:       %{libgps}
Requires:       %{name} = %{version}
Requires:       pkgconfig
Requires:       python3-curses
Requires:       python3-gpsd = %{version}

%description devel
This package provides C header files for the gpsd shared libraries that
manage access to a GPS for applications and debugging tools. You will
need to have gpsd installed for it to work.

%package -n %{libgps}
Summary:        Shared library for GPS applications
Group:          System/Libraries

%description -n %{libgps}
This package provides the shared library for gpsd and other GPS aware
applications.

%package -n %{libQgps}
Summary:        Shared Qt library for GPS applications
Group:          System/Libraries

%description -n %{libQgps}
This package provides the shared Qt library for gpsd and other GPS aware
applications.

%package -n python2-gpsd
Summary:        Client libraries in C and Python for talking to a running gpsd or GPS
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Provides:       python-gpsd = %{version}-%{release}
Obsoletes:      python-gpsd < %{version}-%{release}

%description -n python2-gpsd
This package provides python modules and tools for the gpsd shared libraries.
You will need to have gpsd installed for it to work.

%package -n python3-gpsd
Summary:        Client libraries in C and Python3 for talking to a running gpsd or GPS
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description -n python3-gpsd
This package provides python3 modules and tools for the gpsd shared libraries.
You will need to have gpsd installed for it to work.

%package clients
Summary:        Example clients for gpsd
Group:          Hardware/Other
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gpsd
Requires:       python3-serial

%description clients
xgps is a simple test client for gpsd with an X interface. It displays
current GPS position/time/velocity information and (for GPSes that
support the feature) the locations of accessible satellites.

xgpsspeed is a speedometer that uses position information from the GPS.
It accepts an -h option and optional argument as for gps, or a -v
option to dump the package version and exit. Additionally, it accepts
-rv (reverse video) and -nc (needle color) options.

cgps resembles xgps, but without the pictorial satellite display.  It
can run on a serial terminal or terminal emulator.

%prep
%if %{with python2}
mkdir -p %{name}-%{version}/python2
tar -xf %{SOURCE0} -C %{name}-%{version}/python2
pushd %{name}-%{version}/python2/%{name}-%{version}
%patch0
%patch1
popd
%endif
mkdir -p %{name}-%{version}/python3
tar -xf %{SOURCE0} -C %{name}-%{version}/python3
pushd %{name}-%{version}/python3/%{name}-%{version}
%patch0
%patch1
popd

%build

# The SCons description does not handle CXXFLAGS correctly, pass C++ flags also in CFLAGS
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
pyversions=( "python3" )
pylibdir=( "%{python3_sitearch}" )
%if %{with python2}
pyversions+=( "python2" )
pylibdir+=( "%{python2_sitearch}")
%endif
cnt=0
for i in "${pyversions[@]}"; do
    pushd %{name}-%{version}/${i}/%{name}-%{version}

    # breaks with %{?_smp_mflags}
    scons \
        dbus_export=yes \
        systemd=yes \
        libQgpsmm=yes \
        qt=yes \
        qt_versioned=5 \
        leapfetch=no \
        prefix="" \
        sysconfdif=%{_sysconfdir} \
        bindir=%{_bindir} \
        includedir=%{_includedir} \
        libdir=%{_libdir} \
        sbindir=%{_sbindir} \
        mandir=%{_mandir} \
        docdir=%{_docdir}/%{name} \
        icondir=%{_datadir}/icons/hicolor/128x128/apps \
        python_shebang=%{_bindir}/${i} \
        pkgconfigdir=%{_libdir}/pkgconfig \
        udevdir=$(dirname %{_udevrulesdir}) \
        target_python=${i} \
        python_libdir=${pylibdir[$cnt]} \
        unitdir=%{_unitdir} \
        mibdir=%{_datadir}/snmp/mibs/%{name} \
        build

    # Fix python interpreter path.
    sed -e "s,#!%{_bindir}/\(python[23]\?\|env \+python[23]\?\),#!%{_bindir}/${i},g" -i gps/*.py

    popd
    cnt=`expr $cnt + 1`
done

%install
# The SCons description does not handle CXXFLAGS correctly, pass C++ flags also in CFLAGS
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
# Install python2 first
%if %{with python2}
pushd %{name}-%{version}/python2/%{name}-%{version}

DESTDIR=%{buildroot} scons nostrip=True install systemd_install

# Now delete all the installed files except the python2 files
find %{buildroot} \( -not -type d -a -not -path "*/python2.*/*" \) -delete

popd
%endif
pushd %{name}-%{version}/python3/%{name}-%{version}

DESTDIR=%{buildroot} scons nostrip=True install systemd_install

install -d -m 755 %{buildroot}%{_udevdir}
install -d -m 755 %{buildroot}%{_udevdir}/rules.d
install -d -m 755 %{buildroot}%{_fillupdir}
install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}%{_udevdir}/rules.d/51-gpsd.rules
install -m 755 %{SOURCE2} %{buildroot}%{_udevdir}/gpsd.sh
install -m 644 %{SOURCE3} %{buildroot}%{_fillupdir}
# install desktop entries
install -D -m 644 -t %{buildroot}%{_datadir}/applications/ packaging/X11/xgps.desktop
install -D -m 644 -t %{buildroot}%{_datadir}/applications/ packaging/X11/xgpsspeed.desktop
ln -s  	%{_sbindir}/service %{buildroot}%{_sbindir}/rcgpsd

%fdupes -s %{buildroot}%{_mandir}

# strip absolute path and suffix
sed -i -e 's#Icon=.*/\([^/]\+\)\(\..\+\)#Icon=\1#' %{buildroot}%{_datadir}/applications/xgps{,speed}.desktop
%suse_update_desktop_file -r xgpsspeed System Monitor
%suse_update_desktop_file -r xgps System Monitor

%pre
%service_add_pre gpsd.service gpsdctl@.service gpsd.socket

%post
%if 0%{?suse_version} > 1500
%ldconfig
%else
/sbin/ldconfig
%endif
%fillup_only -n gpsd
%service_add_post gpsd.service gpsdctl@.service gpsd.socket
%udev_rules_update

%preun
%service_del_preun gpsd.service gpsdctl@.service gpsd.socket

%postun
%if 0%{?suse_version} > 1500
%ldconfig
%else
/sbin/ldconfig
%endif
%service_del_postun gpsd.service gpsdctl@.service gpsd.socket

%if 0%{?suse_version} > 1500
%ldconfig_scriptlets -n %{libgps}
%ldconfig_scriptlets -n %{libQgps}
%else
%post -n %{libgps} -p /sbin/ldconfig
%postun -n %{libgps} -p /sbin/ldconfig
%post -n %{libQgps} -p /sbin/ldconfig
%postun -n %{libQgps} -p /sbin/ldconfig
%endif

%files
%license %{name}-%{version}/python3/%{name}-%{version}/COPYING
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/{COPYING,build.adoc}
%{_mandir}/man1/gpsctl.1%{?ext_man}
%{_mandir}/man8/gpsd.8%{?ext_man}
%{_mandir}/man8/gpsdctl.8%{?ext_man}
%{_mandir}/man8/gpsinit.8%{?ext_man}
%{_udevdir}/gpsd.sh
%{_udevdir}/rules.d/*
%{_unitdir}/gpsd.service
%{_unitdir}/gpsd.socket
%{_unitdir}/gpsdctl@.service
%{_sbindir}/rcgpsd
%{_sbindir}/gpsd
%{_sbindir}/gpsdctl
%{_bindir}/gpsctl
%{_fillupdir}/sysconfig.gpsd

%files -n %{libgps}
%{_libdir}/libgps.so.*
%{_libdir}/libgpsdpacket.so.*

%files -n %{libQgps}
%{_libdir}/libQgpsmm.so.*

%files devel
%doc %{name}-%{version}/python3/%{name}-%{version}/TODO
%{_mandir}/man1/gpscat.1%{?ext_man}
%{_mandir}/man1/gpsfake.1%{?ext_man}
%{_mandir}/man1/gpsdebuginfo.1%{?ext_man}
%{_mandir}/man1/gpsdecode.1%{?ext_man}
%{_mandir}/man1/gpsprof.1%{?ext_man}
%{_mandir}/man3/libgps.3%{?ext_man}
%{_mandir}/man3/libgpsmm.3%{?ext_man}
%{_mandir}/man3/libQgpsmm.3%{?ext_man}
%{_mandir}/man5/gpsd_json.5%{?ext_man}
%{_bindir}/gpsfake
%{_bindir}/gpscat
%{_bindir}/gpsdebuginfo
%{_bindir}/gpsdecode
%{_bindir}/gpsprof
%{_includedir}/gps.h
%{_includedir}/libgpsmm.h
%{_libdir}/libgps.so
%{_libdir}/libgpsdpacket.so
%{_libdir}/pkgconfig/libgps.pc
%{_libdir}/libQgpsmm.so
%{_libdir}/libQgpsmm.prl
%{_libdir}/pkgconfig/Qgpsmm.pc

%if %{with python2}
%files -n python2-gpsd
%{python_sitearch}/gps/
%{python_sitearch}/gps-%{version}.*
%endif

%files -n python3-gpsd
%{python3_sitearch}/gps/
%{python3_sitearch}/gps-%{version}.*

%files clients
%{_mandir}/man1/cgps.1%{?ext_man}
%{_mandir}/man1/gegps.1%{?ext_man}
%{_mandir}/man1/gps.1%{?ext_man}
%{_mandir}/man1/gps2udp.1%{?ext_man}
%{_mandir}/man1/gpscsv.1%{?ext_man}
%{_mandir}/man1/gpsmon.1%{?ext_man}
%{_mandir}/man1/gpspipe.1%{?ext_man}
%{_mandir}/man1/gpsplot.1%{?ext_man}
%{_mandir}/man1/gpsrinex.1%{?ext_man}
%{_mandir}/man1/gpssnmp.1%{?ext_man}
%{_mandir}/man1/gpssubframe.1%{?ext_man}
%{_mandir}/man1/gpxlogger.1%{?ext_man}
%{_mandir}/man1/lcdgps.1%{?ext_man}
%{_mandir}/man1/ntpshmmon.1%{?ext_man}
%{_mandir}/man1/ubxtool.1%{?ext_man}
%{_mandir}/man1/xgps.1%{?ext_man}
%{_mandir}/man1/xgpsspeed.1%{?ext_man}
%{_mandir}/man1/zerk.1%{?ext_man}
%{_mandir}/man8/ppscheck.8%{?ext_man}
%{_bindir}/gegps
%{_bindir}/xgps
%{_bindir}/xgpsspeed
%{_bindir}/cgps
%{_bindir}/lcdgps
%{_bindir}/gpsmon
%{_bindir}/gpspipe
%{_bindir}/gps2udp
%{_bindir}/gpxlogger
%{_bindir}/ntpshmmon
%{_bindir}/ppscheck
%{_bindir}/ubxtool
%{_bindir}/zerk
%{_bindir}/gpsrinex
%{_bindir}/gpscsv
%{_bindir}/gpsplot
%{_bindir}/gpssubframe
%{_bindir}/gpssnmp
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%dir %{_datadir}/snmp/mibs/%{name}
%{_datadir}/snmp/mibs/gpsd/GPSD-MIB

%changelog
