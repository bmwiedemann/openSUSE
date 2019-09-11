#
# spec file for package libcryptopp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define minor 2
%define patch 0
%define pkg_version %{major}%{minor}%{patch}

Name:           libcryptopp
# WARNING: Execute "sh precheckin_baselibs.sh" to update baselibs.conf
# WARNING: uses source tarball name to create lib name.
Version:        %{major}.%{minor}.%{patch}
Release:        0
# There is no upstream interface version information.
# Therefore we need unique basenames (see boo#1027192):
%define sover %{major}_%{minor}_%{patch}
Summary:        Cryptographic library for C++
License:        BSL-1.0
Group:          Development/Libraries/C and C++
Url:            http://www.cryptopp.com
Source:         https://github.com/weidai11/cryptopp/archive/CRYPTOPP_%{major}_%{minor}_%{patch}.tar.gz
Source1:        precheckin_baselibs.sh
Source2:        baselibs.conf
# PATCH-FEATURE-OPENSUSE libcryptopp-shared.patch -- improve shared library creation
Patch1:         libcryptopp-shared.patch
# PATCH-UPSTREAM from git see https://github.com/weidai11/cryptopp/issues/865
Patch4:         0001-Fix-TCXXFLAGS-using-openSUSE-standard-flags-GH-865.patch
Patch5:         0001-Fix-missing-if-statement.patch
Patch6:         cve-2019-14318.patch
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Crypto++ library is a C++ class library of cryptographic schemes.
Also contains:
pseudo random number generators (PRNG): ANSI X9.17 appendix C,
RandomPool, RDRAND, RDSEED, NIST Hash DRBG.

%package -n %{name}%{sover}
Summary:        Cryptographic Library for C++
Group:          System/Libraries
Obsoletes:      %{name}%{major}_%{minor} = %{version}

%description -n %{name}%{sover}
The Crypto++ library provides authenticated encryption, stream and
block ciphers, block cipher operation modes, message authentication
codes, hash functions, PKI crypto, key agreement schemes and elliptic
curve crypto.

%package -n %{name}-devel
Summary:        Development files for libcryptopp, a cryptographic library for C++
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Obsoletes:      %{name}-devel-static

%description -n %{name}-devel
The Crypto++ library provides authenticated encryption, stream and
block ciphers, block cipher operation modes, message authentication
codes, hash functions, PKI crypto, key agreement schemes and elliptic
curve crypto. This package is used for crypto++ development.


%prep
%setup -q -n "cryptopp-CRYPTOPP_%{major}_%{minor}_%{patch}"
%patch1 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
echo %{major}.%{minor}.%{patch}
echo %{pkg_version}
#mv config.recommend config.h

%build
%ifarch %{arm} i586
%define _lto_cflags %{nil}
%endif
CXXFLAGS="-DNDEBUG %{optflags} -fpic -fPIC -pthread -fopenmp"
# aarch64 arm -march=armv7-a -mfpu=neon
%ifarch ppc64
CXXFLAGS="$CXXFLAGS -DCRYPTOPP_DISABLE_ALTIVEC"
%endif
make %{?_smp_mflags} \
    CXXFLAGS="$CXXFLAGS" \
    DESTDIR="" \
    PREFIX="%{_prefix}" \
    LIB="%{_lib}" \
    CXX="g++" \
    LIBSUFFIX="-%{version}" \
    LDFLAGS="-pthread" \
    all static

%install
make \
    DESTDIR=%{buildroot} \
    PREFIX="%{_prefix}" \
    LIB="%{_lib}" \
    LIBSUFFIX="-%{version}" \
    install

rm -rf "%{buildroot}%{_bindir}" %{buildroot}%{_datadir}/cryptopp
rm -rf "%{buildroot}%{_bindir}"
rm -rf %{buildroot}%{_libdir}/*.a
# Install .pc file with correct version field.
mkdir %{buildroot}%{_libdir}/pkgconfig/
echo "prefix=%{_prefix}" >%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "exec_prefix=\${prefix}" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "lib=%{_lib}" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "libdir=\${exec_prefix}/\${lib}" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "includedir=\${prefix}/include" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "Name: libcrypto++" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "Description: General purpose cryptographic shared library" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "URL: http://www.cryptopp.com" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "Version: %{version}" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "Requires:" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "Libs: -lcryptopp" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "Cflags:" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc
echo "" >>%{buildroot}%{_libdir}/pkgconfig/cryptopp.pc

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%{_libdir}/libcryptopp.so.%{major}.*
%license License.txt

%files -n %{name}-devel
%defattr(-,root,root)
%doc Readme.txt
%license License.txt
%{_includedir}/cryptopp
%{_libdir}/libcryptopp.so
%{_libdir}/pkgconfig/cryptopp.pc

%changelog
