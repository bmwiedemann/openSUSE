#
# spec file for package perl-Lingua-Translit
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


Name:           perl-Lingua-Translit
Version:        0.28
Release:        0
%define cpan_name Lingua-Translit
Summary:        Transliterates Text Between Writing Systems
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-Translit/
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALINKE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Lingua::Translit can be used to convert text from one writing system to
another, based on national or international transliteration tables. Where
possible a reverse transliteration is supported.

The term 'transliteration' describes the conversion of text from one
writing system or alphabet to another one. The conversion is ideally
unique, mapping one character to exactly one character, so the original
spelling can be reconstructed. Practically this is not always the case and
one single letter of the original alphabet can be transcribed as two, three
or even more letters.

Furthermore there is more than one transliteration scheme for one writing
system. Therefore it is an important and necessary information, which
scheme will be or has been used to transliterate a text, to work
integrative and be able to reconstruct the original data.

Reconstruction is a problem though for non-unique transliterations, if no
language specific knowledge is available as the resulting clusters of
letters may be ambiguous. For example, the Greek character "PSI" maps to
"ps", but "ps" could also result from the sequence "PI", "SIGMA" since "PI"
maps to "p" and "SIGMA" maps to s. If a transliteration table leads to
ambiguous conversions, the provided table cannot be used reverse.

Otherwise the table can be used in both directions, if appreciated. So if
ISO 9 is originally created to convert Cyrillic letters to the Latin
alphabet, the reverse transliteration will transform Latin letters to
Cyrillic.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes README translit

%changelog
