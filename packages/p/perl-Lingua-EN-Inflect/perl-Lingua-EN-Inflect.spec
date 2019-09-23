#
# spec file for package perl-Lingua-EN-Inflect
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Lingua-EN-Inflect
Version:        1.904
Release:        0
%define cpan_name Lingua-EN-Inflect
Summary:        Convert singular to plural. Select "a" or "an"
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
*[_Note:_ This module is strictly in maintenance mode now. Take a look at
the newer Lingua::EN::Inflexion module, which offers a cleaner and more
convenient interface, has many more features (including plural->singular
inflexions), and is also much better tested. If you have existing code that
relies on Lingua::EN::Inflect, see the section of the documentation
entitled "CONVERTING FROM LINGUA::EN::INFLECT". ]*

The exportable subroutines of Lingua::EN::Inflect provide plural
inflections, "a"/"an" selection for English words, and manipulation of
numbers as words

Plural forms of all nouns, most verbs, and some adjectives are provided.
Where appropriate, "classical" variants (for example: "brother" ->
"brethren", "dogma" -> "dogmata", etc.) are also provided.

Pronunciation-based "a"/"an" selection is provided for all English words,
and most initialisms.

It is also possible to inflect numerals (1,2,3) to ordinals (1st, 2nd, 3rd)
and to English words ("one", "two", "three).

In generating these inflections, Lingua::EN::Inflect follows the Oxford
English Dictionary and the guidelines in Fowler's Modern English Usage,
preferring the former where the two disagree.

The module is built around standard British spelling, but is designed to
cope with common American variants as well. Slang, jargon, and other
English dialects are _not_ explicitly catered for.

Where two or more inflected forms exist for a single word (typically a
"classical" form and a "modern" form), Lingua::EN::Inflect prefers the more
common form (typically the "modern" one), unless "classical" processing has
been specified (see "MODERN VS CLASSICAL INFLECTIONS").

%prep
%setup -q -n %{cpan_name}-%{version}
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
%doc Changes README

%changelog
