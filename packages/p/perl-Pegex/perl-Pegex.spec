#
# spec file for package perl-Pegex
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


%define cpan_name Pegex
Name:           perl-Pegex
Version:        0.750.0
Release:        0
# 0.75 -> normalize -> 0.750.0
%define cpan_version 0.75
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Acmeist PEG Parser Framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(XXX) >= 0.350
BuildRequires:  perl(YAML::PP) >= 0.019
Requires:       perl(File::ShareDir::Install)
Requires:       perl(JSON::PP)
Requires:       perl(XXX) >= 0.350
Requires:       perl(YAML::PP) >= 0.019
Provides:       perl(Pegex) = %{version}
Provides:       perl(Pegex::Base)
Provides:       perl(Pegex::Bootstrap)
Provides:       perl(Pegex::Compiler)
Provides:       perl(Pegex::Constant)
Provides:       perl(Pegex::Grammar)
Provides:       perl(Pegex::Grammar::Atoms)
Provides:       perl(Pegex::Input)
Provides:       perl(Pegex::Module)
Provides:       perl(Pegex::Optimizer)
Provides:       perl(Pegex::Parser)
Provides:       perl(Pegex::Parser::Indent)
Provides:       perl(Pegex::Pegex::AST)
Provides:       perl(Pegex::Pegex::Grammar)
Provides:       perl(Pegex::Receiver)
Provides:       perl(Pegex::Regex)
Provides:       perl(Pegex::Tree)
Provides:       perl(Pegex::Tree::Wrap)
%undefine       __perllib_provides
%{perl_requires}

%description
Pegex is an Acmeist parser framework. It allows you to easily create
parsers that will work equivalently in lots of programming languages! The
inspiration for Pegex comes from the parsing engine upon which the
postmodern programming language *Perl 6* is based on. Pegex brings this
beauty to the other _just_modern languages that have a normal regular
expression engine available.

Pegex gets it name by combining Parsing Expression Grammars (PEG), with
Regular Expressions (Regex). That's actually what Pegex does.

PEG is the cool new way to elegantly specify recursive descent grammars.
The Perl 6 language is defined in terms of a self modifying PEG language
called *Perl 6 Rules*. Regexes are familiar to programmers of most modern
programming languages. Pegex defines a simple PEG syntax, where all the
terminals are regexes. This means that Pegex can be quite fast and
powerful.

Pegex attempts to be the simplest way to define new (or old) Domain
Specific Languages (DSLs) that need to be used in several programming
languages and environments. Things like JSON, YAML, Markdown etc. It also
great for writing parsers/compilers that only need to work in one language.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING example README
%license LICENSE

%changelog
