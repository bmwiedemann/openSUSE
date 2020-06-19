#
# spec file for package ghc-bytestring-builder
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


%global pkg_name bytestring-builder
Name:           ghc-%{pkg_name}
Version:        0.10.8.2.0
Release:        0
Summary:        The new bytestring builder, packaged outside of GHC
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros

%description
This is the bytestring builder that is debuting in bytestring-0.10.4.0, which
should be shipping with GHC 7.8, probably late in 2013. This builder has
several nice simplifications and improvements, and more out-of-box
functionality than the older blaze-builder.

Note that this package detects which version of bytestring you are compiling
against, and if you are compiling against bytestring-0.10.4 or later, will be
an empty package.

This package lets the new interface and implementation be used with most older
compilers without upgrading bytestring, which can be rather problematic.
In conjunction with blaze-builder-0.4 or later, which offers an implementation
of blaze-builder in terms of bytestring-builder, this should let most people
try the new interface and implementation without causing undue compatibility
problems with packages that depend on blaze-builder.

GHC 7.6 did debut an almost identical interface and implementation, but with
slightly different module names and organization. Trying to re-export/rename
the builder provided with 7.6 did not turn out to be very practical, because
this interface includes new functions that rely on Builder internals, which are
not exported in 7.6. Furthermore, these module names should be deprecated in
7.10.

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
%doc CHANGELOG.md

%changelog
