#
# spec file for package pen
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


Name:           pen
Version:        0.26.1
Release:        0
Summary:        A simple load balancer for TCP-based protocols
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            http://siag.nu/pen/
Source0:        http://siag.nu/pub/pen/%{name}-%{version}.tar.gz
Source1:        %{name}.cfg
Source2:        init.%{name}
Source3:        runpen.sh
Source4:        pen.service
BuildRequires:  systemd-rpm-macros
%systemd_requires

%description
Pen is a load balancer for "simple" TCP-based protocols such as HTTP or
SMTP. It allows several servers to appear as one to the outside and
automatically detects servers that are down and distributes clients
among the available servers. This gives high availability and scalable
performance.

The load balancing algorithm keeps track of clients and will try to
send them back to the server they visited the last time. This is useful
for applications that maintain state between connections in the server,
including most modern web applications.

When pen detects that a server is unavailable, it scans for another
starting with the server after the most recently used one. That way we
get load balancing and "fair" failover for free.

Correctly configured, pen can ensure that a server farm is always
available, even when individual servers are brought down for
maintenance or reconfiguration.

The final single point of failure, pen itself, can be eliminated by
running pen on several servers, using VRRP to decide which is active.

%prep
%setup -q

%build
%configure \
  --with-daemon
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_sbindir}
%make_install
# Install pen init script
install -d %{buildroot}/%{_datadir}/pen/scripts
install -m 0744 %{SOURCE2} %{buildroot}/%{_datadir}/pen/scripts/rcpen
install -d %{buildroot}/%{_unitdir}
install -m 0444 %{SOURCE4} %{buildroot}/%{_unitdir}/pen.service
install -m 0744 %{SOURCE3} %{buildroot}%{_bindir}/runpen.sh
install -d %{buildroot}%{_sysconfdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.cfg
ln -sf service %{buildroot}%{_sbindir}/rcpen
mkdir -p %{buildroot}/%{_docdir}
mv %{buildroot}%{_prefix}/doc/pen %{buildroot}/%{_docdir}

%pre
%service_add_pre pen.service

%post
%service_add_post pen.service

%preun
%service_del_preun pen.service

%postun
%service_del_postun pen.service

%files
%{_docdir}/*
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/pen
%{_unitdir}/pen.service
%{_bindir}/%{name}
%{_bindir}/runpen.sh
%{_bindir}/mergelogs
%{_bindir}/penctl
%{_bindir}/penlog
%{_bindir}/penlogd
%{_sbindir}/rc%{name}
%config(noreplace) %{_sysconfdir}/%{name}.cfg

%changelog
