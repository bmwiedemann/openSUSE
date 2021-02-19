#
# spec file for package perl-Test-Class
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Test-Class
Name:           perl-Test-Class
Version:        0.52
Release:        0
Summary:        Easily create test classes in an xUnit/JUnit style
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MRO::Compat) >= 0.11
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::Builder) >= 0.78
BuildRequires:  perl(Test::Exception) >= 0.250000
BuildRequires:  perl(Test::More) >= 0.78
BuildRequires:  perl(Test::Simple) >= 0.78
BuildRequires:  perl(Try::Tiny)
Requires:       perl(MRO::Compat) >= 0.11
Requires:       perl(Module::Runtime)
Requires:       perl(Test::Builder) >= 0.78
Requires:       perl(Test::Simple) >= 0.78
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
Test::Class provides a simple way of creating classes and objects to test
your code in an xUnit style.

Built using Test::Builder, it was designed to work with other Test::Builder
based modules (Test::More, Test::Differences, Test::Exception, etc.).

_Note:_ This module will make more sense, if you are already familiar with
the "standard" mechanisms for testing perl code. Those unfamiliar with
Test::Harness, Test::Simple, Test::More and friends should go take a look
at them now. Test::Tutorial is a good starting point.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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

%changelog
