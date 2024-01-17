#
# spec file for package perl-SQL-Tokenizer
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright Andrey Karepin <egdfree@opensuse.org>
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


%define cpan_name SQL-Tokenizer
Name:           perl-SQL-Tokenizer
Version:        0.24
Release:        0
Summary:        A simple SQL tokenizer
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/SQL-Tokenizer/
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
## for SLE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
SQL::Tokenizer is a simple tokenizer for SQL queries. It does not claim to
be a parser or query verifier. It just creates sane tokens from a valid SQL
query.

It supports SQL with comments like:

 -- This query is used to insert a message into
 -- logs table
 INSERT INTO log (application, message) VALUES (?, ?)

Also supports '''', '""' and '\'' escaping methods, so tokenizing queries
like the one below should not be a problem:

 INSERT INTO log (application, message)
 VALUES ('myapp', 'Hey, this is a ''single quoted string''!')

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
%doc Changes README

%changelog
