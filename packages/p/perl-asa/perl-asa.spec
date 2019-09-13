#
# spec file for package perl-asa
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-asa
Version:        1.04
Release:        0
%define cpan_name asa
Summary:        Lets your class/object say it works like something else
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Perl 5 doesn't natively support Java-style interfaces, and it doesn't
support Perl 6 style roles either.

You can get both of these things in half a dozen different ways via various
CPAN modules, but they usually require that you buy into "their way" of
implementing your code.

Other have turned to "duck typing".

This is, for the most part, a fairly naive check that says "can you do this
method", under the "if it looks like a duck, and quacks like a duck, then
it must be a duck".

It assumes that if you have a '->quack' method, then they will treat you as
a duck, because doing things like adding 'Duck' to your '@ISA' array means
you are also forced to take their implementation.

There is, of course, a better way.

For better or worse, Perl's '->isa' functionality to determine if something
is or is not a particular class/object is defined as a *method*, not a
function, and so that means that as well as adding something to you '@ISA'
array, so that Perl's 'UNIVERSAL::isa' method can work with it, you are
also allowed to simply overload your own 'isa' method and answer directly
whether or not you are something.

The simplest form of the idiom looks like this.

  sub isa {
      return 1 if $_[1] eq 'Duck';
      shift->SUPER::isa(@_);
  }

This reads "Check my type as normal, but if anyone wants to know if I'm a
duck, then tell them yes".

Now, there are a few people that have argued that this is "lying" about
your class, but this argument is based on the idea that '@ISA' is somehow
more "real" than using the method directly.

It also assumes that what you advertise you implement needs to be in sync
with the method resolution for any given function. But in the best and
cleanest implementation of code, the API is orthogonal (although most often
related) to the implementation.

And although '@ISA' is about implementation *and* API, overloading 'isa' to
let you change your API is not at all bad when seen in this light.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
