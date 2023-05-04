#
# spec file for package perl-Time-Local
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


%define cpan_name Time-Local
Name:           perl-Time-Local
Version:        1.35
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Efficiently compute time from local and GMT time
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
This module provides functions that are the inverse of built-in perl
functions 'localtime()' and 'gmtime()'. They accept a date as a six-element
array, and return the corresponding 'time(2)' value in seconds since the
system epoch (Midnight, January 1, 1970 GMT on Unix, for example). This
value can be positive or negative, though POSIX only requires support for
positive values, so dates before the system's epoch may not work on all
operating systems.

It is worth drawing particular attention to the expected ranges for the
values provided. The value for the day of the month is the actual day (i.e.
1..31), while the month is the number of months since January (0..11). This
is consistent with the values returned from 'localtime()' and 'gmtime()'.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
