#
# spec file for package amavisd-new
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


%define avspool        %{_localstatedir}/spool/amavis
%define avdb           %{_localstatedir}/spool/amavis/db
%define avquarantine   %{_localstatedir}/spool/amavis/virusmails
%define logmsg         logger -t %{name}/rpm

Name:           amavisd-new
Version:        2.13.0
Release:        0
Summary:        High-Performance E-Mail Virus Scanner
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://gitlab.com/amavis/amavis/
Source0:        https://gitlab.com/amavis/amavis/-/archive/v%{version}/amavis-v%{version}.tar.bz2
Source1:        sysconfig.amavis
Source3:        amavisd-new-rpmlintrc
Source5:        amavis.service
# PATCH-FIX-UPSTREAM -- detect myhostname via Net::Domain::hostfqdn()
Patch2:         amavisd-new-2.3.0-myhostname.patch
# PATCH-FIX-OPENSUSE -- amavisd-new-no-berkeleydb.patch
Patch3:         amavisd-new-no-berkeleydb.patch
BuildRequires:  perl-App-cpanminus
BuildRequires:  perl-Dist-Zilla
BuildRequires:  group(vscan)
BuildRequires:  user(vscan)
Requires:       file
Requires:       smtp_daemon
Requires:       perl(Archive::Zip) >= 1.14
Requires:       perl(Compress::Raw::Zlib) >= 2.017
Requires:       perl(Compress::Zlib) >= 1.35
Requires:       perl(Convert::BinHex)
Requires:       perl(Digest::MD5) >= 2.22
Requires:       perl(IO::Socket::SSL)
Requires:       perl(IO::Stringy)
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::Parser)
Requires:       perl(Mail::DKIM) >= 0.31
Requires:       perl(Mail::Internet) >= 1.58
Requires:       perl(Net::Domain)
Requires:       perl(Net::LibIDN2)
Requires:       perl(Net::Server) >= 2.0
Requires:       perl(Time::HiRes) >= 1.49
Requires:       perl(Unix::Syslog)
Requires(post): %fillup_prereq
Requires(post): %{_bindir}/newaliases
Requires(pre):  group(vscan)
Requires(pre):  user(vscan)
Recommends:     %{name}-docs = %{version}
Recommends:     arc
Recommends:     arj
Recommends:     bzip2
Recommends:     cabextract
Recommends:     clamav
Recommends:     cpio
Recommends:     gzip
Recommends:     lhasa
Recommends:     lzop
Recommends:     ncompress
Recommends:     p7zip
Recommends:     spax
Recommends:     tnef
Recommends:     unrar
Recommends:     zoo
Recommends:     perl(Mail::SpamAssassin)
Recommends:     perl(Net::LDAP)
Suggests:       perl(DBD::mysql)
Suggests:       perl(DBI)
BuildArch:      noarch
%{?systemd_ordering}
%{perl_requires}

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
%autosetup -n amavis-v%{version} -p1
for i in $(find bin/ conf/ -maxdepth 1 -name "amavisd*"); do
    if [[ $i == *patch ]] ; then continue; fi
    if [[ $i == *patch ]] ; then continue; fi
    if [[ $i == *spec ]] ; then continue; fi
    echo "patching file $i"
    sed -i "s|^# \$MYHOME =.*|\$MYHOME = '%{avspool}';|g; \
            s|/var/amavis/db|%{avdb}|g; \
            s|/var/virusmails|%{avquarantine}|g; \
            s|/var/amavis/amavisd.sock|%{avspool}/amavisd.sock|g" $i
done

# ---------------------------------------------------------------------------

%build
dzil build --no-tgz --in Amavis
cd Amavis
perl Makefile.PL

# ---------------------------------------------------------------------------

%install
cd Amavis
make install INSTALLDIRS=vendor \
             INSTALLBIN=/usr/sbin \
             INSTALLSITEBIN=/usr/sbin \
             INSTALLVENDORBIN=/usr/sbin \
             INSTALLSCRIPT=/usr/sbin \
             INSTALLSITESCRIPT=/usr/sbin \
             INSTALLVENDORSCRIPT=/usr/sbin \
             DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{avquarantine}
mkdir -p %{buildroot}%{avspool}/{tmp,var}
mkdir -p %{buildroot}%{avdb}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_sysconfdir}/openldap/schema
mkdir -p %{buildroot}%{perl_vendorlib}
install -m 644 conf/amavisd.conf %{buildroot}%{_sysconfdir}/amavisd.conf
install -m 644 $RPM_SOURCE_DIR/sysconfig.amavis %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}
install -m 644 contrib/LDAP.schema %{buildroot}%{_sysconfdir}/openldap/schema/amavisd-new.schema
install -m 644 contrib/JpegTester.pm %{buildroot}/%{perl_vendorlib}/JpegTester.pm
ln -s service %{buildroot}/%{_sbindir}/rcamavis
rm -rf %{buildroot}/%{perl_archlib}/
rm -rf %{buildroot}/%{perl_vendorarch}/

%pre
%service_add_pre amavis.service

%preun
%service_del_preun amavis.service

%post
%{fillup_only -n amavis}
# Only on install
if [ ${1:-0} -eq 1 ] && ! grep -q "^virusalert:" %{_sysconfdir}/aliases; then
  echo "virusalert:	root" >> %{_sysconfdir}/aliases
  %logmsg "Added alias for user virusalert to %{_sysconfdir}/aliases"
  if [ -x %{_bindir}/newaliases ]; then
    newaliases >/dev/null 2>&1 || :
  else
    %logmsg "Cannot execute newaliases. Please run it manually."
  fi
fi
%service_add_post amavis.service

%postun
%service_del_postun amavis.service

%files
%license LICENSE
%doc AAAREADME.first
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/amavisd.conf
%config(noreplace) %{_sysconfdir}/openldap/schema/amavisd-new.schema
%{_fillupdir}/sysconfig.amavis
%{_sbindir}/*
%{perl_vendorlib}/JpegTester.pm
%{perl_vendorlib}/Amavis.pm
%{perl_vendorlib}/Amavis
%{perl_vendorlib}/Mail/SpamAssassin/Logger/Amavislog.pm
%{_unitdir}/amavis.service
%dir %{perl_vendorlib}/Mail
%dir %{perl_vendorlib}/Mail/SpamAssassin
%dir %{perl_vendorlib}/Mail/SpamAssassin/Logger
%defattr(0750,vscan,vscan,0750)
%dir %{avspool}/
%dir %{avspool}/tmp
%dir %{avspool}/db
%dir %{avspool}/var
%dir %{avquarantine}

%files docs
%defattr(0644,root,root,0755)
%doc RELEASE_NOTES README_FILES TODO
%doc conf/amavisd-custom.conf conf/amavisd.conf-default conf/amavisd-docker.conf
%doc contrib/LDAP.ldif
/usr/share/man/man3/Amavis::SpamControl::RspamdClient.3pm.gz

%changelog
