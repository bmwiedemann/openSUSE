#
# spec file for package ghc-wai-extra
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


%global pkg_name wai-extra
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        3.1.0
Release:        0
Summary:        Provides some basic WAI handlers and middleware
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http2-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-void-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-word8-devel
BuildRequires:  ghc-zlib-devel
%if %{with tests}
BuildRequires:  ghc-hspec-devel
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

* GZip Compression

Negotiate HTTP payload gzip compression.

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

%prep
%autosetup -n %{pkg_name}-%{version}

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

%changelog
