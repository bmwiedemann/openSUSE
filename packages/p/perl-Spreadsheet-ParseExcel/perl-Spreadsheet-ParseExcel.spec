#
# spec file for package perl-Spreadsheet-ParseExcel
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


Name:           perl-Spreadsheet-ParseExcel
Version:        0.65
Release:        0
%define cpan_name Spreadsheet-ParseExcel
Summary:        Read information from an Excel file.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Spreadsheet-ParseExcel/
Source:         http://www.cpan.org/authors/id/D/DO/DOUGW/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%{perl_requires}

%description
The Spreadsheet::ParseExcel module can be used to read information from
Excel 95-2003 binary files.

The module cannot read files in the Excel 2007 Open XML XLSX format. See
the the Spreadsheet::XLSX manpage module instead.

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
%doc Changes CP932Excel.map examples README README_Japan.htm

%changelog
