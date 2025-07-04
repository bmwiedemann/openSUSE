#
# spec file for package perl-Test-Spec
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Test-Spec
Name:           perl-Test-Spec
Version:        0.540.0
Release:        0
# 0.54 -> normalize -> 0.540.0
%define cpan_version 0.54
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Write tests in a declarative specification style
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKZHAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::GlobalPhase)
BuildRequires:  perl(Package::Stash) >= 0.230
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(Test::Deep) >= 0.103
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Tie::IxHash)
Requires:       perl(Devel::GlobalPhase)
Requires:       perl(Package::Stash) >= 0.230
Requires:       perl(TAP::Parser)
Requires:       perl(Test::Deep) >= 0.103
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::Trap)
Requires:       perl(Tie::IxHash)
Provides:       perl(Test::Spec) = %{version}
Provides:       perl(Test::Spec::Context)
Provides:       perl(Test::Spec::Example)
Provides:       perl(Test::Spec::ExportProxy)
Provides:       perl(Test::Spec::Mocks)
Provides:       perl(Test::Spec::Mocks::Expectation)
Provides:       perl(Test::Spec::Mocks::MockObject)
Provides:       perl(Test::Spec::Mocks::Stub)
Provides:       perl(Test::Spec::SharedHash)
Provides:       perl(Test::Spec::TodoExample)
%undefine       __perllib_provides
%{perl_requires}

%description
This is a declarative specification-style testing system for
behavior-driven development (BDD) in Perl. The tests (a.k.a. examples) are
named with strings instead of subroutine names, so your fingers will suffer
less fatigue from underscore-itis, with the side benefit that the test
reports are more legible.

This module is inspired by and borrows heavily from at
http://rspec.info/documentation, a BDD tool for the Ruby programming
language.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
