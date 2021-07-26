#
# spec file for package perl-DBIx-Class-Schema-Config
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name DBIx-Class-Schema-Config
Name:           perl-DBIx-Class-Schema-Config
Version:        0.001014
Release:        0
Summary:        Credential Management for DBIx::Class
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYMKAT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::Any) >= 0.23
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class) >= 0.08100
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(URI)
BuildRequires:  perl(namespace::clean)
Requires:       perl(Config::Any) >= 0.23
Requires:       perl(DBD::SQLite)
Requires:       perl(DBIx::Class) >= 0.08100
Requires:       perl(DBIx::Class::Schema)
Requires:       perl(File::HomeDir)
Requires:       perl(Hash::Merge)
Requires:       perl(URI)
Requires:       perl(namespace::clean)
%{perl_requires}

%description
DBIx::Class::Schema::Config is a subclass of DBIx::Class::Schema that
allows the loading of credentials & configuration from a file. The actual
code itself would only need to know about the name used in the
configuration file. This aims to make it simpler for operations teams to
manage database credentials.

A simple tutorial that compliments this documentation and explains
converting an existing DBIx::Class Schema to use this software to manage
credentials can be found at
http://www.symkat.com/credential-management-in-dbix-class

%prep
%autosetup  -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

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
%doc Changes README

%changelog
