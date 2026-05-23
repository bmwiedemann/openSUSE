#
# spec file for package perl-Mojo-SQL
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


%define cpan_name Mojo-SQL
Name:           perl-Mojo-SQL
Version:        0.20.0
Release:        0
# 0.02 -> normalize -> 0.20.0
%define cpan_version 0.02
License:        MIT
Summary:        Safely generate and compose SQL statements
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mojolicious) >= 9.410
Requires:       perl(Mojolicious) >= 9.410
Provides:       perl(Mojo::SQL) = %{version}
Provides:       perl(Mojo::SQL::Statement)
%undefine       __perllib_provides
%{perl_requires}

%description
Mojo::SQL safely generates and composes SQL statements. To prevent SQL
injection attacks, every '?' in the input becomes a placeholder in the
generated query, with the corresponding value bound to it. Partial
statements can be composed recursively to build more complex queries.

Literal question marks can be escaped with '??'.

  use Mojo::SQL qw(sql);

  my $role    = 'admin';
  my $partial = sql('AND role = ?', $role);
  my $name    = 'root';

  # {text => 'SELECT * FROM users WHERE name = $1 AND role = $2', values => ['root', 'admin']}
  my $query = sql('SELECT * FROM users WHERE name = ? ?', $name, $partial)->to_query;

Make partial statements optional to dynamically generate 'WHERE' clauses.

  my $optional = $foo ? sql('AND foo IS NOT NULL') : sql('');
  my $query    = sql('SELECT * FROM users WHERE name = ? ?', 'sebastian', $optional)->to_query;

If you need a little more control over the generated SQL query, you can
also bypass safety features with "sql_unsafe". But make sure to handle
unsafe values yourself with appropriate escaping functions for your
database. For PostgreSQL there are "escape_literal" and "escape_identifier"
functions included with this module.

  use Mojo::SQL qw(sql sql_unsafe escape_literal);

  my $role    = 'role = ' . escape_literal('power user');
  my $partial = sql_unsafe 'AND ?', $role;
  my $name    = 'root';

  # {text => "SELECT * FROM users WHERE name = \$1 AND role = 'power user'", values => ['root']}
  my $query = sql('SELECT * FROM users WHERE name = ? ?', $name, $partial)->to_query;

For databases that do not support numbered placeholders like '$1' and '$2',
you can set a custom character with the 'placeholder' option.

  # {text => 'SELECT * FROM users WHERE name = ?', values => ['root']}
  my $query = sql('SELECT * FROM users WHERE name = ?', 'root')->to_query({placeholder => '?'});

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
