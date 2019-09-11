#
# spec file for package froxlor
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


%define apache_serverroot %(%{_sbindir}/apxs2 -q DATADIR)
%define apache_sysconfdir %(%{_sbindir}/apxs2 -q SYSCONFDIR)
Name:           froxlor
Version:        0.9.40.1
Release:        0
Summary:        Froxlor Server Management Panel a php web-based administration software
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.froxlor.org/
Source0:        froxlor-%{version}.tar.bz2
Source1:        leap42.xml
Source2:        froxlor.conf
Source3:        froxlor.cron
Source4:        froxlor.logrotate
Patch1:         froxlor.sql.patch
Patch2:         froxlor-pdns.diff
BuildRequires:  apache2-devel
BuildRequires:  bind
BuildRequires:  fdupes
# Hard requirements
Requires:       apache2
#Requires:       apache2-mod_php7
BuildRequires:  cron
Requires:       cron
Requires:       logrotate
Requires:       php-bcmath
Requires:       php-curl
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-openssl
Requires:       php-pdo
Requires:       php-posix
Requires:       php-zip
Requires:       postfix
Requires:       postfix-mysql
#Requires:       pure-ftpd
#Requires:       php-mbstring
#Requires:       courier-authlib
#Requires:       courier-authlib-mysql
#Requires:       courier-authlib-userdb
#Requires:       courier-imap
#Requires:       cyrus-sasl-saslauthd
#Requires:       cyrus-sasl-sqlauxprop
Recommends:     mysql
Recommends:     pdns
Recommends:     proftpd-mysql
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A Server Management Panel is a php web-based administration software.
Developed by experienced server administrators this open source (GPL) panel
simplifies
the effort of managing your hosting platform

Froxlor can help you set up and manage a lot of system-services, like web-,
mail- and
ftpserver and it also brings some nice features such as a complete
support-ticket system
and an implementation of the Application Packaging Standard.


%prep
%setup -q -n %{name}
#%patch0 -p1
%patch1 
%patch2 -p1

%build

%install
idir=%{buildroot}/srv/www/htdocs/%{name}
mkdir -p $idir
cp -aRf * $idir
touch $idir/lib/userdata.inc.php
rm -f $idir/COPYING
# apache config
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d/
cp %{SOURCE2} %{buildroot}%{apache_sysconfdir}/conf.d/froxlor.conf
# bind
mkdir -p %{buildroot}%{_sysconfdir}/named.d/
touch %{buildroot}%{_sysconfdir}/named.d/froxlor_bind.conf
# cron
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
cp %{S:3} %{buildroot}%{_sysconfdir}/cron.d/froxlor
# logrotate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
cp %{S:4} %{buildroot}%{_sysconfdir}/logrotate.d/froxlor
# openSUSE config template
cp %{S:1} $idir/lib/configfiles/

%fdupes %{buildroot}%{_datadir}/%{name}
%fdupes %{buildroot}/srv/www/htdocs/%{name}

%files
%defattr(-,root,root)
%attr(0755, wwwrun, root) %dir /srv/www/htdocs/%{name}/lib
/srv/www/htdocs/%{name}/
%config %{apache_sysconfdir}/conf.d/*
%license COPYING
%ghost %config(noreplace) /srv/www/htdocs/%{name}/lib/userdata.inc.php
%config %{_sysconfdir}/named.d/froxlor_bind.conf
%config %{_sysconfdir}/cron.d/froxlor
%config %{_sysconfdir}/logrotate.d/froxlor

%changelog
