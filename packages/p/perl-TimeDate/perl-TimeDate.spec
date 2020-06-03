#
# spec file for package perl-TimeDate
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-TimeDate
Version:        2.33
Release:        0
%define cpan_name TimeDate
Summary:        TimeDate Perl module
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc ChangeLog README

%changelog
