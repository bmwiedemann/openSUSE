#
# spec file for package pdnsd
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


Name:           pdnsd
Version:        1.2.9a
Release:        0
Summary:        A caching DNS proxy for small networks or dialin accounts
License:        GPL-3.0-or-later
Group:          Productivity/Networking/DNS/Servers
Url:            http://members.home.nl/p.a.rombouts/pdnsd.html

Source0:        http://members.home.nl/p.a.rombouts/pdnsd/releases/pdnsd-%{version}-par.tar.gz
Source1:        pdnsd.service
Recommends:     %{name}-doc
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
pdnsd is a proxy DNS daemon with permanent (disk-)cache and the ability
to serve local records. It is designed to detect network outages or hangups
and to prevent DNS-dependent applications like Netscape Navigator from hanging.

The original author of pdnsd is Thomas Moestl, but pdnsd is no longer maintained
by him. This is an extensively revised version by Paul A. Rombouts.
For a description of the changes see http://www.phys.uu.nl/~rombouts/pdnsd.html
and the file README.par in %{_docdir}/%{name}-doc.

%package doc
Summary:        Docs for %{name}
Group:          Productivity/Networking/DNS/Servers
%if 0%{?suse_version} >= 1140
BuildArch:      noarch
%endif
Requires:       %{name}

%description doc
This package provides various text files for %{name}.

%prep
%setup -q

%build
%configure --with-cachedir="%{_localstatedir}/cache/%{name}" \
	--enable-specbuild \
	--with-query-method=udptcp \
	--enable-ipv6 \
	--with-par-queries=3

make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/init.d
mkdir -p %{buildroot}/%{_unitdir}
cp -a %{SOURCE1} %{buildroot}/%{_unitdir}/
cp %{buildroot}%{_sysconfdir}/%{name}.conf.sample %{buildroot}%{_sysconfdir}/%{name}.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
getent group pdns >/dev/null || /usr/sbin/groupadd -r pdns
%service_add_pre pdnsd.service

%post
%service_add_post pdnsd.service

%preun
%service_del_preun pdnsd.service

%postun
%service_del_postun pdnsd.service

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pdnsd.conf
%{_sysconfdir}/pdnsd.conf.sample
%{_sbindir}/*%{name}*
%{_mandir}/man*/%{name}*
%config(noreplace) %attr(-,pdns,pdns) %ghost  %{_localstatedir}/cache/%{name}/%{name}.cache
%dir %{_localstatedir}/cache/%{name}
%{_unitdir}/*.service

%files doc
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING* NEWS README* THANKS TODO

%changelog
