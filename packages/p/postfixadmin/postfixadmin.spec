#
# spec file for package postfixadmin
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2007-2022 Christian Boltz
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


Name:           postfixadmin
Version:        3.3.13
Release:        0
URL:            http://postfixadmin.sourceforge.net/
Source0:        https://github.com/postfixadmin/postfixadmin/archive/%{name}-%{version}.tar.gz
Source1:        config.local.php
Source2:        apache-postfixadmin.conf

BuildArch:      noarch

# Web interface
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_ver}
Requires:       php_database
%else
Requires:       php
Requires:       php_any_db
Recommends:     php-mysql
%endif

Requires:       /usr/sbin/sendmail
Requires:       php-mbstring
Requires:       php-phar
Requires:       php-spl

Recommends:     php-imap
Recommends:     postfixadmin-apache

# test/*, xmlrpc.php, squirrelmail plugin
# big dependency, not needed by all users - therefore no hard Requirement
%if 0%{?suse_version}
Recommends:     php5-ZendFramework < 2.0
%endif

# vacation.pl
Requires:       perl(DBI)
Requires:       perl(Email::Sender::Simple)
Requires:       perl(Email::Sender::Transport::SMTP)
Requires:       perl(Email::Simple)
Requires:       perl(Email::Simple::Creator)
Requires:       perl(Email::Valid)
Requires:       perl(Encode)
Requires:       perl(File::Basename)
Requires:       perl(Getopt::Std)
Requires:       perl(Log::Log4perl)
Requires:       perl(MIME::EncWords)
Requires:       perl(Try::Tiny)
Requires:       perl(strict)

# cleanupdirs.pl
Requires:       perl(File::Path)
Requires:       perl(Getopt::Long)
# mkeveryone.pl
Requires:       perl(Fcntl)
Requires:       perl(IO)
Requires:       perl(IO::File)
Requires:       perl(POSIX)
Requires:       perl(Time::Local)
# fetchmail.pl
Requires:       perl(File::Temp)
Requires:       perl(LockFile::Simple)
Requires:       perl(Sys::Syslog)

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_ver}
# create vacation user/group
PreReq:         shadow-utils
%define apache_group apache
%else
# create vacation user/group
PreReq:         shadow
%define apache_group www
Recommends:     postfix
Suggests:       php-pgsql
%endif

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_ver}
# Do not check any files in ADDITIONS for Requires, see https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
%global __requires_exclude_from ^%{_prefix}/lib/%{name}/ADDITIONS/.*$
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Summary:        Web-based management tool for Postfix virtual domains, mailboxes and aliases
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Frontends

%description
PostfixAdmin is a PHP based application that handles Postfix Style Virtual Domains and
Users that are stored in MySQL or PostgreSQL.

Postfix Admin supports:
- Virtual Mailboxes / Virtual Aliases / Forwarders
- Alias domains (Domain to Domain forwarding with recipient validation)
- Vacation (auto-response) for Virtual Mailboxes.
- Quota / Alias & Mailbox limits per domain.
- Fetchmail integration
- Packaged with over 25 languages.

%package apache
Requires:       apache2
Summary:        Postfixadmin - Apache configuration
Group:          Productivity/Networking/Web/Utilities

%description apache
PostfixAdmin is a PHP based application that handles Postfix Style Virtual
Domains and Users that are stored in MySQL or PostgreSQL.

This package holds the apache configuration.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build

%install
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/%{name}
#mkdir -p -m0755 %{buildroot}%{_datadir}/%{name}
mkdir -p -m0755 %{buildroot}%{_localstatedir}/spool/vacation
mkdir -p -m0755 %{buildroot}/%{_prefix}/lib/%{name}

mv VIRTUAL_VACATION/vacation.pl %{buildroot}%{_prefix}/lib/%{name}/
# compatibility symlink to match documentation
( cd %{buildroot}%{_localstatedir}/spool/vacation/ && ln -s ../../../usr/lib/%{name}/vacation.pl )

# copy over the code
mkdir -p -m0755 %{buildroot}/usr/share/%{name}/
install -m 0644 *.php composer.* %{buildroot}/usr/share/%{name}/
mv %{buildroot}/usr/share/%{name}/config.inc.php %{buildroot}/etc/%{name}/
install -m 0644 %{S:1} %{buildroot}/etc/%{name}/config.local.php
for d in configs languages lib model public scripts templates ; do # not copied here: ADDITIONS/ debian/ DOCUMENTS/ tests/ VIRTUAL_VACATION/
    cp -rp $d %{buildroot}/usr/share/%{name}/
