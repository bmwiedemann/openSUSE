#
# spec file for package perl-Sort-Naturally
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Sort-Naturally
Version:        1.03
Release:        0
%define cpan_name Sort-Naturally
Summary:        sort lexically, but sort numeral parts numerically
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sort-Naturally/
Source:         http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Sort::Naturally)
%{perl_requires}

%description
This module exports two functions, 'nsort' and 'ncmp'; they are used in
implementing my idea of a "natural sorting" algorithm. Under natural
sorting, numeric substrings are compared numerically, and other
word-characters are compared lexically.

This is the way I define natural sorting:

* *

  Non-numeric word-character substrings are sorted lexically,
  case-insensitively: "Foo" comes between "fish" and "fowl".

* *

  Numeric substrings are sorted numerically: "100" comes after "20", not
  before.

* *

  \W substrings (neither words-characters nor digits) are _ignored_.

* *

  Our use of \w, \d, \D, and \W is locale-sensitive: Sort::Naturally uses a
  'use locale' statement.

* *

  When comparing two strings, where a numeric substring in one place is
  _not_ up against a numeric substring in another, the non-numeric always
  comes first. This is fudged by reading pretending that the lack of a
  number substring has the value -1, like so:

    foo       =>  "foo",  -1
    foobar    =>  "foo",  -1,  "bar"
    foo13     =>  "foo",  13,
    foo13xyz  =>  "foo",  13,  "xyz"

  That's so that "foo" will come before "foo13", which will come before
  "foobar".

* *

  The start of a string is exceptional: leading non-\W (non-word,
  non-digit) components are are ignored, and numbers come _before_ letters.

* *

  I define "numeric substring" just as sequences matching m/\d+/ --
  scientific notation, commas, decimals, etc., are not seen. If your data
  has thousands separators in numbers ("20,000 Leagues Under The Sea" or
  "20.000 lieues sous les mers"), consider stripping them before feeding
  them to 'nsort' or 'ncmp'.

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
%doc ChangeLog README

%changelog
