#
# spec file for package ghc-skein
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


%global pkg_name skein
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.0.9.4
Release:        0
Summary:        Skein, a family of cryptographic hash functions.  Includes Skein-MAC as well
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
%if %{with tests}
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-devel
%endif

%description
Skein (<http://www.skein-hash.info/>) is a family of fast secure cryptographic
hash functions designed by Niels Ferguson, Stefan Lucks, Bruce Schneier, Doug
Whiting, Mihir Bellare, Tadayoshi Kohno, Jon Callas and Jesse Walker.

This package uses bindings to the optimized C implementation of Skein.
We provide a high-level interface (see module "Crypto.Skein") to some of the
Skein use cases. We also provide a low-level interface (see module
"Crypto.Skein.Internal") should you need to use Skein in a different way.

Currently we have support for Skein as cryptographic hash function as Skein as
a message authentication code (Skein-MAC). For examples of how to use this
package, see "Crypto.Skein" module documentation.

This package includes Skein v1.3. Versions of this package before 1.0.0
implemented Skein v1.1.

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

%changelog
