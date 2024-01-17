#
# spec file for package perl-Test-Number-Delta
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Number-Delta
Version:        1.060000
Release:        0
%define cpan_version 1.06
Provides:       perl(Test::Number::Delta) = 1.060000
%define cpan_name Test-Number-Delta
Summary:        Compare the difference between numbers against a given tolerance
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Number-Delta/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
At some point or another, most programmers find they need to compare
floating-point numbers for equality. The typical idiom is to test if the
absolute value of the difference of the numbers is within a desired
tolerance, usually called epsilon. This module provides such a function for
use with the Test::More manpage. Usage is similar to other test functions
described in the Test::More manpage. Semantically, the 'delta_within'
function replaces this kind of construct:

 ok ( abs($p - $q) < $epsilon, '$p is equal to $q' ) or
     diag "$p is not equal to $q to within $epsilon";

While there's nothing wrong with that construct, it's painful to type it
repeatedly in a test script. This module does the same thing with a single
function call. The 'delta_ok' function is similar, but either uses a global
default value for epsilon or else calculates a 'relative' epsilon on the
fly so that epsilon is scaled automatically to the size of the arguments to
'delta_ok'. Both functions are exported automatically.

Because checking floating-point equality is not always reliable, it is not
possible to check the 'equal to' boundary of 'less than or equal to
epsilon'. Therefore, Test::Number::Delta only compares if the absolute
value of the difference is *less than* epsilon (for equality tests) or
*greater than* epsilon (for inequality tests).

%prep
%setup -q -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING.mkdn LICENSE README

%changelog
