#
# spec file for package perl-Spreadsheet-XLSX
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Spreadsheet-XLSX
Version:        0.15
Release:        0
%define cpan_name Spreadsheet-XLSX
Summary:        Perl extension for reading MS Excel 2007 files;
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Spreadsheet-XLSX/
Source0:        http://www.cpan.org/authors/id/M/MI/MIKEB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.18
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Archive::Zip) >= 1.18
Requires:       perl(Spreadsheet::ParseExcel)
Requires:       perl(Test::NoWarnings)
%{perl_requires}

%description
This module is a (quick and dirty) emulation of Spreadsheet::ParseExcel for
Excel 2007 (.xlsx) file format. It supports styles and many of Excel's
quirks, but not all. It populates the classes from Spreadsheet::ParseExcel
for interoperability; including Workbook, Worksheet, and Cell.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes README

%changelog
