#
# spec file for package perl-Date-Calc
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


%define cpan_name Date-Calc
Name:           perl-Date-Calc
Version:        6.400.0
Release:        0
# 6.4 -> normalize -> 6.400.0
%define cpan_version 6.4
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Gregorian calendar date calculations
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STBEY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         fix2038.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Bit::Vector) >= 7.400
BuildRequires:  perl(Carp::Clan) >= 6.40.0
Requires:       perl(Bit::Vector) >= 7.400
Requires:       perl(Carp::Clan) >= 6.40.0
Provides:       perl(Date::Calc) = %{version}
Provides:       perl(Date::Calc::Object) = %{version}
Provides:       perl(Date::Calc::PP) = %{version}
Provides:       perl(Date::Calendar) = %{version}
Provides:       perl(Date::Calendar::Profiles) = %{version}
Provides:       perl(Date::Calendar::Year) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Date::Calc::XS) >= 6.400
%{perl_requires}

%description
  * 'use Date::Calc qw( Days_in_Year Days_in_Month ... );'

  * 'use Date::Calc qw(:all);'

You can either specify the functions you want to import explicitly by
enumerating them between the parentheses of the "'qw()'" operator, or you
can use the "':all'" tag instead to import *ALL* available functions.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc CHANGES.txt CREDITS.txt README.txt
%license license

%changelog
