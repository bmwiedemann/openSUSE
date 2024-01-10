#
# spec file for package perl-Spreadsheet-ParseExcel
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Spreadsheet-ParseExcel
Name:           perl-Spreadsheet-ParseExcel
Version:        0.660.0
Release:        0
%define cpan_version 0.66
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Read information from an Excel file
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::RC4)
BuildRequires:  perl(Digest::Perl::MD5)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(OLE::Storage_Lite) >= 0.19
Requires:       perl(Crypt::RC4)
Requires:       perl(Digest::Perl::MD5)
Requires:       perl(IO::Scalar)
Requires:       perl(OLE::Storage_Lite) >= 0.19
Provides:       perl(Spreadsheet::ParseExcel) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Cell) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Dump) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::FmtDefault) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::FmtJapan) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::FmtJapan2) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::FmtUnicode) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Font) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Format) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::SaveParser) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::SaveParser::Workbook) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::SaveParser::Worksheet) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Utility) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Workbook) = %{version}
Provides:       perl(Spreadsheet::ParseExcel::Worksheet) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
The Spreadsheet::ParseExcel module can be used to read information from
Excel 95-2003 binary files.

The module cannot read files in the Excel 2007 Open XML XLSX format. See
the Spreadsheet::XLSX module instead.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CP932Excel.map examples README README_Japan.htm

%changelog
