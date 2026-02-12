#
# spec file for package perl-Inline-C
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Inline-C
Name:           perl-Inline-C
Version:        0.820.0
Release:        0
# 0.82 -> normalize -> 0.820.0
%define cpan_version 0.82
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        C Language Support for Inline
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Inline) >= 0.86
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pegex) >= 0.660
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(autodie)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(ExtUtils::MakeMaker) >= 7.00
Requires:       perl(Inline) >= 0.86
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Pegex) >= 0.660
Provides:       perl(Inline::C) = %{version}
Provides:       perl(Inline::C::Parser)
Provides:       perl(Inline::C::Parser::Pegex)
Provides:       perl(Inline::C::Parser::Pegex::AST)
Provides:       perl(Inline::C::Parser::Pegex::Grammar)
Provides:       perl(Inline::C::Parser::RecDescent)
Provides:       perl(Inline::C::Parser::RegExp)
%undefine       __perllib_provides
%{perl_requires}

%description
'Inline::C' is a module that allows you to write Perl subroutines in C.
Since version 0.30 the Inline module supports multiple programming
languages and each language has its own support module. This document
describes how to use Inline with the C programming language. It also goes a
bit into Perl C internals.

If you want to start working with programming examples right away, check
out Inline::C::Cookbook. For more information on Inline in general, see
Inline.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTING example README
%license LICENSE

%changelog
