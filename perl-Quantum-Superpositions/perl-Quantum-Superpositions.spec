#
# spec file for package perl-Quantum-Superpositions
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


Name:           perl-Quantum-Superpositions
Version:        2.03
Release:        0
%define cpan_name Quantum-Superpositions
Summary:        QM-like superpositions in Perl
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Quantum-Superpositions/
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEMBARK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Multimethods)
Requires:       perl(Class::Multimethods)
%{perl_requires}

%description
The Quantum::Superpositions module adds two new operators to Perl: 'any'
and 'all'.

Each of these operators takes a list of values (states) and superimposes
them into a single scalar value (a superposition), which can then be stored
in a standard scalar variable.

The 'any' and 'all' operators produce two distinct kinds of superposition.
The 'any' operator produces a disjunctive superposition, which may
(notionally) be in any one of its states at any time, according to the
needs of the algorithm that uses it.

In contrast, the 'all' operator creates a conjunctive superposition, which
is always in every one of its states simultaneously.

Superpositions are scalar values and hence can participate in arithmetic
and logical operations just like any other type of scalar. However, when an
operation is applied to a superposition, it is applied (notionally) in
parallel to each of the states in that superposition.

For example, if a superposition of states 1, 2, and 3 is multiplied by 2:

	$result = any(1,2,3) * 2;

the result is a superposition of states 2, 4, and 6. If that result is then
compared with the value 4:

	if ($result == 4) { print "fore!" }

then the comparison also returns a superposition: one that is both true and
false (since the equality is true for one of the states of '$result' and
false for the other two).

Of course, a value that is both true and false is of no use in an 'if'
statement, so some mechanism is needed to decide which superimposed boolean
state should take precedence.

This mechanism is provided by the two types of superposition available. A
disjunctive superposition is true if any of its states is true, whereas a
conjunctive superposition is true only if all of its states are true.

Thus the previous example does print "fore!", since the 'if' condition is
equivalent to:

	if (any(2,4,6) == 4)...

It suffices that any one of 2, 4, or 6 is equal to 4, so the condition is
true and the 'if' block executes.

On the other hand, had the control statement been:

        if (all(2,4,6) == 4)...

the condition would fail, since it is not true that all of 2, 4, and 6 are
equal to 4.

Operations are also possible between two superpositions:

        if (all(1,2,3)*any(5,6) < 21) 
                { print "no alcohol"; }
                
        if (all(1,2,3)*any(5,6) < 18)
                { print "no entry"; }
                
        if (any(1,2,3)*all(5,6) < 18)
                { print "under-age" }

In this example, the string "no alcohol" is printed because the
superposition produced by the multiplication is the Cartesian product of
the respective states of the two operands: 'all(5,6,10,12,15,18)'. Since
all of these resultant states are less that 21, the condition is true. In
contrast, the string "no entry" is not printed, because not all the
product's states are less than 18.

Note that the type of the first operand determines the type of the result
of an operation. Hence the third string -- "underage" -- is printed,
because multiplying a disjunctive superposition by a conjunctive
superposition produces a result that is disjunctive:
'any(5,6,10,12,15,18)'. The condition of the 'if' statement asks whether
any of these values is less than 18, which is true.

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
%doc Changes

%changelog
