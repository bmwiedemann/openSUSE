#
# spec file for package ghc-cassava
#
# Copyright (c) 2020 SUSE LLC
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


%global pkg_name cassava
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.5.2.0
Release:        0
Summary:        A CSV parsing and encoding library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Only-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-short-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
'cassava' is a library for parsing and encoding [RFC
4180](https://tools.ietf.org/html/rfc4180) compliant [comma-separated values
(CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) data, which is a
textual line-oriented format commonly used for exchanging tabular data.

'cassava''s API includes support for

- Index-based record-conversion - Name-based record-conversion - Typeclass
directed conversion of fields and records - Built-in field-conversion instances
for standard types - Customizable record-conversion instance derivation via GHC
generics - Low-level
[bytestring](https://hackage.haskell.org/package/bytestring) builders (see
"Data.Csv.Builder") - Incremental decoding and encoding API (see
"Data.Csv.Incremental") - Streaming API for constant-space decoding (see
"Data.Csv.Streaming")

Moreover, this library is designed to be easy to use; for instance, here's a
very simple example of encoding CSV data:

>>> Data.Csv.encode [("John",27),("Jane",28)] "John,27rnJane,28rn"

Please refer to the documentation in "Data.Csv" and the included
[README](#readme) for more usage examples.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

%build
%define cabal_configure_options -f-bytestring--lt-0_10_4
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
%doc CHANGES.md README.md examples

%changelog
