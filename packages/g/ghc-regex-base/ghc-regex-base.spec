#
# spec file for package ghc-regex-base
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


%global pkg_name regex-base
Name:           ghc-%{pkg_name}
Version:        0.94.0.1
Release:        0
Summary:        Common "Text.Regex.*" API for Regex matching
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
ExcludeArch:    %{ix86}

%description
This package does not provide the ability to do regular expression matching.
Instead, it provides the type classes that constitute the abstract API that is
implemented by 'regex-*' backends such as:

* <https://hackage.haskell.org/package/regex-posix regex-posix>

* <https://hackage.haskell.org/package/regex-parsec regex-parsec>

* <https://hackage.haskell.org/package/regex-dfa regex-dfa>

* <https://hackage.haskell.org/package/regex-tdfa regex-tdfa>

* <https://hackage.haskell.org/package/regex-pcre regex-pcre>

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
%doc ChangeLog.md

%changelog
