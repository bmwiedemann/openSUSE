#
# spec file for package perl-BerkeleyDB
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


Name:           perl-BerkeleyDB
Version:        0.64
Release:        0
%define cpan_name BerkeleyDB
Summary:        Perl extension for Berkeley DB version 2, 3, 4, 5 or 6
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc BerkeleyDB.pod.P Changes dbinfo mkpod README Todo

%changelog
