#
# spec file for package perl-Spreadsheet-ReadSXC
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Spreadsheet-ReadSXC
Version:        0.20
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Spreadsheet-ReadSXC
Summary:        Extract OpenOffice 1.x spreadsheet data
Url:            http://search.cpan.org/dist/Spreadsheet-ReadSXC/
Group:          Development/Libraries/Perl
#Source:        http://www.cpan.org/authors/id/T/TE/TERHECHTE/Spreadsheet-ReadSXC-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
#
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(XML::Parser)
Requires:       perl(Archive::Zip)
Requires:       perl(Compress::Zlib)
Requires:       perl(XML::Parser)
%{perl_requires}

%description
Spreadsheet::ReadSXC extracts data from OpenOffice 1.x spreadsheet files
(.sxc). It exports the function read_sxc() which takes a filename and an
optional reference to a hash of options as arguments and returns a
reference to a hash of references to two-dimensional arrays. The hash keys
correspond to the names of worksheets in the OpenOffice workbook. The
two-dimensional arrays correspond to rows and cells in the respective
spreadsheets. If you don't like this because the order of sheets is not
preserved in a hash, read on. The 'OrderBySheet' option provides an array
of hashes instead.

If you prefer to unpack the .sxc file yourself, you can use the function
read_xml_file() instead and pass the path to content.xml as an argument. Or
you can extract the XML string from content.xml and pass the string to the
function read_xml_string(). Both functions also take a reference to a hash
of options as an optional second argument.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README t.sxc

%changelog
