#
# spec file for package ghc-tree-diff
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


%global pkg_name tree-diff
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.2
Release:        0
Summary:        Diffing of (expression) trees
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-bytestring-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsers-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-uuid-types-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-trifecta-devel
%endif

%description
Common diff algorithm works on list structures:

' diff :: Eq a => [a] -> [a] -> [Edit a] '

This package works on trees.

' treeDiff :: Eq a => Tree a -> Tree a -> Edit (EditTree a) '

This package also provides a way to diff arbitrary ADTs, using
'Generics'-derivable helpers.

This package differs from <http://hackage.haskell.org/package/gdiff gdiff>, in
a two ways: 'tree-diff' doesn't have patch function, and the "edit-script" is a
tree itself, which is useful for pretty-printing.

' >>> prettyEditExpr $ ediff (Foo 42 [True, False] "old") (Foo 42 [False,
False, True] "new") Foo {fooBool = [-True, +False, False, +True], fooInt = 42,
fooString = -"old" +"new"} '.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
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
%doc ChangeLog.md README.md

%changelog
