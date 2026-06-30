#
# spec file for package perl-Time-Moment
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Time-Moment
Name:           perl-Time-Moment
Version:        0.460.0
Release:        0
# 0.46 -> normalize -> 0.460.0
%define cpan_version 0.46
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Represents a date and time of day with an offset from UTC
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(Test::Fatal) >= 0.6
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Number::Delta) >= 1.60
BuildRequires:  perl(Test::Requires)
Provides:       perl(Time::Moment) = %{version}
Provides:       perl(Time::Moment::Adjusters) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'Time::Moment' is an immutable object that represents a specific date and
time of day, along with an offset from UTC, within the ISO 8601 calendar
system. Time is measured in nanoseconds since '0001-01-01T00Z'. Leap
seconds are not accounted for in 'Time::Moment'; each day is assumed to
have exactly '86,400,000,000,000' nanoseconds.

Time::Moment supports all epoch integers from '-62,135,596,800' to
'253,402,300,799', allowing for nanosecond precision for any instant within
the range '0001-01-01T00:00:00Z' to '9999-12-31T23:59:59Z'.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
