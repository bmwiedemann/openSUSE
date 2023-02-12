#
# spec file for package kismet
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


%ifarch %{ix86} x86_64
%bcond_with ubertooth
%endif

%define realver 2022-08-R1
Name:           kismet
Version:        2022_08_R1
Release:        0
Summary:        An 802.11 Wireless Network Sniffer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://www.kismetwireless.net/
#Git-Clone:     https://github.com/kismetwireless/kismet.git
Source:         https://github.com/kismetwireless/kismet/archive/%{name}-%{realver}.tar.gz
Source2:        %{name}.sysusers
Patch0:         kismet-fix-build.patch
Patch1:         harden_kismet.service.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libpcap-devel
BuildRequires:  libsensors4-devel
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libnl-3.0) >= 3.0
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libwebsockets) >= 3.2.0
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
%if 0%{with ubertooth}
BuildRequires:  libbtbb-devel
BuildRequires:  ubertooth-devel
%endif
Recommends:     kismet-capture-bt-geiger
Recommends:     kismet-capture-freaklabs-zigbee
Recommends:     kismet-capture-linux-bluetooth
Recommends:     kismet-capture-linux-wifi
Recommends:     kismet-capture-nrf-51822
Recommends:     kismet-capture-nrf-52840
Recommends:     kismet-capture-nrf-mousejack
Recommends:     kismet-capture-rz-killerbee
Recommends:     kismet-capture-sdr-rtl433
Recommends:     kismet-capture-sdr-rtladsb
Recommends:     kismet-capture-sdr-rtlamr
Recommends:     kismet-capture-ti-cc2540
Recommends:     kismet-logtools
Requires(pre):  permissions
Requires(pre):  shadow
Provides:       group(kismet)
Provides:       user(kismet)
%if 0%{with ubertooth}
Recommends:     kismet-capture-ubertooth-one
%endif
%{?systemd_ordering}
%{?sysusers_requires}

%global homedir %{_localstatedir}/lib/%{name}

%description
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

Kismet works with Wi-Fi interfaces, Bluetooth interfaces, some
SDR (software defined radio) hardware like the RTLSDR, and other
specialized capture hardware.

%package logtools
Summary:        Kismet logtools
Group:          Productivity/Networking/Diagnostic
Requires:       kismet = %{version}

%description logtools
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains several kismetdb log tools
 - kismetdb_dump_devices
 - kismetdb_statistics
 - kismetdb_strip_packets
 - kismetdb_to_kml
 - kismetdb_to_wiglecsv

%package capture-linux-bluetooth
Summary:        Kismet Linux Bluetooth capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-linux-bluetooth
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains Kismet Linux Bluetooth capture helper.

%package capture-linux-wifi
Summary:        Kismet Linux WiFi capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-linux-wifi
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains Kismet Linux WiFi capture helper.

%package capture-sdr-rtl433
Summary:        Kismet SDR rtl433 capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       python3-protobuf >= 3.0.0
Requires:       python3-websockets
Requires:       rtl_433

%description capture-sdr-rtl433
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains Kismet SDR rtl433 capture helper.
https://kismetwireless.net/docs/readme/datasources_sdr_rtl433/

%package capture-sdr-rtlamr
Summary:        Kismet SDR rtlamr capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       python3-numpy
Requires:       python3-protobuf >= 3.0.0
Requires:       python3-websockets
Recommends:     rtl_amr

%description capture-sdr-rtlamr
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains Kismet SDR rtlamr capture helper.
https://kismetwireless.net/docs/readme/datasources_sdr_rtlamr/

%package capture-sdr-rtladsb
Summary:        Kismet SDR rtladsb capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       python3-numpy
Requires:       python3-protobuf >= 3.0.0
Requires:       python3-websockets
Requires:       rtl-sdr

%description capture-sdr-rtladsb
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the SDR rtladsb capture helper.
https://kismetwireless.net/docs/readme/datasources_sdr_rtladsb/

