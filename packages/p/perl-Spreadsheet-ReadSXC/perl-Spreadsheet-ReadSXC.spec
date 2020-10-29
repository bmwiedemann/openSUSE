#
# spec file for package perl-Spreadsheet-ReadSXC
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Spreadsheet-ReadSXC
Version:        0.32
Release:        0
%define cpan_name Spreadsheet-ReadSXC
Summary:        Extract OpenOffice 1.x spreadsheet data
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-OPENSUSE Do not requires Filter:signatures, as we have perl > 5.20
Patch0:         remove_filter_signatures.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.34
#BuildRequires:  perl(Filter::signatures) >= 0.16
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(PerlIO::gzip)
BuildRequires:  perl(PerlX::Maybe)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XML::Twig::XPath)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPathEngine)
Requires:       perl(Archive::Zip) >= 1.34
#Requires:       perl(Filter::signatures) >= 0.16
Requires:       perl(Moo) >= 2
Requires:       perl(PerlIO::gzip)
Requires:       perl(PerlX::Maybe)
Requires:       perl(XML::Twig)
Requires:       perl(XML::Twig::XPath)
Requires:       perl(XML::XPath)
Requires:       perl(XML::XPathEngine)
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

Spreadsheet::ReadSXC uses XML::Twig to parse the XML contained in .sxc
files. Only the contents of text:p elements are returned, not the actual
values of table:value attributes. For example, a cell might have a
table:value-type attribute of "currency", a table:value attribute of
"-1500.99" and a table:currency attribute of "USD". The text:p element
would contain "-$1,500.99". This is the string which is returned by the
read_sxc() function, not the value of -1500.99.

Spreadsheet::ReadSXC was written with data import into an SQL database in
mind. Therefore empty spreadsheet cells correspond to undef values in array
rows. The example code above shows how to replace undef values with empty
strings.

If the .sxc file contains an empty spreadsheet its hash element will point
to an empty array (unless you use the 'NoTruncate' option in which case it
will point to an array of an array containing one undefined element).

OpenOffice uses UTF-8 encoding. It depends on your environment how the data
returned by the XML Parser is best handled:

  use Unicode::String qw(latin1 utf8);
  $unicode_string = utf8($$workbook_ref{"Sheet1"}[0][0])->as_string;

  # this will not work for characters outside ISO-8859-1:

  $latin1_string = utf8($$workbook_ref{"Sheet1"}[0][0])->latin1;

Of course there are other modules than Unicode::String on CPAN that handle
conversion between encodings. It's your choice.

Table rows in .sxc files may have a "table:number-rows-repeated" attribute,
which is often used for consecutive empty rows. When you format whole rows
and/or columns in OpenOffice, it sets the numbers of rows in a worksheet to
32,000 and the number of columns to 256, even if only a few lower-numbered
rows and cells actually contain data. Spreadsheet::ReadSXC truncates such
sheets so that there are no empty rows after the last row containing data
and no empty columns after the last column containing data (unless you use
the 'NoTruncate' option).

Still it is perfectly legal for an .sxc file to apply the
"table:number-rows-repeated" attribute to rows that actually contain data
(although I have only been able to produce such files manually, not through
OpenOffice itself). To save on memory usage in these cases,
Spreadsheet::ReadSXC does not copy rows by value, but by reference
(remember that multi-dimensional arrays in Perl are really arrays of
references to arrays). Therefore, if you change a value in one row, it is
possible that you find the corresponding value in the next row changed,
too:

  $$workbook_ref{"Sheet1"}[0][0] = 'new string';
  print $$workbook_ref{"Sheet1"}[1][0];

As of version 0.20 the references returned by read_sxc() et al. remain
valid after subsequent calls to the same function. In earlier versions,
calling read_sxc() with a different file as the argument would change the
data referenced by the original return value, so you had to derefence it
before making another call. Thanks to H. Merijn Brand for fixing this.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
