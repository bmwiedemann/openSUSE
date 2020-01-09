#
# spec file for package osmo-trx
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           osmo-trx
Version:        1.2.0
Release:        0
Summary:        SDR transceiver that implements Layer 1 of a GSM BTS
License:        AGPL-3.0-or-later
Group:          Productivity/Telephony/Servers
URL:            https://osmocom.org/projects/osmotrx/wiki/OsmoTRX
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  pkgconfig(LimeSuite)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(libosmocore) >= 1.3.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.3.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.3.0
BuildRequires:  pkgconfig(libosmovty) >= 1.3.0
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(uhd)
BuildRequires:  pkgconfig(usrp) >= 3.3
%{?systemd_requires}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif

%description
OsmoTRX is a software-defined radio transceiver that implements the Layer 1
physical layer of a BTS comprising the following 3GPP specifications:

TS 05.01 "Physical layer on the radio path"
TS 05.02 "Multiplexing and Multiple Access on the Radio Path"
TS 05.04 "Modulation"
TS 05.10 "Radio subsystem synchronization"

In this context, BTS is "Base transceiver station". It's the stations that
connect mobile phones to the mobile network.

3GPP is the "3rd Generation Partnership Project" which is the collaboration
between different telecommunication associations for developing new
generations of mobile phone networks. (post-2G/GSM)

%package uhd
Summary:        SDR transceiver that implements Layer 1 of a GSM BTS (UHD)
Group:          Productivity/Telephony/Servers

%description uhd
OsmoTRX is a software-defined radio transceiver that implements the Layer 1
physical layer of a BTS comprising the following 3GPP specifications:

TS 05.01 "Physical layer on the radio path"
TS 05.02 "Multiplexing and Multiple Access on the Radio Path"
TS 05.04 "Modulation"
TS 05.10 "Radio subsystem synchronization"

In this context, BTS is "Base transceiver station". It's the stations that
connect mobile phones to the mobile network.

3GPP is the "3rd Generation Partnership Project" which is the collaboration
between different telecommunication associations for developing new
generations of mobile phone networks. (post-2G/GSM)

%package usrp1
Summary:        SDR transceiver that implements Layer 1 of a GSM BTS (USRP1)
Group:          Productivity/Telephony/Servers

%description usrp1
OsmoTRX is a software-defined radio transceiver that implements the Layer 1
physical layer of a BTS comprising the following 3GPP specifications:

TS 05.01 "Physical layer on the radio path"
TS 05.02 "Multiplexing and Multiple Access on the Radio Path"
TS 05.04 "Modulation"
TS 05.10 "Radio subsystem synchronization"

In this context, BTS is "Base transceiver station". It's the stations that
connect mobile phones to the mobile network.

3GPP is the "3rd Generation Partnership Project" which is the collaboration
between different telecommunication associations for developing new
generations of mobile phone networks. (post-2G/GSM)

%package lms
Summary:        SDR transceiver that implements Layer 1 of a GSM BTS (LimeSuite)
Group:          Productivity/Telephony/Servers

%description lms
OsmoTRX is a software-defined radio transceiver that implements the Layer 1
physical layer of a BTS comprising the following 3GPP specifications:

TS 05.01 "Physical layer on the radio path"
TS 05.02 "Multiplexing and Multiple Access on the Radio Path"
TS 05.04 "Modulation"
TS 05.10 "Radio subsystem synchronization"

In this context, BTS is "Base transceiver station". It's the stations that
connect mobile phones to the mobile network.

3GPP is the "3rd Generation Partnership Project" which is the collaboration
between different telecommunication associations for developing new
generations of mobile phone networks. (post-2G/GSM)

%prep
%setup -q

%build
echo "%{version}" >.tarball-version
autoreconf -fiv
%configure \
    --docdir=%{_docdir}/%{name} \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-lms \
    --with-uhd \
    --with-usrp1
make V=1 %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-trx-lms
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-trx-uhd
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-trx-usrp1
%fdupes -s %{buildroot}/%{_datadir}

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%pre lms
%service_add_pre osmo-trx-lms.service
%post lms
%service_add_post osmo-trx-lms.service
%preun lms
%service_del_preun osmo-trx-lms.service
%postun lms
%service_del_postun osmo-trx-lms.service

%pre uhd
%service_add_pre osmo-trx-uhd.service
%post uhd
%service_add_post osmo-trx-uhd.service
%preun uhd
%service_del_preun osmo-trx-uhd.service
%postun uhd
%service_del_postun osmo-trx-uhd.service

%pre usrp1
%service_add_pre osmo-trx-usrp1.service
%post usrp1
%service_add_post osmo-trx-usrp1.service
%preun usrp1
%service_del_preun osmo-trx-usrp1.service
%postun usrp1
%service_del_postun osmo-trx-usrp1.service

%files
%license COPYING
%doc README.md
%doc %{_docdir}/%{name}/examples

%files lms
%{_bindir}/osmo-trx-lms
%{_sbindir}/rcosmo-trx-lms
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-trx-lms.cfg
%{_unitdir}/osmo-trx-lms.service

%files uhd
%{_bindir}/osmo-trx-uhd
%{_sbindir}/rcosmo-trx-uhd
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-trx-uhd.cfg
%{_unitdir}/osmo-trx-uhd.service

%files usrp1
%{_bindir}/osmo-trx-usrp1
%{_sbindir}/rcosmo-trx-usrp1
%dir %{_datadir}/usrp
%dir %{_datadir}/usrp/rev2
%dir %{_datadir}/usrp/rev4
%{_datadir}/usrp/rev2/std_inband.rbf
%{_datadir}/usrp/rev4/std_inband.rbf
%{_unitdir}/osmo-trx-usrp1.service

%changelog
