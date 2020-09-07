#
# spec file for package ghc-double-conversion
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


%global pkg_name double-conversion
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.0.2.0
Release:        0
Summary:        Fast conversion between double precision floating point and text
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  libstdc++-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
A library that performs fast, accurate conversion between double precision
floating point and text.

This library is implemented as bindings to the C++ 'double-conversion' library
written by Florian Loitsch at Google:
<https://github.com/floitsch/double-conversion>.

The 'Text' versions of these functions are about 30 times faster than the
default 'show' implementation for the 'Double' type.

The 'ByteString' versions are /slower/ than the 'Text' versions; roughly half
the speed. (This seems to be due to the cost of allocating 'ByteString' values
via 'malloc'.)

As a final note, be aware that the 'bytestring-show' package is about 50%
slower than simply using 'show'.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       libstdc++-devel
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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc README.markdown

%changelog
