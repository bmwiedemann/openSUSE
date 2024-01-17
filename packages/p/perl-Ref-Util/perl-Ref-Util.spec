#
# spec file for package perl-Ref-Util
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


Name:           perl-Ref-Util
Version:        0.204
Release:        0
%define cpan_name Ref-Util
Summary:        Utility functions for checking references
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Ref-Util/
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Ref::Util::XS)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Ref::Util::XS)
%{perl_requires}

%description
Ref::Util introduces several functions to help identify references in a
*smarter* (and usually faster) way. In short:

    # conventional approach             # with Ref::Util

    ref( $foo ) eq 'ARRAY'              is_plain_arrayref( $foo )

    use Scalar::Util qw( reftype );
    reftype( $foo ) eq 'ARRAY'          is_arrayref( $foo )

The difference:

* * No comparison against a string constant

When you call 'ref', you stringify the reference and then compare it to
some string constant (like 'ARRAY' or 'HASH'). Not just awkward, it's
brittle since you can mispell the string.

If you use Scalar::Util's 'reftype', you still compare it as a string:

    if ( reftype($foo) eq 'ARRAY' ) { ... }

* * Supports blessed variables

*Note:* In future versions, the idea is to make the default functions use
the *plain* variation, which means explicitly non-blessed references.

If you want to explicitly check for *blessed* references, you should use
the 'is_blessed_*' functions. There will be an 'is_any_*' variation which
will act like the current main functions - not caring whether it's blessed
or not.

When calling 'ref', you receive either the reference type (*SCALAR*,
*ARRAY*, *HASH*, etc.) or the package it's blessed into.

When calling 'is_arrayref' (et. al.), you check the variable flags, so even
if it's blessed, you know what type of variable is blessed.

    my $foo = bless {}, 'PKG';
    ref($foo) eq 'HASH'; # fails

    use Ref::Util 'is_hashref';
    my $foo = bless {}, 'PKG';
    is_hashref($foo); # works

On the other hand, in some situations it might be better to specifically
exclude blessed references. The rationale for that might be that merely
because some object happens to be implemented using a hash doesn't mean
it's necessarily correct to treat it as a hash. For these situations, you
can use 'is_plain_hashref' and friends, which have the same performance
benefits as 'is_hashref'.

There is also a family of functions with names like 'is_blessed_hashref';
these return true for blessed object instances that are implemented using
the relevant underlying type.

* * Supports tied variables and magic

Tied variables (used in Readonly, for example) are supported.

    use Ref::Util qw<is_plain_hashref>;
    use Readonly;

    Readonly::Scalar my $rh2 => { a => { b => 2 } };
    is_plain_hashref($rh2); # success

Ref::Util added support for this in 0.100. Prior to this version the test
would fail.

* * Ignores overloading

These functions ignore overloaded operators and simply check the variable
type. Overloading will likely not ever be supported, since I deem it
problematic and confusing.

Overloading makes your variables opaque containers and hides away *what*
they are and instead require you to figure out *how* to use them. This
leads to code that has to test different abilities (in 'eval', so it
doesn't crash) and to interfaces that get around what a person thought you
would do with a variable. This would have been alright, except there is no
clear way of introspecting it.

* * Ignores subtle types:

The following types, provided by Scalar::Util's 'reftype', are not
supported:

  * * 'VSTRING'

This is a 'PVMG' ("normal" variable) with a flag set for VSTRINGs. Since
this is not a reference, it is not supported.

  * * 'LVALUE'

A variable that delegates to another scalar. Since this is not a reference,
it is not supported.

  * * 'INVLIST'

I couldn't find documentation for this type.

Support might be added, if a good reason arises.

* * Usually fast

When possible, Ref::Util uses Ref::Util::XS as its implementation. (If you
don't have a C compiler available, it uses a pure Perl fallback that has
all the other advantages of Ref::Util, but isn't as fast.)

In fact, Ref::Util::XS has two alternative implementations available
internally, depending on the features supported by the version of Perl
you're using. For Perls that supports custom OPs, we actually add an OP
(which is faster); for other Perls, the implementation that simply calls an
XS function (which is still faster than the pure-Perl equivalent).

See below for benchmark results.

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
%license LICENSE

%changelog
