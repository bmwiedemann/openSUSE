#
# spec file for package amavisd-new
#
# Copyright (c) 2020 SUSE LLC
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
%define _buildshell /bin/bash

%define avspool        /var/spool/amavis
%define avdb           /var/spool/amavis/db
%define avquarantine   /var/spool/amavis/virusmails
%define logmsg         logger -t %{name}/rpm
%define avuser         vscan
%define avgroup        vscan
Name:           amavisd-new
Version:        2.11.1
Release:        0
Summary:        High-Performance E-Mail Virus Scanner
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://amavis.org/
Source0:        https://amavis.org/%{name}-%{version}.tar.bz2
Source1:        sysconfig.amavis
Source2:        rc.amavis
Source3:        amavisd-new-rpmlintrc
Source4:        amavisd-milter-1.6.1.tar.gz
Source5:        amavis.service
Source6:        amavisd-milter.sh
Patch1:         activate_virus_scanner.diff
# PATCH-FIX-UPSTREAM -- detect myhostname via Net::Domain::hostfqdn()
Patch2:         amavisd-new-2.10.1-myhostname.patch
# PATCH-FIX-UPSTREAM -- originating was not recognized for DKIM signing
Patch3:         dkim-signing.diff
BuildRequires:  sed
BuildRequires:  sendmail
BuildRequires:  sendmail-devel
BuildRequires:  xz
Requires:       bzip2
Requires:       file
Requires:       gzip
Requires:       perl-Archive-Tar
Requires:       perl-Archive-Zip
Requires:       perl-BerkeleyDB
Requires:       perl-Compress-Zlib
Requires:       perl-Convert-BinHex
Requires:       perl-Convert-TNEF
Requires:       perl-Convert-UUlib
Requires:       perl-IO-stringy
Requires:       perl-MIME-tools
Requires:       perl-Mail-DKIM
Requires:       perl-MailTools
Requires:       perl-Net-LibIDN
Requires:       perl-Net-Server
Requires:       perl-Unix-Syslog
Requires:       perl-spamassassin
Requires:       sharutils
Requires:       smtp_daemon
Requires:       spamassassin
Requires:       zoo
Recommends:     unar
Recommends:     clamav perl-spamassassin
Recommends:     perl-DBI
Recommends:     perl-ldap
Recommends:     perl-Authen-SASL
Recommends:     perl-Mail-ClamAV
Recommends:     p7zip
Recommends:     binutils
Recommends:     %{name}-docs = %{version}
Requires(pre):  util-linux-systemd
Requires(post): util-linux-systemd
Requires(pre):  shadow
Requires(post): %fillup_prereq
Requires(post): grep
OrderWithRequires(post): /usr/bin/newaliases
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
Provides:       amavisd-milter = 1.6.0
Obsoletes:      amavisd-milter <= 1.5.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Amavisd-new is a high-performance interface between mailer (MTA) and
content checkers: virus scanners or SpamAssassin. It talks to the MTA
via (E)SMTP, LMTP. It works with the
following MTAs:

- postfix
- sendmail (sendmail-milter)
- exim


%package docs
Summary:        Documentation for the High-Performance E-Mail Virus Scanner
Group:          Documentation/Other
Recommends:     %{name} = %{version}

%description docs
Amavisd-new is a high-performance interface between mailer (MTA) and
content checkers: virus scanners or SpamAssassin. It talks to the MTA
via (E)SMTP, LMTP.

This package contains the documentation and Release-Notes.

