#
# spec file for package ghc-scientific
#
# Copyright (c) 2019 SUSE LLC
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


%global pkg_name scientific
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.6.2
Release:        0
Summary:        Numbers represented using scientific notation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-integer-logarithms-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-smallcheck-devel
BuildRequires:  ghc-tasty-ant-xml-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-smallcheck-devel
%endif

%description
"Data.Scientific" provides the number type 'Scientific'. Scientific numbers are
arbitrary precision and space efficient. They are represented using
<http://en.wikipedia.org/wiki/Scientific_notation scientific notation>.
The implementation uses a coefficient 'c :: 'Integer'' and a base-10 exponent
'e :: 'Int''. A scientific number corresponds to the 'Fractional' number:
''fromInteger' c * 10 '^^' e'.

Note that since we're using an 'Int' to represent the exponent these numbers
aren't truly arbitrary precision. I intend to change the type of the exponent
to 'Integer' in a future release.

The main application of 'Scientific' is to be used as the target of parsing
arbitrary precision numbers coming from an untrusted source. The advantages
over using 'Rational' for this are that:

* A 'Scientific' is more efficient to construct. Rational numbers need to be
constructed using '%' which has to compute the 'gcd' of the 'numerator' and
'denominator'.

* 'Scientific' is safe against numbers with huge exponents. For example:
'1e1000000000 :: 'Rational'' will fill up all space and crash your program.
Scientific works as expected:

>>> read "1e1000000000" :: Scientific 1.0e1000000000

* Also, the space usage of converting scientific numbers with huge exponents to
''Integral's' (like: 'Int') or ''RealFloat's' (like: 'Double' or 'Float') will
always be bounded by the target type.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc changelog

%changelog
