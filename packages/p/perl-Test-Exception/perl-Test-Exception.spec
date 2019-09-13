#
# spec file for package perl-Test-Exception
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


Name:           perl-Test-Exception
Version:        0.430000
Release:        0
%define cpan_version 0.43
Provides:       perl(Test::Exception) = 0.430000
%define cpan_name Test-Exception
Summary:        Test exception-based code
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Exception/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sub::Uplevel) >= 0.18
BuildRequires:  perl(Test::Builder) >= 0.7
BuildRequires:  perl(Test::Builder::Tester) >= 1.07
BuildRequires:  perl(Test::More) >= 0.7
Requires:       perl(Sub::Uplevel) >= 0.18
Requires:       perl(Test::Builder) >= 0.7
Requires:       perl(Test::Builder::Tester) >= 1.07
%{perl_requires}

%description
This module provides a few convenience methods for testing exception based
code. It is built with Test::Builder and plays happily with Test::More and
friends.

If you are not already familiar with Test::More now would be the time to go
take a look.

You can specify the test plan when you 'use Test::Exception' in the same
way as 'use Test::More'. See Test::More for details.

NOTE: Test::Exception only checks for exceptions. It will ignore other
methods of stopping program execution - including exit(). If you have an
exit() in evalled code Test::Exception will not catch this with any of its
testing functions.

NOTE: This module uses Sub::Uplevel and relies on overriding
'CORE::GLOBAL::caller' to hide your test blocks from the call stack. If
this use of global overrides concerns you, the Test::Fatal module offers a
more minimalist alternative.

* *throws_ok*

Tests to see that a specific exception is thrown. throws_ok() has two
forms:

  throws_ok BLOCK REGEX, TEST_DESCRIPTION
  throws_ok BLOCK CLASS, TEST_DESCRIPTION

In the first form the test passes if the stringified exception matches the
give regular expression. For example:

    throws_ok { read_file( 'unreadable' ) } qr/No file/, 'no file';

If your perl does not support 'qr//' you can also pass a regex-like string,
for example:

    throws_ok { read_file( 'unreadable' ) } '/No file/', 'no file';

The second form of throws_ok() test passes if the exception is of the same
class as the one supplied, or a subclass of that class. For example:

    throws_ok { $foo->bar } "Error::Simple", 'simple error';

Will only pass if the 'bar' method throws an Error::Simple exception, or a
subclass of an Error::Simple exception.

You can get the same effect by passing an instance of the exception you
want to look for. The following is equivalent to the previous example:

    my $SIMPLE = Error::Simple->new;
    throws_ok { $foo->bar } $SIMPLE, 'simple error';

Should a throws_ok() test fail it produces appropriate diagnostic messages.
For example:

    not ok 3 - simple error
    #     Failed test (test.t at line 48)
    # expecting: Error::Simple exception
    # found: normal exit

Like all other Test::Exception functions you can avoid prototypes by
passing a subroutine explicitly:

    throws_ok( sub {$foo->bar}, "Error::Simple", 'simple error' );

A true value is returned if the test succeeds, false otherwise. On exit $@
is guaranteed to be the cause of death (if any).

A description of the exception being checked is used if no optional test
description is passed.

NOTE: Remember when you 'die $string_without_a_trailing_newline' perl will
automatically add the current script line number, input line number and a
newline. This will form part of the string that throws_ok regular
expressions match against.

* *dies_ok*

Checks that a piece of code dies, rather than returning normally. For
example:

    sub div {
        my ( $a, $b ) = @_;
        return $a / $b;
    };

    dies_ok { div( 1, 0 ) } 'divide by zero detected';

    # or if you don't like prototypes
    dies_ok( sub { div( 1, 0 ) }, 'divide by zero detected' );

A true value is returned if the test succeeds, false otherwise. On exit $@
is guaranteed to be the cause of death (if any).

Remember: This test will pass if the code dies for any reason. If you care
about the reason it might be more sensible to write a more specific test
using throws_ok().

The test description is optional, but recommended.

* *lives_ok*

Checks that a piece of code doesn't die. This allows your test script to
continue, rather than aborting if you get an unexpected exception. For
example:

    sub read_file {
        my $file = shift;
        local $/;
        open my $fh, '<', $file or die "open failed ($!)\n";
        $file = <FILE>;
        return $file;
    };

    my $file;
    lives_ok { $file = read_file('test.txt') } 'file read';

    # or if you don't like prototypes
    lives_ok( sub { $file = read_file('test.txt') }, 'file read' );

Should a lives_ok() test fail it produces appropriate diagnostic messages.
For example:

    not ok 1 - file read
    #     Failed test (test.t at line 15)
    # died: open failed (No such file or directory)

A true value is returned if the test succeeds, false otherwise. On exit $@
is guaranteed to be the cause of death (if any).

The test description is optional, but recommended.

* *lives_and*

Run a test that may throw an exception. For example, instead of doing:

  my $file;
  lives_ok { $file = read_file('answer.txt') } 'read_file worked';
  is $file, "42", 'answer was 42';

You can use lives_and() like this:

  lives_and { is read_file('answer.txt'), "42" } 'answer is 42';
  # or if you don't like prototypes
  lives_and(sub {is read_file('answer.txt'), "42"}, 'answer is 42');

Which is the same as doing

  is read_file('answer.txt'), "42\n", 'answer is 42';

unless 'read_file('answer.txt')' dies, in which case you get the same kind
of error as lives_ok()

  not ok 1 - answer is 42
  #     Failed test (test.t at line 15)
  # died: open failed (No such file or directory)

A true value is returned if the test succeeds, false otherwise. On exit $@
is guaranteed to be the cause of death (if any).

The test description is optional, but recommended.

%prep
%setup -q -n %{cpan_name}-%{cpan_version}
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
%doc Changes

%changelog
