#
# spec file for package cabal2spec
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


%global pkg_name cabal2spec
%bcond_with tests
Name:           %{pkg_name}
Version:        2.6.1
Release:        0
Summary:        Convert Cabal files into rpm spec files
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
%endif

%description
Convert Cabal files into a
<http://ftp.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html spec file>
suitable for building the package with the RPM package manager. This tool
primarily targets the <http://www.suse.com/ SUSE> and <http://www.opensuse.org
openSUSE> familiy of distributions. Support for other RPM-based distributions
is currently not available. Check out
<http://hackage.haskell.org/package/cabal-rpm cabal-rpm> if you need this.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%setup -q

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc README.md

%changelog
