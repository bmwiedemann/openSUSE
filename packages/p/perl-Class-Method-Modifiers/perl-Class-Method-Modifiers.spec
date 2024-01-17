#
# spec file for package perl-Class-Method-Modifiers
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Class-Method-Modifiers
Name:           perl-Class-Method-Modifiers
Version:        2.15
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provides Moose-like method modifiers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
Method modifiers are a convenient feature from the CLOS (Common Lisp Object
System) world.

In its most basic form, a method modifier is just a method that calls
'$self->SUPER::foo(@_)'. I for one have trouble remembering that exact
invocation, so my classes seldom re-dispatch to their base classes. Very
bad!

'Class::Method::Modifiers' provides three modifiers: 'before', 'around',
and 'after'. 'before' and 'after' are run just before and after the method
they modify, but can not really affect that original method. 'around' is
run in place of the original method, with a hook to easily call that
original method. See the MODIFIERS section for more details on how the
particular modifiers work.

One clear benefit of using 'Class::Method::Modifiers' is that you can
define multiple modifiers in a single namespace. These separate modifiers
don't need to know about each other. This makes top-down design easy. Have
a base class that provides the skeleton methods of each operation, and have
plugins modify those methods to flesh out the specifics.

Parent classes need not know about 'Class::Method::Modifiers'. This means
you should be able to modify methods in _any_ subclass. See
Term::VT102::ZeroBased for an example of subclassing with
'Class::Method::Modifiers'.

In short, 'Class::Method::Modifiers' solves the problem of making sure you
call '$self->SUPER::foo(@_)', and provides a cleaner interface for it.

As of version 1.00, 'Class::Method::Modifiers' is faster in some cases than
Moose. See _benchmark/method_modifiers.pl_ in the Moose distribution.

'Class::Method::Modifiers' also provides an additional "modifier" type,
'fresh'; see below.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
