#
# spec file for package perl-Time-Local
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Time-Local
Version:        1.28
Release:        0
%define cpan_name Time-Local
Summary:        Efficiently compute time from local and GMT time
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc appveyor.yml Changes CONTRIBUTING.md README.md
%license LICENSE

%changelog
