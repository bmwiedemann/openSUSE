#
# spec file for package perl-DBD-CSV
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DBD-CSV
Version:        0.54
Release:        0
%define cpan_name DBD-CSV
Summary:        DBI driver for CSV files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBD-CSV/
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::File) >= 0.42
BuildRequires:  perl(DBI) >= 1.628
BuildRequires:  perl(SQL::Statement) >= 1.405
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Text::CSV_XS) >= 1.01
Requires:       perl(DBD::File) >= 0.42
Requires:       perl(DBI) >= 1.628
Requires:       perl(SQL::Statement) >= 1.405
Requires:       perl(Test::More) >= 0.9
Requires:       perl(Text::CSV_XS) >= 1.01
Recommends:     perl(DBD::File) >= 0.44
Recommends:     perl(DBI) >= 1.641
Recommends:     perl(SQL::Statement) >= 1.412
Recommends:     perl(Test::More) >= 1.302136
Recommends:     perl(Text::CSV_XS) >= 1.35
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
