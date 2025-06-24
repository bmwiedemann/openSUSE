#
# spec file for package perl-Perl-PrereqScanner
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


%define cpan_name Perl-PrereqScanner
Name:           perl-Perl-PrereqScanner
Version:        1.100.0
Release:        0
# 1.100 -> normalize -> 1.100.0
%define cpan_version 1.100
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tool to scan your Perl code for its prerequisites
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.124
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Path)
BuildRequires:  perl(Moo) >= 2.0
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(PPI) >= 1.215
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(String::RewritePrefix) >= 0.5
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(CPAN::Meta::Requirements) >= 2.124
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Path)
Requires:       perl(Moo) >= 2.0
Requires:       perl(Moo::Role)
Requires:       perl(PPI) >= 1.215
Requires:       perl(Params::Util)
Requires:       perl(String::RewritePrefix) >= 0.5
Requires:       perl(Types::Standard)
Requires:       perl(namespace::autoclean)
Provides:       perl(Perl::PrereqScanner) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner::Aliased) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner::Moose) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner::POE) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner::Perl5) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner::Superclass) = %{version}
Provides:       perl(Perl::PrereqScanner::Scanner::TestMore) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The scanner will extract loosely your distribution prerequisites from your
files.

The extraction may not be perfect but tries to do its best. It will
currently find the following prereqs:

  * plain lines beginning with 'use' or 'require' in your perl modules and
scripts, including minimum perl version

  * regular inheritance declared with the 'base' and 'parent' pragmata

  * Moose inheritance declared with the 'extends' keyword

  * Moose roles included with the 'with' keyword

  * OO namespace aliasing using the 'aliased' module

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
