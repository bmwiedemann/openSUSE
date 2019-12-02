#
# spec file for package kismet
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


%define realver 2019-09-R1
Name:           kismet
Version:        2019_09_R1
Release:        0
Summary:        An 802.11 Wireless Network Sniffer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://www.kismetwireless.net/
#Git-Clone:     https://github.com/kismetwireless/kismet.git
Source:         https://github.com/kismetwireless/kismet/archive/%{name}-%{realver}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libpcap-devel
BuildRequires:  libsensors4-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.0
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Recommends:     kismet-capture-linux-wifi
Recommends:     kismet-capture-linux-bluetooth
Recommends:     kismet-capture-freaklabs-zigbee
Recommends:     kismet-capture-nrf-mousejack
Recommends:     kismet-capture-sdr-rtladsb
Recommends:     kismet-capture-sdr-rtlamr
Recommends:     kismet-capture-sdr-rtl433
Recommends:     kismet-logtools
%{?systemd_requires}

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

%package capture-freaklabs-zigbee
Summary:        Kismet Freaklabs Zigbee capture helper
Group:          Productivity/Networking/Diagnostic
Requires:       python3-protobuf >= 3.0.0
Requires:       python3-pyserial

%description capture-freaklabs-zigbee
Kismet is a wireless network and device detector, sniffer, wardriving
tool, and WIDS (wireless intrusion detection) framework.

This subpackage contains the Freaklabs Zigbee captere helper.

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
# HACK: Add python DESTDIR support for python stuff
find . -type f -name "Makefile*" -exec sed -i 's|setup.py install|setup.py install --root=$(DESTDIR)|g' {} \;
# Fix wrong-script-end-of-line-encoding
sed -i 's/\r$//' http_data/css/layout.css

%build
%configure \
    --sysconfdir=%{_sysconfdir}/kismet \
    --disable-optimization
make %{?_smp_mflags} all-with-plugins

%install
export INSTUSR=`id -un`
export INSTGRP=`id -gn`
export MANGRP=`id -gn`
%make_install rpm
install -D -m 0644 packaging/systemd/kismet.service %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%fdupes -s %{buildroot}%{_datadir}/kismet

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

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
%config %{_sysconfdir}/kismet/kismet_storage.conf
%config %{_sysconfdir}/kismet/kismet_uav.conf
%{_bindir}/kismet
%{_bindir}/kismet_server
%{_bindir}/kismet_cap_kismetdb
%{_bindir}/kismet_cap_pcapfile
%dir %{_datadir}/kismet
%{_datadir}/kismet/httpd
%{_datadir}/kismet/kismet_manuf.txt
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%files logtools
%{_bindir}/kismetdb_dump_devices
%{_bindir}/kismetdb_statistics
%{_bindir}/kismetdb_strip_packets
%{_bindir}/kismetdb_to_kml
%{_bindir}/kismetdb_to_wiglecsv

%files capture-linux-bluetooth
%{_bindir}/kismet_cap_linux_bluetooth

%files capture-linux-wifi
%{_bindir}/kismet_cap_linux_wifi

%files capture-nrf-mousejack
%{_bindir}/kismet_cap_nrf_mousejack

%files capture-freaklabs-zigbee
%{_bindir}/kismet_cap_freaklabs_zigbee
%{python3_sitelib}/KismetCaptureFreaklabsZigbee*

%files capture-sdr-rtladsb
%{_bindir}/kismet_cap_sdr_rtladsb
%{_bindir}/kismet_cap_sdr_rtladsb_mqtt
%{python3_sitelib}/KismetCaptureRtladsb*

%files capture-sdr-rtlamr
%{_bindir}/kismet_cap_sdr_rtlamr
%{_bindir}/kismet_cap_sdr_rtlamr_mqtt
%{python3_sitelib}/KismetCaptureRtlamr*

%files capture-sdr-rtl433
%{_bindir}/kismet_cap_sdr_rtl433
%{_bindir}/kismet_cap_sdr_rtl433_mqtt
%{python3_sitelib}/KismetCaptureRtl433*

%files devel
%{_libdir}/pkgconfig/kismet.pc

%changelog
