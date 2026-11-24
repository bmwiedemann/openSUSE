#
# spec file for package ghc-yesod-core
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


%global pkg_name yesod-core
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        1.7.0.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Creation of type-safe, RESTful web applications
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-attoparsec-aeson-devel
BuildRequires:  ghc-auto-update-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-clientsession-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-encoding-devel
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-path-pieces-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-compat-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-word8-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-aeson-prof
BuildRequires:  ghc-auto-update-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-clientsession-prof
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-encoding-prof
BuildRequires:  ghc-entropy-prof
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-path-pieces-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-shakespeare-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-compat-prof
BuildRequires:  ghc-th-lift-instances-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-wai-logger-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-word8-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-th-abstraction-devel
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-hspec-expectations-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-th-abstraction-prof
%endif
%endif

%description
API docs and the README are available at
<http://www.stackage.org/package/yesod-core>.

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
%doc ChangeLog.md README.md docs

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
