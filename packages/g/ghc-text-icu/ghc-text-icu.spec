#
# spec file for package ghc-text-icu
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name text-icu
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8.0.2
Release:        0
Summary:        Bindings to the ICU library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  libicu-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc)
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
Haskell bindings to the International Components for Unicode (ICU) libraries.
These libraries provide robust and full-featured Unicode services on a wide
variety of platforms.

Features include:

* Both pure and impure bindings, to allow for fine control over efficiency and
ease of use.

* Breaking of strings on character, word, sentence, and line boundaries.

* Access to the Unicode Character Database (UCD) of character metadata.

* String collation functions, for locales where the conventions for
lexicographic ordering differ from the simple numeric ordering of character
codes.

* Character set conversion functions, allowing conversion between Unicode and
over 220 character encodings.

* Unicode normalization. (When implementations keep strings in a normalized
form, they can be assured that equivalent strings have a unique binary
representation.)

* Regular expression search and replace.

* Security checks for visually confusable (spoofable) strings.

* Bidirectional Unicode algorithm

* Calendar objects holding dates and times.

* Number and calendar formatting.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       libicu-devel
Requires:       pkgconfig
Requires:       pkgconfig(icu-i18n)
Requires:       pkgconfig(icu-io)
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

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
%doc README.markdown changelog.md

%changelog
