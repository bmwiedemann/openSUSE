#
# spec file for package spamassassin
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without test

%define ix_version 4.00
%define spd_version 2.61
%define sa_version 4.0.0
%define sa_float %(echo %{sa_version} | awk -F. '{ printf "%d.%03d%03d", $1, $2, $3 }')
%define perl_float %(echo %{perl_version} | awk -F. '{ printf "%d.%03d", $1, $2 }')
%define rules_revision 1905950

%define IXHASH iXhash2-%{ix_version}
%define SPAMPD spampd-%{spd_version}

Name:           spamassassin
Version:        %{sa_version}
Release:        0
Summary:        Extensible email filter which is used to identify spam
License:        Apache-2.0
Group:          Productivity/Networking/Email/Utilities
URL:            https://spamassassin.apache.org/
Source0:        https://downloads.apache.org/spamassassin/source/Mail-SpamAssassin-%{sa_version}.tar.bz2
Source1:        https://downloads.apache.org/spamassassin/source/Mail-SpamAssassin-rules-%{sa_version}.r%{rules_revision}.tgz
Source2:        https://mailfud.org/iXhash2/%{IXHASH}.tar.gz
Source3:        https://github.com/mpaperno/spampd/archive/%{spd_version}.tar.gz#/%{SPAMPD}.tar.gz
Source10:       local.cf
Source11:       README.SUSE
Source12:       sysconfig.spamd
Source14:       sysconfig.spampd
Source15:       timed-sa-update
Source16:       spamd.service
Source17:       spampd.service
Source18:       sa-update.service
Source19:       sa-update.timer
Source100:      https://downloads.apache.org/spamassassin/source/Mail-SpamAssassin-%{sa_version}.tar.bz2.asc
Source101:      https://downloads.apache.org/spamassassin/source/Mail-SpamAssassin-rules-%{sa_version}.r%{rules_revision}.tgz.asc
# Keyring downloaded from https://www.apache.org/dist/spamassassin/KEYS
Source102:      spamassassin.keyring
Source103:      %{name}-rpmlintrc
Patch1:         patch-PgSQL
Patch2:         patch-URIDNSBL
Patch3:         patch-SQL_ASCII_SORT
Patch6:         bnc#582111.diff
Patch7:         basic-lint-without-sandbox.patch
Patch10:        iXhash2-meta-rules.patch
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# optional, but want them for build (test)
BuildRequires:  curl >= 7.2.14
BuildRequires:  gpg
BuildRequires:  netcfg
BuildRequires:  re2c
BuildRequires:  wget >= 1.8.2
#
Requires:       re2c
Requires:       spamassassin-spamc = %{sa_version}
Requires:       (curl >= 7.2.14 or wget >= 1.8.2)
Requires:       perl(Archive::Tar) >= 1.23
Requires:       perl(Error)
Requires:       perl(IO::Zlib) >= 1.04
Requires:       perl(LWP)
Requires:       perl(Mail::SpamAssassin) = %{sa_float}
Requires:       perl(Net::Server::PreForkSimple)
Requires(post): %fillup_prereq
%{?systemd_ordering}

%description
spamassassin adds a header line that shows if the mail has been
determined spam or not. This way, you can decide what to do with the
mail within the scope of your own filtering rules in your MUA (Mail
User Agent, your mail program) or your LDA (Local Delivery Agent).

See the files in the documentation directory
%{_docdir}/spamassassin/ for more information on how to
use the filter.

%package spamc
Summary:        Spammassassin Client
Group:          Productivity/Networking/Email/Utilities

%description spamc
Spamc is the client to contact the spammassassin spamd daemon. It should
be used in place of "spamassassin" in scripts to process mail.

