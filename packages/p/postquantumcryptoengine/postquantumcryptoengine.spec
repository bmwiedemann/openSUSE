#
# spec file for package postquantumcryptoengine
#
# Copyright (c) 2025 SUSE LLC
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


%define sover   1

Name:           postquantumcryptoengine
Version:        5.3.101
Release:        0
Summary:        Post-quantum cryptopgraphy extension for bctoolbox
License:        GPL-3.0-or-later
URL:            https://gitlab.linphone.org/BC/public/postquantumcryptoengine
Source:         https://gitlab.linphone.org/BC/public/postquantumcryptoengine/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  bctoolbox-devel >= %{version}
BuildRequires:  cmake >= 3.22
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  liboqs-devel >= 0.8

%description
An extension to the bctoolbox library providing post-quantum
cryptography algorithms.

%package -n lib%{name}%{sover}
Summary:        Post-quantum algorithm extension for bctoolbox
Group:          System/Libraries

%description -n lib%{name}%{sover}
An extension to the bctoolbox library providing post-quantum
cryptography algorithms:

* Kyber 512, 768 and 1024
* HQC 128, 192 and 256 (NIST round 3 version)
* X25519 and X448 in KEM version and a way to combine two or more of
  these

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DENABLE_UNIT_TESTS=OFF
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.md

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%dir %{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/*
%dir %{_datadir}/PostQuantumCryptoEngine
%dir %{_datadir}/PostQuantumCryptoEngine/cmake
%{_datadir}/PostQuantumCryptoEngine/cmake/*

%changelog
