#
# spec file for package smcroute
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           smcroute
Version:        2.5.6
Release:        0
Summary:        Static multicast routing for UNIX
License:        GPL-3.0-only
Group:          Productivity/Networking/Routing
URL:            https://troglobit.com/projects/smcroute/
#Git-Clone:     https://github.com/troglobit/smcroute.git
Source:         https://github.com/troglobit/smcroute/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         harden_smcroute.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(systemd)

%description
SMCRoute is a UNIX/Linux tool to manage and monitor multicast routes.
It supports both IPv4 and IPv6 multicast routing.

SMCRoute can be used as an alternative to dynamic multicast routers like
mrouted or pimd in setups where static multicast routes should be
maintained and/or no proper IGMP or MLD signaling exists.

Multicast routes exist in the UNIX kernel as long as a multicast routing
daemon runs. On Linux, multiple multicast routers can run simultaneously
using different multicast routing tables.

%prep
%setup -q
sed -i 's|@DOCDIR@|%{_docdir}/smcroute/|g' smcroute.service.in
%patch0 -p1

# remove file not used by Linux with incompatible Apple license
rm src/ip_mroute.h

%build
autoreconf -fiv
%configure \
    --with-systemd \
    --disable-silent-rules
%make_build

%install
%make_install
install -Dm0644 smcroute.conf %{buildroot}/%{_sysconfdir}/smcroute.conf
install -d %{buildroot}/%{_sysconfdir}/smcroute.d/
rm -rf %{buildroot}/%{_datadir}/doc
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service
%service_add_pre %{name}.socket

%post
%service_add_post %{name}.service
%service_add_post %{name}.socket

%preun
%service_del_preun %{name}.service
%service_del_preun %{name}.socket

%postun
%service_del_postun %{name}.service
%service_del_postun %{name}.socket

%files
%doc README.md
%license COPYING
%{_sbindir}/smcroutectl
%{_sbindir}/smcrouted
%{_sbindir}/smcroute
%{_sbindir}/rcsmcroute
%config %{_sysconfdir}/smcroute.conf
%config %{_sysconfdir}/smcroute.d
%{_mandir}/man5/smcroute.conf.5%{?ext_man}
%{_mandir}/man8/smcroutectl.8%{?ext_man}
%{_mandir}/man8/smcrouted.8%{?ext_man}
%{_unitdir}/%{name}.service

%changelog
