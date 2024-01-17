#
# spec file for package perl-Dancer2-Plugin-Auth-Extensible-Provider-DBIC
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


Name:           perl-Dancer2-Plugin-Auth-Extensible-Provider-DBIC
Version:        0.624
Release:        0
%define cpan_name Dancer2-Plugin-Auth-Extensible-Provider-DBIC
Summary:        Authenticate via the Dancer2::Plugin::DBIC plugin
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABEVERLEY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBIx::Class::ResultClass::HashRefInflator)
BuildRequires:  perl(Dancer2) >= 0.200000
BuildRequires:  perl(Dancer2::Core::Types)
BuildRequires:  perl(Dancer2::Plugin::Auth::Extensible) >= 0.708
BuildRequires:  perl(Dancer2::Plugin::DBIC) >= 0.0012
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(Moo)
BuildRequires:  perl(String::CamelCase)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(namespace::clean)
Requires:       perl(DBIx::Class::ResultClass::HashRefInflator)
Requires:       perl(Dancer2) >= 0.200000
Requires:       perl(Dancer2::Core::Types)
Requires:       perl(Dancer2::Plugin::Auth::Extensible) >= 0.708
Requires:       perl(Dancer2::Plugin::DBIC) >= 0.0012
Requires:       perl(DateTime)
Requires:       perl(Moo)
Requires:       perl(String::CamelCase)
Requires:       perl(namespace::clean)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(Test::MockDateTime)
# MANUAL END

%description
This class is an authentication provider designed to authenticate users
against a database, using Dancer2::Plugin::DBIC to access a database.

See Dancer2::Plugin::DBIC for how to configure a database connection
appropriately; see the CONFIGURATION section below for how to configure
this authentication provider with database details.

See Dancer2::Plugin::Auth::Extensible for details on how to use the
authentication framework.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes ignore.txt README
%license LICENSE

%changelog
