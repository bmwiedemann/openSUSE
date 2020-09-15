#
# spec file for package perl-SQL-Translator
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-SQL-Translator
Version:        1.62
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
%define cpan_name SQL-Translator
Summary:        Manipulate structured data definitions (SQL and more)
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND GPL-2.0-only
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(DBI) >= 1.54
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::ShareDir) >= 1.0
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Package::Variant) >= 1.001001
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny) >= 0.04
BuildRequires:  perl(XML::Writer) >= 0.500
BuildRequires:  perl(YAML) >= 0.66
Requires:       perl(Carp::Clan)
Requires:       perl(DBI) >= 1.54
Requires:       perl(Digest::SHA)
Requires:       perl(File::ShareDir) >= 1.0
Requires:       perl(Moo) >= 1.000003
Requires:       perl(Package::Variant) >= 1.001001
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Sub::Quote)
Requires:       perl(Try::Tiny) >= 0.04
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS Changes README
%license LICENSE

%changelog
