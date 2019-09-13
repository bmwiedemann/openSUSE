#
# spec file for package perl-Text-Unidecode
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Unidecode
Version:        1.30
Release:        0
%define cpan_name Text-Unidecode
Summary:        Plain Ascii Transliterations of Unicode Text
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Unidecode/
Source0:        http://www.cpan.org/authors/id/S/SB/SBURKE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
It often happens that you have non-Roman text data in Unicode, but you
can't display it-- usually because you're trying to show it to a user via
an application that doesn't support Unicode, or because the fonts you need
aren't accessible. You could represent the Unicode characters as "???????"
or "\15BA\15A0\1610...", but that's nearly useless to the user who actually
wants to read what the text says.

What Text::Unidecode provides is a function, 'unidecode(...)' that takes
Unicode data and tries to represent it in US-ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at _transliteration_-- i.e.,
conveying, in Roman letters, the pronunciation expressed by the text in
some other writing system. (See the example in the synopsis.)

NOTE:

To make sure your perldoc/Pod viewing setup for viewing this page is
working: The six-letter word "résumé" should look like "resume" with an "/"
accent on each "e".

For further tests, and help if that doesn't work, see below, A POD ENCODING
TEST.

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog LICENSE README TODO.txt

%changelog