%package capture-nrf-mousejack
Summary:        Kismet nRF MouseJack capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       kismet = %{version}

%description capture-nrf-mousejack
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the nRF MouseJack capture helper.
https://kismetwireless.net/docs/readme/datasources_nrf_mousejack/

%package capture-rz-killerbee
Summary:        Kismet Killerbee Sniffer capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       kismet = %{version}

%description capture-rz-killerbee
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the Killerbee Sniffer capture helper.

%package capture-freaklabs-zigbee
Summary:        Kismet Freaklabs Zigbee capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       python3-protobuf >= 3.0.0
Requires:       python3-pyserial

%description capture-freaklabs-zigbee
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the Freaklabs Zigbee capture helper.

%package capture-ti-cc2540
Summary:        Kismet TI CC2540 (BTLE) capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-ti-cc2540
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the Texas Instruments CC2540 BTLE capture
helper.

%package capture-ti-cc-2531
Summary:        Kismet TICC2531 802.15.4 Zigbee Sniffer capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-ti-cc-2531
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the Texas Instruments  TICC2531 802.15.4
Zigbee Sniffer capture helper.

%package capture-nrf-51822
Summary:        Kismet nRF 51822 (BTLE) capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-nrf-51822
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the nRF 51822 BTLE capture helper.

%package capture-nrf-52840
Summary:        Kismet nRF 52840 (BTLE) capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-nrf-52840
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the nRF 52840 BTLE capture helper.

%package capture-nrf-nxp-kw41z
Summary:        Kismet NXP KW41Z BTLE and Zigbee Sniffer capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-nrf-nxp-kw41z
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the NXP KW41Z BTLE and Zigbee Sniffer capture
helper.

%package capture-bt-geiger
Summary:        Kismet BTLE geiger counter capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-bt-geiger
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the BTLE geiger counter capture helper.

%if 0%{with ubertooth}
%package capture-ubertooth-one
Summary:        Kismet Ubertooth One (BTLE) capture helper
Group:          Productivity/Networking/Diagnostic

%description capture-ubertooth-one
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the Ubertooth One (BTLE) capture helper.
%endif

%package devel
Summary:        Development files for kismet
Group:          Development/Libraries/C and C++
Requires:       kismet = %{version}

%description devel
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains files files for developing applications that
want to make use of kismet.

