#
# spec file for package ghc-network-bsd
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


%global pkg_name network-bsd
Name:           ghc-%{pkg_name}
Version:        2.8.1.0
Release:        0
Summary:        POSIX network database (<netdb.h>) API
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/3.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-rpm-macros

%description
This package provides Haskell bindings to the the [POSIX network database
(<netdb.h>)
API](http://pubs.opengroup.org/onlinepubs/009696699/basedefs/netdb.h.html).

=== Relationship to the 'network' package

The 'network' package version 2.* series provides "Network.BSD" but it is
removed starting with 'network' version 3.0.

This package provides the "Network.BSD" module split off from the
<https://hackage.haskell.org/package/network network package>.

If in addition to the 'network''s modules also "Network.BSD" is necessary, add
'network-bsd' to your dependencies like so:

> library > build-depends: network >= 2.7 && < 3.1 > , network-bsd >= 2.7 && <
2.9

I.e. you can control the version of the 'network' package independently.

__NOTE__: Starting with 'network-bsd-2.8.1.0' the APIs of 'network' and
'network-bsd' evolve differently, and consequently the versioning doesn't match
up anymore! Moreover, also starting with version 'network-bsd-2.8.1.0' this
package requires 'network >= 3' in order to avoid module name clashes with
'network < 3''s "Network.BSD" module.

However, 'network-bsd-2.7.0.0' and 'network-bsd-2.8.0.0' passes thru the
"Network.BSD" module from 'network-2.7.*' and 'network-2.8.*' respectively in a
non-clashing way via Cabal's
<https://www.haskell.org/cabal/users-guide/developing-packages.html#pkg-field-library-reexported-modules
reexported-modules> feature while ensuring a well-defined
<https://pvp.haskell.org/ API versioning> of the observable API of
'network-bsd'. This is why the example above supporting a wide range of
'network' versions works by including version 2.7.0.0 in the required version
range of 'network-bsd'.

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
%doc CHANGELOG.md

%changelog
