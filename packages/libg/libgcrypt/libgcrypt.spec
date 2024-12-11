#
# spec file for package libgcrypt
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


%define libsover 20
%define libsoname %{name}%{libsover}
%define hmac_key orboDeJITITejsirpADONivirpUkvarP
Name:           libgcrypt
Version:        1.11.0
Release:        0
Summary:        The GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://gnupg.org/software/libgcrypt
Source:         https://gnupg.org/ftp/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2.sig
Source2:        baselibs.conf
Source3:        random.conf
Source4:        hwf.deny
# https://www.gnupg.org/signature_key.html
Source5:        https://gnupg.org/signature_key.asc#/%{name}.keyring
Source99:       libgcrypt.changes
Patch1:         libgcrypt-1.10.0-allow_FSM_same_state.patch
#PATCH-FIX-OPENSUSE Do not pull revision info from GIT when autoconf is run
Patch2:         libgcrypt-nobetasuffix.patch
# FIPS patches:
#PATCH-FIX-SUSE bsc#1190700 FIPS: Provide a service-level indicator for PK
Patch100:       libgcrypt-FIPS-SLI-pk.patch
#PATCH-FIX-SUSE bsc#1190700 FIPS: Check keylength in gcry_fips_indicator_kdf()
Patch101:       libgcrypt-FIPS-SLI-kdf-leylength.patch
#PATCH-FIX-SUSE bsc#1190700 FIPS add indicators
Patch102:       libgcrypt-FIPS-SLI-hash-mac.patch
#PATCH-FIX-SUSE bsc#1202117 FIPS: Get most of the entropy from rndjent_poll
Patch104:       libgcrypt-FIPS-rndjent_poll.patch
#PATCH-FIX-SUSE bsc#1220896 FIPS: Replace the built-in jitter rng with standalone version
Patch105:       libgcrypt-FIPS-jitter-standalone.patch
#PATCH-FIX-SUSE bsc#1220895 FIPS: Enforce the interpretation and use of jitter rng
Patch106:       libgcrypt-FIPS-jitter-errorcodes.patch
#PATCH-FIX-SUSE bsc#1220893 FIPS: Use Jitter RNG for the whole length entropy buffer
Patch107:       libgcrypt-FIPS-jitter-whole-entropy.patch
BuildRequires:  automake >= 1.14
BuildRequires:  libgpg-error-devel >= 1.49
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
%{?suse_build_hwcaps_libs}

%description
Libgcrypt is a general purpose library of cryptographic building
blocks.  It is originally based on code used by GnuPG.  It does not
provide any implementation of OpenPGP or other protocols.  Thorough
understanding of applied cryptography is required to use Libgcrypt.

%package -n %{libsoname}
Summary:        The GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
BuildRequires:  jitterentropy-devel >= 3.4.0
Requires:       libjitterentropy3 >= 3.4.0
Provides:       %{libsoname}-hmac = %{version}-%{release}
Obsoletes:      %{libsoname}-hmac < %{version}-%{release}

%description -n %{libsoname}
Libgcrypt is a general purpose crypto library based on the code used in
GnuPG (alpha version).

%package devel
Summary:        The GNU Crypto Library
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       glibc-devel
Requires:       jitterentropy-devel >= 3.4.0
Requires:       libgpg-error-devel >= 1.49

%description devel
Libgcrypt is a general purpose library of cryptographic building
blocks.  It is originally based on code used by GnuPG.  It does not
provide any implementation of OpenPGP or other protocols.  Thorough
understanding of applied cryptography is required to use Libgcrypt.

This package contains needed files to compile and link against the
library.

%prep
%autosetup -p1

# Rename the internal .hmac file to include the so library version
sed -i "s/libgcrypt\.so\.hmac/\.libgcrypt\.so\.%{libsover}\.hmac/g" src/Makefile.am src/Makefile.in

# Replace the built-in jitter rng with the standalone version [bsc#1220896]
find . -type f -name "jitterentropy*" -print -delete

%build
export PUBKEYS="dsa elgamal rsa ecc"
export CIPHERS="arcfour blowfish cast5 des aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20 sm4 aria"
export DIGESTS="crc gostr3411-94 md4 md5 rmd160 sha1 sha256 sha512 sha3 tiger whirlpool stribog blake2 sm3"
export KDFS="s2k pkdf2 scrypt"

autoreconf -fi
date=$(date -u '+%%Y-%%m-%%dT%%H:%%M+0000' -r %{SOURCE99})
sed -e "s,BUILD_TIMESTAMP=.*,BUILD_TIMESTAMP=$date," -i configure
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
%configure \
           --with-fips-module-version="Libgcrypt version %{version}-%{release}" \
           --enable-hmac-binary-check="%{hmac_key}" \
           --enable-ciphers="$CIPHERS" \
           --enable-pubkey-ciphers="$PUBKEYS" \
           --enable-digests="$DIGESTS" \
           --enable-kdfs="$KDFS" \
           --enable-noexecstack \
           --disable-static \
%ifarch %{sparc}
           --disable-asm \
%endif
           --enable-random=getentropy \
           --enable-jent-support \
           %{nil}

%make_build

%check
make -k check
# run the regression tests also in FIPS mode
LIBGCRYPT_FORCE_FIPS_MODE=1 make -k check || true

%install
%make_install

# this is a hack that re-defines the __spec_install_post macro
# for a simple reason: the macro strips the binaries and thereby
# invalidates a HMAC that may have been created earlier.
# solution: create the hashes _after_ the macro runs.
%define libpath %{buildroot}%{_libdir}/libgcrypt.so.%{libsover}.?.?
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    cd src \
    sed -i -e 's|FILE=.*|FILE=\\\$1|' gen-note-integrity.sh \
    READELF=readelf AWK=awk ECHO_N="-n" bash gen-note-integrity.sh %{libpath} > %{libpath}.hmac \
    objcopy --update-section .note.fdo.integrity=%{libpath}.hmac %{libpath} %{libpath}.new \
    mv -f %{libpath}.new %{libpath} \
    rm -f %{libpath}.hmac \
%{nil}

rm %{buildroot}%{_libdir}/%{name}.la

# Create /etc/gcrypt directory and install random.conf
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/gcrypt
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/gcrypt/random.conf
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/gcrypt/hwf.deny

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%license COPYING COPYING.LIB LICENSES
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_libdir}/%{name}.so.*
%dir %{_sysconfdir}/gcrypt
%config(noreplace) %{_sysconfdir}/gcrypt/random.conf
%config(noreplace) %{_sysconfdir}/gcrypt/hwf.deny

%files devel
%license COPYING COPYING.LIB LICENSES
%{_bindir}/dumpsexp
%{_bindir}/hmac256
%{_bindir}/mpicalc
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libgcrypt.pc
%{_datadir}/aclocal/%{name}.m4
%{_includedir}/gcrypt*.h
%{_infodir}/gcrypt.info*%{ext_info}*
%{_mandir}/man1/*

%changelog
