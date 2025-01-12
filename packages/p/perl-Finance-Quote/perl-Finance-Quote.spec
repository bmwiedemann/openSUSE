#
# spec file for package perl-Finance-Quote
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


%define cpan_name Finance-Quote
Name:           perl-Finance-Quote
Version:        1.640.0
Release:        0
# 1.64 -> normalize -> 1.640.0
%define cpan_version 1.64
#Upstream: GPL-1.0-or-later
License:        GPL-2.0-or-later
Summary:        Get stock and mutual fund quotes from various exchanges
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPSCHUCK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Range)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(HTTP::CookieJar::LWP) >= 0.014
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent) >= 6.48
BuildRequires:  perl(Module::CPANTS::Analyse)
BuildRequires:  perl(Module::Load) >= 0.36
BuildRequires:  perl(Mozilla::CA)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Spreadsheet::XLSX)
BuildRequires:  perl(String::Util)
BuildRequires:  perl(Test2) >= 1.302167
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::Escape) >= 3.31
BuildRequires:  perl(Web::Scraper)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(feature)
Requires:       perl(Compress::Zlib)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::TableExtract)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(HTML::TreeBuilder::XPath)
Requires:       perl(HTTP::CookieJar::LWP) >= 0.014
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(HTTP::Status)
Requires:       perl(IO::String)
Requires:       perl(IO::Uncompress::Unzip)
Requires:       perl(JSON)
Requires:       perl(LWP::Protocol::http)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::UserAgent) >= 6.48
Requires:       perl(Module::Load) >= 0.36
Requires:       perl(Mozilla::CA)
Requires:       perl(Readonly)
Requires:       perl(Spreadsheet::XLSX)
Requires:       perl(String::Util)
Requires:       perl(Test2) >= 1.302167
Requires:       perl(Text::Template)
Requires:       perl(Time::Piece)
Requires:       perl(Time::Seconds)
Requires:       perl(Try::Tiny)
Requires:       perl(URI::Escape) >= 3.31
Requires:       perl(Web::Scraper)
Requires:       perl(XML::LibXML)
Provides:       perl(Finance::Quote) = %{version}
Provides:       perl(Finance::Quote::AEX) = %{version}
Provides:       perl(Finance::Quote::ASEGR) = %{version}
Provides:       perl(Finance::Quote::ASX) = %{version}
Provides:       perl(Finance::Quote::AlphaVantage) = %{version}
Provides:       perl(Finance::Quote::BSEIndia) = %{version}
Provides:       perl(Finance::Quote::BVB) = %{version}
Provides:       perl(Finance::Quote::Bloomberg) = %{version}
Provides:       perl(Finance::Quote::BorsaItaliana) = %{version}
Provides:       perl(Finance::Quote::Bourso) = %{version}
Provides:       perl(Finance::Quote::CSE) = %{version}
Provides:       perl(Finance::Quote::Comdirect) = %{version}
Provides:       perl(Finance::Quote::Consorsbank) = %{version}
Provides:       perl(Finance::Quote::Currencies) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::AlphaVantage) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::CurrencyFreaks) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::ECB) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::FinanceAPI) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::Fixer) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::OpenExchange) = %{version}
Provides:       perl(Finance::Quote::CurrencyRates::YahooJSON) = %{version}
Provides:       perl(Finance::Quote::DWS) = %{version}
Provides:       perl(Finance::Quote::Deka) = %{version}
Provides:       perl(Finance::Quote::FTfunds) = %{version}
Provides:       perl(Finance::Quote::FinanceAPI) = %{version}
Provides:       perl(Finance::Quote::Finanzpartner) = %{version}
Provides:       perl(Finance::Quote::Fondsweb) = %{version}
Provides:       perl(Finance::Quote::Fool) = %{version}
Provides:       perl(Finance::Quote::GoldMoney) = %{version}
Provides:       perl(Finance::Quote::GoogleWeb) = %{version}
Provides:       perl(Finance::Quote::HU) = %{version}
Provides:       perl(Finance::Quote::IndiaMutual) = %{version}
Provides:       perl(Finance::Quote::MarketWatch) = %{version}
Provides:       perl(Finance::Quote::MorningstarAU) = %{version}
Provides:       perl(Finance::Quote::MorningstarCH) = %{version}
Provides:       perl(Finance::Quote::MorningstarJP) = %{version}
Provides:       perl(Finance::Quote::MorningstarUK) = %{version}
Provides:       perl(Finance::Quote::NSEIndia) = %{version}
Provides:       perl(Finance::Quote::NZX) = %{version}
Provides:       perl(Finance::Quote::OnVista) = %{version}
Provides:       perl(Finance::Quote::Oslobors) = %{version}
Provides:       perl(Finance::Quote::SEB) = %{version}
Provides:       perl(Finance::Quote::SIX) = %{version}
Provides:       perl(Finance::Quote::Sinvestor) = %{version}
Provides:       perl(Finance::Quote::StockData) = %{version}
Provides:       perl(Finance::Quote::Stooq) = %{version}
Provides:       perl(Finance::Quote::TMX) = %{version}
Provides:       perl(Finance::Quote::TSP) = %{version}
Provides:       perl(Finance::Quote::TesouroDireto) = %{version}
Provides:       perl(Finance::Quote::Tiaacref) = %{version}
Provides:       perl(Finance::Quote::Tradegate) = %{version}
Provides:       perl(Finance::Quote::TreasuryDirect) = %{version}
Provides:       perl(Finance::Quote::Troweprice) = %{version}
Provides:       perl(Finance::Quote::TwelveData) = %{version}
Provides:       perl(Finance::Quote::Union) = %{version}
Provides:       perl(Finance::Quote::UserAgent) = %{version}
Provides:       perl(Finance::Quote::XETRA) = %{version}
Provides:       perl(Finance::Quote::YahooJSON) = %{version}
Provides:       perl(Finance::Quote::YahooWeb) = %{version}
Provides:       perl(Finance::Quote::ZA) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module gets stock quotes from various internet sources all over the
world. Quotes are obtained by constructing a quoter object and using the
fetch method to gather data, which is returned as a two-dimensional hash
(or a reference to such a hash, if called in a scalar context). For
example:

    $q = Finance::Quote->new;
    %info = $q->fetch("australia", "CML");
    print "The price of CML is ".$info{"CML", "price"};

The first part of the hash (eg, "CML") is referred to as the stock. The
second part (in this case, "price") is referred to as the label.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README
%license LICENSE

%changelog
