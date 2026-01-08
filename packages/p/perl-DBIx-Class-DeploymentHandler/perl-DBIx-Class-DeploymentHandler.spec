#
# spec file for package perl-DBIx-Class-DeploymentHandler
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name DBIx-Class-DeploymentHandler
Name:           perl-DBIx-Class-DeploymentHandler
Version:        0.002235
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extensible DBIx::Class deployment
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/W/WE/WESM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Context::Preserve) >= 0.10
BuildRequires:  perl(DBD::SQLite) >= 1.350
BuildRequires:  perl(DBIx::Class) >= 0.81.210
BuildRequires:  perl(Log::Contextual) >= 0.5.5
BuildRequires:  perl(Module::Runtime) >= 0.1
BuildRequires:  perl(Moose) >= 1
BuildRequires:  perl(MooseX::Role::Parameterized) >= 0.180
BuildRequires:  perl(Path::Class) >= 0.260
BuildRequires:  perl(SQL::SplitStatement) >= 1.0.200
BuildRequires:  perl(SQL::Translator) >= 1.630
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Test::Fatal) >= 0.6
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires) >= 0.60
BuildRequires:  perl(Text::Brew) >= 0.20
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(YAML) >= 0.660
BuildRequires:  perl(aliased)
BuildRequires:  perl(autodie)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent) >= 0.225
Requires:       perl(Carp::Clan)
Requires:       perl(Context::Preserve) >= 0.10
Requires:       perl(DBIx::Class) >= 0.81.210
Requires:       perl(Log::Contextual) >= 0.5.5
Requires:       perl(Module::Runtime) >= 0.1
Requires:       perl(Moose) >= 1
Requires:       perl(MooseX::Role::Parameterized) >= 0.180
Requires:       perl(Path::Class) >= 0.260
Requires:       perl(SQL::SplitStatement) >= 1.0.200
Requires:       perl(SQL::Translator) >= 1.630
Requires:       perl(Sub::Exporter::Progressive)
Requires:       perl(Text::Brew) >= 0.20
Requires:       perl(Try::Tiny)
Requires:       perl(YAML) >= 0.660
Requires:       perl(autodie)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent) >= 0.225
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(YAML)
# MANUAL END

%description
'DBIx::Class::DeploymentHandler' is, as its name suggests, a tool for
deploying and upgrading databases with DBIx::Class. It is designed to be
much more flexible than DBIx::Class::Schema::Versioned, hence the use of
Moose and lots of roles.

'DBIx::Class::DeploymentHandler' itself is just a recommended set of roles
that we think will not only work well for everyone, but will also yield the
best overall mileage. Each role it uses has its own nuances and
documentation, so I won't describe all of them here, but here are a few of
the major benefits over how DBIx::Class::Schema::Versioned worked (and
DBIx::Class::DeploymentHandler::Deprecated tries to maintain compatibility
with):

  * Downgrades in addition to upgrades.

  * Multiple sql files files per upgrade/downgrade/install.

  * Perl scripts allowed for upgrade/downgrade/install.

  * Just one set of files needed for upgrade, unlike before where one might
need to generate 'factorial(scalar @versions)', which is just silly.

  * And much, much more!

That's really just a taste of some of the differences. Check out each role
for all the details.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

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
%doc Changes README TODO
%license LICENSE

%changelog
