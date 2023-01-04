#
# spec file for package perl-Pod-Coverage-TrustPod
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


%define cpan_name Pod-Coverage-TrustPod
Name:           perl-Pod-Coverage-TrustPod
Version:        0.100006
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Allow a module's pod to contain Pod::Coverage hints
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Pod::Coverage::CountParents)
BuildRequires:  perl(Pod::Eventual::Simple)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Pod::Coverage::CountParents)
Requires:       perl(Pod::Eventual::Simple)
Requires:       perl(Pod::Find)
%{perl_requires}

%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

Here is a sample Perl module:

  package Foo::Bar;

  =head1 NAME

  Foo::Bar - a bar at which fooes like to drink

  =head1 METHODS

  =head2 fee

  returns the bar tab

  =cut

  sub fee { ... }

  =head2 fie

  scoffs at bar tab

  =cut

  sub fie { ... }

  sub foo { ... }

  =begin Pod::Coverage

    foo

  =end Pod::Coverage

  =cut

This file would report full coverage, because any non-empty lines inside a
block of POD targeted to Pod::Coverage are treated as 'trustme' patterns.
Leading and trailing whitespace is stripped and the remainder is treated as
a regular expression anchored at both ends.

Remember, anywhere you could use '=begin' and '=end' as above, you could
instead write:

  =for Pod::Coverage foo

In some cases, you may wish to make the entire file trusted. The special
pattern '*EVERYTHING*' may be provided to do just this.

Keep in mind that Pod::Coverage::TrustPod sets up exceptions using the
"trust" mechanism rather than the "privacy" mechanism in Pod::Coverage.
This is unlikely ever to matter to you, but it's true.

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
%doc Changes README
%license LICENSE

%changelog
