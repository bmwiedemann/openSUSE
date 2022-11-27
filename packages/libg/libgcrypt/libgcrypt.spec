#
# spec file for package libgcrypt
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


%define build_hmac256 1
%define libsover 20
%define libsoname %{name}%{libsover}
%define hmac_key orboDeJITITejsirpADONivirpUkvarP
Name:           libgcrypt
Version:        1.10.1
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
# https://gnupg.org/signature_key.asc
Source5:        libgcrypt.keyring
Source99:       libgcrypt.changes
Patch1:         libgcrypt-1.10.0-allow_FSM_same_state.patch
#PATCH-FIX-UPSTREAM bsc#1190700 FIPS: Provide a service-level indicator for PK
Patch2:         libgcrypt-FIPS-SLI-pk.patch
#PATCH-FIX-SUSE bsc#1190700 FIPS add indicators
Patch3:         libgcrypt-FIPS-SLI-hash-mac.patch
#PATCH-FIX-SUSE bsc#1190700 FIPS: Check keylength in gcry_fips_indicator_kdf()
Patch4:         libgcrypt-FIPS-SLI-kdf-leylength.patch
#PATCH-FIX-SUSE bsc#1182983 gpg: out of core handler ignored in FIPS mode while typing Tab key to Auto-Completion
Patch5:         libgcrypt-1.10.0-out-of-core-handler.patch
#PATCH-FIX-UPSTREAM bsc#1202117 jsc#SLE-24941 FIPS: Port libgcrypt to use jitterentropy
Patch6:         libgcrypt-jitterentropy-3.4.0.patch
#PATCH-FIX-SUSE bsc#1202117 FIPS: Get most of the entropy from rndjent_poll
Patch7:         libgcrypt-FIPS-rndjent_poll.patch
#PATCH-FIX-SUSE Check the FIPS "module is complete" trigger file .fips
Patch8:         libgcrypt-1.10.0-use-fipscheck.patch
BuildRequires:  automake >= 1.14
BuildRequires:  libgpg-error-devel >= 1.27
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig

%description
Libgcrypt is a general purpose library of cryptographic building
blocks.  It is originally based on code used by GnuPG.  It does not
provide any implementation of OpenPGP or other protocols.  Thorough
understanding of applied cryptography is required to use Libgcrypt.

%package -n %{libsoname}
Summary:        The GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Suggests:       %{libsoname}-hmac = %{version}-%{release}

%description -n %{libsoname}
Libgcrypt is a general purpose crypto library based on the code used in
GnuPG (alpha version).

%package -n %{libsoname}-hmac
Summary:        HMAC checksums for the GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{libsoname} = %{version}-%{release}

%description -n %{libsoname}-hmac
Libgcrypt is a general purpose crypto library based on the code used in
GnuPG (alpha version). This package contains the HMAC checksum files
for integrity checking the library, as required by FIPS 140-2.

%package devel
Summary:        The GNU Crypto Library
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       glibc-devel
Requires:       libgpg-error-devel >= 1.27

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

%build
echo building with build_hmac256 set to %{build_hmac256}

export PUBKEYS="dsa elgamal rsa ecc"
export CIPHERS="arcfour blowfish cast5 des aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20 sm4"
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
           --enable-m-guard \
%ifarch %{sparc}
           --disable-asm \
%endif
           --enable-random=getentropy \
           %{nil}

%make_build

%check
%make_build check
# run the regression tests also in FIPS mode
LIBGCRYPT_FORCE_FIPS_MODE=1 make -k check VERBOSE=1 || true

# Install the FIPS hmac file
cp src/.libgcrypt.so.%{libsover}.hmac %{buildroot}%{_libdir}/

# create the FIPS "module is complete" trigger file
%if 0%{?build_hmac256}
touch %{buildroot}%{_libdir}/.%{name}.so.%{libsover}.fips
%endif

%install
%make_install
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

%files -n %{libsoname}-hmac
%{_libdir}/.libgcrypt.so.*.hmac
%if 0%{?build_hmac256}
%{_libdir}/.libgcrypt.so.*.fips
%endif

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
