#
# spec file for package sarg
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           sarg
Version:        2.3.10
Release:        0
Summary:        Squid Analysis Report Generator
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
Url:            http://sarg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        sarg.conf
Source2:        http://www.initzero.it/products/opensource/sarg-reports/download/sarg-reports
Source3:        sarg.hosts
Source4:        sysconfig.sarg
Source5:        cron.daily.sarg
Source6:        cron.weekly.sarg
Source7:        cron.monthly.sarg
Source8:        sarg-reports.1.gz
Source9:        sarg-apache.conf
Source10:       platform_suse.gif
# PATCH-FIX-UPSTREAM sarg-2.3.1-config.patch
Patch0:         sarg-2.3.1-config.patch
Patch1:         sarg-2.3.2-limits_h.diff
# PATCH-FIX-OPENSUSE do not build with werror
Patch2:         sarg-no-werror.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gd-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  pcre-devel
Requires(post): %fillup_prereq
Recommends:     cron
Recommends:     http_proxy

%description
Sarg -- Squid Analysis Report Generator is a tool that allows you to
view "where" your users are going to on the Internet. Sarg generate
reports in html, with fields such as: users, IP Addresses, bytes,
sites, and times.

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
cp %{SOURCE2} .

%build
chmod a+x user_limit_block
# gettext in soruce < gettext in distro
sed -i -e 's|AM_GNU_GETTEXT_VERSION(\[0.18\])|AM_GNU_GETTEXT_VERSION(\[0.19\])|g' configure.in
cp %{_datadir}/gettext/po/Makefile.in.in po
autoreconf -fvi
%configure \
        --sysconfdir=%{_datadir}/%{name} \
        --mandir=%{_mandir}/ \
        --localedir=%{_datadir}/sarg/languages \
        --enable-sargphp=/srv/www/htdocs
make %{?_smp_mflags}

%install
install -d  %{buildroot}/srv/www/htdocs
%make_install
install -d  %{buildroot}%{_sysconfdir}/apache2/conf.d
install -d  %{buildroot}/srv/www/sarg
install -d  %{buildroot}%{_datadir}/%{name}/languages
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sarg.conf
install -m 644 %{SOURCE9} %{buildroot}%{_sysconfdir}/apache2/conf.d/
install -m 644 %{SOURCE10} %{buildroot}/srv/www/sarg/
ln -s -f ../../..%{_sysconfdir}/sarg.conf %{buildroot}%{_datadir}/%{name}/sarg.conf
install -d %{buildroot}%{_sbindir}
install -m 755 %{SOURCE2} %{buildroot}%{_sbindir}
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/sarg.hosts
install -d %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}
install -D -m 755 %{SOURCE5} %{buildroot}%{_sysconfdir}/cron.daily/suse.de-sarg
install -D -m 755 %{SOURCE6} %{buildroot}%{_sysconfdir}/cron.weekly/suse.de-sarg
install -D -m 755 %{SOURCE7} %{buildroot}%{_sysconfdir}/cron.monthly/suse.de-sarg
install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 644 %{SOURCE8} %{buildroot}%{_mandir}/man8

%post
%{fillup_only -n sarg}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/sarg.conf
%dir %{_sysconfdir}/cron.daily
%dir %{_sysconfdir}/cron.weekly
%dir %{_sysconfdir}/cron.monthly
%{_sysconfdir}/cron.*/suse.de-sarg
%dir /etc/apache2
%dir /etc/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/sarg-apache.conf
%{_bindir}/sarg
%{_sbindir}/sarg-reports
%dir %{_datadir}/%{name}
%dir /srv/www/sarg
/srv/www/sarg/platform_suse.gif
%{_datadir}/%{name}/css.tpl
%{_datadir}/%{name}/exclude_codes
%{_datadir}/%{name}/sarg.conf
%{_datadir}/%{name}/sarg.hosts
%{_datadir}/%{name}/user_limit_block
%{_datadir}/%{name}/languages
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_fillupdir}/sysconfig.sarg

%defattr(0644,root,root,0755)
/srv/www/htdocs/sarg-php
%{_mandir}/man1/%{name}*
%{_mandir}/man8/%{name}-report*
%license COPYING LICENSE
%doc CONTRIBUTORS ChangeLog DONATIONS README

%changelog
