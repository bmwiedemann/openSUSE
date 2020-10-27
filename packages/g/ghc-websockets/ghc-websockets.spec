#
# spec file for package ghc-websockets
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


%global pkg_name websockets
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.12.7.1
Release:        0
Summary:        A sensible and clean way to write WebSocket-capable servers in Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
This library allows you to write WebSocket-capable servers.

An example server:
<https://github.com/jaspervdj/websockets/blob/master/example/server.lhs>

An example client:
<https://github.com/jaspervdj/websockets/blob/master/example/client.hs>

See also:

* The specification of the WebSocket protocol:
<http://www.whatwg.org/specs/web-socket-protocol/>

* The JavaScript API for dealing with WebSockets:
<http://www.w3.org/TR/websockets/>.

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
cabal-tweak-dep-ver base64-bytestring '< 1.2' '< 2'

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
%license LICENCE

%files devel -f %{name}-devel.files
%doc CHANGELOG

%changelog
