#
# spec file for package perl-Data-ShowTable
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Data-ShowTable
Name:           perl-Data-ShowTable
Version:        4.600.0
Release:        0
# 4.6 -> normalize -> 4.600.0
%define cpan_version 4.6
#Upstream: SUSE-Public-Domain
License:        GPL-2.0-or-later
Summary:        Perl module to automatically format columnar data
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKSTE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Data::ShowTable) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The *ShowTable* module provides subroutines to display tabular data,
typially from a database, in nicely formatted columns, in several formats.
Its arguments can either be given in a fixed order, or, as a single,
anonymous hash-array.

The output format for any one invocation can be one of four possible
styles:

* Box

A tabular format, with the column titles and the entire table surrounded by
a "box" of "'+'", "'-'", and "'|'" characters. See "ShowBoxTable" for
details.

* Table

A simple tabular format, with columns automatically aligned, with column
titles. See "ShowSimpleTable".

* List

A _list_ style, where columns of data are listed as a _name_:_value_ pair,
one pair per line, with rows being one or more column values, separated by
an empty line. See "ShowListTable".

* HTML

The data is output as an HTML _TABLE_, suitable for display through a
_Web_-client. See "ShowHTMLTable". Input can either be plain ASCII text, or
text with embedded HTML elements, depending upon an argument or global
parameter.

The subroutines which perform these displays are listed below.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc bump-version Changes Copyright gen-html gen-tests GNU-LICENSE README showtable testfile testfile.lst testfile.tabs test.pl.off

%changelog
