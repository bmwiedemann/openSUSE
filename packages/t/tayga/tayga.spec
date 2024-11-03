#
# spec file for package tayga
#
# Copyright (c) 2024 SUSE LLC
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


Name:           tayga
Version:        0.9.2
Release:        0
Summary:        Out-of-kernel stateless NAT64 implementation
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.litech.org/tayga/
Source0:        http://www.litech.org/tayga/%{name}-%{version}.tar.bz2
Source1:        tayga_setup_tun
Source2:        tayga_destroy_tun
Source3:        tayga.service
Patch0:         tayga-obey-cflags.diff
Patch1:         tayga-fix-gcc14.patch
BuildRequires:  autoconf
BuildRequires:  automake

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.

%prep
%autosetup -p1
sed -i 's|%{_localstatedir}/db/tayga|%{_localstatedir}/lib/tayga|g' tayga.conf.example

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
mv %{buildroot}%{_sysconfdir}/tayga.conf{.example,}
install -d %{buildroot}%{_var}/lib/tayga
install -m 0755 %{SOURCE1} %{SOURCE2} %{buildroot}%{_sbindir}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/tayga.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rctayga

%pre
%service_add_pre tayga.service

%post
%service_add_post tayga.service

%preun
%service_del_preun tayga.service

%postun
%service_del_postun tayga.service

%files
%license COPYING
%doc README
%config(noreplace) %{_sysconfdir}/tayga.conf
%dir %{_var}/lib/tayga
%{_sbindir}/tayga
%{_sbindir}/rctayga
%{_sbindir}/tayga_setup_tun
%{_sbindir}/tayga_destroy_tun
%{_mandir}/man5/tayga.conf.5%{?ext_man}
%{_mandir}/man8/tayga.8%{?ext_man}
%{_unitdir}/tayga.service

%changelog
