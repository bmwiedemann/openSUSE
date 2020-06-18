#
# spec file for package osmo-bts
#
# Copyright (c) 2020 SUSE LLC
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


Name:           osmo-bts
Version:        1.2.0
Release:        0
Summary:        Osmocom BTS-Side code (Abis, scheduling)
License:        AGPL-3.0-or-later AND GPL-2.0-only
Group:          Productivity/Telephony/Servers
URL:            https://osmocom.org/projects/osmobts/wiki/Wiki
Source:         %{name}-%{version}.tar.xz
Patch0:         0001-fix-compilation-with-gcc-10.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmoabis) >= 0.6.0
BuildRequires:  pkgconfig(libosmocodec) >= 1.3.0
BuildRequires:  pkgconfig(libosmocoding) >= 1.3.0
BuildRequires:  pkgconfig(libosmocore) >= 1.3.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.3.0
BuildRequires:  pkgconfig(libosmogb)
BuildRequires:  pkgconfig(libosmogsm) >= 1.3.0
BuildRequires:  pkgconfig(libosmotrau) >= 0.6.0
BuildRequires:  pkgconfig(libosmovty) >= 1.3.0

%description
Osmocom BTS-Side code (A-bis, scheduling).

%package -n osmo-bts-virtual
Summary:        Virtual Osmocom GSM BTS (no RF hardware; GSMTAP/UDP)
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities

%description -n osmo-bts-virtual
This version of OsmoBTS doesn't use actual GSM PHY/Hardware/RF, but
utilizes GSMTAP-over-UDP frames for the Um interface.  This is useful
in fully virtualized setups e.g. in combination with OsmocomBB virt_phy.

%package -n osmo-bts-omldummy
Summary:        Osmocom CI: Bring up only OML without RSL
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities

%description -n osmo-bts-omldummy
This is used only in integration testing, where in the TTCN-3 testsuite
we currently have no A-bis OML implementation, but only a RSL one.

%prep
%setup -q
%patch0 -p1

%build
echo "%{version}" >.tarball-version
autoreconf -fi
%configure \
    --docdir="%{_docdir}/%{name}" \
    --with-systemdsystemunitdir=%{_unitdir} \
    --enable-trx
make V=1 %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-bts-trx
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-bts-virtual

%pre
%service_add_pre osmo-bts-trx.service
%post
%service_add_post osmo-bts-trx.service
%preun
%service_del_preun osmo-bts-trx.service
%postun
%service_del_postun osmo-bts-trx.service

%pre virtual
%service_add_pre osmo-bts-virtual.service
%post virtual
%service_add_post  osmo-bts-virtual.service
%preun virtual
%service_del_preun osmo-bts-virtual.service
%postun virtual
%service_del_postun osmo-bts-virtual.service

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%files
%license COPYING
%doc README.md
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-bts-trx
%{_docdir}/%{name}/examples/osmo-bts-trx/osmo-bts-trx-calypso.cfg
%{_docdir}/%{name}/examples/osmo-bts-trx/osmo-bts-trx.cfg
%dir %{_docdir}/%{name}/examples/osmo-bts-virtual
%{_docdir}/%{name}/examples/osmo-bts-virtual/openbsc-virtual.cfg
%{_docdir}/%{name}/examples/osmo-bts-virtual/osmo-bts-virtual.cfg
%{_bindir}/osmo-bts-trx
%{_sbindir}/rcosmo-bts-trx
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-bts-trx.cfg
%{_unitdir}/osmo-bts-trx.service

%files -n osmo-bts-virtual
%{_bindir}/osmo-bts-virtual
%{_sbindir}/rcosmo-bts-virtual
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-bts-virtual.cfg
%{_unitdir}/osmo-bts-virtual.service

%files -n osmo-bts-omldummy
%{_bindir}/osmo-bts-omldummy

%changelog
