#
# spec file for package ghc-base-compat
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


%global pkg_name base-compat
Name:           ghc-%{pkg_name}
Version:        0.11.2
Release:        0
Summary:        A compatibility layer for base
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-unix-devel

%description
Provides functions available in later versions of 'base' to a wider range of
compilers, without requiring you to use CPP pragmas in your code. See the
<https://github.com/haskell-compat/base-compat/blob/master/base-compat/README.markdown
README> for what is covered. Also see the
<https://github.com/haskell-compat/base-compat/blob/master/base-compat/CHANGES.markdown
changelog> for recent changes.

Note that 'base-compat' does not add any orphan instances. There is a separate
package, '<http://hackage.haskell.org/package/base-orphans base-orphans>', for
that.

In addition, 'base-compat' does not backport any data types or type classes.
See
'<https://github.com/haskell-compat/base-compat/blob/master/base-compat/README.markdown#data-types-and-type-classes
this section of the README>' for more info.

'base-compat' is designed to have zero dependencies. For a version of
'base-compat' that depends on compatibility libraries for a wider support
window, see the '<http://hackage.haskell.org/package/base-compat-batteries
base-compat-batteries>' package. Most of the modules in this library have the
same names as in 'base-compat-batteries' to make it easier to switch between
the two. There also exist versions of each module with the suffix '.Repl',
which are distinct from anything in 'base-compat-batteries', to allow for
easier use in GHCi.

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
%doc CHANGES.markdown README.markdown

%changelog