%package -n perl-Mail-SpamAssassin
Summary:        Perl Modules For Using Spamassassin Within An Own Perl Script
Group:          Development/Libraries/Perl
BuildRequires:  perl(Archive::Tar) >= 1.23
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Copy) >= 2.02
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(Getopt::Long) >= 2.32
BuildRequires:  perl(HTML::Parser) >= 3.43
BuildRequires:  perl(IO::Zlib) >= 1.04
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mail::DKIM) >= 0.37
BuildRequires:  perl(Net::DNS) >= 0.69
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(NetAddr::IP) >= 4.010
BuildRequires:  perl(Pod::Usage) >= 1.10
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
# required for tests
BuildRequires:  perl(Devel::Cycle)
#BuildRequires:  perl(Perl::Critic::Policy::Perlsecret)
BuildRequires:  perl(Perl::Critic::Policy::TestingAndDebugging::ProhibitNoStrict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
# optional, but want them for build (test)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(Encode::Detect::Detector)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL) >= 1.76
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IP::Country::Fast)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mail::SPF) >= 2.001
BuildRequires:  perl(Net::CIDR::Lite)
BuildRequires:  perl(Net::Ident)
BuildRequires:  perl(Net::LibIDN)
BuildRequires:  perl(Net::Patricia) >= 1.16
BuildRequires:  perl(Razor2::Client::Agent) >= 2.61
#
Requires:       perl(Archive::Zip)
Requires:       perl(Digest::SHA1)
Requires:       perl(Errno)
Requires:       perl(File::Copy) >= 2.02
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(HTML::Parser) >= 3.43
Requires:       perl(Mail::DKIM) >= 0.31
Requires:       perl(Net::DNS) >= 0.69
Requires:       perl(NetAddr::IP) >= 4.010
Requires:       perl(Pod::Usage) >= 1.10
Requires:       perl(Sys::Hostname)
Requires:       perl(Time::HiRes)
Requires:       perl(Time::Local)
Recommends:     perl(Archive::Tar) >= 1.23
Recommends:     perl(BSD::Resource)
Recommends:     perl(Compress::Zlib)
Recommends:     perl(DB_File)
Recommends:     perl(Email::Address::XS)
Recommends:     perl(Encode::Detect::Detector)
Recommends:     perl(Getopt::Long) >= 2.32
Recommends:     perl(HTTP::Date)
Recommends:     perl(IO::Socket::INET6)
Recommends:     perl(IO::Socket::IP)
Recommends:     perl(IO::Socket::SSL) >= 1.76
Recommends:     perl(IO::String)
Recommends:     perl(IO::Zlib) >= 1.04
Recommends:     perl(IP::Country::Fast)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(MIME::Base64)
Recommends:     perl(Mail::DKIM) >= 0.37
Recommends:     perl(Mail::SPF) >= 2.001
Recommends:     perl(Net::CIDR::Lite)
Recommends:     perl(Net::DNS) >= 0.58
Recommends:     perl(Net::Ident)
Recommends:     perl(Net::LibIDN)
Recommends:     perl(Net::Patricia) >= 1.16
Recommends:     perl(Net::SMTP)
Recommends:     perl(Razor2::Client::Agent) >= 2.61
Recommends:     perl(Test::More)
Suggests:       perl(DBD::mysql)
Suggests:       perl(DBI)
Suggests:       perl(Geo::IP)
Suggests:       perl(GeoIP2::Database::Reader)
Provides:       perl-spamassassin = %{sa_version}
Obsoletes:      perl-spamassassin < %{sa_version}
BuildArch:      noarch
%{perl_requires}

%description -n perl-Mail-SpamAssassin
This package contains the perl modules for the spamassassin, including
the filter rules. This package is required for the package
"spamassassin", the commandline tool.

%package -n perl-Mail-SpamAssassin-Plugin-iXhash2
Version:        %{ix_version}
Release:        0
Summary:        The iXhash plugin for SpamAssassin
Group:          Development/Libraries/Perl
Requires:       perl(Digest::MD5)
Requires:       perl(Mail::SpamAssassin) = %{sa_float}
Provides:       perl-Mail-SpamAssassin-Plugin-iXhash = %{ix_version}
Obsoletes:      perl-Mail-SpamAssassin-Plugin-iXhash < %{ix_version}
BuildArch:      noarch
%{perl_requires}

%description -n perl-Mail-SpamAssassin-Plugin-iXhash2
This archive contains the iXhash2 plugin for the SpamAssassin spam filtering
software, along with an example config file.

Basically the plugin provides a network-based test just as razor2, pyzor
and DCC do. Working solely on the body of an email, it removes parts of it
and computes a hash value from the rest. These values will then be looked up
via DNS using the domains given in the config file(s).

%prep
%setup -q -n Mail-SpamAssassin-%{sa_version} -a 2 -a 3
tar -zxf %{SOURCE1} -C rules
%patch1
%patch2 -p1
%patch3
%patch6
%patch7 -p1
%patch10 -p1
cp %{SOURCE11} ./

