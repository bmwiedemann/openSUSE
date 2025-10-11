#
# spec file for package perl-PPIx-Regexp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name PPIx-Regexp
Name:           perl-PPIx-Regexp
Version:        0.91.0
Release:        0
# 0.091 -> normalize -> 0.91.0
%define cpan_version 0.091
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse regular expressions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420
BuildRequires:  perl(PPI::Document) >= 1.238
BuildRequires:  perl(PPI::Dumper) >= 1.238
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(PPI::Document) >= 1.238
Requires:       perl(PPI::Dumper) >= 1.238
Requires:       perl(Task::Weaken)
Provides:       perl(PPIx::Regexp) = %{version}
Provides:       perl(PPIx::Regexp::Constant) = 0.85.40
Provides:       perl(PPIx::Regexp::Constant::Inf) = %{version}
Provides:       perl(PPIx::Regexp::Dumper) = %{version}
Provides:       perl(PPIx::Regexp::Element) = %{version}
Provides:       perl(PPIx::Regexp::Lexer) = %{version}
Provides:       perl(PPIx::Regexp::Node) = %{version}
Provides:       perl(PPIx::Regexp::Node::Range) = %{version}
Provides:       perl(PPIx::Regexp::Node::Unknown) = %{version}
Provides:       perl(PPIx::Regexp::Structure) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Assertion) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Atomic_Script_Run) = %{version}
Provides:       perl(PPIx::Regexp::Structure::BranchReset) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Capture) = %{version}
Provides:       perl(PPIx::Regexp::Structure::CharClass) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Code) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Main) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Modifier) = %{version}
Provides:       perl(PPIx::Regexp::Structure::NamedCapture) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Quantifier) = %{version}
Provides:       perl(PPIx::Regexp::Structure::RegexSet) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Regexp) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Replacement) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Script_Run) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Subexpression) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Switch) = %{version}
Provides:       perl(PPIx::Regexp::Structure::Unknown) = %{version}
Provides:       perl(PPIx::Regexp::Support) = %{version}
Provides:       perl(PPIx::Regexp::Token) = %{version}
Provides:       perl(PPIx::Regexp::Token::Assertion) = %{version}
Provides:       perl(PPIx::Regexp::Token::Backreference) = %{version}
Provides:       perl(PPIx::Regexp::Token::Backtrack) = %{version}
Provides:       perl(PPIx::Regexp::Token::CharClass) = %{version}
Provides:       perl(PPIx::Regexp::Token::CharClass::POSIX) = %{version}
Provides:       perl(PPIx::Regexp::Token::CharClass::POSIX::Unknown) = %{version}
Provides:       perl(PPIx::Regexp::Token::CharClass::Simple) = %{version}
Provides:       perl(PPIx::Regexp::Token::Code) = %{version}
Provides:       perl(PPIx::Regexp::Token::Comment) = %{version}
Provides:       perl(PPIx::Regexp::Token::Condition) = %{version}
Provides:       perl(PPIx::Regexp::Token::Control) = %{version}
Provides:       perl(PPIx::Regexp::Token::Delimiter) = %{version}
Provides:       perl(PPIx::Regexp::Token::Greediness) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Assertion) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Atomic_Script_Run) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::BranchReset) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Code) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Modifier) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::NamedCapture) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Script_Run) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Subexpression) = %{version}
Provides:       perl(PPIx::Regexp::Token::GroupType::Switch) = %{version}
Provides:       perl(PPIx::Regexp::Token::Interpolation) = %{version}
Provides:       perl(PPIx::Regexp::Token::Literal) = %{version}
Provides:       perl(PPIx::Regexp::Token::Modifier) = %{version}
Provides:       perl(PPIx::Regexp::Token::NoOp) = %{version}
Provides:       perl(PPIx::Regexp::Token::Operator) = %{version}
Provides:       perl(PPIx::Regexp::Token::Quantifier) = %{version}
Provides:       perl(PPIx::Regexp::Token::Recursion) = %{version}
Provides:       perl(PPIx::Regexp::Token::Reference) = %{version}
Provides:       perl(PPIx::Regexp::Token::Structure) = %{version}
Provides:       perl(PPIx::Regexp::Token::Unknown) = %{version}
Provides:       perl(PPIx::Regexp::Token::Unmatched) = %{version}
Provides:       perl(PPIx::Regexp::Token::Whitespace) = %{version}
Provides:       perl(PPIx::Regexp::Tokenizer) = %{version}
Provides:       perl(PPIx::Regexp::Util) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The purpose of the _PPIx-Regexp_ package is to parse regular expressions in
a manner similar to the way the PPI package parses Perl. This class forms
the root of the parse tree, playing a role similar to PPI::Document.

This package shares with PPI the property of being round-trip safe. That
is,

 my $expr = 's/ ( \d+ ) ( \D+ ) /$2$1/smxg';
 my $re = PPIx::Regexp->new( $expr );
 print $re->content() eq $expr ? "yes\n" : "no\n"

should print 'yes' for any valid regular expression.

Navigation is similar to that provided by PPI. That is to say, things like
'children', 'find_first', 'snext_sibling' and so on all work pretty much
the same way as in PPI.

The class hierarchy is also similar to PPI. Except for some utility classes
(the dumper, the lexer, and the tokenizer) all classes are descended from
PPIx::Regexp::Element, which provides basic navigation. Tokens are
descended from PPIx::Regexp::Token, which provides content. All containers
are descended from PPIx::Regexp::Node, which provides for children, and all
structure elements are descended from PPIx::Regexp::Structure, which
provides beginning and ending delimiters, and a type.

There are two features of PPI that this package does not provide -
mutability and operator overloading. There are no plans for serious
mutability, though something like PPI's 'prune' functionality might be
considered. Similarly there are no plans for operator overloading, which
appears to the author to represent a performance hit for little tangible
gain.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README SECURITY

%changelog
