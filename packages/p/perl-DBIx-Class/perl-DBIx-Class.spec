#
# spec file for package perl-DBIx-Class
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


%define cpan_name DBIx-Class
Name:           perl-DBIx-Class
Version:        0.082844
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extensible and flexible object <-> relational mapper
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Grouped) >= 0.10012
BuildRequires:  perl(Class::C3::Componentised) >= 1.0009
BuildRequires:  perl(Class::Inspector) >= 1.24
BuildRequires:  perl(Config::Any) >= 0.20
BuildRequires:  perl(Context::Preserve) >= 0.01
BuildRequires:  perl(DBD::SQLite) >= 1.29
BuildRequires:  perl(DBI) >= 1.57
BuildRequires:  perl(Data::Dumper::Concise) >= 2.020
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(MRO::Compat) >= 0.12
BuildRequires:  perl(Module::Find) >= 0.07
BuildRequires:  perl(Moo) >= 2.000
BuildRequires:  perl(Package::Stash) >= 0.28
BuildRequires:  perl(Path::Class) >= 0.18
BuildRequires:  perl(SQL::Abstract::Classic) >= 1.91
BuildRequires:  perl(Scope::Guard) >= 0.03
BuildRequires:  perl(Sub::Name) >= 0.04
BuildRequires:  perl(Test::Deep) >= 0.101
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn) >= 0.21
BuildRequires:  perl(Text::Balanced) >= 2.00
BuildRequires:  perl(Try::Tiny) >= 0.07
BuildRequires:  perl(namespace::clean) >= 0.24
Requires:       perl(Class::Accessor::Grouped) >= 0.10012
Requires:       perl(Class::C3::Componentised) >= 1.0009
Requires:       perl(Class::Inspector) >= 1.24
Requires:       perl(Config::Any) >= 0.20
Requires:       perl(Context::Preserve) >= 0.01
Requires:       perl(DBI) >= 1.57
Requires:       perl(Data::Dumper::Concise) >= 2.020
Requires:       perl(Devel::GlobalDestruction) >= 0.09
Requires:       perl(Hash::Merge) >= 0.12
Requires:       perl(MRO::Compat) >= 0.12
Requires:       perl(Module::Find) >= 0.07
Requires:       perl(Moo) >= 2.000
Requires:       perl(Path::Class) >= 0.18
Requires:       perl(SQL::Abstract::Classic) >= 1.91
Requires:       perl(Scope::Guard) >= 0.03
Requires:       perl(Sub::Name) >= 0.04
Requires:       perl(Text::Balanced) >= 2.00
Requires:       perl(Try::Tiny) >= 0.07
Requires:       perl(namespace::clean) >= 0.24
%{perl_requires}
# MANUAL BEGIN
# workaround a spurious test failure in "skipped" t/cdbi/mk_group_accessors.t
BuildRequires:  perl(Class::DBI)
# MANUAL END

%description
This is an SQL to OO mapper with an object API inspired by Class::DBI (with
a compatibility layer as a springboard for porting) and a resultset API
that allows abstract encapsulation of database operations. It aims to make
representing queries in your code as perl-ish as possible while still
providing access to as many of the capabilities of the database as
possible, including retrieving related records from multiple tables in a
single query, 'JOIN', 'LEFT JOIN', 'COUNT', 'DISTINCT', 'GROUP BY', 'ORDER
BY' and 'HAVING' support.

DBIx::Class can handle multi-column primary and foreign keys, complex
queries and database-level paging, and does its best to only query the
database in order to return something you've directly asked for. If a
resultset is used as an iterator it only fetches rows off the statement
handle as requested in order to minimise memory usage. It has
auto-increment support for SQLite, MySQL, PostgreSQL, Oracle, SQL Server
and DB2 and is known to be used in production on at least the first four,
and is fork- and thread-safe out of the box (although your DBD may not be).

This project is still under rapid development, so large new features may be
marked *experimental* - such APIs are still usable but may have edge bugs.
Failing test cases are _always_ welcome and point releases are put out
rapidly as bugs are found and fixed.

We do our best to maintain full backwards compatibility for published APIs,
since DBIx::Class is used in production in many organisations, and even
backwards incompatible changes to non-published APIs will be fixed if
they're reported and doing so doesn't cost the codebase anything.

The test suite is quite substantial, and several developer releases are
generally made to CPAN before the branch for the next release is merged
back to trunk for a major release.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc AUTHORS Changes examples README
%license LICENSE

%changelog
