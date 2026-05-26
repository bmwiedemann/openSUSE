#
# spec file for package perl-Minion-Backend-SQLite
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


%define cpan_name Minion-Backend-SQLite
Name:           perl-Minion-Backend-SQLite
Version:        6.0.0
Release:        0
# v6.0.0 -> normalize -> 6.0.0
%define cpan_version v6.0.0
License:        Artistic-2.0
Summary:        SQLite backend for Minion job queue
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::SQLite) >= 1.680
BuildRequires:  perl(Minion) >= 12.0
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.34
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::SQLite) >= 4.0
BuildRequires:  perl(Mojolicious) >= 7.490
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(DBD::SQLite) >= 1.680
Requires:       perl(Minion) >= 12.0
Requires:       perl(Mojo::SQLite) >= 4.0
Requires:       perl(Mojolicious) >= 7.490
%{perl_requires}

%description
Minion::Backend::SQLite is a backend for Minion based on Mojo::SQLite. All
necessary tables will be created automatically with a set of migrations
named 'minion'. If no connection string or ':temp:' is provided, the
database will be created in a temporary directory.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md examples README
%license LICENSE

%changelog
