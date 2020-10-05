#
# spec file for package perl-Mojo-Pg
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


Name:           perl-Mojo-Pg
Version:        4.20
Release:        0
%define cpan_name Mojo-Pg
Summary:        Wrapper around DBD::Pg for using PostgreSql with Mojolicious
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::Pg) >= 3.007004
BuildRequires:  perl(Mojolicious) >= 8.50
BuildRequires:  perl(SQL::Abstract) >= 1.86
Requires:       perl(DBD::Pg) >= 3.007004
Requires:       perl(Mojolicious) >= 8.50
Requires:       perl(SQL::Abstract) >= 1.86
%{perl_requires}

%description
Mojo::Pg is a tiny wrapper around DBD::Pg that makes at
http://www.postgresql.org a lot of fun to use with the at
https://mojolicious.org real-time web framework. Perform queries blocking
and non-blocking, use all at
https://www.postgresql.org/docs/current/static/sql.html PostgreSQL has to
offer, generate CRUD queries from data structures, manage your database
schema with migrations and build scalable real-time web applications with
the publish/subscribe pattern.

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
%doc Changes examples README.md
%license LICENSE

%changelog
