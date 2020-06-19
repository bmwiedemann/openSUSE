#
# spec file for package ghc-hxt-regex-xmlschema
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


%global pkg_name hxt-regex-xmlschema
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        9.2.0.3
Release:        0
Summary:        A regular expression library for W3C XML Schema regular expressions
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-hxt-charproperties-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif

%description
This library supports full W3C XML Schema regular expressions inclusive all
Unicode character sets and blocks. The complete grammar can be found under
<http://www.w3.org/TR/xmlschema11-2/#regexs>. It is implemented by the
technique of derivations of regular expressions.

The W3C syntax is extended to support not only union of regular sets, but also
intersection, set difference, exor. Matching of subexpressions is also
supported.

The library can be used for constricting lightweight scanners and tokenizers.
It is a standalone library, no external regex libraries are used.

Extensions in 9.2: The library does nor only support String's, but also
ByteString's and Text in strict and lazy variants.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%setup -q -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%doc examples

%changelog
