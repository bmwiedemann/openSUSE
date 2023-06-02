#
# spec file for package perl-Number-Format
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.76
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for formatting numbers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
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
  KIBI_SUFFIX       - suffix to add when format_bytes formats kibibytes (iec)
  MEBI_SUFFIX       -    "    "  "    "        "         "    mebibytes (iec)
  GIBI_SUFFIX       -    "    "  "    "        "         "    gibibytes (iec)

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
%doc CHANGES README TODO

%changelog
