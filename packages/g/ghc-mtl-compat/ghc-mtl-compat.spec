#
# spec file for package ghc-mtl-compat
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


%global pkg_name mtl-compat
Name:           ghc-%{pkg_name}
Version:        0.2.2
Release:        0
Summary:        Backported Control.Monad.Except module from mtl
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros

%description
This package backports the "Control.Monad.Except" module from 'mtl' (if using
'mtl-2.2.0.1' or earlier), which reexports the 'ExceptT' monad transformer and
the 'MonadError' class.

This package should only be used if there is a need to use the
'Control.Monad.Except' module specifically. If you just want the 'mtl' class
instances for 'ExceptT', use 'transformers-compat' instead, since 'mtl-compat'
does nothing but reexport the instances from that package.

Note that unlike how 'mtl-2.2' or later works, the "Control.Monad.Except"
module defined in this package exports all of 'ExceptT''s monad class
instances. Therefore, you may have to declare 'import Control.Monad.Except ()'
at the top of your file to get all of the 'ExceptT' instances in scope.

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
%ghc_lib_build_without_haddock

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
