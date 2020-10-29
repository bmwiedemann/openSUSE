#
# spec file for package libgcrypt
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


%define build_hmac256 1
%define separate_hmac256_binary 0
%define libsover 20
%define libsoname %{name}%{libsover}
%define cavs_dir %{_libexecdir}/%{name}/cavs
Name:           libgcrypt
Version:        1.8.7
Release:        0
Summary:        The GNU Crypto Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://directory.fsf.org/wiki/Libgcrypt
Source:         https://gnupg.org/ftp/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2.sig
Source2:        baselibs.conf
Source4:        %{name}.keyring
# https://www.gnupg.org/signature_key.en.html
# cavs test framework
Source5:        cavs-test.sh
Source6:        cavs_driver.pl
Source99:       %{name}.changes
Patch3:         %{name}-1.4.1-rijndael_no_strict_aliasing.patch
Patch4:         %{name}-sparcv9.diff
#PATCH-FIX-UPSTREAM: bnc#701267, explicitly link with $(DL_LIBS)
#was: libgcrypt-1.5.0-as-needed.patch
Patch5:         libgcrypt-unresolved-dladdr.patch
#PATCH-FIX-SUSE: N/A
Patch7:         libgcrypt-1.5.0-LIBGCRYPT_FORCE_FIPS_MODE-env.diff
Patch12:        libgcrypt-1.6.1-use-fipscheck.patch
Patch13:        libgcrypt-1.6.1-fips-cavs.patch
#PATCH-FIX-SUSE: bnc#724841, fix a random device opening routine
Patch14:        libgcrypt-1.6.1-fips-cfgrandom.patch
Patch28:        libgcrypt-fix-rng.patch
#PATCH-FIX-SUSE add FIPS CAVS test app for DRBG
Patch30:        drbg_test.patch
#PATCH-FIX-UPSTREAM bsc#1064455 fipsdrv patch to enable --algo for dsa-sign
Patch35:        libgcrypt-fipsdrv-enable-algo-for-dsa-sign.patch
#PATCH-FIX-UPSTREAM bsc#1064455 fipsdrv patch to enable --algo for dsa-verify
Patch36:        libgcrypt-fipsdrv-enable-algo-for-dsa-verify.patch
Patch39:        libgcrypt-1.8.3-fips-ctor.patch
Patch42:        libgcrypt-fips_rsa_no_enforced_mode.patch
Patch43:        libgcrypt-1.8.4-use_xfree.patch
Patch44:        libgcrypt-1.8.4-allow_FSM_same_state.patch
Patch45:        libgcrypt-1.8.4-getrandom.patch
#PATCH-FIX-UPSTREAM bsc#1138939 CVE-2019-12904 C implementation of AES is
#vulnerable to a flush-and-reload side-channel attack
Patch46:        libgcrypt-CVE-2019-12904-GCM-Prefetch.patch
Patch47:        libgcrypt-CVE-2019-12904-GCM.patch
Patch48:        libgcrypt-CVE-2019-12904-AES.patch
Patch49:        libgcrypt-1.8.4-fips_ctor_skip_integrity_check.patch
#PATCH-FIX-SUSE bsc#1155338 bsc#1155338 FIPS: CMAC AES and TDES self tests missing
Patch50:        libgcrypt-CMAC-AES-TDES-selftest.patch
#PATCH-FIX-SUSE Fix test in FIPS mode
Patch51:        libgcrypt-dsa-rfc6979-test-fix.patch
Patch52:        libgcrypt-fix-tests-fipsmode.patch
#PATCH-FIX-SUSE bsc#1155337 FIPS: RSA/DSA/ECDSA are missing hashing operation
Patch53:        libgcrypt-FIPS-RSA-DSA-ECDSA-hashing-operation.patch
#PATCH-FIX-SUSE bsc#1161220 FIPS: libgcrypt RSA siggen/keygen: 4k not supported
Patch54:        libgcrypt-1.8.4-fips-keygen.patch
#PATCH-FIX-SUSE bsc#1164950 Run self-tests from the constructor
Patch55:        libgcrypt-invoke-global_init-from-constructor.patch
#PATCH-FIX-SUSE bsc#1164950 Restore the self-tests from the constructor
Patch56:        libgcrypt-Restore-self-tests-from-constructor.patch
Patch57:        libgcrypt-FIPS-GMAC_AES-benckmark.patch
Patch58:        libgcrypt-global_init-constructor.patch
Patch59:        libgcrypt-random_selftests-testentropy.patch
Patch60:        libgcrypt-rsa-no-blinding.patch
Patch61:        libgcrypt-ecc-ecdsa-no-blinding.patch
#PATCH-FIX-SUSE bsc#1165539 FIPS: Use the new signature operation in PCT
Patch62:        libgcrypt-PCT-RSA.patch
Patch63:        libgcrypt-PCT-DSA.patch
Patch64:        libgcrypt-PCT-ECC.patch
Patch65:        libgcrypt-fips_selftest_trigger_file.patch
BuildRequires:  automake >= 1.14
BuildRequires:  fipscheck
BuildRequires:  libgpg-error-devel >= 1.25
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
Requires:       libgpg-error-devel >= 1.13
Requires(post): %{install_info_prereq}

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
Requires:       libgpg-error-devel
Requires(post): %{install_info_prereq}

%description hmac256
Libgcrypt is a general purpose library of cryptographic building
blocks.  It is originally based on code used by GnuPG.  It does not
provide any implementation of OpenPGP or other protocols.  Thorough
understanding of applied cryptography is required to use Libgcrypt.

%endif  # #if separate_hmac256_binary

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

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/gcrypt.info.gz

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gcrypt.info.gz

%files -n %{libsoname}
%license COPYING.LIB
%{_libdir}/%{name}.so.*
%if 0%{?build_hmac256}
%{_libdir}/.libgcrypt.so.*.hmac
%endif # %%if 0%%{?build_hmac256}

%files -n %{libsoname}-hmac
%if 0%{?build_hmac256}
%{_libdir}/.libgcrypt.so.*.fips
%endif # %%if 0%%{?build_hmac256}

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
%endif # %%if 0%%{?separate_hmac256_binary}
%{_bindir}/hmac256
%{_bindir}/.hmac256.hmac
%doc %{_mandir}/man1/hmac256.1*

%files cavs
%{_libexecdir}/%{name}

%changelog
