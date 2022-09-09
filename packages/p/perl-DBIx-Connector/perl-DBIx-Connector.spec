#
# spec file for package perl-DBIx-Connector
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name DBIx-Connector
Name:           perl-DBIx-Connector
Version:        0.58
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Fast, safe DBI connection and transaction management
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.605
Requires:       perl(DBI) >= 1.605
Recommends:     perl(DBI) >= 1.614
%{perl_requires}

%description
DBIx::Connector provides a simple interface for fast and safe DBI
connection and transaction management. Connecting to a database can be
expensive; you don't want your application to re-connect every time you
need to run a query. The efficient thing to do is to hang on to a database
handle to maintain a connection to the database in order to minimize that
overhead. DBIx::Connector lets you do that without having to worry about
dropped or corrupted connections.

You might be familiar with Apache::DBI and with the DBI's
'connect_cached()' constructor. DBIx::Connector serves a similar need, but
does a much better job. How is it different? I'm glad you asked!

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%license LICENSE

%changelog
