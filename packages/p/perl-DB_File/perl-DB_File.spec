#
# spec file for package perl-DB_File
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name DB_File
Name:           perl-DB_File
Version:        1.860
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl access to Berkeley DB 1.x
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
%if 0%{?suse_version} >= 1140
BuildRequires:  libdb-4_8-devel
%else
BuildRequires:  libdb-4_5-devel
%endif
# MANUAL END

%description
*DB_File* is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 1.x (if you have a newer version
of DB, see Using DB_File with Berkeley DB version 2 or greater). It is
assumed that you have a copy of the Berkeley DB manual pages at hand when
reading this documentation. The interface defined here mirrors the Berkeley
DB interface closely.

Berkeley DB is a C library which provides a consistent interface to a
number of database formats. *DB_File* provides an interface to all three of
the database types currently supported by Berkeley DB.

The file types are:

* *DB_HASH*

This database type allows arbitrary key/value pairs to be stored in data
files. This is equivalent to the functionality provided by other hashing
packages like DBM, NDBM, ODBM, GDBM, and SDBM. Remember though, the files
created using DB_HASH are not compatible with any of the other packages
mentioned.

A default hashing algorithm, which will be adequate for most applications,
is built into Berkeley DB. If you do need to use your own hashing algorithm
it is possible to write your own in Perl and have *DB_File* use it instead.

* *DB_BTREE*

The btree format allows arbitrary key/value pairs to be stored in a sorted,
balanced binary tree.

As with the DB_HASH format, it is possible to provide a user defined Perl
routine to perform the comparison of keys. By default, though, the keys are
stored in lexical order.

* *DB_RECNO*

DB_RECNO allows both fixed-length and variable-length flat text files to be
manipulated using the same key/value pair interface as in DB_HASH and
DB_BTREE. In this case the key will consist of a record (line) number.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes dbinfo README

%changelog
