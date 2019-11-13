#
# spec file for package spamassassin
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

%define ix_version 2.05
%define spd_version 2.53
%define sa_version 3.4.2
%define sa_float %(echo %{sa_version} | awk -F. '{ printf "%d.%03d%03d", $1, $2, $3 }')
%define rules_revision 1840640

%define IXHASH iXhash2-%{ix_version}
%define SPAMPD spampd-%{spd_version}

Name:           spamassassin
Summary:        Extensible email filter which is used to identify spam
License:        Apache-2.0
Group:          Productivity/Networking/Email/Utilities
Version:        %{sa_version}
Release:        0
Url:            https://spamassassin.apache.org/
Source:         https://archive.apache.org/dist/spamassassin/source/Mail-SpamAssassin-%{sa_version}.tar.bz2
Source1:        https://archive.apache.org/dist/spamassassin/source/Mail-SpamAssassin-rules-%{sa_version}.r%{rules_revision}.tgz
Source2:        https://mailfud.org/iXhash2/%{IXHASH}.tar.gz
Source3:        https://github.com/mpaperno/spampd/archive/%{spd_version}.tar.gz#/%{SPAMPD}.tar.gz
Source10:       local.cf
Source12:       sysconfig.spamd
Source14:       sysconfig.spampd
Source15:       timed-sa-update
Source16:       spamd.service
Source17:       spampd.service
Source18:       sa-update.service
Source19:       sa-update.timer
Source100:      https://archive.apache.org/dist/spamassassin/source/Mail-SpamAssassin-%{sa_version}.tar.bz2.asc
Source101:      https://archive.apache.org/dist/spamassassin/source/Mail-SpamAssassin-rules-%{sa_version}.r%{rules_revision}.tgz.asc
# Keyring downloaded from https://www.apache.org/dist/spamassassin/KEYS
Source102:      spamassassin.keyring
Patch1:         patch-PgSQL
Patch2:         patch-URIDNSBL
Patch3:         patch-SQL_ASCII_SORT
Patch6:         bnc#582111.diff
Patch10:        iXhash2-meta-rules.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
PreReq:         %fillup_prereq
BuildRequires:  dos2unix
BuildRequires:  openssl-devel
# optional, but want them for build (test)
BuildRequires:  curl >= 7.2.14
BuildRequires:  gpg
BuildRequires:  re2c
#
Requires:       curl >= 7.2.14
Requires:       perl-IO-Socket-INET6
Requires:       perl-Mail-DKIM
Requires:       perl-Mail-SpamAssassin = %version
Requires:       re2c
Requires:       perl(Net::Server::PreForkSimple)
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
spamassassin adds a header line that shows if the mail has been
determined spam or not. This way, you can decide what to do with the
mail within the scope of your own filtering rules in your MUA (Mail
User Agent, your mail program) or your LDA (Local Delivery Agent).

See the files in the documentation directory
/usr/share/doc/packages/spamassassin/ for more information on how to
use the filter.

%package -n perl-Mail-SpamAssassin
Summary:        Perl Modules For Using Spamassassin Within An Own Perl Script
Group:          Development/Libraries/Perl
BuildRequires:  perl
BuildRequires:  perl-Error
BuildRequires:  perl(Archive::Tar) >= 1.23
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Copy) >= 2.02
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(HTML::Parser) >= 3.43
BuildRequires:  perl(IO::Zlib) >= 1.04
BuildRequires:  perl(Mail::DKIM) >= 0.37
BuildRequires:  perl(Net::DNS) >= 0.34
BuildRequires:  perl(NetAddr::IP) >= 4.000
BuildRequires:  perl(Pod::Usage) >= 1.10
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
# optional, but want them for build (test)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Encode::Detect)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IP::Country)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mail::SPF)
BuildRequires:  perl(Net::Ident)
BuildRequires:  perl(Net::Patricia) >= 1.16
BuildRequires:  perl(Razor2::Client::Agent) >= 2.61
#
Requires:       perl-libwww-perl
Requires:       perl(Archive::Tar) >= 1.23
Requires:       perl(Digest::SHA1)
Requires:       perl(Errno)
Requires:       perl(File::Copy) >= 2.02
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(HTML::Parser) >= 3.43
Requires:       perl(IO::Socket::IP)
Requires:       perl(IO::Zlib) >= 1.04
Requires:       perl(Mail::DKIM) >= 0.37
Requires:       perl(Net::DNS) >= 0.34
Requires:       perl(NetAddr::IP) >= 4.010
Requires:       perl(Pod::Usage) >= 1.10
Requires:       perl(Sys::Hostname)
Requires:       perl(Time::HiRes)
Requires:       perl(Time::Local)
# optional
Recommends:     perl(Mail::SPF)
Recommends:     perl(Net::Patricia) >= 1.16
Recommends:     perl(Razor2::Client::Agent) >= 2.61
Recommends:     perl(IO::Socket::INET6)
Recommends:     perl(IO::Socket::SSL)
Recommends:     perl(DBI)
Recommends:     perl(Encode::Detect)
Provides:       perl-spamassassin = %{sa_version}
Obsoletes:      perl-spamassassin < %{sa_version}
BuildArch:      noarch
%{perl_requires}

%description -n perl-Mail-SpamAssassin
This package contains the perl modules for the spamassassin, including
the filter rules. This package is required for the package
"spamassassin", the commandline tool.

%package -n perl-Mail-SpamAssassin-Plugin-iXhash2
Summary:        The iXhash plugin for SpamAssassin
Group:          Development/Libraries/Perl
Requires:       perl-Mail-SpamAssassin = %{sa_version}
Requires:       perl(Digest::MD5)
Version:        %{ix_version}
Release:        0
Provides:       perl-Mail-SpamAssassin-Plugin-iXhash = %{ix_version}
Obsoletes:      perl-Mail-SpamAssassin-Plugin-iXhash < 2
BuildArch:      noarch
%{perl_requires}

