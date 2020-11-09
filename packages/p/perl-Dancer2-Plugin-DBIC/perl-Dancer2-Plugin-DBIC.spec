#
# spec file for package perl-Dancer2-Plugin-DBIC
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


Name:           perl-Dancer2-Plugin-DBIC
Version:        0.0100
Release:        0
%define cpan_name Dancer2-Plugin-DBIC
Summary:        DBIx::Class interface for Dancer2 applications
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBICx::Sugar) >= 0.0200
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(Dancer2) >= 0.153002
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Exception)
Requires:       perl(DBICx::Sugar) >= 0.0200
Requires:       perl(Dancer2) >= 0.153002
Requires:       perl(Dancer2::Plugin)
Recommends:     perl(DBIx::Class::Schema::Loader) >= 0.07002
%{perl_requires}

%description
This plugin makes it very easy to create Dancer2 applications that
interface with databases. It automatically exports the keyword 'schema'
which returns a DBIx::Class::Schema object. It also exports the keywords
'resultset' and 'rset'. You just need to configure your database connection
information. For performance, schema objects are cached in memory and are
lazy loaded the first time they are accessed.

This plugin is a thin wrapper around DBICx::Sugar.

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
%doc CHANGES README
%license LICENSE

%changelog
