#
# spec file for package perl-Switch
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Switch
Version:        2.17
Release:        0
%define cpan_name Switch
Summary:        A switch statement for Perl, do not use if you can use given/when
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Switch/
Source:         http://www.cpan.org/authors/id/C/CH/CHORNY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Text::Balanced) >= 2
Requires:       perl(Text::Balanced) >= 2
%{perl_requires}

%description
The Switch.pm module implements a generalized case mechanism that covers
most (but not all) of the numerous possible combinations of switch and case
values described above.

The module augments the standard Perl syntax with two new control
statements: 'switch' and 'case'. The 'switch' statement takes a single
scalar argument of any type, specified in parentheses. 'switch' stores this
value as the current switch value in a (localized) control variable. The
value is followed by a block which may contain one or more Perl statements
(including the 'case' statement described below). The block is
unconditionally executed once the switch value has been cached.

A 'case' statement takes a single scalar argument (in mandatory parentheses
if it's a variable; otherwise the parens are optional) and selects the
appropriate type of matching between that argument and the current switch
value. The type of matching used is determined by the respective types of
the switch value and the 'case' argument, as specified in Table 1. If the
match is successful, the mandatory block associated with the 'case'
statement is executed.

In most other respects, the 'case' statement is semantically identical to
an 'if' statement. For example, it can be followed by an 'else' clause, and
can be used as a postfix statement qualifier.

However, when a 'case' block has been executed control is automatically
transferred to the statement after the immediately enclosing 'switch'
block, rather than to the next statement within the block. In other words,
the success of any 'case' statement prevents other cases in the same scope
from executing. But see the "Allowing fall-through" manpage below.

Together these two new statements provide a fully generalized case
mechanism:

        use Switch;

        # AND LATER...

        %special = ( woohoo => 1,  d'oh => 1 );

        while (<>) {
	    chomp;
            switch ($_) {
                case (%special) { print "homer\n"; }      # if $special{$_}
                case /[a-z]/i   { print "alpha\n"; }      # if $_ =~ /a-z/i
                case [1..9]     { print "small num\n"; }  # if $_ in [1..9]
                case { $_[0] >= 10 } { print "big num\n"; } # if $_ >= 10
                print "must be punctuation\n" case /\W/;  # if $_ ~= /\W/
	    }
        }

Note that 'switch'es can be nested within 'case' (or any other) blocks, and
a series of 'case' statements can try different types of matches -- hash
membership, pattern match, array intersection, simple equality, etc. --
against the same switch value.

The use of intersection tests against an array reference is particularly
useful for aggregating integral cases:

        sub classify_digit
        {
                switch ($_[0]) { case 0            { return 'zero' }
                                 case [2,4,6,8]    { return 'even' }
                                 case [1,3,5,7,9]  { return 'odd' }
                                 case /[A-F]/i     { return 'hex' }
                               }
        }

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
