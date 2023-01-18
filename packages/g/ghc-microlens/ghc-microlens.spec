#
# spec file for package ghc-microlens
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


%global pkg_name microlens
Name:           ghc-%{pkg_name}
Version:        0.4.13.1
Release:        0
Summary:        A tiny lens library with no dependencies
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}

%description
NOTE: If you're writing an app, you probably want
<http://hackage.haskell.org/package/microlens-platform microlens-platform> – it
has the most features. <http://hackage.haskell.org/package/microlens microlens>
is intended more for library writers who want a tiny lens library (after all,
lenses are pretty useful for everything, not just for updating records!).

This library is an extract from <http://hackage.haskell.org/package/lens lens>
(with no dependencies). It's not a toy lenses library, unsuitable for “real
world”, but merely a small one. It is compatible with lens, and should have
same performance. It also has better documentation.

There's a longer readme <https://github.com/monadfix/microlens#readme on
Github>. It has a migration guide for lens users, a description of other
packages in the family, a discussion of other lens libraries you could use
instead, and so on.

Here are some usecases for this library:

* You want to define lenses or traversals in your own library, but don't want
to depend on lens. Having lenses available often make working with a library
more pleasant.

* You just want to be able to use lenses to transform data (or even just use
'over _1' to change the first element of a tuple).

* You are new to lenses and want a small library to play with.

However, don't use this library if:

* You need 'Iso's, 'Prism's, indexed traversals, or actually anything else
which isn't defined here (though some indexed functions are available elsewhere
– containers and vector provide them for their types, and
<http://hackage.haskell.org/package/ilist ilist> provides indexed functions for
lists).

* You want a library with a clean, understandable implementation (in which case
you're looking for <http://hackage.haskell.org/package/lens-simple
lens-simple>).

As already mentioned, if you're writing an application which uses lenses more
extensively, look at <http://hackage.haskell.org/package/microlens-platform
microlens-platform> – it combines features of most other microlens packages
(<http://hackage.haskell.org/package/microlens-mtl microlens-mtl>,
<http://hackage.haskell.org/package/microlens-th microlens-th>,
<http://hackage.haskell.org/package/microlens-ghc microlens-ghc>).

If you want to export getters or folds and don't mind the
<http://hackage.haskell.org/package/contravariant contravariant> dependency,
please consider using <http://hackage.haskell.org/package/microlens-contra
microlens-contra>.

If you haven't ever used lenses before, read
<http://hackage.haskell.org/package/lens-tutorial/docs/Control-Lens-Tutorial.html
this tutorial>. (It's for lens, but it applies to microlens just as well.)

Note that microlens has no dependencies starting from GHC 7.10 (base-4.8).
Prior to that, it depends on transformers-0.2 or above.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
