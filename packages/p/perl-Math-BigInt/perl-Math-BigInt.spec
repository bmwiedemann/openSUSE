#
# spec file for package perl-Math-BigInt
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


%define cpan_name Math-BigInt
Name:           perl-Math-BigInt
Version:        2.3.3
Release:        0
# 2.003003 -> normalize -> 2.3.3
%define cpan_version 2.003003
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Arbitrary size integer math package
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.58
BuildRequires:  perl(Math::Complex) >= 1.36
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Carp) >= 1.22
Requires:       perl(Math::Complex) >= 1.36
Provides:       perl(Math::BigFloat) = %{version}
Provides:       perl(Math::BigInt) = %{version}
Provides:       perl(Math::BigInt::Calc) = %{version}
Provides:       perl(Math::BigInt::Lib) = %{version}
Provides:       perl(Math::BigRat) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
Recommends:     perl(bignum) >= 0.22
Recommends:     perl(Math::BigInt::FastCalc) >= 0.25
Recommends:     perl(Math::BigInt::GMP) >= 1.35
Recommends:     perl(Math::BigInt::Pari) >= 1.15
Recommends:     perl(Math::BigRat) >= 0.2602
# MANUAL END

%description
Math::BigInt provides support for arbitrary precision integers. Overloading
is also provided for Perl operators.

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
%doc BUGS CHANGES CREDITS examples GOALS HISTORY NEW README README.md TODO
%license LICENSE

%changelog