%prep
%setup -q -a 4
%patch1 -p1
%patch2 -p1
%patch3 -p1
for i in $(find -maxdepth 1 -name "amavisd*" | sed s#./##); do
    if [[ $i == *patch ]] ; then continue; fi
    if [[ $i == *patch ]] ; then continue; fi
    if [[ $i == *spec ]] ; then continue; fi
    if [[ $i == amavisd-milter* ]] ; then continue; fi
    echo "patching file $i"
    sed -i "s|\$daemon_user  = 'vscan';|\$daemon_user  = '%{avuser}';|g; \
            s|\$daemon_group = 'vscan';|\$daemon_group = '%{avgroup}';|g; \
            s|^# \$MYHOME =.*|\$MYHOME = '%{avspool}';|g; \
            s|/var/amavis/db|%{avdb}|g; \
            s|/var/virusmails|%{avquarantine}|g; \
            s|/var/amavis/amavisd.sock|%{avspool}/amavisd.sock|g" $i
done

# ---------------------------------------------------------------------------

%build
cd amavisd-milter*
%configure --localstatedir="%{avspool}"
make %{?_smp_mflags}

# ---------------------------------------------------------------------------

%install
mkdir -p %{buildroot}%{avquarantine}
mkdir -p %{buildroot}%{avspool}/{tmp,var}
mkdir -p %{buildroot}%{avdb}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}/etc/openldap/schema
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 644 $RPM_SOURCE_DIR/sysconfig.amavis %{buildroot}%{_fillupdir}
install -m 755 amavisd %{buildroot}/%{_sbindir}/amavisd
install -m 755 amavisd-agent %{buildroot}/%{_sbindir}/amavisd-agent
install -m 755 amavisd-nanny %{buildroot}/%{_sbindir}/amavisd-nanny
install -m 755 amavisd-release %{buildroot}/%{_sbindir}/amavisd-release
install -m 755 p0f-analyzer.pl %{buildroot}/%{_sbindir}/p0f-analyzer.pl
install -m 644 amavisd.conf %{buildroot}/etc/amavisd.conf
install -m 644 LDAP.schema %{buildroot}/etc/openldap/schema/amavisd-new.schema
install -m 644 JpegTester.pm %{buildroot}/%{perl_vendorlib}/JpegTester.pm
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{S:5} %{buildroot}%{_unitdir}
ln -s service %{buildroot}/%{_sbindir}/rcamavis
install -m 755 %{S:6} %{buildroot}%{_sbindir}/
cd amavisd-milter*
%make_install

%pre
getent group %{avgroup} >/dev/null || \
	%{_sbindir}/groupadd -r %{avgroup}
%{logmsg} "Added group %{avgroup} for package %{name}"
getent passwd %{avuser} >/dev/null || \
	%{_sbindir}/useradd -r -o -g %{avgroup} -u 65 -s /bin/false \
	-c "Vscan account" -d %{avspool} %{avuser}
%{_sbindir}/usermod %{avuser} -g %{avgroup} 2> /dev/null || :
%{logmsg} "Added user %{avuser} for package %{name}"
%service_add_pre amavis.service

%preun
%service_del_preun amavis.service
exit 0

%post
%{fillup_only -n amavis}
%service_add_post amavis.service
# Update ?
if [ ${1:-0} -gt 1 ]; then
 : OK currently nothing to do
else
  if [ -r etc/aliases ]; then
    if ! grep -q "^virusalert:" etc/aliases; then
      echo "virusalert:	root" >> etc/aliases
      %{logmsg} "Added alias for user virusalert to /etc/aliases"
      if [ -x usr/bin/newaliases ]; then
          usr/bin/newaliases >/dev/null 2>&1 || true
      else
          %{logmsg} "Cannot execute newaliases. Please run it manually."
      fi
    fi
  fi
fi

%postun
%service_del_postun amavis.service

%files
%defattr(-,root,root)
%doc AAAREADME.first LICENSE
%doc LDAP.ldif
%dir /etc/openldap
%dir /etc/openldap/schema
%dir /usr/lib/tmpfiles.d
%if 0%{?suse_version} < 1230
%config /etc/init.d/amavis
%endif
%config(noreplace) /etc/amavisd.conf
%config(noreplace) /etc/openldap/schema/amavisd-new.schema
%{_fillupdir}/sysconfig.amavis
%{_sbindir}/*
%{perl_vendorlib}/JpegTester.pm
%{_unitdir}/amavis.service
%{_sbindir}/amavisd-milter.sh
%defattr(0750,%{avuser},%{avgroup}, 0750)
%dir %{avspool}
%dir %{avspool}/tmp
%dir %{avspool}/db
%dir %{avspool}/var
%dir %{avquarantine}

%files docs
%defattr(0644,root,root,0755)
%doc RELEASE_NOTES
%doc README_FILES
%doc test-messages
%doc amavisd.conf-*
%doc MANIFEST TODO
%doc test-messages
%doc %{_mandir}/man8/amavisd-milter*

%changelog
