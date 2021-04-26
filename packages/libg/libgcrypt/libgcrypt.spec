#
# spec file for package libgcrypt
#
# Copyright (c) 2021 SUSE LLC
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
%define separate_hmac256_binary 0
%define libsover 20
%define libsoname %{name}%{libsover}
%define cavs_dir %{_libexecdir}/%{name}/cavs
Name:           libgcrypt
Version:        1.9.3
Release:        0
Summary:        The GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://directory.fsf.org/wiki/Libgcrypt
Source:         https://gnupg.org/ftp/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2.sig
Source2:        baselibs.conf
# https://www.gnupg.org/signature_key.en.html
Source4:        libgcrypt.keyring
# cavs test framework
Source5:        cavs-test.sh
Source6:        cavs_driver.pl
Source7:        random.conf
Source99:       libgcrypt.changes
Patch1:         libgcrypt-1.4.1-rijndael_no_strict_aliasing.patch
Patch2:         libgcrypt-sparcv9.diff
#PATCH-FIX-SUSE: N/A
Patch3:         libgcrypt-1.5.0-LIBGCRYPT_FORCE_FIPS_MODE-env.diff
Patch4:         libgcrypt-1.6.1-use-fipscheck.patch
Patch5:         libgcrypt-1.6.1-fips-cavs.patch
Patch6:         libgcrypt-fix-rng.patch
#PATCH-FIX-SUSE add FIPS CAVS test app for DRBG
Patch7:         drbg_test.patch
#PATCH-FIX-UPSTREAM bsc#1064455 fipsdrv patch to enable --algo for dsa-sign
Patch8:         libgcrypt-fipsdrv-enable-algo-for-dsa-sign.patch
#PATCH-FIX-UPSTREAM bsc#1064455 fipsdrv patch to enable --algo for dsa-verify
Patch9:         libgcrypt-fipsdrv-enable-algo-for-dsa-verify.patch
Patch10:        libgcrypt-1.8.3-fips-ctor.patch
Patch11:        libgcrypt-1.8.4-use_xfree.patch
Patch12:        libgcrypt-1.8.4-allow_FSM_same_state.patch
Patch13:        libgcrypt-1.8.4-getrandom.patch
Patch14:        libgcrypt-1.8.4-fips_ctor_skip_integrity_check.patch
#PATCH-FIX-SUSE Fix test in FIPS mode
Patch15:        libgcrypt-dsa-rfc6979-test-fix.patch
Patch16:        libgcrypt-fix-tests-fipsmode.patch
#PATCH-FIX-SUSE bsc#1155337 FIPS: RSA/DSA/ECDSA are missing hashing operation
Patch17:        libgcrypt-FIPS-RSA-DSA-ECDSA-hashing-operation.patch
#PATCH-FIX-SUSE bsc#1161220 FIPS: libgcrypt RSA siggen/keygen: 4k not supported
Patch18:        libgcrypt-1.8.4-fips-keygen.patch
#PATCH-FIX-SUSE bsc#1164950 Run self-tests from the constructor
Patch19:        libgcrypt-invoke-global_init-from-constructor.patch
#PATCH-FIX-SUSE bsc#1164950 Restore the self-tests from the constructor
Patch20:        libgcrypt-Restore-self-tests-from-constructor.patch
Patch21:        libgcrypt-FIPS-GMAC_AES-benckmark.patch
Patch22:        libgcrypt-global_init-constructor.patch
Patch23:        libgcrypt-random_selftests-testentropy.patch
Patch24:        libgcrypt-rsa-no-blinding.patch
Patch25:        libgcrypt-ecc-ecdsa-no-blinding.patch
#PATCH-FIX-SUSE bsc#1165539 FIPS: Use the new signature operation in PCT
Patch26:        libgcrypt-PCT-RSA.patch
Patch27:        libgcrypt-PCT-DSA.patch
Patch28:        libgcrypt-PCT-ECC.patch
Patch29:        libgcrypt-fips_selftest_trigger_file.patch
BuildRequires:  automake >= 1.14
BuildRequires:  fipscheck
BuildRequires:  libgpg-error-devel >= 1.27
BuildRequires:  libtool
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

%package cavs
Summary:        The GNU Crypto Library
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       %{libsoname}-hmac

%description cavs
CAVS testing framework for libgcrypt

%if 0%{?separate_hmac256_binary}
%package hmac256
Summary:        The GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       libgpg-error-devel >= 1.27

%description hmac256
Libgcrypt is a general purpose library of cryptographic building
blocks.  It is originally based on code used by GnuPG.  It does not
provide any implementation of OpenPGP or other protocols.  Thorough
understanding of applied cryptography is required to use Libgcrypt.

%endif

%prep
%setup -q
%autopatch -p1

%build
echo building with build_hmac256 set to %{build_hmac256}
autoreconf -fi
date=$(date -u +%{Y}-%{m}-%{dT}%{H}:%{M}+0000 -r %{SOURCE99})
sed -e "s,BUILD_TIMESTAMP=.*,BUILD_TIMESTAMP=$date," -i configure
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
%configure \
           --enable-noexecstack \
           --disable-static \
           --enable-m-guard \
%ifarch %{sparc}
           --disable-asm \
%endif
           --enable-hmac-binary-check \
           --enable-random=linux
%make_build

%if 0%{?build_hmac256}
# this is a hack that re-defines the __os_install_post macro
# for a simple reason: the macro strips the binaries and thereby
# invalidates a HMAC that may have been created earlier.
# solution: create the hashes _after_ the macro runs.
#
# this shows up earlier because otherwise the %%expand of
# the macro is too late.
%{expand:%%global __os_install_post {%__os_install_post
    fipshmac %{buildroot}/%{_bindir}/hmac256
    fipshmac %{buildroot}/%{_libdir}/*.so.??
}}
%endif

%check
fipshmac src/.libs/libgcrypt.so.??
%make_build check

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la

# cavs
install -m 0755 -d %{buildroot}%{cavs_dir}
install -m 0755 %{SOURCE5} %{buildroot}%{cavs_dir}
install -m 0755 %{SOURCE6} %{buildroot}%{cavs_dir}

mv %{buildroot}%{_bindir}/fipsdrv %{buildroot}%{cavs_dir}
mv %{buildroot}%{_bindir}/drbg_test %{buildroot}%{cavs_dir}

# create the FIPS "module is complete" trigger file
%if 0%{?build_hmac256}
touch %{buildroot}/%{_libdir}/.%{name}.so.%{libsover}.fips
%endif

# Create /etc/gcrypt directory and install random.conf
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/gcrypt
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/gcrypt/random.conf

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%license COPYING.LIB
%{_libdir}/%{name}.so.*
%dir %{_sysconfdir}/gcrypt
%config(noreplace) %{_sysconfdir}/gcrypt/random.conf
%if 0%{?build_hmac256}
%{_libdir}/.libgcrypt.so.*.hmac
%endif

%files -n %{libsoname}-hmac
%if 0%{?build_hmac256}
%{_libdir}/.libgcrypt.so.*.fips
%endif

%files devel
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_infodir}/gcrypt.info*%{ext_info}
%{_bindir}/dumpsexp
%{_bindir}/mpicalc
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_includedir}/gcrypt*.h
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/pkgconfig/libgcrypt.pc

%if 0%{?separate_hmac256_binary}
%files hmac256
%endif
%{_bindir}/hmac256
%{_bindir}/.hmac256.hmac
%doc %{_mandir}/man1/hmac256.1*

%files cavs
%{_libexecdir}/%{name}

%changelog
