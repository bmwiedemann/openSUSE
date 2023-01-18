#
# spec file for package ghc-double-conversion
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


%global pkg_name double-conversion
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.0.4.2
Release:        0
Summary:        Fast conversion between single and double precision floating point and text
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
Patch0:         riscv.patch
BuildRequires:  gcc-c++
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  libstdc++-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
A library that performs fast, accurate conversion between floating point and
text.

This library is implemented as bindings to the C++ 'double-conversion' library
written by Florian Loitsch at Google:
<https://github.com/floitsch/double-conversion>.

Now it can convert single precision numbers, and also it can create Builder,
instead of bytestring or text.

The 'Text' versions of these functions are about 30 times faster than the
default 'show' implementation for the 'Double' type.

The 'ByteString' versions are have very close speed to the 'Text' versions;

Builder versions (both for Text and Bytestring) are slower on single value, but
they are much faster on large number of values (up to 20x faster on list with
20000 doubles).

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
%autosetup -p1 -n %{pkg_name}-%{version}
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

%files devel -f %{name}-devel.files
%doc README.markdown

%changelog
