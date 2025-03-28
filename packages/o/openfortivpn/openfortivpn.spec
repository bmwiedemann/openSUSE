#
# spec file for package openfortivpn
#
# Copyright (c) 2025 SUSE LLC
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


Name:           openfortivpn
Version:        1.23.1
Release:        0
Summary:        Client for PPP+SSL VPN tunnel services
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/adrienverge/openfortivpn
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         harden_openfortivpn@.service.patch
Patch1:         openfortivpn-fix-usr-bin-env.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
Requires:       ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
    --with-systemdsystemunitdir=%{_unitdir}
%make_build

%install
%make_install
rm -f %{buildroot}/%{_datadir}/openfortivpn/config.template

%preun
%service_del_preun openfortivpn@.service

%postun
%service_del_postun openfortivpn@.service

%pre
%service_add_pre openfortivpn@.service

%post
%service_add_post openfortivpn@.service

%files
%license LICENSE LICENSE.OpenSSL
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%{_unitdir}/%{name}@.service

%changelog
