#
# spec file for package perl-List-UtilsBy
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name List-UtilsBy
Name:           perl-List-UtilsBy
Version:        0.12
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Higher-order list utility functions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
This module provides a number of list utility functions, all of which take
an initial code block to control their behaviour. They are variations on
similar core perl or 'List::Util' functions of similar names, but which use
the block to control their behaviour. For example, the core Perl function
'sort' takes a list of values and returns them, sorted into order by their
string value. The sort_by function sorts them according to the string value
returned by the extra function, when given each value.

   my @names_sorted = sort @names;

   my @people_sorted = sort_by { $_->name } @people;

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
