#
# spec file for package perl-DateTime
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


%define cpan_name DateTime
Name:           perl-DateTime
Version:        1.59
Release:        0
License:        Artistic-2.0
Summary:        Date and time object for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(DateTime::Locale) >= 1.060000
BuildRequires:  perl(DateTime::TimeZone) >= 2.44
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Params::ValidationCompiler) >= 0.26
BuildRequires:  perl(Specio) >= 0.18
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Specio::Subs)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(parent)
Requires:       perl(DateTime::Locale) >= 1.060000
Requires:       perl(DateTime::TimeZone) >= 2.44
Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(Params::ValidationCompiler) >= 0.26
Requires:       perl(Specio) >= 0.18
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Exporter)
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::Library::Numeric)
Requires:       perl(Specio::Library::String)
Requires:       perl(Specio::Subs)
Requires:       perl(Try::Tiny)
Requires:       perl(namespace::autoclean) >= 0.19
Requires:       perl(parent)
%{perl_requires}

%description
DateTime is a class for the representation of date/time combinations, and
is part of the Perl DateTime project.

It represents the Gregorian calendar, extended backwards in time before its
creation (in 1582). This is sometimes known as the "proleptic Gregorian
calendar". In this calendar, the first day of the calendar (the epoch), is
the first day of year 1, which corresponds to the date which was
(incorrectly) believed to be the birth of Jesus Christ.

The calendar represented does have a year 0, and in that way differs from
how dates are often written using "BCE/CE" or "BC/AD".

For infinite datetimes, please see the DateTime::Infinite module.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS leaptab.txt precious.toml README.md TODO
%license LICENSE

%changelog
