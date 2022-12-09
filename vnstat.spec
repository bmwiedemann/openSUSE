#
# spec file for package vnstat
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} >= 1210
%bcond_without systemd
%else
%bcond_with systemd
%endif
Name:           vnstat
Version:        2.10
Release:        0
Summary:        Network Traffic Monitor
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://humdi.net/vnstat
Source:         https://humdi.net/vnstat/vnstat-%{version}.tar.gz
Source98:       https://humdi.net/vnstat/vnstat-%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring
Source2:        vnstat-cgi.conf
Source3:        vnstat-create-db.sh
Source4:        vnstat.init
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  gd-devel
BuildRequires:  glibc-devel
BuildRequires:  sqlite3-devel
Requires:       %{_bindir}/killall
Requires:       /bin/ls
Requires:       /bin/su
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%else
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
%endif

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
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_localstatedir}/lib/vnstat/

install -Dm 0755 examples/vnstat.cgi %{buildroot}/srv/vnstat/vnstat.cgi
install -Dm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/apache2/conf.d/vnstat.conf

install -Dm 0755 %{SOURCE3} %{buildroot}%{_bindir}/vnstat-create-db

%if %{with systemd}
install -Dm 0644 examples/systemd/simple/vnstat.service %{buildroot}%{_unitdir}/vnstatd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcvnstatd
%else
install -Dm 0755 %{SOURCE4} %{buildroot}%{_initddir}/vnstatd
mkdir -p %{buildroot}%{_sbindir}/
ln -s %{_initddir}/vnstatd %{buildroot}%{_sbindir}/rcvnstatd
%endif

%check
make check

%pre
%{_sbindir}/groupadd -r vnstat &> /dev/null || :
%{_sbindir}/useradd -g vnstat -s /bin/sh -r -c "vnstat daemon" -d %{_localstatedir}/lib/vnstat vnstat &>/dev/null ||:
%if 0%{?with_systemd}
%service_add_pre vnstatd.service
%endif

%post
%if %{with systemd}
%service_add_post vnstatd.service
%else
%fillup_and_insserv vnstatd
%endif

%preun
%if %{with systemd}
%service_del_preun vnstatd.service
%else
%stop_on_removal vnstatd
%endif

%postun
%if %{with systemd}
%service_del_postun vnstatd.service
%else
%restart_on_update vnstatd
%insserv_cleanup
%endif

%files
%defattr(-,root,root)
%doc CHANGES FAQ README UPGRADE
%license COPYING
%config(noreplace) %{_sysconfdir}/vnstat.conf
%{_bindir}/vnstat-create-db
%{_bindir}/vnstat
%{_sbindir}/vnstatd
%{_sbindir}/rcvnstatd
%if %{with systemd}
%{_unitdir}/vnstatd.service
%else
%{_initddir}/vnstatd
%endif
%{_mandir}/man1/vnstat.1%{?ext_man}
%{_mandir}/man8/vnstatd.8%{?ext_man}
%{_mandir}/man5/vnstat.conf.5%{?ext_man}
%attr(0755,vnstat,root) %{_localstatedir}/lib/vnstat

%files cgi
%defattr(-,root,root)
%dir %{_sysconfdir}/apache2/
%dir %{_sysconfdir}/apache2/conf.d/
%config(noreplace) %{_sysconfdir}/apache2/conf.d/vnstat.conf
%{_bindir}/vnstati
%{_mandir}/man1/vnstati.1.gz
/srv/vnstat/

%changelog
