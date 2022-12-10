#
# spec file for package perl-DBIx-Class-Schema-Loader
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name DBIx-Class-Schema-Loader
Name:           perl-DBIx-Class-Schema-Loader
Version:        0.07051
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Create a DBIx::Class::Schema based on a database
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Accessor::Grouped) >= 0.10008
BuildRequires:  perl(Class::C3::Componentised) >= 1.0008
BuildRequires:  perl(Class::Inspector) >= 1.27
BuildRequires:  perl(Class::Unload) >= 0.07
BuildRequires:  perl(DBD::SQLite) >= 1.29
BuildRequires:  perl(DBIx::Class) >= 0.08127
BuildRequires:  perl(Data::Dump) >= 1.06
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(File::Path) >= 2.070000
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(Lingua::EN::Inflect::Number) >= 1.1
BuildRequires:  perl(Lingua::EN::Inflect::Phrase) >= 0.15
BuildRequires:  perl(Lingua::EN::Tagger) >= 0.23
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(MRO::Compat) >= 0.09
BuildRequires:  perl(Scope::Guard) >= 0.20
BuildRequires:  perl(String::CamelCase) >= 0.04
BuildRequires:  perl(String::ToIdentifier::EN) >= 0.05
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::Deep) >= 0.107
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn) >= 0.21
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(curry) >= 1.000000
BuildRequires:  perl(namespace::clean) >= 0.23
Requires:       perl(Carp::Clan)
Requires:       perl(Class::Accessor::Grouped) >= 0.10008
Requires:       perl(Class::C3::Componentised) >= 1.0008
Requires:       perl(Class::Inspector) >= 1.27
Requires:       perl(Class::Unload) >= 0.07
Requires:       perl(DBIx::Class) >= 0.08127
Requires:       perl(Data::Dump) >= 1.06
Requires:       perl(Exporter) >= 5.63
Requires:       perl(Hash::Merge) >= 0.12
Requires:       perl(Lingua::EN::Inflect::Number) >= 1.1
Requires:       perl(Lingua::EN::Inflect::Phrase) >= 0.15
Requires:       perl(Lingua::EN::Tagger) >= 0.23
Requires:       perl(List::Util) >= 1.33
Requires:       perl(MRO::Compat) >= 0.09
Requires:       perl(Scope::Guard) >= 0.20
Requires:       perl(String::CamelCase) >= 0.04
Requires:       perl(String::ToIdentifier::EN) >= 0.05
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(Try::Tiny)
Requires:       perl(curry) >= 1.000000
Requires:       perl(namespace::clean) >= 0.23
%{perl_requires}

%description
DBIx::Class::Schema::Loader automates the definition of a
DBIx::Class::Schema by scanning database table definitions and setting up
the columns, primary keys, unique constraints and relationships.

See dbicdump for the 'dbicdump' utility.

DBIx::Class::Schema::Loader currently supports only the DBI storage type.
It has explicit support for DBD::Pg, DBD::mysql, DBD::DB2, DBD::Firebird,
DBD::InterBase, DBD::Informix, DBD::SQLAnywhere, DBD::SQLite, DBD::Sybase
(for Sybase ASE and MSSSQL), DBD::ODBC (for MSSQL, MSAccess, Firebird and
SQL Anywhere) DBD::ADO (for MSSQL and MSAccess) and DBD::Oracle. Other DBI
drivers may function to a greater or lesser degree with this loader,
depending on how much of the DBI spec they implement, and how standard
their implementation is.

Patches to make other DBDs work correctly welcome.

See DBIx::Class::Schema::Loader::DBI::Writing for notes on writing your own
vendor-specific subclass for an unsupported DBD driver.

This module requires DBIx::Class 0.08127 or later, and obsoletes the older
DBIx::Class::Loader.

See DBIx::Class::Schema::Loader::Base for available options.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
