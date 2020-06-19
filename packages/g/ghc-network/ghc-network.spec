#
# spec file for package ghc-network
#
# Copyright (c) 2019 SUSE LLC
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


%global pkg_name network
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        3.1.1.1
Release:        0
Summary:        Low-level networking interface
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
%endif

%description
This package provides a low-level networking interface.

=== High-Level Packages Other packages provide higher level interfaces:

* connection * hookup * network-simple

=== Extended Packages 'network' seeks to provide a cross-platform core for
networking. As such some APIs live in extended libraries. Packages in the
'network' ecosystem are often prefixed with 'network-'.

==== 'network-bsd' In 'network-3.0.0.0' the 'Network.BSD' module was split off
into its own package, 'network-bsd-3.0.0.0'.

==== 'network-uri' In 'network-2.6' the 'Network.URI' module was split off into
its own package, 'network-uri-2.6'. If you're using the 'Network.URI' module
you can automatically get it from the right package by adding this to your
'.cabal' file:

> library > build-depends: network-uri-flag.

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
%doc CHANGELOG.md README.md examples

%changelog
