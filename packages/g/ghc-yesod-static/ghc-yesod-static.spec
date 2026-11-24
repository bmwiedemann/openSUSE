#
# spec file for package ghc-yesod-static
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


%global pkg_name yesod-static
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        1.6.1.3
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Static file serving subsite for Yesod Web Framework
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
# https://github.com/yesodweb/yesod/pull/1916.patch
Patch01:        support-modern-crypton-versions.patch
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-crypton-conduit-devel
BuildRequires:  ghc-crypton-devel
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
BuildRequires:  ghc-ram-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-wai-app-static-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-yesod-core-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-conduit-prof
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-css-text-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-hjsmin-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-mime-types-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-ram-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-wai-app-static-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-yesod-core-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-rio-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-yesod-test-devel
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-rio-prof
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-yesod-test-prof
%endif
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
%autosetup -p2 -n %pkg_name-%{version}
cabal-tweak-dep-ver ram '< 0.22' '< 1'

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
