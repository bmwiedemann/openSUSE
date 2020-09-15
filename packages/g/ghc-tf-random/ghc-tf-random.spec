#
# spec file for package ghc-tf-random
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


%global pkg_name tf-random
Name:           ghc-%{pkg_name}
Version:        0.5
Release:        0
Summary:        High-quality splittable pseudorandom number generator
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel

%description
This package contains an implementation of a high-quality splittable
pseudorandom number generator. The generator is based on a cryptographic hash
function built on top of the ThreeFish block cipher. See the paper /Splittable
Pseudorandom Number Generators Using Cryptographic Hashing/ by Claessen, Pałka
for details and the rationale of the design.

The package provides the following:

* A splittable PRNG that implements the standard 'System.Random.RandomGen'
class.

* The generator also implements an alternative version of the
'System.Random.TF.Gen.RandomGen' class (exported from "System.Random.TF.Gen"),
which requires the generator to return pseudorandom integers from the full
32-bit range, and contains an n-way split function.

* An alternative version of the 'Random' class is provided, which is linked to
the new 'RandomGen' class, together with 'Random' instances for some integral
types.

* Two functions for initialising the generator with a non-deterministic seed:
one using the system time, and one using the '/dev/urandom' UNIX special file.

The package uses an adapted version of the reference C implementation of
ThreeFish from the reference package of the Skein hash function
(<https://www.schneier.com/skein.html>), originally written by Doug Whiting.

Please note that even though the generator provides very high-quality
pseudorandom numbers, it has not been designed with cryptographic applications
in mind.

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
%license LICENSE.brg LICENSE.tf
%doc ChangeLog

%changelog
