#
# spec file for package perl-Spreadsheet-Read
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


%define cpan_name Spreadsheet-Read
Name:           perl-Spreadsheet-Read
Version:        0.84
Release:        0
Summary:        Read the data from a spreadsheet
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
Patch0:         nonstdperlpath.patch
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
Recommends:     perl(Data::Peek) >= 0.50
Recommends:     perl(File::Temp) >= 0.2311
Recommends:     perl(IO::Scalar)
Recommends:     perl(Test::More) >= 1.302183
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Spreadsheet::ParseExcel) >= 0.34
BuildRequires:  perl(Spreadsheet::ParseExcel::FmtDefault)
BuildRequires:  perl(Spreadsheet::ParseXLSX) >= 0.24
BuildRequires:  perl(Text::CSV_XS) >= 0.71
Recommends:     perl(Spreadsheet::ReadSXC) >= 0.20
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
%autosetup  -n %{cpan_name}-%{version} -p1
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
# disable installation of examples to {_bindir}
export AUTOMATED_TESTING=1
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md examples README

%changelog
