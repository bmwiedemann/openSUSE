#
# spec file for package perl-Test-utf8
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Test-utf8
Name:           perl-Test-utf8
Version:        1.30.0
Release:        0
# 1.03 -> normalize -> 1.30.0
%define cpan_version 1.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Handy utf8 tests
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
Provides:       perl(Test::utf8) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is a collection of tests useful for dealing with utf8 strings
in Perl.

This module has two types of tests: The validity tests check if a string is
valid and not corrupt, whereas the characteristics tests will check that
string has a given set of characteristics.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README

%changelog
