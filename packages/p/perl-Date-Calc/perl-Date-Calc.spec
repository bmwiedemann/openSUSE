#
# spec file for package perl-Date-Calc
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Date-Calc
Version:        6.4
Release:        0
%define cpan_name Date-Calc
Summary:        Gregorian calendar date calculations
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Date-Calc/
Source0:        http://www.cpan.org/authors/id/S/ST/STBEY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         fix2038.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Bit::Vector) >= 7.4
BuildRequires:  perl(Carp::Clan) >= 6.04
Requires:       perl(Bit::Vector) >= 7.4
Requires:       perl(Carp::Clan) >= 6.04
Recommends:     perl(Date::Calc::XS) >= 6.4
%{perl_requires}

%description
* *

  'use Date::Calc qw( Days_in_Year Days_in_Month ... );'

* *

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES.txt CREDITS.txt README.txt

%changelog
