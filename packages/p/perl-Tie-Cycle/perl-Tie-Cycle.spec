#
# spec file for package perl-Tie-Cycle
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


%define cpan_name Tie-Cycle
Name:           perl-Tie-Cycle
Version:        1.229.0
Release:        0
# 1.229 -> normalize -> 1.229.0
%define cpan_version 1.229
License:        Artistic-2.0
Summary:        Cycle through a list of values via a scalar
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 1
Provides:       perl(Tie::Cycle) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
You use 'Tie::Cycle' to go through a list over and over again. Once you get
to the end of the list, you go back to the beginning. You don't have to
worry about any of this since the magic of tie does that for you.

The tie takes an array reference as its third argument. The tie should
succeed unless the argument is not an array reference. Previous versions
required you to use an array that had more than one element (what's the
pointing of looping otherwise?), but I've removed that restriction since
the number of elements you want to use may change depending on the
situation.

During the tie, this module makes a shallow copy of the array reference. If
the array reference contains references, and those references are changed
after the tie, the elements of the cycle will change as well. See the
included _test.pl_ script for an example of this effect.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING.md examples SECURITY.md
%license LICENSE

%changelog
