#
# spec file for package perl-Spreadsheet-XLSX
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


%define cpan_name Spreadsheet-XLSX
Name:           perl-Spreadsheet-XLSX
Version:        0.17
Release:        0
Summary:        Perl extension for reading MS Excel 2007 files;
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.18
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warnings)
Requires:       perl(Archive::Zip) >= 1.18
Requires:       perl(Spreadsheet::ParseExcel)
%{perl_requires}

%description
This module is a (quick and dirty) emulation of Spreadsheet::ParseExcel for
Excel 2007 (.xlsx) file format. It supports styles and many of Excel's
quirks, but not all. It populates the classes from Spreadsheet::ParseExcel
for interoperability; including Workbook, Worksheet, and Cell.

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

%changelog
