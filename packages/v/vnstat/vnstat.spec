#
# spec file for package vnstat
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


Name:           vnstat
Version:        2.13
Release:        0
Summary:        Network Traffic Monitor
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://humdi.net/vnstat
Source:         https://humdi.net/vnstat/vnstat-%{version}.tar.gz
Source2:        vnstat-cgi.conf
Source3:        vnstat-create-db.sh
Source4:        vnstat.init
Source98:       https://humdi.net/vnstat/vnstat-%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  gd-devel
BuildRequires:  glibc-devel
BuildRequires:  sqlite3-devel
Requires:       %{_bindir}/killall
Requires:       /bin/ls
Requires:       /bin/su
Provides:       group(vnstat)
Provides:       user(vnstat)
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
vnStat is a network traffic monitor for Linux that keeps a log of
daily network traffic for the selected interface(s). vnStat isn't a
packet sniffer. The traffic information is analyzed from the /proc
filesystem, so vnStat can be used without root permissions.

%package cgi
Summary:        Graph Visualization CGI Script for %{name}
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Recommends:     apache2

%description cgi
vnStat is a network traffic monitor for Linux that keeps a log of
daily network traffic for the selected interface(s). vnStat isn't a
packet sniffer. The traffic information is analyzed from the /proc
filesystem, so vnStat can be used without root permissions.

This package contains a CGI script that visualizes graphs of the
collected traffic statistics.

%prep
%setup -q
# Add user and group to the systemd service.
sed -i 's/\(\[Service\]\)/\1\nUser=vnstat\nGroup=vnstat/' examples/systemd/simple/vnstat.service

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_localstatedir}/lib/vnstat/

install -Dm 0755 examples/vnstat.cgi %{buildroot}/srv/vnstat/vnstat.cgi
install -Dm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/apache2/conf.d/vnstat.conf

install -Dm 0755 %{SOURCE3} %{buildroot}%{_bindir}/vnstat-create-db

install -Dm 0644 examples/systemd/simple/vnstat.service %{buildroot}%{_unitdir}/vnstatd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcvnstatd

%check
%make_build check

%pre
%{_sbindir}/groupadd -r vnstat &> /dev/null || :
%{_sbindir}/useradd -g vnstat -s /bin/sh -r -c "vnstat daemon" -d %{_localstatedir}/lib/vnstat vnstat &>/dev/null ||:
%service_add_pre vnstatd.service

%post
%service_add_post vnstatd.service

%preun
%service_del_preun vnstatd.service

%postun
%service_del_postun vnstatd.service

%files
%doc CHANGES FAQ README UPGRADE
%license COPYING
%config(noreplace) %{_sysconfdir}/vnstat.conf
%{_bindir}/vnstat-create-db
%{_bindir}/vnstat
%{_sbindir}/vnstatd
%{_sbindir}/rcvnstatd
%{_unitdir}/vnstatd.service
%{_mandir}/man1/vnstat.1%{?ext_man}
%{_mandir}/man8/vnstatd.8%{?ext_man}
%{_mandir}/man5/vnstat.conf.5%{?ext_man}
%attr(0755,vnstat,root) %{_localstatedir}/lib/vnstat

%files cgi
%dir %{_sysconfdir}/apache2/
%dir %{_sysconfdir}/apache2/conf.d/
%config(noreplace) %{_sysconfdir}/apache2/conf.d/vnstat.conf
%{_bindir}/vnstati
%{_mandir}/man1/vnstati.1%{?ext_man}
/srv/vnstat/

%changelog
