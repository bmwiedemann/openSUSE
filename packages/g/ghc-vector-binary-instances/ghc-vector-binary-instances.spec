#
# spec file for package ghc-vector-binary-instances
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


%global pkg_name vector-binary-instances
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.5.1
Release:        0
Summary:        Instances of Data.Binary for vector
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Instances for Binary for the types defined in the vector package, making it
easy to serialize vectors to and from disk. We use the generic interface to
vectors, so all vector types are supported. Specific instances are provided for
unboxed, boxed and storable vectors.

To serialize a vector:

> *Data.Vector.Binary> let v = Data.Vector.fromList [1..10] >
*Data.Vector.Binary> v > fromList [1,2,3,4,5,6,7,8,9,10] :: Data.Vector.Vector
> *Data.Vector.Binary> encode v > Chunk
"NULNULNULNULNUL...NULNULNULtNULNULNULNULn" Empty

Which you can in turn compress before writing to disk:

> compress . encode $ v > Chunk "US139bNULNULN...229240,254:NULNULNUL" Empty

Try the cereal-vector package if you are looking for Data.Serialize instances.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library
development files.

%prep
%autosetup -n %{pkg_name}-%{version}
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

%changelog
