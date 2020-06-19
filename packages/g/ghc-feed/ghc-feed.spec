#
# spec file for package ghc-feed
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


%global pkg_name feed
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.3.0.1
Release:        0
Summary:        Interfacing with RSS (v 0.9x, 2.x, 1.0) + Atom feeds
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-locale-compat-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-types-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
%endif

%description
Interfacing with RSS (v 0.9x, 2.x, 1.0) + Atom feeds.

To help working with the multiple feed formats we've ended up with, this set of
modules provides parsers, pretty printers and some utility code for querying
and just generally working with a concrete representation of feeds in Haskell.

See here for an example of how to create an Atom feed:
<https://github.com/bergmark/feed/blob/master/tests/Example/CreateAtom.hs>

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

%prep
%setup -q -n %{pkg_name}-%{version}
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
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/tests
%dir %{_datadir}/%{pkg_name}-%{version}/tests/files
%{_datadir}/%{pkg_name}-%{version}/tests/files/*.xml

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
