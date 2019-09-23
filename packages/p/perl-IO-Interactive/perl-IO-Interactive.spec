#
# spec file for package perl-IO-Interactive
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


Name:           perl-IO-Interactive
Version:        1.022
Release:        0
%define cpan_name IO-Interactive
Summary:        Utilities for interactive I/O
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Interactive/
Source0:        http://www.cpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
%{perl_requires}

%description
This module provides three utility subroutines that make it easier to
develop interactive applications...

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
%doc Changes examples LICENSE

%changelog
