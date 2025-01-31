#
# spec file for package perl-IO-Interactive
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name IO-Interactive
Name:           perl-IO-Interactive
Version:        1.26.0
Release:        0
# 1.026 -> normalize -> 1.26.0
%define cpan_version 1.026
License:        Artistic-2.0
Summary:        Utilities for interactive I/O
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 1
Provides:       perl(IO::Interactive) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides three utility subroutines that make it easier to
develop interactive applications.

The 'ARGV' filehandle, the one that '<>' or an empty 'readline()' uses, has
various magic associated with it. It's not actually opened until you try to
read from it. Checking '-t ARGV' before you've tried to read from it might
give you the wrong answer. Not only that, you might not read from 'ARGV'.
If the value in '@ARGV' is the magic filename '-' (a convention to mean the
standard filehandle for input or output), 'ARGV' might actually be 'STDIN'.
You don't want to think about all of this. This module is discussed in
_Perl Best Practices_ on page 218. Also see the 'ARGV' entry in perlvar and
the 'readline' entry in perlfunc.

* 'is_interactive()'

This subroutine returns true if '*ARGV' and the currently selected
filehandle (usually '*STDOUT') are connected to the terminal. The test is
considerably more sophisticated than:

    -t *ARGV && -t *STDOUT

as it takes into account the magic behaviour of '*ARGV'.

You can also pass 'is_interactive' a writable filehandle, in which case it
requires that filehandle be connected to a terminal (instead of the
currently selected). The usual suspect here is '*STDERR':

    if ( is_interactive(*STDERR) ) {
        carp $warning;
    }

Note that 'is_interactive' may return true in a Windows Scheduled Task. See
Github #6 (https://github.com/briandfoy/io-interactive/issues/6).

* 'interactive()'

This subroutine returns '*STDOUT' if 'is_interactive' is true. If
'is_interactive()' is false, 'interactive' returns a filehandle that does
not print.

This makes it easy to create applications that print out only when the
application is interactive:

    print {interactive} "Please enter a value: ";
    my $value = <>;

You can also pass 'interactive' a writable filehandle, in which case it
writes to that filehandle if it is connected to a terminal (instead of
writing to '*STDOUT'). Once again, the usual suspect is '*STDERR':

    print {interactive(*STDERR)} $warning;

* 'busy {...}'

This subroutine takes a block as its single argument and executes that
block. Whilst the block is executed, '*ARGV' is temporarily replaced by a
closed filehandle. That is, no input from '*ARGV' is possible in a 'busy'
block. Furthermore, any attempts to send input into the 'busy' block
through '*ARGV' is intercepted and a warning message is printed to
'*STDERR'. The 'busy' call returns a filehandle that contains the
intercepted input.

A 'busy' block is therefore useful to prevent attempts at input when the
program is busy at some non-interactive task.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples SECURITY.md
%license LICENSE

%changelog
