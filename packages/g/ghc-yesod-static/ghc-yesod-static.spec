#
# spec file for package ghc-yesod-static
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


%global pkg_name yesod-static
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.6.0.1
Release:        0
Summary:        Static file serving subsite for Yesod Web Framework
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-conduit-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-css-text-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hjsmin-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mime-types-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-wai-app-static-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-yesod-core-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-yesod-test-devel
%endif

%description
API docs and the README are available at
<http://www.stackage.org/package/yesod-static>.

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
%doc ChangeLog.md README.md

%changelog
