#
# spec file for package ndpmon
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           ndpmon
Version:        2.1.0
Release:        0
Summary:        IPv6 Neighbor Discovery Protocol Monitor
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Diagnostic
URL:            http://ndpmon.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/ndpmon/ndpmon_%{version}.tar.gz
Source1:        ndpmon.service
# manuf file from wireshark 1.12.3
Source2:        https://raw.githubusercontent.com/wireshark/wireshark/master/manuf
Source3:        ndpmon.service
# PATCH-FIX-OPENSUSE ndpmon-2.1.0-install.patch -- Fix install locations
Patch0:         ndpmon-2.1.0-install.patch
# PATCH-FIX-OPENSUSE ndpmon-no-date-time.patch -- Don't embed build date and time in binary
Patch1:         ndpmon-no-date-time.patch
# PATCH-FIX-OPENSUSE ndpmon-config.patch -- Fix examples in default config
Patch2:         ndpmon-config.patch
BuildRequires:  automake
BuildRequires:  libpcap-devel
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       python
Requires:       python-lxml
Requires(pre):  %fillup_prereq

%description
NDPMon, Neighbor Discovery Protocol Monitor, is a tool working with ICMPv6
packets. NDPMon observes the local network to see if nodes using neighbor
discovery messages behave properly. When it detects a suspicious Neighbor
Discovery message, it notifies the administrator by writing in the syslog and
in some cases by sending an email report.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
find . -type f -exec chmod 0644 {} \;

%build
export FLAGS="%{optflags}"
#without autoreconf, the %%makeinstall fails
autoreconf -fi
%configure \
    --enable-mac-resolv \
    --enable-countermeasures \
    --enable-webinterface \
    --with-webdir=/srv/www
make %{?_smp_mflags}

%install
%make_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/ndpmon.service
%if 0%{?suse_version} > 1220
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcndpmon
%endif
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/ndpmon/plugins/mac_resolv

%pre
%service_add_pre ndpmon.service

%post
%service_add_post ndpmon.service

%preun
%service_del_preun ndpmon.service

%postun
%service_del_postun ndpmon.service

%files
%license COPYING
%doc CHANGES README
%{_mandir}/man8/ndpmon.8%{ext_man}
%dir %{_sysconfdir}/ndpmon
%{_unitdir}/ndpmon.service
%config(noreplace) %{_sysconfdir}/ndpmon/config_ndpmon.xml
%{_sysconfdir}/ndpmon/config_ndpmon.dtd
%{_prefix}/lib/ndpmon
%{_sbindir}/ndpmon
%{_sbindir}/rcndpmon
%dir %{_localstatedir}/lib/ndpmon
%config(noreplace) %{_localstatedir}/lib/ndpmon/*.xml
%{_localstatedir}/lib/ndpmon/*.dtd
%dir /srv/www/ndpmon
/srv/www/ndpmon/*.css
/srv/www/ndpmon/*.html
/srv/www/ndpmon/*.xsl
/srv/www/ndpmon/config_ndpmon.xml
%dir /srv/www/ndpmon/img
/srv/www/ndpmon/img/*

%changelog
