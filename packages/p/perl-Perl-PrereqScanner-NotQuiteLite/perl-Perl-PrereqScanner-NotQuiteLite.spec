#
# spec file for package perl-Perl-PrereqScanner-NotQuiteLite
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


%define cpan_name Perl-PrereqScanner-NotQuiteLite
Name:           perl-Perl-PrereqScanner-NotQuiteLite
Version:        0.9917
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tool to scan your Perl code for its prerequisites
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.150010
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.140000
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.09
BuildRequires:  perl(Module::CPANfile) >= 1.1004
BuildRequires:  perl(Module::CoreList) >= 3.11
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Parse::Distname)
BuildRequires:  perl(Regexp::Trie)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::UseAllModules) >= 0.17
BuildRequires:  perl(parent)
Requires:       perl(CPAN::Meta::Prereqs) >= 2.150010
Requires:       perl(CPAN::Meta::Requirements) >= 2.140000
Requires:       perl(Data::Dump)
Requires:       perl(Module::CPANfile) >= 1.1004
Requires:       perl(Module::CoreList) >= 3.11
Requires:       perl(Module::Find)
Requires:       perl(Parse::Distname)
Requires:       perl(Regexp::Trie)
Requires:       perl(parent)
%{perl_requires}

%description
Perl::PrereqScanner::NotQuiteLite is yet another prerequisites scanner. It
passes almost all the scanning tests for Perl::PrereqScanner and
Module::ExtractUse (ie. except for a few dubious ones), and runs slightly
faster than PPI-based Perl::PrereqScanner. However, it doesn't run as fast
as Perl::PrereqScanner::Lite (which uses an XS lexer).

Perl::PrereqScanner::NotQuiteLite also recognizes 'eval'. Prerequisites in
'eval' are not considered as requirements, but you can collect them as
suggestions.

Conditional requirements or requirements loaded in a block are treated as
recommends. Noed modules are stored separately (since 0.94). You may or may
not need to merge them into requires.

Perl::PrereqScanner::NotQuiteLite can also recognize some of the new
language features such as 'say', subroutine signatures, and postfix
dereferences, to improve the minimum perl requirement (since 0.9905).

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
