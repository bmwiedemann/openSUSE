#
# spec file for package ghc-algebraic-graphs
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


%global pkg_name algebraic-graphs
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.5
Release:        0
Summary:        A library for algebraic graph construction and transformation
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-inspection-testing-devel
%endif

%description
<https://github.com/snowleopard/alga Alga> is a library for algebraic
construction and manipulation of graphs in Haskell. See
<https://github.com/snowleopard/alga-paper this paper> for the motivation
behind the library, the underlying theory and implementation details.

The top-level module
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph.html
Algebra.Graph> defines the main data type for /algebraic graphs/
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph.html#t:Graph
Graph>, as well as associated algorithms. For type-safe representation and
manipulation of /non-empty algebraic graphs/, see
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-NonEmpty.html
Algebra.Graph.NonEmpty>. Furthermore, /algebraic graphs with edge labels/ are
implemented in
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-Labelled.html
Algebra.Graph.Labelled>.

The library also provides conventional graph data structures, such as
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-AdjacencyMap.html
Algebra.Graph.AdjacencyMap> along with its various flavours: adjacency maps
specialised to graphs with vertices of type 'Int'
(<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-AdjacencyIntMap.html
Algebra.Graph.AdjacencyIntMap>), non-empty adjacency maps
(<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-NonEmpty-AdjacencyMap.html
Algebra.Graph.NonEmpty.AdjacencyMap>), and adjacency maps with edge labels
(<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-Labelled-AdjacencyMap.html
Algebra.Graph.Labelled.AdjacencyMap>). A large part of the API of algebraic
graphs and adjacency maps is available through the 'Foldable'-like type class
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-ToGraph.html
Algebra.Graph.ToGraph>.

The type classes defined in
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-Class.html
Algebra.Graph.Class> and
<http://hackage.haskell.org/package/algebraic-graphs/docs/Algebra-Graph-HigherKinded-Class.html
Algebra.Graph.HigherKinded.Class> can be used for polymorphic construction and
manipulation of graphs.

This is an experimental library and the API is expected to remain unstable
until version 1.0.0. Please consider contributing to the on-going
<https://github.com/snowleopard/alga/issues discussions on the library API>.

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
%doc AUTHORS.md CHANGES.md README.md

%changelog
