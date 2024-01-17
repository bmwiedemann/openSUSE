#
# spec file for package xls2csv
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xls2csv
Version:        1.07
Release:        0
Summary:        A script that recodes a spreadsheet's charset and saves as CSV
License:        Artistic-1.0 or GPL-2.0+
Group:          Productivity/Text/Convertors
Url:            http://search.cpan.org/~ken/xls2csv/script/xls2csv
# repacked http://search.cpan.org/CPAN/authors/id/K/KE/KEN/%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build)
Requires:       perl
Requires:       perl(Locale::Recode)
Requires:       perl(Spreadsheet::ParseExcel)
Requires:       perl(Spreadsheet::ParseExcel::FmtUnicode)
Requires:       perl(Text::CSV_XS)
Requires:       perl(Unicode::Map)
BuildArch:      noarch

%description
This script will recode a spreadsheet into a different character set and output the recoded data as a csv file.
The script came about after many headaches from dealing with Excel spreadsheets from clients that were being received in various character sets.

%prep
%setup -q

%build
perl Makefile.PL
make %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -name .packlist -print -delete

%files
%defattr(-, root, root)
%{_bindir}/xls2csv
%doc %{_mandir}/man1/xls2csv.1*
%doc Changes README

%changelog
