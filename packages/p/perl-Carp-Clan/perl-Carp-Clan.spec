#
# spec file for package perl-Carp-Clan
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


%define cpan_name Carp-Clan
Name:           perl-Carp-Clan
Version:        6.80.0
Release:        0
# 6.08 -> normalize -> 6.80.0
%define cpan_version 6.08
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Report errors from perspective of caller of a "clan" of modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Carp::Clan) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is based on "'Carp.pm'" from Perl 5.005_03. It has been
modified to skip all package names matching the pattern given in the "use"
statement inside the "'qw()'" term (or argument list).

Suppose you have a family of modules or classes named "Pack::A", "Pack::B"
and so on, and each of them uses "'Carp::Clan qw(^Pack::);'" (or at least
the one in which the error or warning gets raised).

Thus when for example your script "tool.pl" calls module "Pack::A", and
module "Pack::A" calls module "Pack::B", an exception raised in module
"Pack::B" will appear to have originated in "tool.pl" where "Pack::A" was
called, and not in "Pack::A" where "Pack::B" was called, as the unmodified
"'Carp.pm'" would try to make you believe ':-)'.

This works similarly if "Pack::B" calls "Pack::C" where the exception is
raised, et cetera.

In other words, this blames all errors in the "'Pack::*'" modules on the
user of these modules, i.e., on you. ';-)'

The skipping of a clan (or family) of packages according to a pattern
describing its members is necessary in cases where these modules are not
classes derived from each other (and thus when examining '@ISA' - as in the
original "'Carp.pm'" module - doesn't help).

The purpose and advantage of this is that a "clan" of modules can work
together (and call each other) and throw exceptions at various depths down
the calling hierarchy and still appear as a monolithic block (as though
they were a single module) from the perspective of the caller.

In case you just want to ward off all error messages from the module in
which you "'use Carp::Clan'", i.e., if you want to make all error messages
or warnings to appear to originate from where your module was called (this
is what you usually used to "'use Carp;'" for ';-)'), instead of in your
module itself (which is what you can do with a "die" or "warn" anyway), you
do not need to provide a pattern, the module will automatically provide the
correct one for you.

I.e., just "'use Carp::Clan;'" without any arguments and call "carp" or
"croak" as appropriate, and they will automatically defend your module
against all blames!

In other words, a pattern is only necessary if you want to make several
modules (more than one) work together and appear as though they were only
one.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
