# vim: set sw=4 ts=4 et nu:
#
# spec file for package perl-Math-Random-ISAAC
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:           perl-Math-Random-ISAAC
Version:        1.004
Release:        0
Summary:        Perl interface to the ISAAC PRNG algorithm
License:        GPL-2.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-%{version}.tar.gz
Url:            http://search.cpan.org/dist/Math-Random-ISAAC
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::NoWarnings) >= 0.084
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description
As with other Pseudo-Random Number Generator (PRNG) algorithms like the
Mersenne Twister (see Math::Random::MT), this algorithm is designed to
take some seed information and produce seemingly random results as output.
However, ISAAC (Indirection, Shift, Accumulate, Add, and Count) has
different goals than these commonly used algorithms. In particular, it's
really fast - on average, it requires only 18.75 machine cycles to
generate a 32-bit value. This makes it suitable for applications where a
significant amount of random data needs to be produced quickly, such
solving using the Monte Carlo method or for games.
The results are uniformly distributed, unbiased, and unpredictable unless
you know the seed. The algorithm was published by Bob Jenkins in the late
90s and despite the best efforts of many security researchers, no feasible
attacks have been found to date.

%prep
%setup -q -n "Math-Random-ISAAC-%{version}"
%__sed -i '/^auto_install/d' Makefile.PL
%__sed -i 's/6\.31/6.30/g' Makefile.PL

%build
%__perl Makefile.PL PREFIX="%{_prefix}"
%__make %{?_smp_flags}

%install
%perl_make_install
%perl_process_packlist

%check
%__make test

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%dir %{perl_vendorlib}/Math
%dir %{perl_vendorlib}/Math/Random
%{perl_vendorlib}/Math/Random/ISAAC
%{perl_vendorlib}/Math/Random/ISAAC.pm
%doc %{perl_man3dir}/Math::Random::ISAAC.%{perl_man3ext}%{ext_man}
%doc %{perl_man3dir}/Math::Random::ISAAC::*.%{perl_man3ext}%{ext_man}

%changelog
