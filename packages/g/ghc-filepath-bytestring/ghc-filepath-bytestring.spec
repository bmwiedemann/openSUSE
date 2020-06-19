#
# spec file for package ghc-filepath-bytestring
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


%global pkg_name filepath-bytestring
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.4.2.1.6
Release:        0
Summary:        Library for manipulating RawFilePaths in a cross platform way
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-unix-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-filepath-devel
%endif

%description
This package provides functionality for manipulating 'RawFilePath' values.
It can be used as a drop in replacement for the filepath library to get the
benefits of using ByteStrings. It provides three modules:

* "System.FilePath.Posix.ByteString" manipulates POSIX/Linux style
'RawFilePath' values (with '/' as the path separator).

* "System.FilePath.Windows.ByteString" manipulates Windows style 'RawFilePath'
values (with either '\' or '/' as the path separator, and deals with drives).

* "System.FilePath.ByteString" is an alias for the module appropriate to your
platform.

All three modules provide the same API, and the same documentation (calling out
differences in the different variants).

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%setup -q -n %{pkg_name}-%{version}

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
%doc CHANGELOG README.md TODO

%changelog
