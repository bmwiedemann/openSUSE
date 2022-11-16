#
# spec file for package perl-Mail-SpamAssassin-Plugin-dqs
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


Name:           perl-Mail-SpamAssassin-Plugin-dqs
Version:        1.2.2
Release:        0
Summary:        SpamAssassin plugin for Spamhaus Data Query Service (DQS)
License:        Apache-2.0
Group:          Development/Libraries/Perl
URL:            https://github.com/spamhaus/spamassassin-dqs/tags
Source0:        https://github.com/spamhaus/spamassassin-dqs/archive/refs/tags/v%{version}.tar.gz
Source1:        README-SUSE.md
BuildRequires:  spamassassin >= 3.4.1
Requires:       spamassassin >= 3.4.1
%{perl_requires}

%description
The Spamhaus Data Query Service (DQS) plugin for SpamAssassin enhances
existing functions by checking HELO/EHLO, From, Reply-To, Envelope-From
and Return-Path against Spamhaus DBL/ZRD blacklists. It also scans the
e-mail body for e-mail addresses and performs blacklist lookups against
the domains or its authoritative nameservers. Further checks cover the
reverse DNS matches in DBL/ZRD blacklists or the SBL/CSS lookups for IP
addresses or IP addresses of authoritative nameservers of domains being
part of the e-mail body.

While the DQS usage is free under the same terms like when using public
mirrors (which are shipped in SpamAssassin as default configuration), a
registration procedure for a free DQS key is mandatory nevertheless.

%prep
%setup -q -n spamassassin-dqs-%{version}
sed -e 's|<config_directory>|%{perl_vendorlib}/Mail/SpamAssassin/Plugin|' -i sh.pre
cp %{SOURCE1} .

%build

%install
install -D -p -m 0644 SH.pm %{buildroot}%{perl_vendorlib}/Mail/SpamAssassin/Plugin/SH.pm
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 hbltest.sh %{buildroot}%{_bindir}/hbltest.sh
for FILE in sh.pre sh.cf sh_hbl.cf sh_hbl_scores.cf sh_scores.cf ; do
	install -D -p -m 0644 $FILE %{buildroot}%{_sysconfdir}/mail/spamassassin/$FILE
done

%check
# setup config files
mkdir tests
cp %{_sysconfdir}/mail/spamassassin/* tests/
for FILE in sh.pre sh.cf sh_scores.cf ; do
	cp $FILE tests/
done
sed -e 's|%{perl_vendorlib}|%{buildroot}%{perl_vendorlib}|' -i tests/sh.pre
# execute the tests
spamassassin --siteconfigpath=tests --lint > tests/lint.log 2>&1 || { cat tests/lint.log; exit 1; }
grep -q -i fail tests/lint.log && { cat tests/lint.log; exit 1; } || :

%files
%doc Changelog.md NOTICE README.md README-SUSE.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh.cf
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh.pre
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh_hbl.cf
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh_hbl_scores.cf
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh_scores.cf
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/SH.pm
%{_bindir}/hbltest.sh

%changelog
