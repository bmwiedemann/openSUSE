#
# spec file for package perl-Test-Base
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


Name:           perl-Test-Base
Version:        0.89
Release:        0
%define cpan_name Test-Base
Summary:        Data Driven Testing Framework
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Base/
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Diff) >= 1.15
BuildRequires:  perl(Spiffy) >= 0.40
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Diff) >= 0.35
Requires:       perl(Spiffy) >= 0.40
Requires:       perl(Test::More) >= 0.88
Recommends:     perl(Test::Deep)
%{perl_requires}

%description
Testing is usually the ugly part of Perl module authoring. Perl gives you a
standard way to run tests with Test::Harness, and basic testing primitives
with Test::More. After that you are pretty much on your own to develop a
testing framework and philosophy. Test::More encourages you to make your
own framework by subclassing Test::Builder, but that is not trivial.

Test::Base gives you a way to write your own test framework base class that
_is_ trivial. In fact it is as simple as two lines:

    package MyTestFramework;
    use Test::Base -Base;

A module called 'MyTestFramework.pm' containing those two lines, will give
all the power of Test::More and all the power of Test::Base to every test
file that uses it. As you build up the capabilities of 'MyTestFramework',
your tests will have all of that power as well.

'MyTestFramework' becomes a place for you to put all of your reusable
testing bits. As you write tests, you will see patterns and duplication,
and you can "upstream" them into 'MyTestFramework'. Of course, you don't
have to subclass Test::Base at all. You can use it directly in many
applications, including everywhere you would use Test::More.

Test::Base concentrates on offering reusable data driven patterns, so that
you can write tests with a minimum of code. At the heart of all testing you
have inputs, processes and expected outputs. Test::Base provides some clean
ways for you to express your input and expected output data, so you can
spend your

      time focusing on that rather than your code scaffolding.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
