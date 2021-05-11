#
# spec file for package amavisd-new
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.12.1
Release:        0
Summary:        High-Performance E-Mail Virus Scanner
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://gitlab.com/amavis/amavis/
Source0:        https://gitlab.com/amavis/amavis/-/archive/v%{version}/amavis-v%{version}.tar.bz2
Source1:        sysconfig.amavis
Source3:        amavisd-new-rpmlintrc
Source5:        amavis.service
%if 0%{?suse_version} <= 1500
Source10:       system-user-vscan.conf
%endif
Patch1:         activate_virus_scanner.diff
# PATCH-FIX-UPSTREAM -- detect myhostname via Net::Domain::hostfqdn()
Patch2:         amavisd-new-2.10.1-myhostname.patch
# PATCH-FIX-OPENSUSE -- amavisd-new-no-berkeleydb.patch
Patch3:         amavisd-new-no-berkeleydb.patch
%if 0%{?suse_version} > 1500
BuildRequires:  group(vscan)
BuildRequires:  user(vscan)
%else
BuildRequires:  sysuser-tools
%endif
Requires:       file
Requires:       smtp_daemon
Requires:       perl(Archive::Zip) >= 1.14
Requires:       perl(Compress::Raw::Zlib) >= 2.017
Requires:       perl(Compress::Zlib) >= 1.35
Requires:       perl(Convert::BinHex)
Requires:       perl(Digest::MD5) >= 2.22
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::Parser)
Requires:       perl(Mail::DKIM) >= 0.31
Requires:       perl(Mail::Internet) >= 1.58
Requires:       perl(Net::Domain)
Requires:       perl(Net::Server) >= 2.0
Requires:       perl(Time::HiRes) >= 1.49
Requires:       perl(Unix::Syslog)
Requires(post): %fillup_prereq
Requires(post): %{_bindir}/newaliases
%if 0%{?suse_version} > 1500
Requires(pre):  group(vscan)
Requires(pre):  user(vscan)
%else
Requires(pre):  system-user-vscan
%endif
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

%if 0%{?suse_version} <= 1500
%package -n system-user-vscan
Summary:        System user and group vscan
Group:          Productivity/Networking/Security
%sysusers_requires

%description -n system-user-vscan
This package provides the system user 'vscan'.
%endif

%prep
%autosetup -n amavis-v%{version} -p1
for i in $(find -maxdepth 1 -name "amavisd*" | sed s#./##); do
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
%if 0%{?suse_version} <= 1500
# Create vscan user
%sysusers_generate_pre %{SOURCE10} vscan
%endif

# ---------------------------------------------------------------------------

%install
%if 0%{?suse_version} <= 1500
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{avspool}
install -m 644 %{SOURCE10} %{buildroot}%{_sysusersdir}/system-user-vscan.conf
%endif
mkdir -p %{buildroot}%{avquarantine}
mkdir -p %{buildroot}%{avspool}/{tmp,var}
mkdir -p %{buildroot}%{avdb}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_sysconfdir}/openldap/schema
mkdir -p %{buildroot}%{perl_vendorlib}
install -m 644 $RPM_SOURCE_DIR/sysconfig.amavis %{buildroot}%{_fillupdir}
install -m 755 amavisd %{buildroot}/%{_sbindir}/amavisd
install -m 755 amavisd-agent %{buildroot}/%{_sbindir}/amavisd-agent
install -m 755 amavisd-nanny %{buildroot}/%{_sbindir}/amavisd-nanny
install -m 755 amavisd-release %{buildroot}/%{_sbindir}/amavisd-release
install -m 755 p0f-analyzer.pl %{buildroot}/%{_sbindir}/p0f-analyzer.pl
install -m 644 amavisd.conf %{buildroot}%{_sysconfdir}/amavisd.conf
install -m 644 LDAP.schema %{buildroot}%{_sysconfdir}/openldap/schema/amavisd-new.schema
install -m 644 JpegTester.pm %{buildroot}/%{perl_vendorlib}/JpegTester.pm
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}
ln -s service %{buildroot}/%{_sbindir}/rcamavis

%if 0%{?suse_version} <= 1500
%pre -n system-user-vscan -f vscan.pre
%endif

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
%doc LDAP.ldif
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/amavisd.conf
%config(noreplace) %{_sysconfdir}/openldap/schema/amavisd-new.schema
%{_fillupdir}/sysconfig.amavis
%{_sbindir}/*
%{perl_vendorlib}/JpegTester.pm
%{_unitdir}/amavis.service
%defattr(0750,vscan,vscan,0750)
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

%if 0%{?suse_version} <= 1500
%files -n system-user-vscan
%dir %attr(0750,vscan,vscan) %{avspool}
%{_sysusersdir}/system-user-vscan.conf
%endif

%changelog
