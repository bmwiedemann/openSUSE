#
# spec file for package libsecp256k1
#
# Copyright (c) 2024 SUSE LLC
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


%define soname 5
Name:           libsecp256k1
Version:        0.6.0
Release:        0
Summary:        Optimized C library for EC operations on curve secp256k1
License:        MIT
Group:          System/Libraries
URL:            https://github.com/bitcoin/secp256k1
Source0:        https://github.com/bitcoin-core/secp256k1/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Optimized C library for EC operations on curve secp256k1.

%package -n %{name}-%{soname}
Summary:        Optimized C library for EC operations on curve secp256k1
Group:          System/Libraries

%description -n %{name}-%{soname}
The %{name} library is a work in progress and is being used to research best practices. Use at your own risk.

Features:
- secp256k1 ECDSA signing/verification and key generation.
- Adding/multiplying private/public keys.
- Serialization/parsing of private keys, public keys, signatures.
- Constant time, constant memory access signing and pubkey generation.
- Derandomized DSA (via RFC6979 or with a caller provided function.)
- Very efficient implementation.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{soname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%setup -q -n secp256k1-%{version}

%build
./autogen.sh
export CFLAGS_FOR_BUILD="%{optflags}"
%configure \
    --disable-static \
    --enable-module-ecdh \
    --enable-module-recovery \
    --enable-experimental
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -m 0644 -p -t %{buildroot}%{_libdir}/pkgconfig *.pc
find %{buildroot} -type f -name "*.la" -delete -print

%check
./tests

%post -n %{name}-%{soname} -p /sbin/ldconfig
%postun -n %{name}-%{soname} -p /sbin/ldconfig

%files -n %{name}-%{soname}
%{_libdir}/*.so.*
%license COPYING

%files devel
%{_includedir}/*.h
%{_libdir}/pkgconfig/libsecp256k1.pc
%{_libdir}/*.so
%doc README.md
%license COPYING

%changelog
