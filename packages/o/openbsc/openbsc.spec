#
# spec file for package openbsc
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


%define _lto_cflags %nil

Name:           openbsc
Version:        1.3.2
Release:        0
Summary:        Base station controller for a GSM stack
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/openbsc/wiki/OpenBSC
Source:         openbsc-%version.tar.xz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libdbi-drivers-dbd-sqlite3
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbi)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto) >= 0.9.5
BuildRequires:  pkgconfig(libosmo-netif) >= 0.4.0
BuildRequires:  pkgconfig(libosmoabis) >= 0.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.0.1
BuildRequires:  pkgconfig(libosmoctrl) >= 1.0.1
BuildRequires:  pkgconfig(libosmogb) >= 1.0.1
BuildRequires:  pkgconfig(libosmogsm) >= 1.0.1
BuildRequires:  pkgconfig(libosmovty) >= 1.0.1
BuildRequires:  pkgconfig(libsmpp34) >= 1.13.0
BuildRequires:  pkgconfig(sqlite3)
Requires:       libdbi-drivers-dbd-sqlite3
Provides:       osmocom-bsc-sccplite
Provides:       osmocom-nitb

%description
An implementation of the minimal subset of the major backend
components of a GSM network, such as BSC, MSC, HLR, EIR. Using a
commercial GSM BTS and attaching it to a Linux system running the
OpenBSC software allows you to run your own GSM "network in a box".

OsmoBSC can run in one of two modes:
* as OsmoBSC, exposing an A interface towards an external MSC, or
* as OsmoNITB (Network In The Box), which implements a minimal subset
  of the BSC, MSC. SMSC and HLR

%package bs11-utils
Summary:        Command line utilities for Siemens BS-11 BTS
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
Conflicts:      osmo-bsc-bs11-utils

%description bs11-utils
There is a tool in this package for configuring the Siemens BS-11 BTS.
Additionally, it contains one tool for making use of an ISDN-card and the
public telephone network as frequency standard for the E1 line.

%package bsc-sccplite
Summary:        GSM Base Station Controller
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
Recommends:     bsc-sccplite

%description bsc-sccplite
This is the BSC-only version of OpenBSC. It requires a Mobile Switching Center
(MSC) to operate.

You might rather prefer to use openbsc (osmo-nitb) which is considered a
"GSM Network-in-a-Box" and does not depend on a MSC.

%prep
%setup -q

%build
pushd openbsc/
echo "%version" >.tarball-version
autoreconf -fi
%configure --disable-static --includedir="%_includedir/%name" \
	--docdir="%_docdir/%name" --with-systemdsystemunitdir="%_unitdir" \
	--enable-smpp CFLAGS="-Wno-error=implicit -Wno-error=maybe-uninitialized -Wno-error=memset-transposed-args -Wno-error=null-dereference -Wno-error=sizeof-array-argument -Wno-error=sizeof-pointer-memaccess -fcommon"
make %{?_smp_mflags}
popd

%install
pushd openbsc/
%make_install
popd
find %buildroot -type f -name "*.la" -delete -print
install -d %buildroot/%_localstatedir/lib/osmocom

install -d %buildroot/%_sbindir
ln -s %_sbindir/service %buildroot/%_sbindir/rcosmo-nitb
ln -s %_sbindir/service %buildroot/%_sbindir/rcosmo-bsc-mgcp

# FIXME: remove uneeded files
rm -rf %buildroot/%_includedir/%name

%check
pushd openbsc/
make %{?_smp_mflags} check || find . -name testsuite.log -exec cat {} +
popd

%pre
%service_add_pre osmo-nitb.service

%post
%service_add_post osmo-nitb.service

%preun
%service_del_preun osmo-nitb.service

%postun
%service_del_postun osmo-nitb.service

%pre bsc-sccplite
%service_add_pre osmo-bsc-mgcp.service

%post bsc-sccplite
%service_add_post osmo-bsc-mgcp.service

%preun bsc-sccplite
%service_del_preun osmo-bsc-mgcp.service

%postun bsc-sccplite
%service_del_postun osmo-bsc-mgcp.service

%files
%license openbsc/COPYING
%doc openbsc/AUTHORS openbsc/README
%_docdir/openbsc
%_bindir/osmo-nitb
%dir %_sysconfdir/osmocom
%config %_sysconfdir/osmocom/osmo-nitb.cfg
%_unitdir/osmo-nitb.service
%_sbindir/rcosmo-nitb
%dir %_localstatedir/lib/osmocom

%files bs11-utils
%_bindir/bs11_config
%_bindir/isdnsync

%files bsc-sccplite
%_bindir/osmo-bsc_mgcp
%dir %_sysconfdir/osmocom
%config %_sysconfdir/osmocom/osmo-bsc-mgcp.cfg
%_unitdir/osmo-bsc-mgcp.service
%_sbindir/rcosmo-bsc-mgcp

%changelog
