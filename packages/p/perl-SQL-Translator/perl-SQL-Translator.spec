#
# spec file for package perl-SQL-Translator
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


%define cpan_name SQL-Translator
Name:           perl-SQL-Translator
Version:        1.660.0
Release:        0
# 1.66 -> normalize -> 1.660.0
%define cpan_version 1.66
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND GPL-2.0-only
Summary:        SQL DDL transformations and more
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(DBI) >= 1.54
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.54
BuildRequires:  perl(File::ShareDir) >= 1.0
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Package::Variant) >= 1.001001
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception) >= 0.42
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny) >= 0.04
BuildRequires:  perl(XML::Writer) >= 0.500
BuildRequires:  perl(YAML) >= 0.66
Requires:       perl(Carp::Clan)
Requires:       perl(DBI) >= 1.54
Requires:       perl(Digest::SHA)
Requires:       perl(File::ShareDir) >= 1.0
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moo) >= 1.000003
Requires:       perl(Package::Variant) >= 1.001001
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Sub::Quote)
Requires:       perl(Try::Tiny) >= 0.04
Provides:       perl(Parse::RecDescent::SQL::Translator::Parser::DB2::Grammar)
Provides:       perl(SQL::Translator) = %{version}
Provides:       perl(SQL::Translator::Diff)
Provides:       perl(SQL::Translator::Filter::DefaultExtra) = %{version}
Provides:       perl(SQL::Translator::Filter::Globals) = %{version}
Provides:       perl(SQL::Translator::Filter::Names) = %{version}
Provides:       perl(SQL::Translator::Generator::DDL::MySQL)
Provides:       perl(SQL::Translator::Generator::DDL::PostgreSQL)
Provides:       perl(SQL::Translator::Generator::DDL::SQLServer)
Provides:       perl(SQL::Translator::Generator::DDL::SQLite)
Provides:       perl(SQL::Translator::Generator::Role::DDL)
Provides:       perl(SQL::Translator::Generator::Role::Quote)
Provides:       perl(SQL::Translator::Parser) = %{version}
Provides:       perl(SQL::Translator::Parser::Access) = %{version}
Provides:       perl(SQL::Translator::Parser::DB2)
Provides:       perl(SQL::Translator::Parser::DB2::Grammar)
Provides:       perl(SQL::Translator::Parser::DBI) = %{version}
Provides:       perl(SQL::Translator::Parser::DBI::DB2)
Provides:       perl(SQL::Translator::Parser::DBI::MySQL) = %{version}
Provides:       perl(SQL::Translator::Parser::DBI::Oracle) = %{version}
Provides:       perl(SQL::Translator::Parser::DBI::PostgreSQL) = %{version}
Provides:       perl(SQL::Translator::Parser::DBI::SQLServer) = %{version}
Provides:       perl(SQL::Translator::Parser::DBI::SQLite) = %{version}
Provides:       perl(SQL::Translator::Parser::DBI::Sybase) = %{version}
Provides:       perl(SQL::Translator::Parser::Excel) = %{version}
Provides:       perl(SQL::Translator::Parser::JSON) = %{version}
Provides:       perl(SQL::Translator::Parser::MySQL) = %{version}
Provides:       perl(SQL::Translator::Parser::Oracle) = %{version}
Provides:       perl(SQL::Translator::Parser::PostgreSQL) = %{version}
Provides:       perl(SQL::Translator::Parser::SQLServer) = %{version}
Provides:       perl(SQL::Translator::Parser::SQLite) = %{version}
Provides:       perl(SQL::Translator::Parser::Storable) = %{version}
Provides:       perl(SQL::Translator::Parser::Sybase) = %{version}
Provides:       perl(SQL::Translator::Parser::XML) = %{version}
Provides:       perl(SQL::Translator::Parser::XML::SQLFairy) = %{version}
Provides:       perl(SQL::Translator::Parser::YAML) = %{version}
Provides:       perl(SQL::Translator::Parser::xSV) = %{version}
Provides:       perl(SQL::Translator::Producer) = %{version}
Provides:       perl(SQL::Translator::Producer::ClassDBI) = %{version}
Provides:       perl(SQL::Translator::Producer::DB2) = %{version}
Provides:       perl(SQL::Translator::Producer::DiaUml) = %{version}
Provides:       perl(SQL::Translator::Producer::Diagram) = %{version}
Provides:       perl(SQL::Translator::Producer::Dumper) = %{version}
Provides:       perl(SQL::Translator::Producer::GraphViz) = %{version}
Provides:       perl(SQL::Translator::Producer::HTML) = %{version}
Provides:       perl(SQL::Translator::Producer::JSON) = %{version}
Provides:       perl(SQL::Translator::Producer::Latex) = %{version}
Provides:       perl(SQL::Translator::Producer::MySQL) = %{version}
Provides:       perl(SQL::Translator::Producer::Oracle) = %{version}
Provides:       perl(SQL::Translator::Producer::POD) = %{version}
Provides:       perl(SQL::Translator::Producer::PostgreSQL) = %{version}
Provides:       perl(SQL::Translator::Producer::SQLServer) = %{version}
Provides:       perl(SQL::Translator::Producer::SQLite) = %{version}
Provides:       perl(SQL::Translator::Producer::Storable) = %{version}
Provides:       perl(SQL::Translator::Producer::Sybase) = %{version}
Provides:       perl(SQL::Translator::Producer::TT::Base) = %{version}
Provides:       perl(SQL::Translator::Producer::TT::Table) = %{version}
Provides:       perl(SQL::Translator::Producer::TTSchema) = %{version}
Provides:       perl(SQL::Translator::Producer::XML) = %{version}
Provides:       perl(SQL::Translator::Producer::XML::SQLFairy) = %{version}
Provides:       perl(SQL::Translator::Producer::YAML) = %{version}
Provides:       perl(SQL::Translator::Role::BuildArgs)
Provides:       perl(SQL::Translator::Role::Debug)
Provides:       perl(SQL::Translator::Role::Error)
Provides:       perl(SQL::Translator::Role::ListAttr)
Provides:       perl(SQL::Translator::Schema) = %{version}
Provides:       perl(SQL::Translator::Schema::Constants) = %{version}
Provides:       perl(SQL::Translator::Schema::Constraint) = %{version}
Provides:       perl(SQL::Translator::Schema::Field) = %{version}
Provides:       perl(SQL::Translator::Schema::Index) = %{version}
Provides:       perl(SQL::Translator::Schema::IndexField)
Provides:       perl(SQL::Translator::Schema::Object) = %{version}
Provides:       perl(SQL::Translator::Schema::Procedure) = %{version}
Provides:       perl(SQL::Translator::Schema::Role::Compare)
Provides:       perl(SQL::Translator::Schema::Role::Extra)
Provides:       perl(SQL::Translator::Schema::Table) = %{version}
Provides:       perl(SQL::Translator::Schema::Trigger) = %{version}
Provides:       perl(SQL::Translator::Schema::View) = %{version}
Provides:       perl(SQL::Translator::Types)
Provides:       perl(SQL::Translator::Utils) = %{version}
Provides:       perl(SQL::Translator::Utils::Error)
Provides:       perl(Test::SQL::Translator) = %{version}
%undefine       __perllib_provides
Recommends:     perl(GD)
Recommends:     perl(Graph::Directed)
Recommends:     perl(GraphViz)
Recommends:     perl(Spreadsheet::ParseExcel) >= 0.41
Recommends:     perl(Template) >= 2.20
Recommends:     perl(Text::RecordParser) >= 0.02
Recommends:     perl(XML::LibXML) >= 1.69
%{perl_requires}

%description
This documentation covers the API for SQL::Translator. For a more general
discussion of how to use the modules and scripts, please see
SQL::Translator::Manual.

SQL::Translator is a group of Perl modules that converts vendor-specific
SQL table definitions into other formats, such as other vendor-specific
SQL, ER diagrams, documentation (POD and HTML), XML, and Class::DBI
classes. The main focus of SQL::Translator is SQL, but parsers exist for
other structured data formats, including Excel spreadsheets and arbitrarily
delimited text files. Through the separation of the code into parsers and
producers with an object model in between, it's possible to combine any
parser with any producer, to plug in custom parsers or producers, or to
manipulate the parsed data via the built-in object model. Presently only
the definition parts of SQL are handled (CREATE, ALTER), not the
manipulation of data (INSERT, UPDATE, DELETE).

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc AUTHORS Changes README
%license LICENSE

%changelog
