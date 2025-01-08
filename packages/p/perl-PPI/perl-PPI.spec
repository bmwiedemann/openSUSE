#
# spec file for package perl-PPI
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


%define cpan_name PPI
Name:           perl-PPI
Version:        1.281.0
Release:        0
# 1.281 -> normalize -> 1.281.0
%define cpan_version 1.281
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
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::SubCalls) >= 1.07
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(parent)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(Clone) >= 0.30
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Safe::Isa)
Requires:       perl(Storable) >= 2.17
Requires:       perl(Task::Weaken)
Requires:       perl(YAML::PP)
Requires:       perl(version) >= 0.77
Provides:       perl(PPI) = %{version}
Provides:       perl(PPI::Cache) = %{version}
Provides:       perl(PPI::Document) = %{version}
Provides:       perl(PPI::Document::File) = %{version}
Provides:       perl(PPI::Document::Fragment) = %{version}
Provides:       perl(PPI::Document::Normalized) = %{version}
Provides:       perl(PPI::Dumper) = %{version}
Provides:       perl(PPI::Element) = %{version}
Provides:       perl(PPI::Exception) = %{version}
Provides:       perl(PPI::Exception::ParserRejection) = %{version}
Provides:       perl(PPI::Find) = %{version}
Provides:       perl(PPI::Lexer) = %{version}
Provides:       perl(PPI::Node) = %{version}
Provides:       perl(PPI::Normal) = %{version}
Provides:       perl(PPI::Normal::Standard) = %{version}
Provides:       perl(PPI::Singletons) = %{version}
Provides:       perl(PPI::Statement) = %{version}
Provides:       perl(PPI::Statement::Break) = %{version}
Provides:       perl(PPI::Statement::Compound) = %{version}
Provides:       perl(PPI::Statement::Data) = %{version}
Provides:       perl(PPI::Statement::End) = %{version}
Provides:       perl(PPI::Statement::Expression) = %{version}
Provides:       perl(PPI::Statement::Given) = %{version}
Provides:       perl(PPI::Statement::Include) = %{version}
Provides:       perl(PPI::Statement::Include::Perl6) = %{version}
Provides:       perl(PPI::Statement::Null) = %{version}
Provides:       perl(PPI::Statement::Package) = %{version}
Provides:       perl(PPI::Statement::Scheduled) = %{version}
Provides:       perl(PPI::Statement::Sub) = %{version}
Provides:       perl(PPI::Statement::Unknown) = %{version}
Provides:       perl(PPI::Statement::UnmatchedBrace) = %{version}
Provides:       perl(PPI::Statement::Variable) = %{version}
Provides:       perl(PPI::Statement::When) = %{version}
Provides:       perl(PPI::Structure) = %{version}
Provides:       perl(PPI::Structure::Block) = %{version}
Provides:       perl(PPI::Structure::Condition) = %{version}
Provides:       perl(PPI::Structure::Constructor) = %{version}
Provides:       perl(PPI::Structure::For) = %{version}
Provides:       perl(PPI::Structure::Given) = %{version}
Provides:       perl(PPI::Structure::List) = %{version}
Provides:       perl(PPI::Structure::Signature) = %{version}
Provides:       perl(PPI::Structure::Subscript) = %{version}
Provides:       perl(PPI::Structure::Unknown) = %{version}
Provides:       perl(PPI::Structure::When) = %{version}
Provides:       perl(PPI::Token) = %{version}
Provides:       perl(PPI::Token::ArrayIndex) = %{version}
Provides:       perl(PPI::Token::Attribute) = %{version}
Provides:       perl(PPI::Token::BOM) = %{version}
Provides:       perl(PPI::Token::Cast) = %{version}
Provides:       perl(PPI::Token::Comment) = %{version}
Provides:       perl(PPI::Token::DashedWord) = %{version}
Provides:       perl(PPI::Token::Data) = %{version}
Provides:       perl(PPI::Token::End) = %{version}
Provides:       perl(PPI::Token::HereDoc) = %{version}
Provides:       perl(PPI::Token::Label) = %{version}
Provides:       perl(PPI::Token::Magic) = %{version}
Provides:       perl(PPI::Token::Number) = %{version}
Provides:       perl(PPI::Token::Number::Binary) = %{version}
Provides:       perl(PPI::Token::Number::Exp) = %{version}
Provides:       perl(PPI::Token::Number::Float) = %{version}
Provides:       perl(PPI::Token::Number::Hex) = %{version}
Provides:       perl(PPI::Token::Number::Octal) = %{version}
Provides:       perl(PPI::Token::Number::Version) = %{version}
Provides:       perl(PPI::Token::Operator) = %{version}
Provides:       perl(PPI::Token::Pod) = %{version}
Provides:       perl(PPI::Token::Prototype) = %{version}
Provides:       perl(PPI::Token::Quote) = %{version}
Provides:       perl(PPI::Token::Quote::Double) = %{version}
Provides:       perl(PPI::Token::Quote::Interpolate) = %{version}
Provides:       perl(PPI::Token::Quote::Literal) = %{version}
Provides:       perl(PPI::Token::Quote::Single) = %{version}
Provides:       perl(PPI::Token::QuoteLike) = %{version}
Provides:       perl(PPI::Token::QuoteLike::Backtick) = %{version}
Provides:       perl(PPI::Token::QuoteLike::Command) = %{version}
Provides:       perl(PPI::Token::QuoteLike::Readline) = %{version}
Provides:       perl(PPI::Token::QuoteLike::Regexp) = %{version}
Provides:       perl(PPI::Token::QuoteLike::Words) = %{version}
Provides:       perl(PPI::Token::Regexp) = %{version}
Provides:       perl(PPI::Token::Regexp::Match) = %{version}
Provides:       perl(PPI::Token::Regexp::Substitute) = %{version}
Provides:       perl(PPI::Token::Regexp::Transliterate) = %{version}
Provides:       perl(PPI::Token::Separator) = %{version}
Provides:       perl(PPI::Token::Structure) = %{version}
Provides:       perl(PPI::Token::Symbol) = %{version}
Provides:       perl(PPI::Token::Unknown) = %{version}
Provides:       perl(PPI::Token::Whitespace) = %{version}
Provides:       perl(PPI::Token::Word) = %{version}
Provides:       perl(PPI::Tokenizer) = %{version}
Provides:       perl(PPI::Transform) = %{version}
Provides:       perl(PPI::Transform::UpdateCopyright) = %{version}
Provides:       perl(PPI::Util) = %{version}
Provides:       perl(PPI::XSAccessor) = %{version}
%undefine       __perllib_provides
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
