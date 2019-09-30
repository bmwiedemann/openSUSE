#
# spec file for package perl-Text-Capitalize
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


Name:           perl-Text-Capitalize
Version:        1.5
Release:        0
%define cpan_name Text-Capitalize
Summary:        Capitalize strings ("to WORK AS titles" becomes "To Work as Titles")
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOOM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
%{perl_requires}

%description
Text::Capitalize provides some routines for *title-like* formatting of
strings.

The simple *capitalize* function just makes the inital character of each
word uppercase, and forces the rest to lowercase.

The *capitalize_title* function applies English title case rules (discussed
below) where only the "important" words are supposed to be capitalized.
There are also some customization features provided to allow the user to
choose variant rules.

Comparing *capitalize* and *captialize_title*:

  Input:             "lost watches of splitsville"
  capitalize:        "Lost Watches Of Splitsville"
  capitalize_title:  "Lost Watches of Splitsville"

Some examples of formatting with *capitalize_title*:

  Input:             "KiLLiNG TiMe"
  capitalize_title:  "Killing Time"

  Input:             "we have come to wound the autumnal city"
  capitalize_title:  "We Have Come to Wound the Autumnal City"

  Input:             "ask for whom they ask for"
  captialize_title:  "Ask for Whom They Ask For"

Text::Capitalize also provides some functions for special effects such as
*scramble_case*, which typically would be used for this sort of
transformation:

  Input:            "get whacky"
  scramble_case:    "gET wHaCkY"  (or something similar)

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