%prep
%setup -q -n kismet-kismet-%{realver}
%patch0 -p1
# HACK: Add python DESTDIR support for python stuff
find . -type f -name "Makefile*" -exec sed -i 's|setup.py install|setup.py install --root=$(DESTDIR)|g' {} \;
# Fix wrong-script-end-of-line-encoding
sed -i 's/\r$//' http_data/css/layout.css
# rpmlint will complain about missing shebangs otherwise
chmod a-x http_data/css/*.css
%patch1 -p1

%build
%limit_build -m 2500
%configure \
    --sysconfdir=%{_sysconfdir}/kismet \
    --enable-btgeiger \
    --disable-optimization
make %{?_smp_mflags} all
make %{?_smp_mflags} plugins

%sysusers_generate_pre %{SOURCE2} %{name} %{name}.conf

%install
export INSTUSR=`id -un`
export INSTGRP=`id -gn`
export MANGRP=`id -gn`
export SUIDGROUP=`id -gn`
export SUID="no"
%make_install -e
install -D -m 0644 packaging/systemd/kismet.service %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
# kismet home dir
install -m 750 -d %{buildroot}%{homedir}
# kismet systemwide plugin dir
install -d %{buildroot}%{_libdir}/kismet/
# install kismet plugins
install -D plugin-alertsyslog/alertsyslog.so %{buildroot}%{_libdir}/kismet/alertsyslog.so
%fdupes -s %{buildroot}%{_datadir}/kismet

%pre -f %{name}.pre
%service_add_pre %{name}.service

%verifyscript
%verify_permissions -e %{_bindir}/kismet_cap_linux_bluetooth
%verify_permissions -e %{_bindir}/kismet_cap_linux_wifi

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service
%set_permissions %{_bindir}/kismet_cap_linux_bluetooth
%set_permissions %{_bindir}/kismet_cap_linux_wifi

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md README.OLD README.SSL
%dir %{_sysconfdir}/kismet
%config %{_sysconfdir}/kismet/kismet.conf
%config %{_sysconfdir}/kismet/kismet_80211.conf
%config %{_sysconfdir}/kismet/kismet_alerts.conf
%config %{_sysconfdir}/kismet/kismet_filter.conf
%config %{_sysconfdir}/kismet/kismet_httpd.conf
%config %{_sysconfdir}/kismet/kismet_logging.conf
%config %{_sysconfdir}/kismet/kismet_memory.conf
%config %{_sysconfdir}/kismet/kismet_uav.conf
%config %{_sysconfdir}/kismet/kismet_wardrive.conf
%{_bindir}/kismet
%{_bindir}/kismet_discovery
%{_bindir}/kismet_server
%{_bindir}/kismet_cap_kismetdb
%{_bindir}/kismet_cap_pcapfile
%dir %{_datadir}/kismet
%{_datadir}/kismet/kismet_adsb_icao.txt.gz
%{_datadir}/kismet/kismet_manuf.txt.gz
%{_datadir}/kismet/httpd
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%dir %{_libdir}/kismet/
%{_libdir}/kismet/alertsyslog.so
%{_sysusersdir}/%{name}.conf
#
%attr(750,%{name},%{name}) %dir %{homedir}

%files logtools
%{_bindir}/kismetdb_clean
%{_bindir}/kismetdb_dump_devices
%{_bindir}/kismetdb_statistics
%{_bindir}/kismetdb_strip_packets
%{_bindir}/kismetdb_to_gpx
%{_bindir}/kismetdb_to_kml
%{_bindir}/kismetdb_to_pcap
%{_bindir}/kismetdb_to_wiglecsv

%files capture-linux-bluetooth
%verify(not mode caps) %attr(0750,root,kismet) %caps(cap_net_raw,cap_net_admin=ep) %{_bindir}/kismet_cap_linux_bluetooth

%files capture-linux-wifi
%verify(not mode caps) %attr(0750,root,kismet) %caps(cap_net_raw,cap_net_admin=ep) %{_bindir}/kismet_cap_linux_wifi

%files capture-nrf-mousejack
%{_bindir}/kismet_cap_nrf_mousejack

%files capture-rz-killerbee
%attr(755, root, -) %{_bindir}/kismet_cap_rz_killerbee

%files capture-freaklabs-zigbee
%{_bindir}/kismet_cap_freaklabs_zigbee
%{python3_sitelib}/KismetCaptureFreaklabsZigbee*

%files capture-sdr-rtladsb
%{_bindir}/kismet_cap_sdr_rtladsb
%{python3_sitelib}/KismetCaptureRtladsb*

%files capture-sdr-rtlamr
%{_bindir}/kismet_cap_sdr_rtlamr
%{python3_sitelib}/KismetCaptureRtlamr*

%files capture-sdr-rtl433
%{_bindir}/kismet_cap_sdr_rtl433
%{python3_sitelib}/KismetCaptureRtl433*

%files capture-ti-cc2540
%{_bindir}/kismet_cap_ti_cc_2540

%files  capture-ti-cc-2531
%{_bindir}/kismet_cap_ti_cc_2531

%files capture-nrf-51822
%{_bindir}/kismet_cap_nrf_51822

%files capture-nrf-52840
%{_bindir}/kismet_cap_nrf_52840

%files capture-nrf-nxp-kw41z
%{_bindir}/kismet_cap_nxp_kw41z

%files capture-bt-geiger
%{_bindir}/kismet_cap_bt_geiger
%{python3_sitelib}/KismetCaptureBtGeiger*

%if 0%{with ubertooth}
%files capture-ubertooth-one
%{_bindir}/kismet_cap_ubertooth_one
%endif

%files devel
%{_libdir}/pkgconfig/kismet.pc

%changelog
