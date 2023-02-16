#
# spec file for package perl-Carp-Assert-More
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


%define cpan_name Carp-Assert-More
Name:           perl-Carp-Assert-More
Version:        2.2.0
Release:        0
License:        Artistic-2.0
Summary:        Convenience assertions for common situations
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
Requires:       perl(Test::Exception)
%{perl_requires}

%description
Carp::Assert::More is a convenient set of assertions to make the habit of
writing assertions even easier.

Everything in here is effectively syntactic sugar. There's no technical
difference between calling one of these functions:

    assert_datetime( $foo );
    assert_isa( $foo, 'DateTime' );

that are provided by Carp::Assert::More and calling these assertions from
Carp::Assert

    assert( defined $foo );
    assert( ref($foo) eq 'DateTime' );

My intent here is to make common assertions easy so that we as programmers
have no excuse to not use them.

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
%doc Changes README.md

%changelog
