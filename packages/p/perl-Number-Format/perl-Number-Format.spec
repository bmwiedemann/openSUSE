#
# spec file for package perl-Number-Format
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


%define cpan_name Number-Format
Name:           perl-Number-Format
Version:        1.790.0
Release:        0
# 1.79 -> normalize -> 1.790.0
%define cpan_version 1.79
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for formatting numbers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Test::More) >= 0.96
Provides:       perl(Number::Format) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
These functions provide an easy means of formatting numbers in a manner
suitable for displaying to the user.

There are two ways to use this package. One is to declare an object of type
Number::Format, which you can think of as a formatting engine. The various
functions defined here are provided as object methods. The constructor
'new()' can be used to set the parameters of the formatting engine. Valid
parameters are:

  THOUSANDS_SEP     - character inserted between groups of 3 digits
  DECIMAL_POINT     - character separating integer and fractional parts
  MON_THOUSANDS_SEP - like THOUSANDS_SEP, but used for format_price
  MON_DECIMAL_POINT - like DECIMAL_POINT, but used for format_price
  INT_CURR_SYMBOL   - character(s) denoting currency (see format_price())
  DECIMAL_DIGITS    - number of digits to the right of dec point (def 2)
  DECIMAL_FILL      - boolean; whether to add zeroes to fill out decimal
  NEG_FORMAT        - format to display negative numbers (def ``-x'')
  KILO_SUFFIX       - suffix to add when format_bytes formats kilobytes (trad)
  MEGA_SUFFIX       -    "    "  "    "        "         "    megabytes (trad)
  GIGA_SUFFIX       -    "    "  "    "        "         "    gigabytes (trad)
  TERA_SUFFIX       -    "    "  "    "        "         "    terabytes (trad)
  KIBI_SUFFIX       - suffix to add when format_bytes formats kibibytes (iec)
  MEBI_SUFFIX       -    "    "  "    "        "         "    mebibytes (iec)
  GIBI_SUFFIX       -    "    "  "    "        "         "    gibibytes (iec)
  TEBI_SUFFIX       -    "    "  "    "        "         "    tebibytes (iec)

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README TODO
%license LICENSE

%changelog
