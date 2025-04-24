#
# spec file for package libgcrypt
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
#PATCH-FIX-SUSE Remove not used rol64() definition after removing the built-in jitter rng
Patch108:       libgcrypt-rol64-redefinition.patch
#PATCH-FIX-UPSTREAM jsc#PED-12227: SLI revamp and differentiate SHA1 in the service level indicator
Patch200:       libgcrypt-fips-Introduce-an-internal-API-for-FIPS-service-indicator.patch
Patch201:       libgcrypt-fips-Introduce-GCRYCTL_FIPS_SERVICE_INDICATOR-and-the-macro.patch
Patch202:       libgcrypt-fips-kdf-Implement-new-FIPS-service-indicator-for-gcry_kdf_derive.patch
Patch203:       libgcrypt-fips-md-Implement-new-FIPS-service-indicator-for-gcry_md_hash_.patch
Patch204:       libgcrypt-fips-tests-Add-t-digest.patch
Patch205:       libgcrypt-fips-Change-the-internal-API-for-new-FIPS-service-indicator.patch
Patch206:       libgcrypt-fips-md-Implement-new-FIPS-service-indicator-for-gcry_md_open-API.patch
Patch207:       libgcrypt-fips-tests-Add-tests-for-md_open-write-read-close-for-t-digest.patch
Patch208:       libgcrypt-fips-mac-Implement-new-FIPS-service-indicator-for-gcry_mac_open.patch
Patch209:       libgcrypt-fips-cipher-Implement-new-FIPS-service-indicator-for-cipher_open.patch
Patch210:       libgcrypt-tests-fips-Add-gcry_mac_open-tests.patch
Patch211:       libgcrypt-tests-fips-Rename-t-fips-service-ind.patch
Patch212:       libgcrypt-tests-fips-Move-KDF-tests-to-t-fips-service-ind.patch
Patch213:       libgcrypt-tests-fips-Add-gcry_cipher_open-tests.patch
Patch214:       libgcrypt-fips-md-gcry_md_copy-should-care-about-FIPS-service-indicator.patch
Patch215:       libgcrypt-fips-cipher-Implement-FIPS-service-indicator-for-gcry_pk_hash_-API.patch
Patch216:       libgcrypt-fips-Introduce-GCRYCTL_FIPS_REJECT_NON_FIPS.patch
Patch217:       libgcrypt-Fix-the-previous-change.patch
Patch218:       libgcrypt-fips-Rejection-by-GCRYCTL_FIPS_REJECT_NON_FIPS-not-by-open-flags.patch
Patch219:       libgcrypt-fips-cipher-Add-behavior-not-to-reject-but-mark-non-compliant.patch
Patch220:       libgcrypt-fips-ecc-Add-rejecting-or-marking-for-gcry_pk_get_curve.patch
Patch221:       libgcrypt-tests-Add-more-tests-to-tests-t-fips-service-ind.patch
Patch222:       libgcrypt-fips-ecc-Check-DATA-in-gcry_pk_sign-verify-in-FIPS-mode.patch
Patch223:       libgcrypt-fips-cipher-Fix-memory-leak-for-gcry_pk_hash_sign.patch
Patch224:       libgcrypt-build-Improve-__thread-specifier-check.patch
Patch225:       libgcrypt-cipher-Check-and-mark-non-compliant-cipher-modes-in-the-SLI.patch
Patch226:       libgcrypt-cipher-Rename-_gcry_cipher_is_mode_fips_compliant.patch
Patch227:       libgcrypt-cipher-Don-t-differentiate-GCRY_CIPHER_MODE_CMAC-in-FIPS-mode.patch
Patch228:       libgcrypt-cipher-rsa-Mark-reject-SHA1-unknown-with-RSA-signature-generation.patch
Patch229:       libgcrypt-md-Fix-gcry_md_algo_info-to-mark-reject-under-FIPS-mode.patch
Patch230:       libgcrypt-md-Use-check_digest_algo_spec-in-_gcry_md_selftest.patch
Patch231:       libgcrypt-tests-Update-t-fips-service-ind-using-GCRY_MD_SHA256-for-KDF-tests.patch
Patch232:       libgcrypt-fips-cipher-Do-the-computation-when-marking-non-compliant.patch
Patch233:       libgcrypt-tests-Allow-tests-with-USE_RSA.patch
Patch234:       libgcrypt-cipher-Add-KAT-for-non-rfc6979-ECDSA-with-fixed-k.patch
Patch235:       libgcrypt-cipher-Differentiate-use-of-label-K-in-the-SLI.patch
Patch236:       libgcrypt-cipher-Differentiate-igninvflag-in-the-SLI.patch
Patch237:       libgcrypt-cipher-Differentiate-no-blinding-flag-in-the-SLI.patch
Patch238:       libgcrypt-fips-cipher-Add-GCRY_FIPS_FLAG_REJECT_PK_FLAGS.patch
Patch239:       libgcrypt-cipher-ecc-Fix-for-supplied-K.patch
Patch240:       libgcrypt-cipher-visibility-Differentiate-use-of-random-override-in-the-SLI.patch
Patch241:       libgcrypt-cipher-fips-Fix-for-random-override.patch
Patch243:       libgcrypt-md-Make-SHA-1-non-FIPS-internally-for-1.12-API.patch
Patch244:       libgcrypt-fips-Fix-GCRY_FIPS_FLAG_REJECT_MD.patch
Patch245:       libgcrypt-doc-Add-about-GCRYCTL_FIPS_SERVICE_INDICATOR.patch
Patch246:       libgcrypt-doc-Fix-syntax-error.patch

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
LIBGCRYPT_FORCE_FIPS_MODE=1 make -k check

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
