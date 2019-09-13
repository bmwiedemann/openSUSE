#
# spec file for package perl-Test-MockRandom
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


Name:           perl-Test-MockRandom
Version:        1.01
Release:        0
%define cpan_name Test-MockRandom
Summary:        Replaces random number generation with non-random number generation
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-MockRandom/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(version)
%{perl_requires}

%description
This perhaps ridiculous-seeming module was created to test routines that
manipulate random numbers by providing a known output from 'rand'. Given a
list of seeds with 'srand', it will return each in turn. After seeded
random numbers are exhausted, it will always return 0. Seed numbers must be
of a form that meets the expected output from 'rand' as called with no
arguments -- i.e. they must be between 0 (inclusive) and 1 (exclusive). In
order to facilitate generating and testing a nearly-one number, this module
exports the function 'oneish', which returns a number just fractionally
less than one.

Depending on how this module is called with 'use', it will export 'rand' to
a specified package (e.g. a class being tested) effectively overriding and
intercepting calls in that package to the built-in 'rand'. It can also
override 'rand' in the current package or even globally. In all of these
cases, it also exports 'srand' and 'oneish' to the current package in order
to control the output of 'rand'. See USAGE for details.

Alternatively, this module can be used to generate objects, with each
object maintaining its own distinct seed array.

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
%doc Changes CONTRIBUTING examples LICENSE README

%changelog
