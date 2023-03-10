#
# spec file for package perl-Spreadsheet-Read
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


%define cpan_name Spreadsheet-Read
Name:           perl-Spreadsheet-Read
Version:        0.87
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Meta-Wrapper for reading spreadsheet data
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Peek)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Data::Peek)
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(IO::Scalar)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::NoWarnings)
Recommends:     perl(Data::Peek) >= 0.52
Recommends:     perl(File::Temp) >= 0.2311
Recommends:     perl(IO::Scalar)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Spreadsheet::ParseExcel) >= 0.34
BuildRequires:  perl(Spreadsheet::ParseExcel::FmtDefault)
BuildRequires:  perl(Spreadsheet::ParseXLSX) >= 0.24
BuildRequires:  perl(Text::CSV_XS) >= 0.71
Recommends:     perl(Spreadsheet::ReadSXC) >= 0.20
Suggests:       perl-Spreadsheet-Read-scripts = %{version}
# MANUAL END

%description
Spreadsheet::Read tries to transparently read *any* spreadsheet and return
its content in a universal manner independent of the parsing module that
does the actual spreadsheet scanning.

For OpenOffice this module uses Spreadsheet::ReadSXC

For Microsoft Excel this module uses Spreadsheet::ParseExcel or
Spreadsheet::XLSX

For CSV this module uses Text::CSV_XS (0.29 or up required, 0.73 or up
preferred) or Text::CSV_PP (1.05 or up required).

For SquirrelCalc there is a very simplistic built-in parser

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
# MANUAL BEGIN
# Remove xls2csv and xls2csv.1 (conflict with libxls-tools and xls2csv packages)
rm -f %{buildroot}%{_bindir}/xls2csv
rm -f %{buildroot}%{_mandir}/man1/xls2csv.1
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md examples README
%exclude %{_bindir}/*
%exclude %{_mandir}/*

%package scripts
Summary:        Scripts to Work with Spreadsheets
Requires:       perl(HTML::Entities)
Requires:       perl(Spreadsheet::Read) = %{version}
Requires:       perl(Term::ReadKey)
Requires:       perl(Text::CSV_XS)
Requires:       perl(Tk)
Requires:       perl(Tk::TableMatrix::Spreadsheet)
# Conflict with ssdiff
Conflicts:      gnumeric

%description scripts
This package includes some scripts to work with spreadsheets.

%files scripts
%{_bindir}/ss2tk
%{_bindir}/ssdiff
%{_bindir}/xlscat
%{_bindir}/xlsgrep
%{_bindir}/xlsx2csv
%{_mandir}/man1/xlsx2csv.1%{?ext_man}

%changelog
