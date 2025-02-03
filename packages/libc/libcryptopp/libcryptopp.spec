#
# spec file for package libcryptopp
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


%define major 8
%define minor 9
%define patchlevel 0
%define pkg_version %{major}%{minor}%{patchlevel}
# There is no upstream interface version information.
# Therefore we need unique basenames (see boo#1027192):
%define sover %{major}_%{minor}_%{patchlevel}
Name:           libcryptopp
# WARNING: Execute "sh precheckin_baselibs.sh" to update baselibs.conf
# WARNING: uses source tarball name to create lib name.
Version:        %{major}.%{minor}.%{patchlevel}
Release:        0
Summary:        Cryptographic library for C++
License:        BSL-1.0
URL:            https://www.cryptopp.com
Source:         https://github.com/weidai11/cryptopp/archive/CRYPTOPP_%{major}_%{minor}_%{patchlevel}.tar.gz
Source1:        precheckin_baselibs.sh
Source2:        baselibs.conf
# PATCH-FEATURE-OPENSUSE libcryptopp-shared.patch -- improve shared library creation
Patch1:         libcryptopp-shared.patch
# CVE-2023-50980 [bsc#1218219], DoS via malformed DER public key file
Patch2:         libcryptopp-CVE-2023-50980.patch
# CVE-2023-50981 [bsc#1218222], issue on ModularSquareRoot function leads to potential DoS
Patch3:         libcryptopp-CVE-2023-50981.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
The Crypto++ library is a C++ class library of cryptographic schemes.
Also contains:
pseudo random number generators (PRNG): ANSI X9.17 appendix C,
RandomPool, RDRAND, RDSEED, NIST Hash DRBG.

%package -n %{name}%{sover}
Summary:        Cryptographic Library for C++
Obsoletes:      %{name}%{major}_%{minor} = %{version}

%description -n %{name}%{sover}
The Crypto++ library provides authenticated encryption, stream and
block ciphers, block cipher operation modes, message authentication
codes, hash functions, PKI crypto, key agreement schemes and elliptic
curve crypto.

%package -n %{name}-devel
Summary:        Development files for libcryptopp, a cryptographic library for C++
Requires:       %{name}%{sover} = %{version}
Obsoletes:      %{name}-devel-static <= %{version}

%description -n %{name}-devel
The Crypto++ library provides authenticated encryption, stream and
block ciphers, block cipher operation modes, message authentication
codes, hash functions, PKI crypto, key agreement schemes and elliptic
curve crypto. This package is used for crypto++ development.

%prep
%autosetup -p1 -n "cryptopp-CRYPTOPP_%{major}_%{minor}_%{patchlevel}"

%build
%ifarch %{arm} i586
%define _lto_cflags %{nil}
%endif
CXXFLAGS="-DNDEBUG %{optflags} -fpic -fPIC -pthread -fopenmp"
%ifarch i586
  CXXFLAGS="$CXXFLAGS -mmmx -msse2"
%endif
# aarch64 arm -march=armv7-a -mfpu=neon
%ifarch ppc64
CXXFLAGS="$CXXFLAGS -DCRYPTOPP_DISABLE_ALTIVEC"
%endif
%make_build \
    CXXFLAGS="$CXXFLAGS" \
    DESTDIR="" \
    PREFIX="%{_prefix}" \
    LIB="%{_lib}" \
    CXX="g++" \
    LIBSUFFIX="-%{version}" \
    LDFLAGS="-pthread" \
    all static

%install
%make_install \
    PREFIX="%{_prefix}" \
    LIB="%{_lib}" \
    LIBSUFFIX="-%{version}"

rm -rf "%{buildroot}%{_bindir}" %{buildroot}%{_datadir}/cryptopp
rm -rf %{buildroot}%{_libdir}/*.a
dos2unix Readme.txt
# Install .pc file with correct version field.
mkdir %{buildroot}%{_libdir}/pkgconfig/
cat > %{buildroot}%{_libdir}/pkgconfig/cryptopp.pc <<EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name:           libcrypto++
Description:    General purpose cryptographic shared library
URL:            https://www.cryptopp.com
Version:        %{version}
Libs: -lcryptopp
Cflags:
EOF

%check
%ifnarch i586
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %make_build test
%endif

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%{_libdir}/libcryptopp.so.%{major}.*
%license License.txt

%files -n %{name}-devel
%doc Readme.txt
%{_includedir}/cryptopp
%{_libdir}/libcryptopp.so
%{_libdir}/libcryptopp.so.%{major}
%{_libdir}/pkgconfig/cryptopp.pc

%changelog
