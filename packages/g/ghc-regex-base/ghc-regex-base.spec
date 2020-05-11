#
# spec file for package ghc-regex-base
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global pkg_name regex-base
Name:           ghc-%{pkg_name}
Version:        0.94.0.0
Release:        0
Summary:        Common "Text.Regex.*" API for Regex matching
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel

%description
This package doesn't provide the ability to do regex matching, but instead
provides the type-classes that constitute the abstract API that is implemented
by 'regex-*' backends such as

* <//hackage.haskell.org/package/regex-posix regex-posix>

* <//hackage.haskell.org/package/regex-parsec regex-parsec>

* <//hackage.haskell.org/package/regex-dfa regex-dfa>

* <//hackage.haskell.org/package/regex-tdfa regex-tdfa>

* <//hackage.haskell.org/package/regex-pcre regex-pcre>

See also <https://wiki.haskell.org/Regular_expressions> for more information.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc ChangeLog.md

%changelog
