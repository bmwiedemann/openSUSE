#
# spec file for package perl-PPI
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


%define cpan_name PPI
Name:           perl-PPI
Version:        1.277.0
Release:        0
%define cpan_version 1.277
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse, Analyze and Manipulate Perl (without perl)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector) >= 1.22
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::SubCalls) >= 1.07
BuildRequires:  perl(parent)
Requires:       perl(Clone) >= 0.30
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Storable) >= 2.17
Requires:       perl(Task::Weaken)
Provides:       perl(PPI) = 1.277.0
Provides:       perl(PPI::Cache) = 1.277.0
Provides:       perl(PPI::Document) = 1.277.0
Provides:       perl(PPI::Document::File) = 1.277.0
Provides:       perl(PPI::Document::Fragment) = 1.277.0
Provides:       perl(PPI::Document::Normalized) = 1.277.0
Provides:       perl(PPI::Dumper) = 1.277.0
Provides:       perl(PPI::Element) = 1.277.0
Provides:       perl(PPI::Exception) = 1.277.0
Provides:       perl(PPI::Exception::ParserRejection) = 1.277.0
Provides:       perl(PPI::Find) = 1.277.0
Provides:       perl(PPI::Lexer) = 1.277.0
Provides:       perl(PPI::Node) = 1.277.0
Provides:       perl(PPI::Normal) = 1.277.0
Provides:       perl(PPI::Normal::Standard) = 1.277.0
Provides:       perl(PPI::Singletons) = 1.277.0
Provides:       perl(PPI::Statement) = 1.277.0
Provides:       perl(PPI::Statement::Break) = 1.277.0
Provides:       perl(PPI::Statement::Compound) = 1.277.0
Provides:       perl(PPI::Statement::Data) = 1.277.0
Provides:       perl(PPI::Statement::End) = 1.277.0
Provides:       perl(PPI::Statement::Expression) = 1.277.0
Provides:       perl(PPI::Statement::Given) = 1.277.0
Provides:       perl(PPI::Statement::Include) = 1.277.0
Provides:       perl(PPI::Statement::Include::Perl6) = 1.277.0
Provides:       perl(PPI::Statement::Null) = 1.277.0
Provides:       perl(PPI::Statement::Package) = 1.277.0
Provides:       perl(PPI::Statement::Scheduled) = 1.277.0
Provides:       perl(PPI::Statement::Sub) = 1.277.0
Provides:       perl(PPI::Statement::Unknown) = 1.277.0
Provides:       perl(PPI::Statement::UnmatchedBrace) = 1.277.0
Provides:       perl(PPI::Statement::Variable) = 1.277.0
Provides:       perl(PPI::Statement::When) = 1.277.0
Provides:       perl(PPI::Structure) = 1.277.0
Provides:       perl(PPI::Structure::Block) = 1.277.0
Provides:       perl(PPI::Structure::Condition) = 1.277.0
Provides:       perl(PPI::Structure::Constructor) = 1.277.0
Provides:       perl(PPI::Structure::For) = 1.277.0
Provides:       perl(PPI::Structure::Given) = 1.277.0
Provides:       perl(PPI::Structure::List) = 1.277.0
Provides:       perl(PPI::Structure::Subscript) = 1.277.0
Provides:       perl(PPI::Structure::Unknown) = 1.277.0
Provides:       perl(PPI::Structure::When) = 1.277.0
Provides:       perl(PPI::Token) = 1.277.0
Provides:       perl(PPI::Token::ArrayIndex) = 1.277.0
Provides:       perl(PPI::Token::Attribute) = 1.277.0
Provides:       perl(PPI::Token::BOM) = 1.277.0
Provides:       perl(PPI::Token::Cast) = 1.277.0
Provides:       perl(PPI::Token::Comment) = 1.277.0
Provides:       perl(PPI::Token::DashedWord) = 1.277.0
Provides:       perl(PPI::Token::Data) = 1.277.0
Provides:       perl(PPI::Token::End) = 1.277.0
Provides:       perl(PPI::Token::HereDoc) = 1.277.0
Provides:       perl(PPI::Token::Label) = 1.277.0
Provides:       perl(PPI::Token::Magic) = 1.277.0
Provides:       perl(PPI::Token::Number) = 1.277.0
Provides:       perl(PPI::Token::Number::Binary) = 1.277.0
Provides:       perl(PPI::Token::Number::Exp) = 1.277.0
Provides:       perl(PPI::Token::Number::Float) = 1.277.0
Provides:       perl(PPI::Token::Number::Hex) = 1.277.0
Provides:       perl(PPI::Token::Number::Octal) = 1.277.0
Provides:       perl(PPI::Token::Number::Version) = 1.277.0
Provides:       perl(PPI::Token::Operator) = 1.277.0
Provides:       perl(PPI::Token::Pod) = 1.277.0
Provides:       perl(PPI::Token::Prototype) = 1.277.0
Provides:       perl(PPI::Token::Quote) = 1.277.0
Provides:       perl(PPI::Token::Quote::Double) = 1.277.0
Provides:       perl(PPI::Token::Quote::Interpolate) = 1.277.0
Provides:       perl(PPI::Token::Quote::Literal) = 1.277.0
Provides:       perl(PPI::Token::Quote::Single) = 1.277.0
Provides:       perl(PPI::Token::QuoteLike) = 1.277.0
Provides:       perl(PPI::Token::QuoteLike::Backtick) = 1.277.0
Provides:       perl(PPI::Token::QuoteLike::Command) = 1.277.0
Provides:       perl(PPI::Token::QuoteLike::Readline) = 1.277.0
Provides:       perl(PPI::Token::QuoteLike::Regexp) = 1.277.0
Provides:       perl(PPI::Token::QuoteLike::Words) = 1.277.0
Provides:       perl(PPI::Token::Regexp) = 1.277.0
Provides:       perl(PPI::Token::Regexp::Match) = 1.277.0
Provides:       perl(PPI::Token::Regexp::Substitute) = 1.277.0
Provides:       perl(PPI::Token::Regexp::Transliterate) = 1.277.0
Provides:       perl(PPI::Token::Separator) = 1.277.0
Provides:       perl(PPI::Token::Structure) = 1.277.0
Provides:       perl(PPI::Token::Symbol) = 1.277.0
Provides:       perl(PPI::Token::Unknown) = 1.277.0
Provides:       perl(PPI::Token::Whitespace) = 1.277.0
Provides:       perl(PPI::Token::Word) = 1.277.0
Provides:       perl(PPI::Tokenizer) = 1.277.0
Provides:       perl(PPI::Transform) = 1.277.0
Provides:       perl(PPI::Transform::UpdateCopyright) = 1.277.0
Provides:       perl(PPI::Util) = 1.277.0
Provides:       perl(PPI::XSAccessor) = 1.277.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
Parse, Analyze and Manipulate Perl (without perl)

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes dev_notes.txt README
%license LICENSE

%changelog
