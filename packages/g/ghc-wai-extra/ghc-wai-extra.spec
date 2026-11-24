#
# spec file for package ghc-wai-extra
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pkg_name wai-extra
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        3.1.18
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Provides some basic WAI handlers and middleware
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-word8-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-call-stack-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vault-prof
BuildRequires:  ghc-wai-logger-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-word8-prof
%endif
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-zlib-devel
%if %{with ghc_prof}
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-zlib-prof
%endif
%endif

%description
Provides basic WAI handler and middleware functionality:

* WAI Testing Framework

Hspec testing facilities and helpers for WAI.

* Event Source/Event Stream

Send server events to the client. Compatible with the JavaScript EventSource
API.

* Accept Override

Override the Accept header in a request. Special handling for the _accept query
parameter (which is used throughout WAI override the Accept header).

* Add Headers

WAI Middleware for adding arbitrary headers to an HTTP request.

* Clean Path

Clean a request path to a canonical form.

* Combine Headers

Combine duplicate headers into one.

* GZip Compression

Negotiate HTTP payload gzip compression.

* Health check endpoint

Add an empty health check endpoint.

* HTTP Basic Authentication

WAI Basic Authentication Middleware which uses Authorization header.

* JSONP

"JSON with Padding" middleware. Automatic wrapping of JSON responses to convert
into JSONP.

* Method Override / Post

Allows overriding of the HTTP request method via the _method query string
parameter.

* Request Logging

Request logging middleware for development and production environments

* Request Rewrite

Rewrite request path info based on a custom conversion rules.

* Select

Dynamically choose between Middlewares.

* Stream Files

Convert ResponseFile type responses into ResponseStream type.

* Virtual Host

Redirect incoming requests to a new host based on custom rules.

API docs and the README are available at
<http://www.stackage.org/package/wai-extra>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1 -n %pkg_name-%{version}

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
%doc ChangeLog.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
