#
# spec file for package perl-Spreadsheet-ParseXLSX
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


%define cpan_name Spreadsheet-ParseXLSX
Name:           perl-Spreadsheet-ParseXLSX
Version:        0.310.0
Release:        0
%define cpan_version 0.31
License:        MIT
Summary:        Parse XLSX files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUDDLEGG/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Crypt::Mode::CBC)
BuildRequires:  perl(Crypt::Mode::ECB)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Graphics::ColorUtils)
BuildRequires:  perl(OLE::Storage_Lite)
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Spreadsheet::ParseExcel::Utility)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XML::Twig)
Requires:       perl(Archive::Zip)
Requires:       perl(Crypt::Mode::CBC)
Requires:       perl(Crypt::Mode::ECB)
Requires:       perl(Digest::SHA)
Requires:       perl(Graphics::ColorUtils)
Requires:       perl(OLE::Storage_Lite)
Requires:       perl(Spreadsheet::ParseExcel)
Requires:       perl(XML::Twig)
Provides:       perl(Spreadsheet::ParseXLSX) = %{version}
Provides:       perl(Spreadsheet::ParseXLSX::Decryptor) = %{version}
Provides:       perl(Spreadsheet::ParseXLSX::Decryptor::Agile) = %{version}
Provides:       perl(Spreadsheet::ParseXLSX::Decryptor::Standard) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
This module is an adaptor for Spreadsheet::ParseExcel that reads XLSX
files. For documentation about the various data that you can retrieve from
these classes, please see Spreadsheet::ParseExcel,
Spreadsheet::ParseExcel::Workbook, Spreadsheet::ParseExcel::Worksheet, and
Spreadsheet::ParseExcel::Cell.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