done

chmod 755 %{buildroot}/usr/share/%{name}/scripts/postfixadmin-cli
install -d %{buildroot}/usr/bin
( cd %{buildroot}/usr/bin && ln -s /usr/share/%{name}/scripts/postfixadmin-cli . )

install -d %{buildroot}/var/cache/%{name}/templates_c
install -d %{buildroot}/var/cache/%{name}/sessions

# create config.local.php and templates_c symlinks
( cd %{buildroot}/usr/share/%{name} && ln -s /etc/postfixadmin/config.inc.php . )
( cd %{buildroot}/usr/share/%{name} && ln -s /etc/postfixadmin/config.local.php . )
( cd %{buildroot}/usr/share/%{name} && ln -s /var/cache/%{name}/templates_c . )

# remove files related to debian packaging (to avoid it's copied as %doc)
rm -r ADDITIONS/squirrelmail-plugin/debian/
cp -rp ADDITIONS %{buildroot}%{_prefix}/lib//%{name}/
chmod 755 %{buildroot}%{_prefix}/lib/%{name}/ADDITIONS/*.{pl,sh,py} %{buildroot}%{_prefix}/lib/%{name}/ADDITIONS/squirrelmail-plugin/locale/build.sh

# install the apache config file
mkdir -p %{buildroot}%{_sysconfdir}/apache2/conf.d
install -m 0644 %{S:2} %{buildroot}/etc/apache2/conf.d/%{name}.conf

%pre
%{_sbindir}/groupadd -r vacation 2> /dev/null || :
%{_sbindir}/useradd -c "Virtual Vacation" -d %{_localstatedir}/spool/vacation -s /sbin/nologin -M -r -g vacation vacation 2> /dev/null || :
# fix group for vacation user (if created by older versions (< 2012-02-13) of this package, it was created with group users)
%{_sbindir}/usermod -g vacation vacation 2> /dev/null || :

#if [ -z "`grep vacation /etc/postfix/master.cf 2>/dev/null`" ]; then
#cat <<'EOF' >>/etc/postfix/master.cf
## Postfix Admin Vacation
#vacation	unix	-	n	n	-	-	pipe
#	flags=Rq user=vacation argv=/usr/lib/postfixadmin/vacation.pl -f ${sender} -- ${recipient}
#EOF
#fi

%post
# PostfixAdmin 3.2 comes with a new directory layout - warn if config files are found at the old location
# (no automated migration)
if test -f /srv/www/htdocs/postfixadmin/config.inc.php ; then
    echo 'WARNING: /srv/www/htdocs/postfixadmin/config.inc.php found, please migrate your changes to /etc/postfixadmin/config.local.php' >&2
    echo 'WARNING: /srv/www/htdocs/postfixadmin/config.inc.php will be ignored!' >&2
fi
if test -f /srv/www/htdocs/postfixadmin/config.local.php ; then
    echo 'WARNING: /srv/www/htdocs/postfixadmin/config.local.php found, please migrate it to /etc/postfixadmin/config.local.php' >&2
    echo 'WARNING: /srv/www/htdocs/postfixadmin/config.local.php will be ignored!' >&2
fi

%files
%defattr(-,root,root)
%config %dir %{_sysconfdir}/%{name}
%attr(640,root,www) %config %{_sysconfdir}/%{name}/config.inc.php
%attr(640,root,www) %config(noreplace) %{_sysconfdir}/%{name}/config.local.php
%doc DOCUMENTS/* *.TXT README.md VIRTUAL_VACATION
/usr/bin/postfixadmin-cli
/usr/share/%{name}/
%attr(770,root,%{apache_group}) %dir /var/cache/%{name}/
%attr(770,root,%{apache_group}) %dir /var/cache/%{name}/templates_c/
%attr(770,root,%{apache_group}) %dir /var/cache/%{name}/sessions/
%dir %{_prefix}/lib/%{name}/
%{_prefix}/lib/%{name}/ADDITIONS/
%attr( 750,root,vacation)       %{_prefix}/lib/%{name}/vacation.pl
%attr(1770,root,vacation) %dir %{_localstatedir}/spool/vacation
%{_localstatedir}/spool/vacation/vacation.pl

%files apache
%config %dir %{_sysconfdir}/apache2
%config %dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf

%changelog
