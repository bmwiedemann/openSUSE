#
# spec file for package perl-CPAN-Meta-Requirements
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


%define cpan_name CPAN-Meta-Requirements
Name:           perl-CPAN-Meta-Requirements
Version:        2.143
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Set of version requirements for a CPAN dist
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.88
Requires:       perl(version) >= 0.88
%{perl_requires}

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the _META.yml_ or _META.json_ files in CPAN
distributions, and as defined by CPAN::Meta::Spec. It can be built up by
adding more and more constraints, and it will reduce them to the simplest
representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

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
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
