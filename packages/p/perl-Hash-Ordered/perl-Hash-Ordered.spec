#
# spec file for package perl-Hash-Ordered
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


%define cpan_name Hash-Ordered
Name:           perl-Hash-Ordered
Version:        0.014
Release:        0
License:        Apache-2.0
Summary:        Fast, pure-Perl ordered hash class
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
This module implements an ordered hash, meaning that it associates keys
with values like a Perl hash, but keeps the keys in a consistent order.
Because it is implemented as an object and manipulated with method calls,
it is much slower than a Perl hash. This is the cost of keeping order.

However, compared to other *ordered* hash implementations, Hash::Ordered is
optimized for getting and setting individual elements and is generally
faster at most other tasks as well. For specific details, see
Hash::Ordered::Benchmarks.

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
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
