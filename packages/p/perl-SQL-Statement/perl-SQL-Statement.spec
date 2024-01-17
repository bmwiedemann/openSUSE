#
# spec file for package perl-SQL-Statement
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


Name:           perl-SQL-Statement
Version:        1.414
Release:        0
%define cpan_name SQL-Statement
Summary:        SQL parsing and processing engine
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(Math::Base::Convert)
BuildRequires:  perl(Math::Complex) >= 1.56
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Text::Soundex) >= 3.04
Requires:       perl(Clone) >= 0.30
Requires:       perl(Module::Runtime)
Requires:       perl(Params::Util) >= 1.00
Recommends:     perl(Math::Base::Convert)
Recommends:     perl(Math::Complex) >= 1.56
Recommends:     perl(Text::Soundex) >= 3.04
%{perl_requires}

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine. While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complex nested search conditions,
and other features.

SQL::Statement is a small embeddable Database Management System (DBMS).
This means that it provides all of the services of a simple DBMS except
that instead of a persistent storage mechanism, it has two things: 1) an
in-memory storage mechanism that allows you to prepare, execute, and fetch
from SQL statements using temporary tables and 2) a set of software sockets
where any author can plug in any storage mechanism.

There are three main uses for SQL::Statement. One or another (hopefully not
all) may be irrelevant for your needs: 1) to access and manipulate data in
CSV, XML, and other formats 2) to build your own DBD for a new data source
3) to parse and examine the structure of SQL statements.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes GPL-1 GPL-2.0 README README.md
%license ARTISTIC-1.0 LICENSE

%changelog
