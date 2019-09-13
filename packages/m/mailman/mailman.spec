#
# spec file for package mailman
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global _buildshell /bin/bash
%define       m_uid 72
%define       m_gid 67
%define       apache2_confd       %{_sysconfdir}/apache2/conf.d
%define       sendmail_libd       %{_libexecdir}/sendmail.d
%define       mailman_confd       %{_sysconfdir}/mailman
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

# optional: checkdbs, gate_news, nightly_gzip, 
# switched on per default: cull_bad_shunt, disabled, mailpasswds,
# nightly_archives, senddigests
%define timers mailman_cull_bad_shunt.timer mailman_disabled.timer mailman_gate_news.timer mailman_checkdbs.timer mailman_mailpasswds.timer mailman_nightly_archives.timer mailman_nightly_gzip.timer mailman_senddigests.timer mailman_cull_bad_shunt.service mailman_disabled.service mailman_gate_news.service mailman_checkdbs.service mailman_mailpasswds.service mailman_nightly_archives.service mailman_nightly_gzip.service mailman_senddigests.service

Name:           mailman
Version:        2.1.29
Release:        0
Summary:        The GNU Mailing List Manager
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Mailinglists
URL:            http://www.gnu.org/software/mailman/mailman.html
Source0:        https://ftp.gnu.org/gnu/mailman/%{name}-%{version}.tgz
Source1:        README.SUSE
Source2:        mailman-2.1-manpages.tgz
Source4:        mailman-generate-sysconfig
Source5:        rcmailman
Source6:        aliases
Source7:        sysconfig.mailman
Source8:        mailman.sgidlist
Source9:        mailman-apache2.conf
Source10:       mailman-rpmlintrc
Source11:       logrotate.mailman
Source12:       mm-text.png
Source13:       https://ftp.gnu.org/gnu/mailman/%{name}-%{version}.tgz.sig
Source14:       %{name}.keyring
Source15:       systemd-units.tar.xz
Source16:       mailman.service
Source17:       mailman-update-cfg
Patch1:         mailman-wrapper.patch
Patch3:         mailman-2.1.14-python.dif
Patch5:         mailman-2.1.14-editarch.patch
Patch6:         mailman-2.1.14-misc-PACKAGES.diff
Patch7:         mailman-2.1.26-list_lists.patch
Patch10:        mailman-2.1.4-dirmode.patch
Patch11:        mailman-2.1.4-notavaliduser.patch
Patch17:        mailman-weak-password.diff
Patch18:        mailman-2.1.5-no_extra_asian.dif
Patch19:        reproducible.patch
BuildRequires:  aaa_base
BuildRequires:  fdupes
BuildRequires:  krb5
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  postfix
BuildRequires:  pwdutils
BuildRequires:  python-devel
BuildRequires:  python-dnspython
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
#!BuildIgnore:  sendmail
Requires:       aaa_base
Requires:       logrotate
Requires:       python
Requires:       python-dnspython
Requires:       smtp_daemon
Requires:       w3m
Requires(post): %fillup_prereq
Requires(post): coreutils
Requires(post): gawk
Requires(post): group(nobody)
Requires(post): openssl
Requires(post): user(nobody)
Requires(post): user(wwwrun)
Requires(post): permissions
Requires(pre):  permissions
Requires(pre):  shadow
%{?systemd_requires}

# Installation directories
# rpmlint will give an error about hardcoded library path,
# but this is necessary, because there are python executables inside,
# which the user can run in their scripts. 
# see rhbz#226117 for more information
%global mmdir %{_libexecdir}/%{name}
%global varmmdir /var/lib/%{name}
%global docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%global configdir /etc/%{name}
%global datadir %{varmmdir}/data
%global archivesdir %{varmmdir}/archives
%global logdir /var/log/%{name}
%global piddir /var/run/%{name}
%global queuedir /var/spool/%{name}
%global templatedir %{mmdir}/templates
%global httpdconfdir /etc/httpd/conf.d
%global restart_flag /var/run/%{name}-restart-after-rpm-install
%global mmbuilddir %{_builddir}/%{name}-%{version}

%global httpdconffile %{name}.conf
# Now, the user and group the CGIs will expect to be run under.  This should
# match the user and group the web server is configured to run as.  The scripts
# will error out if they are invoked by any other user.
%global cgiuser    apache
%global cgigroup   apache

%description
This is the GNU Mailing List manager. Mailman provides an
easy-to-configure means of maintaining mailing lists including Web
administration. Mailman is written in Python.

%prep
%setup -q
%autopatch -p1
cp -av %{SOURCE1} .
cp -av %{SOURCE8} .
tar -xvf %{SOURCE15}

find . -name \*.py |while read PYFN ; do
    sed -i -e '1s/env python/python/' $PYFN
done

%build
%configure \
    --prefix=%{mmdir} \
    --exec-prefix=%{mmdir} \
    --localstatedir=%{_localstatedir}/run \
    --libexecdir=%{mmdir} \
    --with-groupname=mailman \
    --with-username=mailman \
    --with-var-prefix=%{varmmdir} \
    --without-permcheck \
    --with-cgi-gid=%{cgiuser} \
    --with-mail-gid=%{cgigroup}
