#
# spec file for package osmo-remsim
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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

%define sover 1
Name:           osmo-remsim
Version:        0.2.2
Release:        0
Summary:        Osmocom remote SIM software suite
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Servers
URL:            https://projects.osmocom.org/projects/osmo-remsim
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libcsv-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmoabis)
BuildRequires:  pkgconfig(libosmocore) >= 0.11.0
BuildRequires:  pkgconfig(libosmogsm) >= 0.11.0
BuildRequires:  pkgconfig(libosmosim)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libulfius)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libosmousb)
BuildRequires:  pkgconfig(libosmo-simtrace2)
%{?systemd_ordering}

%description
osmo-remsim is a suite of software programs enabling physical/geographic
separation of a cellular phone (or modem) on the one hand side and the
SIM/USIM/ISIM card on the other side.

Using osmo-remsim, entire fleet of modems/phones can be operated on, as
well as banks of SIM cards and dynamically establish or remove the
connections between modems/phones and cards.

In technical terms, it behaves like a proxy for the ISO 7816 smart
card interface between the MS/UE and the UICC/SIM/USIM/ISIM.

It can also be used with other systems that use contact-based smart
cards according to ISO 7816. Only the T=0 protocol with standard
(non-extended) APDUs is supported.

%package -n libosmo-rspro%{sover}
Summary:        Osmocom Remote SIM protocol library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-rspro%{sover}
libosmo-rsrpo is a utility library for encoding/decoding the ASN.1 BER
based RSPRO (Remote SIM Protocol) protocol used between the osmo-remsim
programs.

%package -n libosmo-rspro-devel
Summary:        Headers for Osmocom Remote SIM
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-rspro%{sover} = %{version}

%description -n libosmo-rspro-devel
libosmo-rsrpo is an utility library for encoding/decoding the ASN.1 BER
based RSPRO (Remote SIM Protocol) protocol used between the osmo-remsim
programs.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-rspro.

%package -n osmo-remsim-server
Summary:        Osmocom Remote SIM Central Server
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Servers

%description -n osmo-remsim-server
The remsim-server is the central element of a osmo-remsim deployment,
it maintains a list of clients + bankds connected to it, as well as the
dynamic SIM card mappings between them.

%package -n osmo-remsim-bankd
Summary:        Osmocom Remote SIM Bank Daemon
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Servers

%description -n osmo-remsim-bankd
The remsim-bankd is managing a bank of SIM card readers and their
respective cards. It establishes a control connection to remsim-server
and receives inbound connections from remsim-clients.

%package -n osmo-remsim-client
Summary:        Osmocom Remote SIM Client
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Servers

%description -n osmo-remsim-client
The remsim-client is managing a given phone/modem. It attaches to the
"cardem" firmware of a SIMtrcace2 (or compatible, such as sysmoQMOD)
hardware and forwards the SIM card communication to a remsim-bankd,
under the control of remsim-server.

%prep
%setup -q

%build
echo "%{version}" >.tarball-version
autoreconf -fi
%configure \
    --disable-static \
    --with-systemdsystemunitdir=%{_unitdir}
make V=1 %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check || find . -name testsuite.log -exec cat {} +

%post   -n libosmo-rspro%{sover} -p /sbin/ldconfig
%postun -n libosmo-rspro%{sover} -p /sbin/ldconfig

%files -n libosmo-rspro%{sover}
%license COPYING
%doc README.md
%{_libdir}/libosmo-rspro.so.%{sover}*

%files -n libosmo-rspro-devel
%{_includedir}/osmocom
%{_includedir}/osmocom/rspro
%{_includedir}/osmocom/rspro/rspro_client.h
%{_libdir}/libosmo-rspro.so
%{_libdir}/pkgconfig/libosmo-rspro.pc

%files -n osmo-remsim-server
%{_bindir}/osmo-remsim-server

%files -n osmo-remsim-bankd
%{_bindir}/osmo-remsim-bankd

%files -n osmo-remsim-client
%{_bindir}/osmo-remsim-client-st2

%changelog
