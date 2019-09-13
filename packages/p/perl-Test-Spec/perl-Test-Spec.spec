#
# spec file for package perl-Test-Spec
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Spec
Version:        0.54
Release:        0
%define cpan_name Test-Spec
Summary:        Write tests in a declarative specification style
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Spec/
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKZHAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::GlobalPhase)
BuildRequires:  perl(Package::Stash) >= 0.23
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(Test::Deep) >= 0.103
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Tie::IxHash)
Requires:       perl(Devel::GlobalPhase)
Requires:       perl(Package::Stash) >= 0.23
Requires:       perl(TAP::Parser)
Requires:       perl(Test::Deep) >= 0.103
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::Trap)
Requires:       perl(Tie::IxHash)
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes README.md

%changelog