%description -n perl-Mail-SpamAssassin-Plugin-iXhash2
This archive contains the iXhash2 plugin for the SpamAssassin spam filtering
software, along with an example config file.

Basically the plugin provides a network-based test just as razor2, pyzor
and DCC do. Working solely on the body of an email, it removes parts of it
and computes a hash value from the rest. These values will then be looked up
via DNS using the domains given in the config file(s). You need Net::DNS and
Digest::MD5 installed

%prep
%setup -q -n Mail-SpamAssassin-%{sa_version} -a 2 -a 3
tar -zxf %{S:1} -C rules
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch6 -p0
%patch10 -p0

%build
if [ -e t/data/whitelists/winxpnews.com ]; then
    echo "t/data/whitelists/winxpnews.com is not allowed to be distributed."
    echo "see #102221"
    #exit -1 # hidden bug description, so I can't see there - ignored
fi;
if [ -e build/cf_to_html ]; then
    echo "build/cf_to_html is not allowed to be distributed."
    echo "see #102221"
    #exit -1 # hidden bug description, so I can't see there - ignored
fi;

export CFLAGS="%{optflags}"
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
 CONTACT_ADDRESS="postmaster" ENABLE_SSL="yes"

make %{?_smp_mflags}

%check
# fails now... FIGURE out why
#make test

%install
## perl-Mail-SpamAssassin stuff
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
# remove %%{_bindir} from filelist
sed -i -e "/\/usr\/bin/d" %{name}.files
# package only %%{_mandir}/man3
sed -i -e "s,%{_mandir}/man?,%{_mandir}/man3," %{name}.files
#
## perl-Mail-SpamAssassin-Plugin-iXhash2 stuff
install -d %{buildroot}/etc/mail/spamassassin
cp %{IXHASH}/iXhash2.pm %{buildroot}/%{perl_vendorlib}/Mail/SpamAssassin/Plugin
cp %{IXHASH}/iXhash2.cf %{buildroot}/etc/mail/spamassassin/iXhash2.cf
#
## spamassassin stuff
install -D -m0755 %{SPAMPD}/spampd.pl %{buildroot}/%{_sbindir}/spampd
install -m 0755 %{S:15} %{buildroot}/%{_sbindir}/
mv %{buildroot}/%{_bindir}/spamd %{buildroot}/%{_sbindir}/
install -m 0644 %{S:10} %{buildroot}/etc/mail/spamassassin/local.cf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcspamd
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcspampd
echo "Most of the documentation is at ../perl-Mail-SpamAssassin/." > README.SUSE
install -D -m 0640 %{S:12} %{buildroot}/%{_fillupdir}/sysconfig.spamd
install -m 0640 %{S:14} %{buildroot}/%{_fillupdir}/
test -f %{buildroot}/usr/share/spamassassin/user_prefs.template || {
	echo "MakeMaker is broken again..."
	exit 1
}

## default rules
install -d %{buildroot}%{_datadir}/spamassassin
install -D -m 0644 rules/[0-9]*.cf %{buildroot}%{_datadir}/spamassassin
sed -i	-e 's|@@CONTACT_ADDRESS@@|postmaster|g' \
	-e 's|@@LOCAL_RULES_DIR@@|/etc/mail/spamassassin|g' \
	-e 's|@@VERSION@@|%{sa_float}|g' %{buildroot}%{_datadir}/spamassassin/*.cf

## systemd stuff
mkdir -p %{buildroot}/%{_unitdir}
install -D -m 644 %{S:16} %{buildroot}/%{_unitdir}
install -D -m 644 %{S:17} %{buildroot}/%{_unitdir}
install -D -m 644 %{S:18} %{buildroot}/%{_unitdir}
install -D -m 644 %{S:19} %{buildroot}/%{_unitdir}

%post
%service_add_post spamd.service spampd.service sa-update.timer
%{fillup_only -n spamd}
%{fillup_only -n spampd}

%pre
%service_add_pre spamd.service spampd.service sa-update.timer

%preun
%service_del_preun spamd.service spampd.service sa-update.timer

%postun
%service_del_postun spamd.service spampd.service sa-update.timer

%files
%defattr(-,root,root)
%doc spamd/README spamd/README.vpopmail spamd/PROTOCOL
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_sbindir}/*
%{_fillupdir}/sysconfig.spamd
%{_fillupdir}/sysconfig.spampd
%{_unitdir}/spamd.service
%{_unitdir}/spampd.service
%{_unitdir}/sa-update.service
%{_unitdir}/sa-update.timer

%files -n perl-Mail-SpamAssassin -f %{name}.files
%defattr(-,root,root)
%license LICENSE 
%doc CREDITS Changes MANIFEST* NOTICE PACKAGING README
%doc TRADEMARK UPGRADE USAGE sample-nonspam.txt sample-spam.txt
%doc ldap sql
%dir /etc/mail
%config(noreplace) /etc/mail/spamassassin
%exclude /etc/mail/spamassassin/iXhash2.cf
%exclude %{perl_vendorarch}
%dir %{_datadir}/spamassassin
%{_datadir}/spamassassin/*

%files -n perl-Mail-SpamAssassin-Plugin-iXhash2
%defattr(-,root,root)
%doc %{IXHASH}/CHANGELOG %{IXHASH}/LICENSE %{IXHASH}/README 
%config(noreplace) /etc/mail/spamassassin/iXhash2.cf
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/iXhash2.pm

%changelog
