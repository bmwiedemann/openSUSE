#
# spec file for package perl-Carp-Assert-More
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


Name:           perl-Carp-Assert-More
Version:        1.24
Release:        0
%define cpan_name Carp-Assert-More
Summary:        Convenience wrappers around Carp::Assert
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Carp::Assert)
Requires:       perl(Test::Exception)
%{perl_requires}

%description
Carp::Assert::More is a set of wrappers around the Carp::Assert functions
to make the habit of writing assertions even easier.

Everything in here is effectively syntactic sugar. There's no technical
reason to use

    assert_isa( $foo, 'HTML::Lint' );

instead of

    assert( defined $foo );
    assert( ref($foo) eq 'HTML::Lint' );

other than readability and simplicity of the code.

My intent here is to make common assertions easy so that we as programmers
have no excuse to not use them.

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
%doc Changes README.md

%changelog
