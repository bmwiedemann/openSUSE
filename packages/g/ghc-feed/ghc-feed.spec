#
# spec file for package ghc-feed
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name feed
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.3.2.1
Release:        0
Summary:        Interfacing with RSS (v 0.9x, 2.x, 1.0) + Atom feeds
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/4.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-old-time-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-locale-compat-devel
BuildRequires:  ghc-time-locale-compat-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-xml-types-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-doctest-driver-gen-devel
BuildRequires:  ghc-doctest-driver-gen-prof
BuildRequires:  ghc-doctest-prof
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-hunit-prof
BuildRequires:  ghc-test-framework-prof
%endif

%description
Interfacing with RSS (v 0.9x, 2.x, 1.0) + Atom feeds.

To help working with the multiple feed formats we've ended up with, this set of
modules provides parsers, pretty printers and some utility code for querying
and just generally working with a concrete representation of feeds in Haskell.

See here for an example of how to create an Atom feed:
<https://github.com/haskell-party/feed/blob/master/tests/Example/CreateAtom.hs>

For basic reading and editing of feeds, consult the documentation of the
Text.Feed.* hierarchy.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

%prep
%autosetup -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal
cabal-tweak-dep-ver base '< 4.20' '< 5'
cabal-tweak-dep-ver base-compat '< 0.14' '< 1'

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
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/tests
%dir %{_datadir}/%{pkg_name}-%{version}/tests/files
%{_datadir}/%{pkg_name}-%{version}/tests/files/*.xml

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
