#
# spec file for package perl-Text-Brew
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


Name:           perl-Text-Brew
Version:        0.02
Release:        0
%define cpan_name Text-Brew
Summary:        An implementation of the Brew edit distance
License:        GPL-2.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Brew/
Source:         http://www.cpan.org/authors/id/K/KC/KCIVEY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Text::Brew)
%{perl_requires}

%description
This module implements the Brew edit distance that is very close to the
dynamic programming technique used for the Wagner-Fischer (and so for the
Levenshtein) edit distance. Please look at the module references below. For
more information about the Brew edit distance see:
<http://ling.ohio-state.edu/~cbrew/795M/string-distance.html>

The difference here is that you have separated costs for the DELetion and
INSertion operations (but with the default to 1 for both, you obtain the
Levenshtein edit distance). But the most interesting feature is that you
can obtain the description of the edits needed to transform the first
string into the second one (not vice versa: here DELetions are separated
from INSertions). The difference from the original algorithm by Chris Brew
is that I have added the SUBST operation, making it different from MATCH
operation.

The symbols used here are:

 INITIAL that is the INITIAL operation (i.e. NO operation)
 MATCH	 that is the MATCH operation (0 is the default cost)
 SUBST	 that is the SUBSTitution operation (1 is the default cost)
 DEL	 that is the DELetion operation (1 is the default cost)
 INS	 that is the INSertion operation (1 is the default cost)

and you can change the default costs (see below).

You can make INS and DEL the same operation in a simple way:

 1) give both the same cost
 2) change the output string DEL to INS/DEL (o whatever)
 3) change the output string INS to INS/DEL (o whatever)

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
%doc Changes README

%changelog