%build
# Run substitutions in default rules
sed -i	-e 's|@@CONTACT_ADDRESS@@|postmaster|g' \
	-e 's|@@LOCAL_RULES_DIR@@|%{_sysconfdir}/mail/spamassassin|g' \
	-e 's|@@VERSION@@|%{sa_float}|g' rules/*.cf

export CFLAGS="%{optflags}"
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
	CONTACT_ADDRESS="postmaster" ENABLE_SSL="yes"

%make_build

%check
%if %{with test}
# Relax the crypto policies for the test-suite
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export OPENSSL_CONF=''
%make_build -j1 test
%endif

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
install -d %{buildroot}%{_sysconfdir}/mail/spamassassin
cp %{IXHASH}/iXhash2.pm %{buildroot}%{perl_vendorlib}/Mail/SpamAssassin/Plugin
cp %{IXHASH}/iXhash2.cf %{buildroot}%{_sysconfdir}/mail/spamassassin/iXhash2.cf
#
## spamassassin stuff
install -D -m0755 %{SPAMPD}/spampd.pl %{buildroot}%{_sbindir}/spampd
install -m 0755 %{SOURCE15} %{buildroot}%{_sbindir}/
mv %{buildroot}%{_bindir}/spamd %{buildroot}%{_sbindir}/
install -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcspamd
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcspampd
install -D -m 0640 %{SOURCE12} %{buildroot}%{_fillupdir}/sysconfig.spamd
install -m 0640 %{SOURCE14} %{buildroot}%{_fillupdir}/
test -f %{buildroot}%{_datadir}/spamassassin/user_prefs.template || {
	echo "MakeMaker is broken again..."
	exit 1
}

## default rules
install -d %{buildroot}%{_datadir}/spamassassin
install -D -m 0644 rules/[0-9]*.cf %{buildroot}%{_datadir}/spamassassin

## systemd stuff
install -d %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE16} %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE17} %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE18} %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE19} %{buildroot}%{_unitdir}

%post
%service_add_post spamd.service spampd.service sa-update.timer
%{fillup_only -n spamd}
%{fillup_only -n spampd}
if [ $1 -gt 1 ]; then
	# Package upgrade
	for dir in $(ls -d %{_sharedstatedir}/%{name}/{,compiled/*/}[0-9\.]* 2>/dev/null); do
		if [ "${dir##*/}" != "%{sa_float}" ]; then
			rm -rf ${dir}
		fi
	done
	find %{_sharedstatedir}/%{name} -type d -empty -delete 2>/dev/null || :

	# Compile rules if Perl and/or spamassassin version changed
	if [ ! -d %{_sharedstatedir}/%{name}/compiled/%{perl_float}/%{sa_float} ]; then
		grep -q "^SPAM_SA_COMPILE.*yes.*" %{_sysconfdir}/sysconfig/spamd && %{_bindir}/sa-compile &> /dev/null || :
	fi
fi

%pre
%service_add_pre spamd.service spampd.service sa-update.timer

%preun
%service_del_preun spamd.service spampd.service sa-update.timer

%postun
%service_del_postun spamd.service spampd.service sa-update.timer
if [ $1 -eq 0 ]; then
	# Package removal
	rm -rf %{_sharedstatedir}/%{name}
fi

%files
%defattr(-,root,root)
%doc spamd/README spamd/README.vpopmail spamd/PROTOCOL README.SUSE
%{_mandir}/man1/sa-*
%{_mandir}/man1/spamassassin*
%{_mandir}/man1/spamd.1*
%{_bindir}/sa-*
%{_bindir}/spamassassin
%{_sbindir}/*
%{_fillupdir}/sysconfig.spamd
%{_fillupdir}/sysconfig.spampd
%{_unitdir}/spamd.service
%{_unitdir}/spampd.service
%{_unitdir}/sa-update.service
%{_unitdir}/sa-update.timer
%ghost %{_sharedstatedir}/%{name}

%files spamc
%defattr(-,root,root)
%license LICENSE
%{_bindir}/spamc
%doc %{_mandir}/man1/spamc.1*

%files -n perl-Mail-SpamAssassin -f %{name}.files
%defattr(-,root,root)
%license LICENSE
%doc CREDITS Changes MANIFEST* NOTICE PACKAGING README
%doc TRADEMARK UPGRADE USAGE sample-nonspam.txt sample-spam.txt
%doc ldap sql
%dir %{_sysconfdir}/mail
%config(noreplace) %{_sysconfdir}/mail/spamassassin
%exclude %{_sysconfdir}/mail/spamassassin/iXhash2.cf
%exclude %{perl_vendorarch}
%dir %{_datadir}/spamassassin
%{_datadir}/spamassassin/*

%files -n perl-Mail-SpamAssassin-Plugin-iXhash2
%license %{IXHASH}/LICENSE
%doc %{IXHASH}/CHANGELOG %{IXHASH}/README
%config(noreplace) %{_sysconfdir}/mail/spamassassin/iXhash2.cf
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/iXhash2.pm

%changelog
