#
# spec file for package perl-Spreadsheet-WriteExcel
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


%define cpan_name Spreadsheet-WriteExcel
Name:           perl-Spreadsheet-WriteExcel
Version:        2.400.0
Release:        0
# 2.40 -> normalize -> 2.400.0
%define cpan_version 2.40
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Write to a cross platform Excel binary file
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(OLE::Storage_Lite) >= 0.190
BuildRequires:  perl(Parse::RecDescent)
Requires:       perl(OLE::Storage_Lite) >= 0.190
Requires:       perl(Parse::RecDescent)
Provides:       perl(Spreadsheet::WriteExcel) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::BIFFwriter) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Big) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Area) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Bar) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Column) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::External) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Line) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Pie) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Scatter) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Chart::Stock) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Examples) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Format) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Formula) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::OLEwriter) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Properties) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Utility) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Workbook) = %{version}
Provides:       perl(Spreadsheet::WriteExcel::Worksheet) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The Spreadsheet::WriteExcel Perl module can be used to create a
cross-platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers, formulas,
hyperlinks, images and charts can be written to the cells.

The file produced by this module is compatible with Excel 97, 2000, 2002,
2003 and 2007.

The module will work on the majority of Windows, UNIX and Mac platforms.
Generated files are also compatible with the Linux/UNIX spreadsheet
applications Gnumeric and OpenOffice.org.

This module cannot be used to write to an existing Excel file (See
MODIFYING AND REWRITING EXCEL FILES).

*Note: This module is in maintenance only mode* and in future will only be
updated with bug fixes. The newer, more feature rich and API compatible
Excel::Writer::XLSX module is recommended instead. See, Migrating to
Excel::Writer::XLSX.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes docs examples README

%changelog
