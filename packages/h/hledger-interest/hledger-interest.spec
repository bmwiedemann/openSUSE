#
# spec file for package hledger-interest
#
# Copyright (c) 2026 SUSE LLC
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


%bcond_with tests
Name:           hledger-interest
Version:        2.0.0
Release:        0
Summary:        Computes interest for a given account
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Decimal-devel
BuildRequires:  ghc-Decimal-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hledger-lib-devel
BuildRequires:  ghc-hledger-lib-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-typed-process-devel
BuildRequires:  ghc-typed-process-prof
%endif

%description
Hledger-interest is a small command-line utility based on Simon Michael's
hledger library. Its purpose is to compute interest for a given ledger account.
Using command line flags, the program can be configured to use various schemes
for day-counting, such as act/act, 30/360, 30E/360, and 30E/360isda.
It supports constant rates, annual interest with a fixed rate, and schedules of
annual rates supplied on the command line or read from a text file.

As an example, consider the loan in the regression fixture
'tests/fixtures/boundaries.journal':

> 2023-01-31 Loan > Assets:Bank EUR 10000.00 > Liabilities:Loan > > 2023-02-28
Payment > Assets:Bank EUR -100.00 > Liabilities:Loan > > 2023-03-31 Payment >
Assets:Bank EUR -100.00 > Liabilities:Loan > > 2023-07-01 Payment on rate
change > Assets:Bank EUR -100.00 > Liabilities:Loan > > 2023-07-01 Second
payment on same day > Assets:Bank EUR -50.00 > Liabilities:Loan > > 2024-01-15
Payment after year end > Assets:Bank EUR -100.00 > Liabilities:Loan > >
2024-02-29 Leap day payment > Assets:Bank EUR -100.00 > Liabilities:Loan > >
2024-03-31 Payment > Assets:Bank EUR -100.00 > Liabilities:Loan > > 2024-04-01
Unrelated transaction > Assets:Bank EUR -10.00 > Expenses:Other

With 5% annual interest and actual-day counting, crediting interest to the loan
account compounds it. The following command prints only the generated interest
postings; its output is checked by the 'annual-act' golden test:

> $ hledger-interest --file=tests/fixtures/boundaries.journal
--source=Expenses:Interest --target=Liabilities:Loan --act --annual=0.05
--quiet Liabilities:Loan > 2023-02-28 5% interest for EUR -10000.00 over 28
days > Liabilities:Loan EUR -38.36 > Expenses:Interest EUR 38.36 > > 2023-03-31
5% interest for EUR -9938.36 over 31 days > Liabilities:Loan EUR -42.20 >
Expenses:Interest EUR 42.20 > > 2023-07-01 5% interest for EUR -9880.56 over 92
days > Liabilities:Loan EUR -124.52 > Expenses:Interest EUR 124.52 > >
2023-12-31 5% interest for EUR -9855.08 over 183 days > Liabilities:Loan EUR
-247.05 > Expenses:Interest EUR 247.05 > > 2024-01-15 5% interest for EUR
-10102.13 over 15 days > Liabilities:Loan EUR -20.70 > Expenses:Interest EUR
20.70 > > 2024-02-29 5% interest for EUR -10022.84 over 45 days >
Liabilities:Loan EUR -61.62 > Expenses:Interest EUR 61.62 > > 2024-03-31 5%
interest for EUR -9984.45 over 31 days > Liabilities:Loan EUR -42.28 >
Expenses:Interest EUR 42.28

Running the utility with '--help' gives a brief overview over the available
options:

> Usage: hledger-interest [OPTION...] ACCOUNT > Default: post at transactions,
rate-period ends, and year ends. > -h --help print this message and exit > -V
--version show version number and exit > -v --verbose print matching input
transactions and generated interest (default) > -q --quiet print generated
interest only > --today alias for --until=today > --until=DATE compute interest
through DATE (YYYY-MM-DD or today); > exclude transactions with later effective
dates > --post-on-transactions post only at transactions (and at
--until/--today); > skip rate-period and automatic year-end postings; >
overrides --post-on-rate-changes > --post-on-rate-changes post at transactions
and rate-period ends; > skip automatic year-end postings; >
--post-on-transactions takes precedence; > --until/--today also post on the
final day > -f FILE --file=FILE input ledger file (pass '-' for stdin) >
default: $LEDGER_FILE or ~/.hledger.journal > -s ACCOUNT --source=ACCOUNT
interest source account > -t ACCOUNT --target=ACCOUNT interest target account >
-I --ignore-assertions ignore any failing balance assertions > --act use
'act/act' day counting convention > (Actual/Actual ISDA; see README) > --30-360
use '30/360' day counting convention > --30E-360 use '30E/360' day counting
convention > --30E-360isda use '30E/360isda' day counting convention >
--constant=RATE fixed annual interest rate > --annual=RATE alias for --constant
> --schedule=SCHEDULE annualized rates and their effective dates; > rates are
fractions: 0.05 means 5% per year > syntax: '[(Date1,Rate1),(Date2,Rate2),...]'
> --schedule-file=PATH read a schedule from a text file; > one date and rate
per line, starting in column 1; > rates: 0.05 or 5%; hledger comments allowed >
--annual-schedule=SCHEDULE alias for --schedule.

%prep
%autosetup

%build
%ghc_bin_build

%install
%ghc_bin_install

%check
%cabal_test

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
