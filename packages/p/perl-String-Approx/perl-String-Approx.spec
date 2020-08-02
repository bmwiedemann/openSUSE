#
# spec file for package perl-String-Approx
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-String-Approx
Version:        3.28
Release:        0
%define cpan_name String-Approx
Summary:        Perl extension for approximate matching (fuzzy matching)
License:        LGPL-2.0 OR Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/String-Approx/
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
String::Approx lets you match and substitute strings approximately. With
this you can emulate errors: typing errorrs, speling errors, closely
related vocabularies (colour color), genetic mutations (GAG ACT),
abbreviations (McScot, MacScot).

NOTE: String::Approx suits the task of *string matching*, not *string
comparison*, and it works for *strings*, not for *text*.

If you want to compare strings for similarity, you probably just want the
Levenshtein edit distance (explained below), the Text::Levenshtein and
Text::LevenshteinXS modules in CPAN. See also Text::WagnerFischer and
Text::PhraseDistance. (There are functions for this in String::Approx, e.g.
adist(), but their results sometimes differ from the bare Levenshtein et
al.)

If you want to compare things like text or source code, consisting of
*words* or *tokens* and *phrases* and *sentences*, or *expressions* and
*statements*, you should probably use some other tool than String::Approx,
like for example the standard UNIX diff(1) tool, or the Algorithm::Diff
module from CPAN.

The measure of *approximateness* is the _Levenshtein edit distance_. It is
the total number of "edits": insertions,

	word world

deletions,

	monkey money

and substitutions

	sun fun

required to transform a string to another string. For example, to transform
_"lead"_ into _"gold"_, you need three edits:

	lead gead goad gold

The edit distance of "lead" and "gold" is therefore three, or 75%.

*String::Approx* uses the Levenshtein edit distance as its measure, but
String::Approx is not well-suited for comparing strings of different
length, in other words, if you want a "fuzzy eq", see above. String::Approx
is more like regular expressions or index(), it finds substrings that are
close matches.>

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog COPYRIGHT COPYRIGHT.agrep LGPL PROBLEMS README README.apse
%license Artistic

%changelog
