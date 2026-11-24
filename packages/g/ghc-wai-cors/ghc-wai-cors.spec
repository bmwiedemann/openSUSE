#
# spec file for package ghc-wai-cors
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


%global pkg_name wai-cors
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.2.7
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        CORS for WAI
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-unicode-symbols-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-wai-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-unicode-symbols-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-wai-prof
%endif
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-websockets-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-websockets-devel
%if %{with ghc_prof}
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-wai-websockets-prof
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-websockets-prof
%endif
%endif

%description
This package provides an implemenation of Cross-Origin resource sharing (CORS)
for <http://hackage.haskell.org/package/wai Wai> that aims to be compliant with
<http://www.w3.org/TR/cors>.

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
%dir %{_datadir}/%pkg_name-%{version}
%dir %{_datadir}/%pkg_name-%{version}/examples
%dir %{_datadir}/%pkg_name-%{version}/test
%{_datadir}/%pkg_name-%{version}/CHANGELOG.md
%{_datadir}/%pkg_name-%{version}/README.md
%{_datadir}/%pkg_name-%{version}/examples/Scotty.hs
%{_datadir}/%pkg_name-%{version}/examples/ServantWai.hs
%{_datadir}/%pkg_name-%{version}/examples/Wai.hs
%{_datadir}/%pkg_name-%{version}/test/index.html
%{_datadir}/%pkg_name-%{version}/test/phantomjs.js

%files devel -f %{name}-devel.files

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
