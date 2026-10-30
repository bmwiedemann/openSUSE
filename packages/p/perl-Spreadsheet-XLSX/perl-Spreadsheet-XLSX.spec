#
# spec file for package perl-Spreadsheet-XLSX
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


%define cpan_name Spreadsheet-XLSX
Name:           perl-Spreadsheet-XLSX
Version:        0.200.0
Release:        0
# 0.20 -> normalize -> 0.200.0
%define cpan_version 0.20
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for reading MS Excel 2007 files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.180
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warnings)
Requires:       perl(Archive::Zip) >= 1.180
Requires:       perl(Spreadsheet::ParseExcel)
Provides:       perl(Spreadsheet::XLSX) = %{version}
Provides:       perl(Spreadsheet::XLSX::Fmt2007) = %{version}
Provides:       perl(Spreadsheet::XLSX::Utility2007) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
ZIP input is limited to 10,000 entries, 64 MiB per uncompressed member, and
256 MiB of total declared uncompressed data, including unused members.
Members used by the parser are decompressed incrementally and their actual
sizes are checked against the limits and ZIP metadata. Exceeding a limit or
encountering inconsistent sizes raises an exception.

Applications needing different limits can scope them to a parsing
operation:

    local $Spreadsheet::XLSX::MAX_MEMBER_SIZE = 128 * 1024 * 1024;
    local $Spreadsheet::XLSX::MAX_TOTAL_SIZE = 512 * 1024 * 1024;
    local $Spreadsheet::XLSX::MAX_MEMBERS = 20000;
    my $excel = Spreadsheet::XLSX->new($filename);

These limits bound uncompressed input, not the total memory used by parsed
cells and XML processing.

This module is a (quick and dirty) emulation of Spreadsheet::ParseExcel for
Excel 2007 (.xlsx) file format. It supports styles and many of Excel's
quirks, but not all. It populates the classes from Spreadsheet::ParseExcel
for interoperability; including Workbook, Worksheet, and Cell.

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
%doc Changes README

%changelog
