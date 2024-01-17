#
# spec file for package sarg
#
# Copyright (c) 2023 SUSE LLC
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


Name:           sarg
Version:        2.4.0
Release:        0
Summary:        Squid Analysis Report Generator
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            http://sarg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        sarg.conf
Source2:        http://www.initzero.it/products/opensource/sarg-reports/download/sarg-reports
Source3:        sarg.hosts
Source4:        %{name}-reports-daily.service
Source5:        %{name}-reports-daily.timer
Source6:        %{name}-reports-weekly.service
Source7:        %{name}-reports-weekly.timer
Source11:       %{name}-reports-monthly.service
Source12:       %{name}-reports-monthly.timer
Source8:        sarg-reports.1.gz
Source9:        sarg-apache.conf
Source10:       platform_suse.gif
# PATCH-FIX-UPSTREAM sarg-2.4.0-config.patch
Patch0:         sarg-2.4.0-config.patch
# PATCH-FIX-OPENSUSE do not build with werror
Patch1:         sarg-2.4.0-no-werror.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gd-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  pcre-devel
# required for the squid user/group
BuildRequires:  squid
Recommends:     http_proxy

%description
Sarg -- Squid Analysis Report Generator is a tool that allows you to
view "where" your users are going to on the Internet. Sarg generate
reports in html, with fields such as: users, IP Addresses, bytes,
sites, and times.

%prep
%autosetup -p1
cp %{SOURCE2} .

%build
chmod a+x user_limit_block
cp %{_datadir}/gettext/po/Makefile.in.in po
autoreconf -fvi
export CFLAGS="%{optflags} -fcommon"
%configure \
  --sysconfdir=%{_datadir}/%{name} \
  --localedir=%{_datadir}/sarg/languages \
  --enable-sargphp=/srv/www/htdocs
%make_build

%install
install -d  %{buildroot}/srv/www/htdocs
%make_install
install -d  %{buildroot}%{_sysconfdir}/apache2/conf.d
install -d %{buildroot}/srv/www/sarg
install -d  %{buildroot}%{_datadir}/%{name}/languages
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sarg.conf
install -m 644 %{SOURCE9} %{buildroot}%{_sysconfdir}/apache2/conf.d/
install -m 644 %{SOURCE10} %{buildroot}/srv/www/sarg/
ln -s -f ../../..%{_sysconfdir}/sarg.conf %{buildroot}%{_datadir}/%{name}/sarg.conf
install -d %{buildroot}%{_sbindir}
install -m 755 %{SOURCE2} %{buildroot}%{_sbindir}
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/sarg.hosts
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/%{name}-reports-daily.service
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_unitdir}/%{name}-reports-daily.timer
install -D -m 0644 %{SOURCE6} %{buildroot}/%{_unitdir}/%{name}-reports-weekly.service
install -D -m 0644 %{SOURCE7} %{buildroot}/%{_unitdir}/%{name}-reports-weekly.timer
install -D -m 0644 %{SOURCE11} %{buildroot}/%{_unitdir}/%{name}-reports-monthly.service
install -D -m 0644 %{SOURCE12} %{buildroot}/%{_unitdir}/%{name}-reports-monthly.timer
install -d %{buildroot}%{_libexecdir}/%{name}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE8} %{buildroot}%{_mandir}/man1

%pre
%service_add_pre %{name}-reports-daily.service %{name}-reports-daily.timer
%service_add_pre %{name}-reports-weekly.service %{name}-reports-weekly.timer
%service_add_pre %{name}-reports-monthly.service %{name}-reports-monthly.timer

%post
%service_add_post %{name}-reports-daily.service %{name}-reports-daily.timer
%service_add_post %{name}-reports-weekly.service %{name}-reports-weekly.timer
%service_add_post %{name}-reports-monthly.service %{name}-reports-monthly.timer

%preun
%service_del_preun %{name}-reports-daily.service %{name}-reports-daily.timer
%service_del_preun %{name}-reports-weekly.service %{name}-reports-weekly.timer
%service_del_preun %{name}-reports-monthly.service %{name}-reports-monthly.timer

%postun
%service_del_postun %{name}-reports-daily.service %{name}-reports-daily.timer
%service_del_postun %{name}-reports-weekly.service %{name}-reports-weekly.timer
%service_del_postun %{name}-reports-monthly.service %{name}-reports-monthly.timer

%files
%config(noreplace) %{_sysconfdir}/sarg.conf
%dir %{_libexecdir}/%{name}
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/sarg-apache.conf
%{_bindir}/sarg
%{_sbindir}/sarg-reports
%dir %{_datadir}/%{name}
%attr(-,squid,squid) %dir /srv/www/sarg
%attr(-,squid,squid) /srv/www/sarg/platform_suse.gif
%{_datadir}/%{name}/css.tpl
%{_datadir}/%{name}/exclude_codes
%{_datadir}/%{name}/sarg.conf
%{_datadir}/%{name}/sarg.hosts
%{_datadir}/%{name}/user_limit_block
%{_datadir}/%{name}/languages
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_unitdir}/%{name}-reports-daily.service
%{_unitdir}/%{name}-reports-daily.timer
%{_unitdir}/%{name}-reports-weekly.service
%{_unitdir}/%{name}-reports-weekly.timer
%{_unitdir}/%{name}-reports-monthly.service
%{_unitdir}/%{name}-reports-monthly.timer

%defattr(0644,root,root,0755)
/srv/www/htdocs/sarg-php
%{_mandir}/man1/%{name}*
%{_mandir}/man1/%{name}-report*
%license COPYING LICENSE
%doc CONTRIBUTORS ChangeLog DONATIONS README

%changelog
