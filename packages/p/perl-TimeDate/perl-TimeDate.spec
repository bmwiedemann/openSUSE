#
# spec file for package perl-TimeDate
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name TimeDate
Name:           perl-TimeDate
Version:        2.330.0
Release:        0
# 2.33 -> normalize -> 2.330.0
%define cpan_version 2.33
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        TimeDate Perl module
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Date::Format) = 2.240.0
Provides:       perl(Date::Format::Generic)
Provides:       perl(Date::Language) = 1.100.0
Provides:       perl(Date::Language::Afar) = 0.990.0
Provides:       perl(Date::Language::Amharic) = 1.0.0
Provides:       perl(Date::Language::Austrian) = 1.10.0
Provides:       perl(Date::Language::Brazilian) = 1.10.0
Provides:       perl(Date::Language::Bulgarian) = 1.10.0
Provides:       perl(Date::Language::Chinese) = 1.0.0
Provides:       perl(Date::Language::Chinese_GB) = 1.10.0
Provides:       perl(Date::Language::Czech) = 1.10.0
Provides:       perl(Date::Language::Danish) = 1.10.0
Provides:       perl(Date::Language::Dutch) = 1.20.0
Provides:       perl(Date::Language::English) = 1.10.0
Provides:       perl(Date::Language::Finnish) = 1.10.0
Provides:       perl(Date::Language::French) = 1.40.0
Provides:       perl(Date::Language::Gedeo) = 0.990.0
Provides:       perl(Date::Language::German) = 1.20.0
Provides:       perl(Date::Language::Greek) = 1.0.0
Provides:       perl(Date::Language::Hungarian) = 1.10.0
Provides:       perl(Date::Language::Icelandic) = 1.10.0
Provides:       perl(Date::Language::Italian) = 1.10.0
Provides:       perl(Date::Language::Norwegian) = 1.10.0
Provides:       perl(Date::Language::Occitan) = 1.40.0
Provides:       perl(Date::Language::Oromo) = 0.990.0
Provides:       perl(Date::Language::Romanian) = 1.10.0
Provides:       perl(Date::Language::Russian) = 1.10.0
Provides:       perl(Date::Language::Russian_cp1251) = 1.10.0
Provides:       perl(Date::Language::Russian_koi8r) = 1.10.0
Provides:       perl(Date::Language::Sidama) = 0.990.0
Provides:       perl(Date::Language::Somali) = 0.990.0
Provides:       perl(Date::Language::Spanish) = 1.0.0
Provides:       perl(Date::Language::Swedish) = 1.10.0
Provides:       perl(Date::Language::Tigrinya) = 1.0.0
Provides:       perl(Date::Language::TigrinyaEritrean) = 1.0.0
Provides:       perl(Date::Language::TigrinyaEthiopian) = 1.0.0
Provides:       perl(Date::Language::Turkish) = 1.0.0
Provides:       perl(Date::Parse) = %{version}
Provides:       perl(Time::Zone) = 2.240.0
Provides:       perl(TimeDate) = 1.210.0
%undefine       __perllib_provides
%{perl_requires}

%description
Date::Parse provides two routines for parsing date strings into time values.

str2time(DATE [, ZONE])

   str2time parses DATE and returns a unix time value, or undef upon failure.
    ZONE, if given, specifies the timezone to assume when parsing if the date
    string does not specify a timezome.

strptime(DATE [, ZONE])

   strptime takes the same arguments as str2time but returns an array of values
    ($ss,$mm,$hh,$day,$month,$year,$zone). Elements are only defined if they
    could be extracted from the date string. The $zone element is the timezone
    offset in seconds from GMT. An empty array is returned upon failure.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc ChangeLog README

%changelog
