#
# spec file for package ghc-cprng-aes
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


%global pkg_name cprng-aes
Name:           ghc-%{pkg_name}
Version:        0.6.1
Release:        0
Summary:        Crypto Pseudo Random Number Generator using AES in counter mode
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cipher-aes-devel
BuildRequires:  ghc-crypto-random-devel
BuildRequires:  ghc-rpm-macros

%description
Simple crypto pseudo-random-number-generator with really good randomness
property.

Using ent, a randomness property maker on one 1Mb sample: Entropy = 7.999837
bits per byte. Optimum compression would reduce the size of this 1048576 byte
file by 0 percent. Chi square distribution for 1048576 samples is 237.02
Arithmetic mean value of data bytes is 127.3422 (127.5 = random) Monte Carlo
value for Pi is 3.143589568 (error 0.06 percent)

Compared to urandom with the same sampling: Entropy = 7.999831 bits per byte.
Optimum compression would reduce the size of this 1048576 byte file by 0
percent. Chi square distribution for 1048576 samples is 246.63 Arithmetic mean
value of data bytes is 127.6347 (127.5 = random). Monte Carlo value for Pi is
3.132465868 (error 0.29 percent).

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
%dir %{_datadir}/%{pkg_name}-%{version}
%{_datadir}/%{pkg_name}-%{version}/README.md

%files devel -f %{name}-devel.files

%changelog
