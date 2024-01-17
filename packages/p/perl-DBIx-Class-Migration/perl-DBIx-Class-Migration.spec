#
# spec file for package perl-DBIx-Class-Migration
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


Name:           perl-DBIx-Class-Migration
Version:        0.075
Release:        0
%define cpan_name DBIx-Class-Migration
Summary:        Use the best tools together for sane database migrations
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.22
BuildRequires:  perl(Config::MySQL) >= 0.02
BuildRequires:  perl(DBD::SQLite) >= 1.46
BuildRequires:  perl(DBIx::Class::DeploymentHandler) >= 0.002223
BuildRequires:  perl(DBIx::Class::Fixtures) >= 1.001039
BuildRequires:  perl(DBIx::Class::Schema::Loader) >= 0.07042
BuildRequires:  perl(Devel::PartialDump) >= 0.17
BuildRequires:  perl(File::ShareDir::ProjectDistDir) >= 1.000004
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Log::Any) >= 1.707
BuildRequires:  perl(Module::Find) >= 0.13
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(MooX::Attribute::ENV) >= 0.02
BuildRequires:  perl(MooX::Options) >= 4.103
BuildRequires:  perl(MooX::Traits) >= 0.005
BuildRequires:  perl(Pod::Parser) >= 1.63
BuildRequires:  perl(SQL::Translator) >= 0.11021
BuildRequires:  perl(Test::Most) >= 0.34
BuildRequires:  perl(Test::Requires) >= 0.10
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Brew) >= 0.02
BuildRequires:  perl(Type::Tiny) >= 1.004004
BuildRequires:  perl(version) >= 0.9924
Requires:       perl(Class::Load) >= 0.22
Requires:       perl(Config::MySQL) >= 0.02
Requires:       perl(DBD::SQLite) >= 1.46
Requires:       perl(DBIx::Class::DeploymentHandler) >= 0.002223
Requires:       perl(DBIx::Class::Fixtures) >= 1.001039
Requires:       perl(DBIx::Class::Schema::Loader) >= 0.07042
Requires:       perl(Devel::PartialDump) >= 0.17
Requires:       perl(File::ShareDir::ProjectDistDir) >= 1.000004
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Log::Any) >= 1.707
Requires:       perl(Module::Find) >= 0.13
Requires:       perl(Moo) >= 2
Requires:       perl(MooX::Attribute::ENV) >= 0.02
Requires:       perl(MooX::Options) >= 4.103
Requires:       perl(MooX::Traits) >= 0.005
Requires:       perl(Pod::Parser) >= 1.63
Requires:       perl(SQL::Translator) >= 0.11021
Requires:       perl(Text::Brew) >= 0.02
Requires:       perl(Type::Tiny) >= 1.004004
Requires:       perl(version) >= 0.9924
%{perl_requires}

%description
DBIx::Class::DeploymentHandler is a state of the art solution to the
problem of creating sane workflows for versioning DBIx::Class managed
database projects. However, since it is more of a toolkit for building
custom versioning and migration workflows than an expression of a
particular migration practice, it might not always be the most approachable
tool. If you are starting a new DBIx::Class project and you don't have a
particular custom workflow need, you might prefer to simply be given a
reasonable clear and standard practice, rather than a toolkit with a set of
example scripts.

DBIx::Class::Migration defines some logic which combines both
DBIx::Class::DeploymentHandler and DBIx::Class::Fixtures, along with a
standard tutorial, to give you a simple and straightforward approach to
solving the problem of how to best create database versions, migrations and
testing data. Additionally it builds on tools like Test::mysqld and
Test::Postgresql58 along with DBD::Sqlite in order to assist you in quickly
creating a local development database sandbox. It offers some integration
points to testing your database, via tools like Test::DBIx::Class in order
to make testing your database driven logic less painful. Lastly, we offer
some thoughts on good development patterns in using databases with
application frameworks like Catalyst.

DBIx::Class::Migration offers code and advice based on my experience of
using DBIx::Class for several years, which hopefully can help you bootstrap
a new project. The solutions given should work for you if you want to use
DBIx::Class and have database migrations, but don't really know what to do
next. These solutions should scale upward from a small project to a medium
project involving many developers and more than one target environment (DEV
-> QA -> Production.) If you have very complex database versioning
requirements, huge teams and difficult architectual issues, you might be
better off building something on top of DBIx::Class::DeploymentHandler
directly.

DBIx::Class::Migration is a base class upon which interfaces like
DBIx::Class::Migration::Script are built.

Please see DBIx::Class::Migration::Tutorial for more approachable
documentation. If you want to read a high level feature overview, see
DBIx::Class::Migration::Features. The remainder of this POD is API level
documentation on the various internals.

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
%doc Changes examples README README.mkdn TODO
%license LICENSE

%changelog
