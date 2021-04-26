#
# spec file for package ghc-http-media
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name http-media
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8.0.0
Release:        0
Summary:        Processing HTTP Content-Type and Accept headers
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/5.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-utf8-string-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
This library is intended to be a comprehensive solution to parsing and
selecting quality-indexed values in HTTP headers. It is capable of parsing both
media types and language parameters from the Accept and Content header
families, and can be extended to match against other accept headers as well.
Selecting the appropriate header value is achieved by comparing a list of
server options against the quality-indexed values supplied by the client.

In the following example, the Accept header is parsed and then matched against
a list of server options to serve the appropriate media using 'mapAcceptMedia':

> getHeader >>= maybe send406Error sendResourceWith . mapAcceptMedia > [
("text/html", asHtml) > , ("application/json", asJson) > ]

Similarly, the Content-Type header can be used to produce a parser for request
bodies based on the given content type with 'mapContentMedia':

> getContentType >>= maybe send415Error readRequestBodyWith .
mapContentMedia > [ ("application/json", parseJson) > , ("text/plain",
parseText) > ]

The API is agnostic to your choice of server.

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
%doc CHANGES.md

%changelog
