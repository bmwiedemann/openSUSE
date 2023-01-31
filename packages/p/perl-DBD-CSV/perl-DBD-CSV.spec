#
# spec file for package perl-DBD-CSV
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name DBD-CSV
Name:           perl-DBD-CSV
Version:        0.60
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        DBI driver for CSV files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::File) >= 0.42
BuildRequires:  perl(DBI) >= 1.628
BuildRequires:  perl(SQL::Statement) >= 1.405
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Text::CSV_XS) >= 1.01
Requires:       perl(DBD::File) >= 0.42
Requires:       perl(DBI) >= 1.628
Requires:       perl(SQL::Statement) >= 1.405
Requires:       perl(Test::More) >= 0.9
Requires:       perl(Text::CSV_XS) >= 1.01
Recommends:     perl(DBD::File) >= 0.44
Recommends:     perl(DBI) >= 1.643
Recommends:     perl(SQL::Statement) >= 1.414
Recommends:     perl(Text::CSV_XS) >= 1.49
%{perl_requires}

%description
The DBD::CSV module is yet another driver for the DBI (Database independent
interface for Perl). This one is based on the SQL "engine" SQL::Statement
and the abstract DBI driver DBD::File and implements access to so-called
CSV files (Comma Separated Values). Such files are often used for exporting
MS Access and MS Excel data.

See DBI for details on DBI, SQL::Statement for details on SQL::Statement
and DBD::File for details on the base class DBD::File.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
