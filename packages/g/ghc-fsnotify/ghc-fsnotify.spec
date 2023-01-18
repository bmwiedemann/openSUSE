#
# spec file for package ghc-fsnotify
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name fsnotify
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.4.1.0
Release:        0
Summary:        Cross platform library for file change notification
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hinotify-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-sandwich-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-unliftio-devel
%endif

%description
Cross platform library for file creation, modification, and deletion
notification. This library builds upon existing libraries for platform-specific
Windows, Mac, and Linux filesystem event notification.

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
%doc CHANGELOG.md README.md

%changelog
