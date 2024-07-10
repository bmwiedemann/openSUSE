#
# spec file for package perl-HTML-TableExtract
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


Name:           perl-HTML-TableExtract
Version:        2.15
Release:        0
%define cpan_name HTML-TableExtract
Summary:        Perl module for extracting the content contained in tables within an HTM[cut]
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSISK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL BEGIN
Patch0:         perl-HTML-TableExtract-test-30_tree.patch
# MANUAL END
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::ElementTable) >= 1.16
BuildRequires:  perl(HTML::Parser)
Requires:       perl(HTML::ElementTable) >= 1.16
Requires:       perl(HTML::Parser)
%{perl_requires}

%description
HTML::TableExtract is a subclass of HTML::Parser that serves to extract the
information from tables of interest contained within an HTML document. The
information from each extracted table is stored in table objects. Tables
can be extracted as text, HTML, or HTML::ElementTable structures (for
in-place editing or manipulation).

There are currently four constraints available to specify which tables you
would like to extract from a document: _Headers_, _Depth_, _Count_, and
_Attributes_.

_Headers_, the most flexible and adaptive of the techniques, involves
specifying text in an array that you expect to appear above the data in the
tables of interest. Once all headers have been located in a row of that
table, all further cells beneath the columns that matched your headers are
extracted. All other columns are ignored: think of it as vertical slices
through a table. In addition, TableExtract automatically rearranges each
row in the same order as the headers you provided. If you would like to
disable this, set _automap_ to 0 during object creation, and instead rely
on the column_map() method to find out the order in which the headers were
found. Furthermore, TableExtract will automatically compensate for cell
span issues so that columns are really the same columns as you would
visually see in a browser. This behavior can be disabled by setting the
_gridmap_ parameter to 0. HTML is stripped from the entire textual content
of a cell before header matches are attempted -- unless the _keep_html_
parameter was enabled.

_Depth_ and _Count_ are more specific ways to specify tables in relation to
one another. _Depth_ represents how deeply a table resides in other tables.
The depth of a top-level table in the document is 0. A table within a
top-level table has a depth of 1, and so on. Each depth can be thought of
as a layer; tables sharing the same depth are on the same layer. Within
each of these layers, _Count_ represents the order in which a table was
seen at that depth, starting with 0. Providing both a _depth_ and a _count_
will uniquely specify a table within a document.

_Attributes_ match based on the attributes of the html <table> tag, for
example, border widths or background color.

Each of the _Headers_, _Depth_, _Count_, and _Attributes_ specifications
are cumulative in their effect on the overall extraction. For instance, if
you specify only a _Depth_, then you get all tables at that depth (note
that these could very well reside in separate higher- level tables
throughout the document since depth extends across tables). If you specify
only a _Count_, then the tables at that _Count_ from all depths are
returned (i.e., the _n_th occurrence of a table at each depth). If you only
specify _Headers_, then you get all tables in the document containing those
column headers. If you have specified multiple constraints of _Headers_,
_Depth_, _Count_, and _Attributes_, then each constraint has veto power
over whether a particular table is extracted.

If no _Headers_, _Depth_, _Count_, or _Attributes_ are specified, then all
tables match.

When extracting only text from tables, the text is decoded with
HTML::Entities by default; this can be disabled by setting the _decode_
parameter to 0.

%prep
%autosetup -p1 -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes examples.html README
%license LICENSE

%changelog
