#
# spec file for package perl-BerkeleyDB
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


%define cpan_name BerkeleyDB
Name:           perl-BerkeleyDB
Version:        0.660.0
Release:        0
# 0.66 -> normalize -> 0.660.0
%define cpan_version 0.66
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for Berkeley DB version 2, 3, 4, 5 or 6
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(BerkeleyDB) = %{version}
Provides:       perl(BerkeleyDB::Btree)
Provides:       perl(BerkeleyDB::CDS::Lock)
Provides:       perl(BerkeleyDB::Common)
Provides:       perl(BerkeleyDB::Cursor)
Provides:       perl(BerkeleyDB::Env)
Provides:       perl(BerkeleyDB::Hash)
Provides:       perl(BerkeleyDB::Heap)
Provides:       perl(BerkeleyDB::Queue)
Provides:       perl(BerkeleyDB::Recno)
Provides:       perl(BerkeleyDB::Term)
Provides:       perl(BerkeleyDB::Txn)
Provides:       perl(BerkeleyDB::TxnMgr)
Provides:       perl(BerkeleyDB::Unknown)
Provides:       perl(BerkeleyDB::_tiedArray)
Provides:       perl(BerkeleyDB::_tiedHash)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  db-devel
# MANUAL END

%description
*NOTE: This document is still under construction. Expect it to be
incomplete in places.*

This Perl module provides an interface to most of the functionality
available in Berkeley DB versions 2, 3, 5 and 6. In general it is safe to
assume that the interface provided here to be identical to the Berkeley DB
interface. The main changes have been to make the Berkeley DB API work in a
Perl way. Note that if you are using Berkeley DB 2.x, the new features
available in Berkeley DB 3.x or later are not available via this module.

The reader is expected to be familiar with the Berkeley DB documentation.
Where the interface provided here is identical to the Berkeley DB library
and the... TODO

The *db_appinit*, *db_cursor*, *db_open* and *db_txn* man pages are
particularly relevant.

The interface to Berkeley DB is implemented with a number of Perl classes.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc BerkeleyDB.pod.P Changes dbinfo mkpod README Todo

%changelog
