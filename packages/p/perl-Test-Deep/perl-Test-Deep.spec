#
# spec file for package perl-Test-Deep
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Deep
Version:        1.128
Release:        0
%define cpan_name Test-Deep
Summary:        Extremely flexible deep comparison
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Deep/
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester) >= 0.04
%{perl_requires}
# MANUAL BEGIN
# necessary because Test::Deep::NoTest does "require Test::Builder"
Requires:       perl-Test-Simple
# MANUAL END

%description
If you don't know anything about automated testing in Perl then you should
probably read about Test::Simple and Test::More before preceding.
Test::Deep uses the Test::Builder framework.

Test::Deep gives you very flexible ways to check that the result you got is
the result you were expecting. At its simplest it compares two structures
by going through each level, ensuring that the values match, that arrays
and hashes have the same elements and that references are blessed into the
correct class. It also handles circular data structures without getting
caught in an infinite loop.

Where it becomes more interesting is in allowing you to do something
besides simple exact comparisons. With strings, the 'eq' operator checks
that 2 strings are exactly equal but sometimes that's not what you want.
When you don't know exactly what the string should be but you do know some
things about how it should look, 'eq' is no good and you must use pattern
matching instead. Test::Deep provides pattern matching for complex data
structures

Test::Deep has *_a lot_* of exports. See EXPORTS below.

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
%doc Changes README TODO

%changelog
