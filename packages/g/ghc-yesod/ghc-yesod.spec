#
# spec file for package ghc-yesod
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


%global pkg_name yesod
Name:           ghc-%{pkg_name}
Version:        1.6.1.1
Release:        0
Summary:        Creation of type-safe, RESTful web applications
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-yesod-core-devel
BuildRequires:  ghc-yesod-form-devel
BuildRequires:  ghc-yesod-persistent-devel
ExcludeArch:    %{ix86}

%description
API docs and the README are available at
<http://www.stackage.org/package/yesod>.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md

%changelog
