#
# spec file for package perl-Net-Whois-Raw
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Net-Whois-Raw
Name:           perl-Net-Whois-Raw
Version:        2.99040
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Get Whois information of domains and IP addresses
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NALOBIN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Net::IDN::Punycode)
BuildRequires:  perl(Regexp::IPv6)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(URI::URL)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(IO::Socket::IP)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::IDN::Punycode)
Requires:       perl(Regexp::IPv6)
Requires:       perl(URI::URL)
%{perl_requires}

%description
Net::Whois::Raw queries WHOIS servers about domains. The module supports
recursive WHOIS queries. Also queries via HTTP is supported for some TLDs.

Setting the variables $OMIT_MSG and $CHECK_FAIL will match the results
against a set of known patterns. The first flag will try to omit the
copyright message/disclaimer, the second will attempt to determine if the
search failed and return undef in such a case.

*IMPORTANT*: these checks merely use pattern matching; they will work on
several servers but certainly not on all of them.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes COPYRIGHT README
%license LICENSE

%changelog
