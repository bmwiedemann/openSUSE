#
# spec file for package perl-Spreadsheet-WriteExcel
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


%define cpan_name Spreadsheet-WriteExcel
Name:           perl-Spreadsheet-WriteExcel
Version:        2.40
Release:        0
Summary:        This Module can be Used to Create Excel Binary Files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://search.cpan.org/dist/Spreadsheet-WriteExcel/
Source:         http://search.cpan.org/CPAN/authors/id/J/JM/JMCNAMARA/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(OLE::Storage_Lite)
BuildRequires:  perl(Parse::RecDescent)
Requires:       perl(Parse::RecDescent)
%{perl_requires}

%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks, and images can be written to the cells.

The Excel file produced by this module is compatible with Excel 5, 95,
97, 2000, and 2002.

The module will work on the majority of Windows, UNIX, and Macintosh
platforms. Generated files are also compatible with Gnumeric and
OpenOffice.org, the Linux/UNIX spreadsheet applications. The generated
files are not compatible with MS Access.

%prep
%setup -q -n Spreadsheet-WriteExcel-%{version}

%build
perl Makefile.PL
%make_build

%check
%ifnarch %{arm}
%make_build test
%endif

%install
%if 0%{?suse_version}
%perl_make_install
%perl_process_packlist
%else
make DESTDIR=%{buildroot} install_vendor
find %{buildroot}%{_prefix} -type f -name perllocal.pod |xargs -i rm -f {}
find %{buildroot}%{_prefix} -type d -depth -exec rmdir {} \; 2>/dev/null
%endif

%files
%{_mandir}/man?/*
%{perl_vendorarch}/auto/Spreadsheet
%{perl_vendorlib}/Spreadsheet
%{_bindir}/chartex
%doc Changes MANIFEST README examples
%if 0%{?suse_version}
%endif

%changelog
