#
# spec file for package ghc-unix-bytestring
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


%global pkg_name unix-bytestring
Name:           ghc-%{pkg_name}
Version:        0.3.7.3
Release:        0
Summary:        Unix/Posix-specific functions for ByteStrings
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros

%description
Unix/Posix-specific functions for ByteStrings.

Provides 'ByteString' file-descriptor based I/O API, designed loosely after the
'String' file-descriptor based I/O API in "System.Posix.IO". The functions here
wrap standard C implementations of the functions specified by the ISO/IEC
9945-1:1990 (``POSIX.1'') and X/Open Portability Guide Issue 4, Version 2
(``XPG4.2'') specifications.

Note that this package doesn't require the 'unix' package as a dependency.
But you'll need it in order to get your hands on an 'Fd', so we're not offering
a complete replacement.

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
%doc CHANGELOG README

%changelog
