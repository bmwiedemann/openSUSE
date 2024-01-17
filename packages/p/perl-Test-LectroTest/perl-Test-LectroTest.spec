#
# spec file for package perl-Test-LectroTest
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


Name:           perl-Test-LectroTest
Version:        0.5001
Release:        0
%define cpan_name Test-LectroTest
Summary:        Easy, automatic, specification-based tests
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-LectroTest/
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMOERTEL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides a simple (yet full featured) interface to LectroTest,
an automated, specification-based testing system for Perl. To use it,
declare properties that specify the expected behavior of your software.
LectroTest then checks your software to see whether those properties hold.

Declare properties using the 'Property' function, which takes a block of
code and promotes it to a Test::LectroTest::Property:

    Property {
        ##[ x <- Int, y <- Int ]##
        MyModule::my_function( $x, $y ) >= 0;
    }, name => "my_function output is non-negative" ;

The first part of the block must contain a generator-binding declaration.
For example:

        ##[  x <- Int, y <- Int  ]##

(Note the special bracketing, which is required.) This particular binding
says, "For all integers _x_ and _y_." (By the way, you aren't limited to
integers. LectroTest also gives you booleans, strings, lists, hashes, and
more, and it lets you define your own generator types. See
Test::LectroTest::Generator for more.)

The second part of the block is simply a snippet of code that makes use of
the variables we bound earlier to test whether a property holds for the
piece of software we are testing:

        MyModule::my_function( $x, $y ) >= 0;

In this case, it asserts that 'MyModule::my_function($x,$y)' returns a
non-negative result. (Yes, '$x' and '$y' refer to the same _x_ and _y_ that
we bound to the generators earlier. LectroTest automagically loads these
lexically bound Perl variables with values behind the scenes.)

*Note:* If you want to use testing assertions like 'ok' from Test::Simple
or 'is', 'like', or 'cmp_ok' from Test::More (and the related family of
Test::Builder-based testing modules), see Test::LectroTest::Compat, which
lets you mix and match LectroTest with these modules.

Finally, we give the whole Property a name, in this case "my_function
output is non-negative." It's a good idea to use a meaningful name because
LectroTest refers to properties by name in its output.

Let's take a look at the finished property specification:

    Property {
        ##[ x <- Int, y <- Int ]##
        MyModule::my_function( $x, $y ) >= 0;
    }, name => "my_function output is non-negative" ;

It says, "For all integers _x_ and _y_, we assert that my_function's output
is non-negative."

To check whether this property holds, simply put it in a Perl program that
uses the Test::LectroTest module. (See the SYNOPSIS for an example.) When
you run the program, LectroTest will load the property (and any others in
the file) and check it by running random trials against the software you're
testing.

*Note:* If you want to place LectroTest property checks into a test plan
managed by Test::Builder-based modules such as Test::Simple or Test::More,
see Test::LectroTest::Compat.

If LectroTest is able to "break" your software during the property check,
it will emit a counterexample to your property's assertions and stop. You
can plug the counterexample back into your software to debug the problem.
(You might also want to add the counterexample to a list of regression
tests.)

A successful LectroTest looks like this:

  1..1
  ok 1 - 'my_function output is non-negative' (1000 attempts)

On the other hand, if you're not so lucky:

  1..1
  not ok 1 - 'my_function output is non-negative' falsified \
      in 324 attempts
  # Counterexample:
  # $x = -34
  # $y = 0

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
%doc buildrpm Changes checkpods README tex THANKS TODO
%license LICENSE

%changelog
