#
# spec file for package perl-PerlX-Maybe
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name PerlX-Maybe
Name:           perl-PerlX-Maybe
Version:        1.202
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Return a pair only if they are both defined
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Exporter::Tiny)
Recommends:     perl(PerlX::Maybe::XS)
%{perl_requires}

%description
Moose classes (and some other classes) distinguish between an attribute
being unset and the attribute being set to undef. Supplying a constructor
arguments like this:

 my $bob = Person->new(
    name => $name,
    age => $age,
 );

Will result in the 'name' and 'age' attributes possibly being set to undef
(if the corresponding '$name' and '$age' variables are not defined), which
may violate the Person class' type constraints.

(Note: if you are the _author_ of the class in question, you can solve this
using MooseX::UndefTolerant. However, some of us are stuck using
non-UndefTolerant classes written by third parties.)

To ensure that the Person constructor does not try to set a name or age at
all when they are undefined, ugly looking code like this is often used:

 my $bob = Person->new(
    defined $name ? (name => $name) : (),
    defined $age ? (age => $age) : (),
 );

or:

 my $bob = Person->new(
    (name => $name) x!!(defined $name),
    (age  => $age)  x!!(defined $age),
 );

A slightly more elegant solution is the 'maybe' function.

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
%doc Changes COPYRIGHT CREDITS doap.ttl README
%license LICENSE

%changelog
