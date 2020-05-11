#
# spec file for package ghc-HsYAML
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global pkg_name HsYAML
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.1.0
Release:        0
Summary:        Pure Haskell YAML 1.2 processor
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
'HsYAML' is a [YAML 1.2](http://yaml.org/spec/1.2/spec.html) processor, i.e.
a library for parsing and serializing YAML documents.

Features of 'HsYAML' include:

* Pure Haskell implementation with small dependency footprint and emphasis on
strict compliance with the [YAML 1.2
specification](http://yaml.org/spec/1.2/spec.html). * Direct decoding to native
Haskell types via ('aeson'-inspired) typeclass-based API (see "Data.YAML").
* Allows round-tripping while preserving ordering, anchors, and comments at
Event-level. * Support for constructing custom YAML node graph representation
(including support for cyclic YAML data structures). * Support for the standard
(untyped) /Failsafe/, (strict) /JSON/, and (flexible) /Core/ "schemas"
providing implicit typing rules as defined in the YAML 1.2 specification
(including support for user-defined custom schemas; see "Data.YAML.Schema").
* Support for emitting YAML using /Failsafe/, (strict) /JSON/, and (flexible)
/Core/ "schemas" (including support for user-defined custom encoding schemas;
see "Data.YAML.Schema"). * Event-based API resembling LibYAML's Event-based API
(see "Data.YAML.Event"). * Low-level API access to lexical token-based scanner
(see "Data.YAML.Token").

See also the <//hackage.haskell.org/package/HsYAML-aeson HsYAML-aeson> package
which allows to decode and encode YAML by leveraging 'aeson''s 'FromJSON' and
'ToJSON' instances.

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
%license LICENSE.GPLv2
%license LICENSE.GPLv3

%files devel -f %{name}-devel.files
%doc ChangeLog.md

%changelog
