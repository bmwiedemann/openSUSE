#
# spec file for package perl-Data-OptList
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


%define cpan_name Data-OptList
Name:           perl-Data-OptList
Version:        0.113
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse and validate simple name/value option pairs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Sub::Install) >= 0.921
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Params::Util)
Requires:       perl(Sub::Install) >= 0.921
%{perl_requires}

%description
Hashes are great for storing named data, but if you want more than one
entry for a name, you have to use a list of pairs. Even then, this is
really boring to write:

  $values = [
    foo => undef,
    bar => undef,
    baz => undef,
    xyz => { ... },
  ];

Just look at all those undefs! Don't worry, we can get rid of those:

  $values = [
    map { $_ => undef } qw(foo bar baz),
    xyz => { ... },
  ];

Aaaauuugh! We've saved a little typing, but now it requires thought to
read, and thinking is even worse than typing... and it's got a bug! It
looked right, didn't it? Well, the 'xyz => { ... }' gets consumed by the
map, and we don't get the data we wanted.

With Data::OptList, you can do this instead:

  $values = Data::OptList::mkopt([
    qw(foo bar baz),
    xyz => { ... },
  ]);

This works by assuming that any defined scalar is a name and any reference
following a name is its value.

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
%doc Changes README
%license LICENSE

%changelog
