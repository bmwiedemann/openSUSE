#
# spec file for package perl-Date-Holidays-CZ
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Date-Holidays-CZ
Version:        0.17
Release:        0
%define cpan_name Date-Holidays-CZ
Summary:        Determine Czech holidays
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Date-Holidays-CZ/
Source0:        Date-Holidays-CZ-0.17.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Calc) >= 5
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Software::License)
Requires:       perl(Date::Calc) >= 5
%{perl_requires}

%description
This module exports a single function named *holidays()* which returns a
list of Czech holidays in a given year.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes example LICENSE README.rst

%changelog
