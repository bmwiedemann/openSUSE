#
# spec file for package perl-URI-db
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


%define cpan_name URI-db
Name:           perl-URI-db
Version:        0.230.0
Release:        0
# 0.23 -> normalize -> 0.230.0
%define cpan_version 0.23
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Database URIs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.30
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.40
BuildRequires:  perl(URI::Nested) >= 0.10
Requires:       perl(URI) >= 1.40
Requires:       perl(URI::Nested) >= 0.10
Provides:       perl(URI::cassandra) = %{version}
Provides:       perl(URI::clickhouse) = 0.200.0
Provides:       perl(URI::cockroach) = %{version}
Provides:       perl(URI::cockroachdb) = %{version}
Provides:       perl(URI::couch) = %{version}
Provides:       perl(URI::couchdb) = %{version}
Provides:       perl(URI::cubrid) = %{version}
Provides:       perl(URI::db) = %{version}
Provides:       perl(URI::db2) = %{version}
Provides:       perl(URI::derby) = %{version}
Provides:       perl(URI::exasol) = %{version}
Provides:       perl(URI::firebird) = %{version}
Provides:       perl(URI::hive) = %{version}
Provides:       perl(URI::impala) = %{version}
Provides:       perl(URI::informix) = %{version}
Provides:       perl(URI::ingres) = %{version}
Provides:       perl(URI::interbase) = %{version}
Provides:       perl(URI::ldapdb) = %{version}
Provides:       perl(URI::maria) = %{version}
Provides:       perl(URI::mariadb) = %{version}
Provides:       perl(URI::max) = %{version}
Provides:       perl(URI::maxdb) = %{version}
Provides:       perl(URI::monet) = %{version}
Provides:       perl(URI::monetdb) = %{version}
Provides:       perl(URI::mongo) = %{version}
Provides:       perl(URI::mongodb) = %{version}
Provides:       perl(URI::mssql) = %{version}
Provides:       perl(URI::mysql) = %{version}
Provides:       perl(URI::oracle) = %{version}
Provides:       perl(URI::pg) = %{version}
Provides:       perl(URI::pgsql) = %{version}
Provides:       perl(URI::pgxc) = %{version}
Provides:       perl(URI::postgres) = %{version}
Provides:       perl(URI::postgresql) = %{version}
Provides:       perl(URI::postgresxc) = %{version}
Provides:       perl(URI::redshift) = %{version}
Provides:       perl(URI::snowflake) = %{version}
Provides:       perl(URI::sqlite) = %{version}
Provides:       perl(URI::sqlite3) = %{version}
Provides:       perl(URI::sqlserver) = %{version}
Provides:       perl(URI::sybase) = %{version}
Provides:       perl(URI::teradata) = %{version}
Provides:       perl(URI::unify) = %{version}
Provides:       perl(URI::vertica) = %{version}
Provides:       perl(URI::yugabyte) = %{version}
Provides:       perl(URI::yugabytedb) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Database URIs

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.md

%changelog
