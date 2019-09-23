#
# spec file for package perl-Data-Dump
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


Name:           perl-Data-Dump
Version:        1.23
Release:        0
%define cpan_name Data-Dump
Summary:        Pretty printing of data structures
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Dump/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provide a few functions that traverse their argument and
produces a string as its result. The string contains Perl code that, when
'eval'ed, produces a deep copy of the original arguments.

The main feature of the module is that it strives to produce output that is
easy to read. Example:

    @a = (1, [2, 3], {4 => 5});
    dump(@a);

Produces:

    "(1, [2, 3], { 4 => 5 })"

If you dump just a little data, it is output on a single line. If you dump
data that is more complex or there is a lot of it, line breaks are
automatically added to keep it easy to read.

The following functions are provided (only the dd* functions are exported
by default):

* dump( ... )

* pp( ... )

  Returns a string containing a Perl expression. If you pass this string to
  Perl's built-in eval() function it should return a copy of the arguments
  you passed to dump().

  If you call the function with multiple arguments then the output will be
  wrapped in parenthesis "( ..., ... )". If you call the function with a
  single argument the output will not have the wrapping. If you call the
  function with a single scalar (non-reference) argument it will just
  return the scalar quoted if needed, but never break it into multiple
  lines. If you pass multiple arguments or references to arrays of hashes
  then the return value might contain line breaks to format it for easier
  reading. The returned string will never be "\n" terminated, even if
  contains multiple lines. This allows code like this to place the
  semicolon in the expected place:

     print '$obj = ', dump($obj), ";\n";

  If dump() is called in void context, then the dump is printed on STDERR
  and then "\n" terminated. You might find this useful for quick debug
  printouts, but the dd*() functions might be better alternatives for this.

  There is no difference between dump() and pp(), except that dump() shares
  its name with a not-so-useful perl builtin. Because of this some might
  want to avoid using that name.

* quote( $string )

  Returns a quoted version of the provided string.

  It differs from 'dump($string)' in that it will quote even numbers and
  not try to come up with clever expressions that might shorten the output.
  If a non-scalar argument is provided then it's just stringified instead
  of traversed.

* dd( ... )

* ddx( ... )

  These functions will call dump() on their argument and print the result
  to STDOUT (actually, it's the currently selected output handle, but
  STDOUT is the default for that).

  The difference between them is only that ddx() will prefix the lines it
  prints with "# " and mark the first line with the file and line number
  where it was called. This is meant to be useful for debug printouts of
  state within programs.

* dumpf( ..., \&filter )

  Short hand for calling the dump_filtered() function of the
  Data::Dump::Filtered manpage. This works like dump(), but the last
  argument should be a filter callback function. As objects are visited the
  filter callback is invoked and it can modify how the objects are dumped.

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
