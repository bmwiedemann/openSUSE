#
# spec file for package ghc-network-uri
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


%global pkg_name network-uri
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.6.4.2
Release:        0
Summary:        URI manipulation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-compat-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
This package provides facilities for parsing and unparsing URIs, and creating
and resolving relative URI references, closely following the URI spec,
<http://www.ietf.org/rfc/rfc3986.txt IETF RFC 3986>.

== Backward-compatibility

In 'network-2.6' the "Network.URI" module was split off from the 'network'
package into this package. If you're using the "Network.URI" module you can be
backward compatible and automatically get it from the right package by using
the </package/network-uri-flag network-uri-flag pseudo-package> in your
'.cabal' file's build-depends (along with dependencies for both 'network-uri'
and 'network'):

> build-depends: > network-uri-flag == 0.1.*

Or you can do the same manually by adding this boilerplate to your '.cabal'
file:

> flag network-uri > description: Get Network.URI from the network-uri package
> default: True > > library > -- ... > if flag(network-uri) > build-depends:
network-uri >= 2.6, network >= 2.6 > else > build-depends: network-uri < 2.6,
network < 2.6

That is, get the module from either 'network < 2.6' or from 'network-uri >=
2.6'.

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
%doc CHANGELOG.md README.md

%changelog
