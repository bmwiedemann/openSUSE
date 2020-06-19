#
# spec file for package ghc-timezone-olson
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


%global pkg_name timezone-olson
Name:           ghc-%{pkg_name}
Version:        0.2.0
Release:        0
Summary:        A pure Haskell parser and renderer for binary Olson timezone files
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-timezone-series-devel

%description
A parser and renderer for binary Olson timezone files whose format is specified
by the tzfile(5) man page on Unix-like systems. For more information about this
format, see <http://www.iana.org/time-zones/repository/tz-link.html>.
Functions are provided for converting the parsed data into 'TimeZoneSeries'
objects from the timezone-series package. On many platforms, binary Olson
timezone files suitable for use with this package are available in the
directory %{_datadir}/zoneinfo and its subdirectories on your computer.
For a way to read binary Olson timezone files at compile time, see the
timezone-olson-th package
(<http://hackage.haskell.org/package/timezone-olson-th>).

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
%doc README.md

%changelog
