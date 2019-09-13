#
# spec file for package perl-DBICx-TestDatabase
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DBICx-TestDatabase
Version:        0.05
Release:        0
%define cpan_name DBICx-TestDatabase
Summary:        Create a Temporary Database From a Dbix::Class::Schema
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBICx-TestDatabase/
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JROCKWAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::SQLite) >= 1.29
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(ok)
Requires:       perl(DBD::SQLite) >= 1.29
Requires:       perl(SQL::Translator)
%{perl_requires}

%description
This module creates a temporary SQLite database, deploys your DBIC schema,
and then connects to it. This lets you easily test your DBIC schema. Since
you have a fresh database for every test, you don't have to worry about
cleaning up after your tests, ordering of tests affecting failure, etc.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

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
