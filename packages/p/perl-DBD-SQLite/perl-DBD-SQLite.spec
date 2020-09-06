#
# spec file for package perl-DBD-SQLite
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


Name:           perl-DBD-SQLite
Version:        1.66
Release:        0
%define cpan_name DBD-SQLite
Summary:        Self-contained RDBMS in a DBI Driver
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.57
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(DBI) >= 1.57
Requires:       perl(Test::More) >= 0.88
%{perl_requires}

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
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes constants.inc dbdimp_tokenizer.inc dbdimp_virtual_table.inc README
%license LICENSE

%changelog
