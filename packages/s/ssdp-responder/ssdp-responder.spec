#
# spec file for package ssdp-responder
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2018-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           ssdp-responder
Version:        2.0
Release:        0
Summary:        SSDP responder for Linux
License:        ISC
Group:          Productivity/Networking/Other
URL:            https://github.com/troglobit/ssdp-responder
#Git-Clone:     https://github.com/troglobit/ssdp-responder.git
Source:         https://github.com/troglobit/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         harden_ssdpd.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
%{?systemd_requires}

%description
ssdpd is a stand-alone daemon that implements the Simple Service
Discovery Protocol (SSDP) for use by networked Linux devices that
want to announce themselves to systems running Windows. ssdpd has a
built-in web server for serving the UPnP XML description which
Windows uses to present the icon when an InternetGatewayDevice is
announced.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --with-systemd=%{_unitdir}
%make_build

%install
%make_install
rm -Rv %{buildroot}/%{_datadir}/doc

%preun
%service_del_preun ssdpd.service

%postun
%service_del_postun ssdpd.service

%pre
%service_add_pre ssdpd.service

%post
%service_add_post ssdpd.service

%files
%doc README.md
%license LICENSE
%{_bindir}/ssdp-scan
%{_sbindir}/ssdpd
%{_mandir}/man1/ssdp-scan.1%{?ext_man}
%{_mandir}/man8/ssdpd.8%{?ext_man}
%{_unitdir}/ssdpd.service

%changelog
