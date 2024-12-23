#
# spec file for package perl-DBD-SQLite
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


%define cpan_name DBD-SQLite
Name:           perl-DBD-SQLite
Version:        1.760.0
Release:        0
# 1.76 -> normalize -> 1.760.0
%define cpan_version 1.76
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Self Contained SQLite RDBMS in a DBI Driver
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-OPENSUSE use system sqlite
Patch0:         perl-DBD-SQLite-use-external-sqlite3.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.48
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(DBI) >= 1.57
Provides:       perl(DBD::SQLite) = %{version}
Provides:       perl(DBD::SQLite::Constants)
Provides:       perl(DBD::SQLite::GetInfo)
Provides:       perl(DBD::SQLite::VirtualTable) = %{version}
Provides:       perl(DBD::SQLite::VirtualTable::Cursor)
Provides:       perl(DBD::SQLite::VirtualTable::FileContent)
Provides:       perl(DBD::SQLite::VirtualTable::FileContent::Cursor)
Provides:       perl(DBD::SQLite::VirtualTable::PerlData)
Provides:       perl(DBD::SQLite::VirtualTable::PerlData::Cursor)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
%if 0%{?sle_version} >= 140000 && 0%{?sle_version} <= 150400
%else
BuildRequires:  sqlite3-devel >= 3.35
Recommends:     sqlite3-devel
%endif
# MANUAL END

%description
SQLite is a public domain file-based relational database engine that you
can find at https://www.sqlite.org/.

*DBD::SQLite* is a Perl DBI driver for SQLite, that includes the entire
thing in the distribution. So in order to get a fast transaction capable
RDBMS working for your perl project you simply have to install this module,
and *nothing* else.

SQLite supports the following features:

* Implements a large subset of SQL92

See https://www.sqlite.org/lang.html for details.

* A complete DB in a single disk file

Everything for your database is stored in a single disk file, making it
easier to move things around than with DBD::CSV.

* Atomic commit and rollback

Yes, *DBD::SQLite* is small and light, but it supports full transactions!

* Extensible

User-defined aggregate or regular functions can be registered with the SQL
parser.

There's lots more to it, so please refer to the docs on the SQLite web
page, listed above, for SQL details. Also refer to DBI for details on how
to use DBI itself. The API works like every DBI module does. However,
currently many statement attributes are not implemented or are limited by
the typeless nature of the SQLite database.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
%if 0%{?sle_version} >= 140000 && 0%{?sle_version} <= 150400
patch -p1 --reverse <%{PATCH0}
%else
# system sqlite librairies will be used
rm sqlite*
perl -i -ne 'print $_ unless m{^sqlite}' MANIFEST
%endif
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
%if 0%{?sle_version} >= 140000 && 0%{?sle_version} <= 150400
%else
mkdir -p %{buildroot}%{perl_vendorarch}/auto/share/dist/%{cpan_name}
ln -fs %{_includedir}/sqlite3ext.h %{buildroot}%{perl_vendorarch}/auto/share/dist/%{cpan_name}/
ln -fs %{_includedir}/sqlite3.h %{buildroot}%{perl_vendorarch}/auto/share/dist/%{cpan_name}/
%endif
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes constants.inc dbdimp_tokenizer.inc dbdimp_virtual_table.inc README
%license LICENSE
# the links are ignored by perl_gen_filelist, so we need to add them manually again
%if 0%{?sle_version} >= 140000 && 0%{?sle_version} <= 150400
%else
%{perl_vendorarch}/auto/share/dist/%{cpan_name}/*.h
%endif

%changelog
