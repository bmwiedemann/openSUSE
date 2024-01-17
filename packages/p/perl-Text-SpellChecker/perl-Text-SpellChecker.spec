#
# spec file for package perl-Text-SpellChecker
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


%define cpan_name Text-SpellChecker
Name:           perl-Text-SpellChecker
Version:        0.14
Release:        0
Summary:        OO interface for spell-checking a block of text
License:        Artistic-1.0 OR GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-SpellChecker/
Source:         http://www.cpan.org/authors/id/B/BD/BDUGGAN/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Text::Hunspell)
Requires:       perl(Text::Hunspell)
BuildArch:      noarch
%{perl_requires}

%description
This module is a thin layer above either Text::Aspell or Text::Hunspell
(preferring the latter if available), and allows one to spellcheck a body
of text.

Whereas Text::(Hu|A)spell deals with words, Text::Spellchecker deals with
blocks of text. For instance, we provide methods for iterating through the
text, serializing the object (thus remembering where we left off), and
highlighting the current misspelled word within the text.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
