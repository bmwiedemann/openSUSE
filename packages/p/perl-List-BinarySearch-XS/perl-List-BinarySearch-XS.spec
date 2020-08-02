#
# spec file for package perl-List-BinarySearch-XS
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


%define cpan_name List-BinarySearch-XS
Name:           perl-List-BinarySearch-XS
Version:        0.09
Release:        0
Summary:        Binary Search a sorted array with XS routines.
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source:         https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.98
#BuildRequires: perl(List::BinarySearch::XS)
#BuildRequires: perl(Test::Kwalitee)
#BuildRequires: perl(Test::Perl::Critic)
%{perl_requires}

%description
A binary search searches _sorted_ lists using a divide and conquer
technique. On each iteration the search domain is cut in half, until the
result is found. The computational complexity of a binary search is O(log
n).

This module implements several Binary Search algorithms using XS code for
optimal performance. You are free to use this module directly, or as a
plugin for the more general List::BinarySearch.

The binary search algorithm implemented in this module is known as a
_Deferred Detection_ Binary Search. Deferred Detection provides *stable
searches*. Stable binary search algorithms have the following
characteristics, contrasted with their unstable binary search cousins:

* * In the case of non-unique keys, a stable binary search will always
  return the lowest-indexed matching element.  An unstable binary search
  would
  return the first one found, which may not be the chronological first.

* * Best and worst case time complexity is always O(log n).  Unstable
  searches may stop once the target is found, but in the worst case are
  still
  O(log n).  In practical terms, this difference is usually not meaningful.

* * Stable binary searches only require one relational comparison of a
  given pair of data elements per iteration, where unstable binary searches
  require two comparisons per iteration.

* * The net result is that although an unstable binary search might have
  better "best case" performance, the fact that a stable binary search gets
  away
  with fewer comparisons per iteration gives it better performance in the
  worst
  case, and approximately equal performance in the average case. By trading
  away
  slightly better "best case" performance, the stable search gains the
  guarantee
  that the element found will always be the lowest-indexed element in a
  range of
  non-unique keys.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
