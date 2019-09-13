#
# spec file for package perl-SQL-SplitStatement
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-SQL-SplitStatement
Version:        1.00020
Release:        0
%define cpan_name SQL-SplitStatement
Summary:        Split any SQL code into atomic statements
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/SQL-SplitStatement/
Source:         http://www.cpan.org/authors/id/E/EM/EMAZEP/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(SQL::Tokenizer) >= 0.22
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More) >= 0.7
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(List::MoreUtils)
Requires:       perl(Regexp::Common)
Requires:       perl(SQL::Tokenizer) >= 0.22
%{perl_requires}

%description
This is a simple module which tries to split any SQL code, even including
non-standard extensions (for the details see the the /SUPPORTED DBMSs
manpage section below), into the atomic statements it is composed of.

The logic used to split the SQL code is more sophisticated than a raw
'split' on the ';' (semicolon) character: first, various different
statement terminator _tokens_ are recognized (see below for the list), then
this module is able to correctly handle the presence of said tokens inside
identifiers, values, comments, 'BEGIN ... END' blocks (even nested),
_dollar-quoted_ strings, MySQL custom 'DELIMITER's, procedural code etc.,
as (partially) exemplified in the the /SYNOPSIS manpage above.

Consider however that this is by no means a validating parser (technically
speaking, it's just a _context-sensitive tokenizer_). It should rather be
seen as an in-progress _heuristic_ approach, which will gradually improve
as test cases will be reported. This also means that, except for the the
/LIMITATIONS manpage detailed below, there is no known (to the author) SQL
code the most current release of this module can't correctly split.

The test suite bundled with the distribution (which now includes the
popular _Sakila_ and _Pagila_ sample db schemata, as detailed in the the
/SHOWCASE manpage section below) should give you an idea of the
capabilities of this module

If your atomic statements are to be fed to a DBMS, you are encouraged to
use the DBIx::MultiStatementDo manpage instead, which uses this module and
also (optionally) offers automatic transactions support, so that you'll
have the _all-or-nothing_ behavior you would probably want.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
