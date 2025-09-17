#
# spec file for package tayga
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} == 1500
%global force_gcc_version 14
%endif

Name:           tayga
Version:        0.9.5
Release:        0
Summary:        Out-of-kernel stateless NAT64 implementation
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.litech.org/tayga/
Source0:        https://github.com/apalrd/tayga/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        tayga_setup_tun
Source2:        tayga_destroy_tun
Patch:          harden-services.patch
ExcludeArch:    %{arm} %{i586}
BuildRequires:  gcc%{?force_gcc_version}

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.

%prep
%autosetup -p1
sed -i 's|%{_localstatedir}/db/tayga|%{_localstatedir}/lib/tayga|g' tayga.conf.example

%build
%make_build CFLAGS="%{optflags}" V=1 RELEASE=1 CC="gcc%{?force_gcc_version:-%{force_gcc_version}}"

%install
#make_install
install -d %{buildroot}%{_var}/lib/tayga
install -d %{buildroot}%{_sysconfdir}/tayga

install -D -m 0644 tayga.conf.example %{buildroot}%{_sysconfdir}/tayga.conf
install -D -m 0755 -t %{buildroot}%{_sbindir} tayga %{SOURCE1} %{SOURCE2}
install -D -m 0644 -t %{buildroot}%{_unitdir}/ tayga.service tayga@.service
install -D -m 0644 -t %{buildroot}%{_mandir}/man5/ *.5
install -D -m 0644 -t %{buildroot}%{_mandir}/man8/ *.8
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
%license LICENSE
%doc README.md
%doc *.sh
%config(noreplace) %{_sysconfdir}/tayga.conf
%dir %{_sysconfdir}/tayga/
%dir %{_var}/lib/tayga/
%{_sbindir}/tayga
%{_sbindir}/rctayga
%{_sbindir}/tayga_setup_tun
%{_sbindir}/tayga_destroy_tun
%{_mandir}/man5/tayga.conf.5%{?ext_man}
%{_mandir}/man8/tayga.8%{?ext_man}
%{_unitdir}/tayga.service
%{_unitdir}/tayga@.service

%changelog
