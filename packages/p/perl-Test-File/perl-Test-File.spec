#
# spec file for package perl-Test-File
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


%define cpan_name Test-File
Name:           perl-Test-File
Version:        1.993
Release:        0
License:        Artistic-2.0
Summary:        Test file attributes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::Builder) >= 1.001006
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
BuildRequires:  perl(Test::More) >= 1
%{perl_requires}

%description
This modules provides a collection of test utilities for file attributes.

Some file attributes depend on the owner of the process testing the file in
the same way the file test operators do. For instance, root (or super-user
or Administrator) may always be able to read files no matter the
permissions.

Some attributes don't make sense outside of Unix, either, so some tests
automatically skip if they think they won't work on the platform. If you
have a way to make these functions work on Windows, for instance, please
send me a patch. :) If you want to pretend to be Windows on a non-Windows
machine (for instance, to test 'skip()'), you can set the
'PRETEND_TO_BE_WINDOWS' environment variable.

The optional NAME parameter for every function allows you to specify a name
for the test. If not supplied, a reasonable default will be generated.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CITATION.cff examples
%license LICENSE

%changelog