make %{?_smp_mflags} OPT="%{optflags} -fpie -pie"

# Mark sitemappgen as non-executable
find . -name sitemapgen -print -exec chmod -x '{}' +

%install
install -d %{buildroot}/{usr/sbin,etc/{mailman,sysconfig,init.d,logrotate.d},%{_fillupdir},bin/conf.d}/
%make_install
# write initial wrapper id files:
. %{SOURCE7}
getent group $MAILMAN_CGI_GID \
    | cut -d: -f3 > %{buildroot}/%{mailman_confd}/mailman.cgi-gid
echo %{m_gid} > %{buildroot}/%{mailman_confd}/mailman.mail-gid

# SuSEconfig stuff:
install -m 644 %{SOURCE7} %{buildroot}%{_fillupdir}/
install -m 755 %{SOURCE4} %{buildroot}%{mmdir}/bin/
install -m 644 %{SOURCE8} %{buildroot}%{mmdir}/sgidlist

# Originally from Fedora, where it is needed because of SELinux, that is
# not the issue here, but still we should not write to the /usr/lib
# unnecessarily
install -m 755 %{SOURCE17} %{buildroot}%{mmdir}/bin/

# Move configuration files to proper location
mv -v %{buildroot}%{mmdir}/Mailman/mm_cfg.py* %{buildroot}%{configdir}/
ln -srf %{buildroot}%{configdir}/mm_cfg.py* %{buildroot}%{mmdir}/Mailman/

# make sure there is a valid  group writable aliases.db
# if the aliases.db would be generated later on, list creation
# through the web interface would not work!
install -m 664 %{SOURCE6} %{buildroot}%{datadir}/aliases

# created in %%post and marked as %%ghost in the file section, so simply fake it:
%{_bindir}/touch \
    %{buildroot}%{datadir}/aliases.db

# apache stuff:
mkdir -p %{buildroot}/%{apache2_confd}
cp -av %{SOURCE9} %{buildroot}/%{apache2_confd}/mailman.conf

# link to enhance interoperability with Sendmail
mkdir -p %{buildroot}/%{sendmail_libd}/bin
ln -sf %{mmdir}/mail/mailman %{buildroot}/%{sendmail_libd}/bin/mailman

# Install manpages
install -d %{buildroot}%{_mandir}/man8/
tar xz -C %{buildroot}%{_mandir}/man8/ -f %{SOURCE2}

# Install configuration of logrotate 
install -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/logrotate.d/mailman

