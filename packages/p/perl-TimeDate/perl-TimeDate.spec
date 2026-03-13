#
# spec file for package perl-TimeDate
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.340.0
Release:        0
# 2.34 -> normalize -> 2.340.0
%define cpan_version 2.34
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Date and time formatting subroutines
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Date::Format) = %{version}
Provides:       perl(Date::Format::Generic) = %{version}
Provides:       perl(Date::Language) = %{version}
Provides:       perl(Date::Language::Afar) = %{version}
Provides:       perl(Date::Language::Amharic) = %{version}
Provides:       perl(Date::Language::Arabic) = %{version}
Provides:       perl(Date::Language::Austrian) = %{version}
Provides:       perl(Date::Language::Brazilian) = %{version}
Provides:       perl(Date::Language::Bulgarian) = %{version}
Provides:       perl(Date::Language::Chinese) = %{version}
Provides:       perl(Date::Language::Chinese_GB) = %{version}
Provides:       perl(Date::Language::Czech) = %{version}
Provides:       perl(Date::Language::Danish) = %{version}
Provides:       perl(Date::Language::Dutch) = %{version}
Provides:       perl(Date::Language::English) = %{version}
Provides:       perl(Date::Language::Finnish) = %{version}
Provides:       perl(Date::Language::French) = %{version}
Provides:       perl(Date::Language::Gedeo) = %{version}
Provides:       perl(Date::Language::German) = %{version}
Provides:       perl(Date::Language::Greek) = %{version}
Provides:       perl(Date::Language::Hungarian) = %{version}
Provides:       perl(Date::Language::Icelandic) = %{version}
Provides:       perl(Date::Language::Italian) = %{version}
Provides:       perl(Date::Language::Norwegian) = %{version}
Provides:       perl(Date::Language::Occitan) = %{version}
Provides:       perl(Date::Language::Oromo) = %{version}
Provides:       perl(Date::Language::Romanian) = %{version}
Provides:       perl(Date::Language::Russian) = %{version}
Provides:       perl(Date::Language::Russian_cp1251) = %{version}
Provides:       perl(Date::Language::Russian_koi8r) = %{version}
Provides:       perl(Date::Language::Sidama) = %{version}
Provides:       perl(Date::Language::Somali) = %{version}
Provides:       perl(Date::Language::Spanish) = %{version}
Provides:       perl(Date::Language::Swedish) = %{version}
Provides:       perl(Date::Language::Tigrinya) = %{version}
Provides:       perl(Date::Language::TigrinyaEritrean) = %{version}
Provides:       perl(Date::Language::TigrinyaEthiopian) = %{version}
Provides:       perl(Date::Language::Turkish) = %{version}
Provides:       perl(Date::Parse) = %{version}
Provides:       perl(Time::Zone) = %{version}
Provides:       perl(TimeDate) = %{version}
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
%doc Changes README
%license LICENSE

%changelog
