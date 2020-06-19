#
# spec file for package ghc-wizards
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


%global pkg_name wizards
Name:           ghc-%{pkg_name}
Version:        1.0.3
Release:        0
Summary:        High level, generic library for interrogative user interfaces
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-control-monad-free-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel

%description
'wizards' is a package designed for the quick and painless development of
/interrogative/ programs, which revolve around a "dialogue" with the user, who
is asked a series of questions in a sequence much like an installation wizard.

Everything from interactive system scripts, to installation wizards, to
full-blown shells can be implemented with the support of 'wizards'.

It is developed transparently on top of a free monad, which separates out the
semantics of the program from any particular interface. A variety of backends
exist, including console-based "System.Console.Wizard.Haskeline" and
"System.Console.Wizard.BasicIO", and the pure "System.Console.Wizard.Pure".
It is also possible to write your own backends, or extend existing back-ends
with new features. While both built-in IO backends operate on a console, there
is no reason why 'wizards' cannot also be used for making GUI wizard
interfaces.

See the github page for examples on usage:

<http://www.github.com/liamoc/wizards>

For creating backends, the module "System.Console.Wizard.Internal" has a brief
tutorial.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
