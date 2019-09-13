#
# spec file for package perl-Mojo-SQLite
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Mojo-SQLite
Version:        3.002
Release:        0
%define cpan_name Mojo-SQLite
Summary:        Tiny Mojolicious wrapper for SQLite
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::SQLite) >= 1.54
BuildRequires:  perl(DBI) >= 1.627
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojolicious) >= 7.32
BuildRequires:  perl(SQL::Abstract) >= 1.81
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.69
BuildRequires:  perl(URI::db) >= 0.15
BuildRequires:  perl(URI::file) >= 4.21
Requires:       perl(DBD::SQLite) >= 1.54
Requires:       perl(DBI) >= 1.627
Requires:       perl(Mojolicious) >= 7.32
Requires:       perl(SQL::Abstract) >= 1.81
Requires:       perl(URI) >= 1.69
Requires:       perl(URI::db) >= 0.15
Requires:       perl(URI::file) >= 4.21
%{perl_requires}

%description
Mojo::SQLite is a tiny wrapper around DBD::SQLite that makes at
https://www.sqlite.org/ a lot of fun to use with the at https://mojolico.us
real-time web framework. Use all at http://sqlite.org/lang.html SQLite has
to offer, generate CRUD queries from data structures, and manage your
database schema with migrations.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.md examples README
%license LICENSE

%changelog
