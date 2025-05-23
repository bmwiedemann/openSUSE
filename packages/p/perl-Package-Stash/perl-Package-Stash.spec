#
# spec file for package perl-Package-Stash
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


%define cpan_name Package-Stash
Name:           perl-Package-Stash
Version:        0.400.0
Release:        0
# 0.40 -> normalize -> 0.400.0
%define cpan_version 0.40
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Routines for manipulating stashes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.11
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.20
BuildRequires:  perl(Module::Implementation) >= 0.60
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
Requires:       perl(Dist::CheckConflicts) >= 0.20
Requires:       perl(Module::Implementation) >= 0.60
Provides:       perl(Package::Stash) = %{version}
Provides:       perl(Package::Stash::PP) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Package::Stash::XS) >= 0.260
%{perl_requires}

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that
behind a simple API.

NOTE: Most methods in this class require a variable specification that
includes a sigil. If this sigil is absent, it is assumed to represent the
IO slot.

Due to limitations in the typeglob API available to perl code, and to
typeglob manipulation in perl being quite slow, this module provides two
implementations - one in pure perl, and one using XS. The XS implementation
is to be preferred for most usages; the pure perl one is provided for cases
where XS modules are not a possibility. The current implementation in use
can be set by setting '$ENV{PACKAGE_STASH_IMPLEMENTATION}' or
'$Package::Stash::IMPLEMENTATION' before loading Package::Stash (with the
environment variable taking precedence), otherwise, it will use the XS
implementation if possible, falling back to the pure perl one.

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
