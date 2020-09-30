#
# spec file for package ghc-HTTP
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


%global pkg_name HTTP
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        4000.3.15
Release:        0
Summary:        A library for client-side HTTP
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-httpd-shed-devel
BuildRequires:  ghc-pureMD5-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
%endif

%description
The HTTP package supports client-side web programming in Haskell. It lets you
set up HTTP connections, transmitting requests and processing the responses
coming back, all from within the comforts of Haskell. It's dependent on the
network package to operate, but other than that, the implementation is all
written in Haskell.

A basic API for issuing single HTTP requests + receiving responses is provided.
On top of that, a session-level abstraction is also on offer (the
'BrowserAction' monad); it taking care of handling the management of persistent
connections, proxies, state (cookies) and authentication credentials required
to handle multi-step interactions with a web server.

The representation of the bytes flowing across is extensible via the use of a
type class, letting you pick the representation of requests and responses that
best fits your use. Some pre-packaged, common instances are provided for you
('ByteString', 'String').

Here's an example use:

> > do > rsp <- Network.HTTP.simpleHTTP (getRequest "http://www.haskell.org/")
> -- fetch document and return it (as a 'String'.) > fmap (take 100)
(getResponseBody rsp) > > do > (_, rsp) > <- Network.Browser.browse $ do >
setAllowRedirects True -- handle HTTP redirects > request $ getRequest
"http://www.haskell.org/" > return (take 100 (rspBody rsp))

__Note:__ This package does not support HTTPS connections. If you need HTTPS,
take a look at the following packages:

* <http://hackage.haskell.org/package/http-streams http-streams>

* <http://hackage.haskell.org/package/http-client http-client> (in combination
with <http://hackage.haskell.org/package/http-client-tls http-client-tls>)

* <http://hackage.haskell.org/package/req req>

* <http://hackage.haskell.org/package/wreq wreq>.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%doc CHANGES

%changelog
