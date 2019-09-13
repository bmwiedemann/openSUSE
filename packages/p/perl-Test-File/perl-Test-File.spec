#
# spec file for package perl-Test-File
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-File
Version:        1.443
Release:        0
%define cpan_name Test-File
Summary:        Test File Attributes
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-File/
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Builder) >= 1.001006
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
BuildRequires:  perl(Test::More) >= 0.95
BuildRequires:  perl(Test::utf8)
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
send me a patch. :) IF you want to pretend to be Windows on a non-Windows
machine (for instance, to test 'skip()'), you can set the
'PRETEND_TO_BE_WINDOWS' environment variable.

The optional NAME parameter for every function allows you to specify a name
for the test. If not supplied, a reasonable default will be generated.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes examples
%license LICENSE

%changelog