# Install timer systemd files
install -D -m 0644 -t %{buildroot}%{_unitdir}/ systemd-units/*

# Install mailman.service
install -m 0644 -t %{buildroot}%{_unitdir}/ %{SOURCE16}

# Install rcmailman to _sbindir
ln -sf /usr/sbin/service %{buildroot}%{_sbindir}/rcmailman

# Add symlinks to _sbindir
for service in %{timers} mailman.service ; do
    if [[ $service =~ \.service ]] ; then
        ln -sf %{_unitdir}/${service} %{buildroot}%{_sbindir}/
    fi
done

# Deduplicate
%fdupes %{buildroot}%{mmdir}

# Change permissions of directories to keep rpmlint silent
find %{buildroot}/%{mmdir} -type d -exec chmod 755 {} +
find %{buildroot}/%{templatedir} -type d -exec chmod 755 {} +
# There is no need for setgid bit in all files in those directories except cgi-bin
chmod %{buildroot}/%{mmdir} -s -R
chmod -s %{buildroot}/%{mmdir} %{buildroot}/%{mmdir}/Mailman
chmod -s %{buildroot}/%{varmmdir} %{buildroot}/%{datadir}
# cgi-bin contains ELF executables which have to have setgid
chmod g+s %{buildroot}/%{mmdir}/cgi-bin/*
chmod g+s %{buildroot}/%{mmdir}/mail/mailman

# Add executable bits to help scripts
chmod +x %{buildroot}/%{mmdir}/Mailman/Archiver/pipermail.py \
    %{buildroot}/%{mmdir}/Mailman/Post.py

# no need for setgid in configdir
chmod %{buildroot}/%{configdir} -s -R
chmod %{buildroot}/%{varmmdir} -s -R

%pre
%service_add_pre %{timers} mailman.service
getent group mailman >/dev/null \
    || %{_sbindir}/groupadd -g %{m_gid} -o -r mailman
getent passwd mailman >/dev/null \
    || %{_sbindir}/useradd -r -o -g mailman -u %{m_uid} -s /bin/bash \
       -c "GNU mailing list manager" -d %{varmmdir} mailman
exit 0

%post
%service_add_post %{timers} mailman.service
%set_permissions %{mmdir} 
%set_permissions %{mmdir}/cgi-bin/admin 
%set_permissions %{mmdir}/cgi-bin/admindb 
%set_permissions %{mmdir}/cgi-bin/confirm 
%set_permissions %{mmdir}/cgi-bin/create 
%set_permissions %{mmdir}/cgi-bin/editarch 
%set_permissions %{mmdir}/cgi-bin/edithtml 
%set_permissions %{mmdir}/cgi-bin/listinfo 
%set_permissions %{mmdir}/cgi-bin/options 
%set_permissions %{mmdir}/cgi-bin/private 
%set_permissions %{mmdir}/cgi-bin/rmlist 
%set_permissions %{mmdir}/cgi-bin/roster 
%set_permissions %{mmdir}/cgi-bin/subscribe 
%set_permissions %{mmdir}/mail/mailman 
%set_permissions %{mmdir}/Mailman 
%set_permissions %{varmmdir}
%set_permissions %{datadir}

if [ -e %{varmmdir}/logs/error ]; then
    chown wwwrun.mailman %{varmmdir}/logs/error
else
    install -m 664 -o wwwrun -g mailman /dev/null %{varmmdir}/logs/error
fi
# handle very old installations
test -d %{_localstatedir}/spool/mailman && {
    echo -n "Moving %{_localstatedir}/spool/mailman -> %{varmmdir}... "
    (cd %{varmmdir} && \
     cp -a %{_localstatedir}/spool/mailman/* .) && \
    rm -rf %{_localstatedir}/spool/mailman
    echo "Done."
}
echo "All done."

# use Mailman facilities for updating old data
%{mmdir}/bin/update
if test -z "$YAST_IS_RUNNING" ; then
    echo "Please remember to run '%{mmdir}/bin/mailman-generate-sysconfig' to configure mailman"
fi

# re-create the list aliases
%{mmdir}/bin/genaliases > /dev/null

# update the alias db file and make it group-writeable (important for
# being able to create mailing lists thru the web interface)
if [ -x %{_sbindir}/postalias -a -r %{datadir}/aliases ]; then
    %{_sbindir}/postalias %{datadir}/aliases || :
    chmod g+w %{datadir}/aliases.db
fi
exit 0

%verifyscript
%verify_permissions -e %{mmdir} 
%verify_permissions -e %{mmdir}/cgi-bin/admin 
%verify_permissions -e %{mmdir}/cgi-bin/admindb 
%verify_permissions -e %{mmdir}/cgi-bin/confirm 
%verify_permissions -e %{mmdir}/cgi-bin/create 
%verify_permissions -e %{mmdir}/cgi-bin/editarch 
%verify_permissions -e %{mmdir}/cgi-bin/edithtml 
%verify_permissions -e %{mmdir}/cgi-bin/listinfo 
%verify_permissions -e %{mmdir}/cgi-bin/options 
%verify_permissions -e %{mmdir}/cgi-bin/private 
%verify_permissions -e %{mmdir}/cgi-bin/rmlist 
%verify_permissions -e %{mmdir}/cgi-bin/roster 
%verify_permissions -e %{mmdir}/cgi-bin/subscribe 
%verify_permissions -e %{mmdir}/mail/mailman 
%verify_permissions -e %{mmdir}/Mailman 
%verify_permissions -e %{varmmdir}
%verify_permissions -e %{datadir}

%preun
%service_del_preun %{timers} mailman.service
%stop_on_removal mailman

%postun
%service_del_postun %{timers} mailman.service
%restart_on_update mailman

%files
%license gnu-COPYING-GPL
%doc ACKNOWLEDGMENTS BUGS FAQ NEWS TODO UPGRADING contrib doc/mailman-admin
%doc README README.*
%{_mandir}/man8/*.8%{?ext_man}
%dir %{mailman_confd}
%config(noreplace) %{_sysconfdir}/logrotate.d/mailman
%config(noreplace) %{mailman_confd}/mailman.*-gid
%config(noreplace) %attr(-, root, mailman) %{configdir}/mm_cfg.py*
%dir %attr(755, root, mailman) %{mmdir}/
%attr(-, root, mailman) %{mmdir}/[^Mmc]*
%attr(-, root, mailman) %{mmdir}/cron
%dir %attr(-, root, mailman) %{mmdir}/cgi-bin
%verify(not mode) %attr(2755, root, mailman) %{mmdir}/cgi-bin/*
%dir %attr(755, root, mailman) %{mmdir}/Mailman/
%attr(-, root, mailman) %{mmdir}/Mailman/*
%attr(-, root, mailman) %{mmdir}/messages
%dir %attr(-, root, mailman) %{mmdir}/mail
%verify(not mode) %attr(2755, root, mailman) %{mmdir}/mail/mailman
%dir %attr(755, mailman, mailman) %{varmmdir}/
%attr(-, root, mailman) %{varmmdir}/[^d]*
%dir %attr(775, root, mailman) %{datadir}/
%config(noreplace) %attr(-, root, mailman) %{datadir}/[^a]*
%config(noreplace) %attr(-, mailman, mailman) %{datadir}/aliases
%ghost %attr(0664, mailman, mailman) %{datadir}/aliases.db
%{_fillupdir}/*
%{_unitdir}/*
%{_sbindir}/*
%dir %{_sysconfdir}/apache2
%dir %{apache2_confd}
%config (noreplace) %{apache2_confd}/mailman.conf
%dir %{sendmail_libd}
%dir %{sendmail_libd}/bin
%{sendmail_libd}/bin/mailman

%changelog
