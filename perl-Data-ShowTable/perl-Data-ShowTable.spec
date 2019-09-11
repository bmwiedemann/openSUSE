#
# spec file for package perl-Data-ShowTable
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


Name:           perl-Data-ShowTable
Version:        4.6
Release:        0
%define cpan_name Data-ShowTable
Summary:        routines to display tabular data in several formats.
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-ShowTable/
Source:         http://www.cpan.org/authors/id/A/AK/AKSTE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The *ShowTable* module provides subroutines to display tabular data,
typially from a database, in nicely formatted columns, in several formats.
Its arguments can either be given in a fixed order, or, as a single,
anonymous hash-array.

The output format for any one invocation can be one of four possible
styles:

* Box

  A tabular format, with the column titles and the entire table surrounded
  by a "box" of "'+'", "'-'", and "'|'" characters. See the "ShowBoxTable"
  manpage for details.

* Table

  A simple tabular format, with columns automatically aligned, with column
  titles. See the "ShowSimpleTable" manpage.

* List

  A _list_ style, where columns of data are listed as a _name_:_value_
  pair, one pair per line, with rows being one or more column values,
  separated by an empty line. See the "ShowListTable" manpage.

* HTML

  The data is output as an HTML _TABLE_, suitable for display through a
  _Web_-client. See the "ShowHTMLTable" manpage. Input can either be plain
  ASCII text, or text with embedded HTML elements, depending upon an
  argument or global parameter.

The subroutines which perform these displays are listed below.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

rm -f pm_to_blib

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
%doc bump-version Changes Copyright gen-html gen-tests GNU-LICENSE MYMETA.json MYMETA.yml README showtable testfile testfile.lst testfile.tabs test.pl.off

%changelog
