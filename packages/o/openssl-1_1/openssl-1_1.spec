#
# spec file for package openssl-1_1
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


%define livepatchable 1

%define ssletcdir %{_sysconfdir}/ssl
%define maj_min 1.1
%define _rname  openssl
%global sslengcnf %{ssletcdir}/engines1.1.d
%global sslengdef %{ssletcdir}/engdef1.1.d
Name:           openssl-1_1
# Don't forget to update the version in the "openssl" meta-package!
Version:        1.1.1w
Release:        0
Summary:        Secure Sockets and Transport Layer Security
License:        OpenSSL
Group:          Productivity/Networking/Security
URL:            https://www.openssl.org/
Source:         https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz
# to get mtime of file:
Source1:        %{name}.changes
Source2:        baselibs.conf
Source3:        https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz.asc
# https://www.openssl.org/about/
# http://pgp.mit.edu:11371/pks/lookup?op=get&search=0xA2D29B7BF295C759#/openssl.keyring
Source4:        %{_rname}.keyring
Source5:        showciphers.c
# PATCH-FIX-OPENSUSE: do not install html mans it takes ages
Patch1:         openssl-1.1.0-no-html.patch
Patch2:         openssl-truststore.patch
Patch3:         openssl-pkgconfig.patch
Patch4:         openssl-DEFAULT_SUSE_cipher.patch
Patch5:         openssl-ppc64-config.patch
Patch6:         openssl-riscv64-config.patch
# PATCH-FIX-UPSTREAM jsc#SLE-6126 and jsc#SLE-6129
Patch8:         0001-s390x-assembly-pack-perlasm-support.patch
Patch9:         0002-crypto-chacha-asm-chacha-s390x.pl-add-vx-code-path.patch
Patch10:        0003-crypto-poly1305-asm-poly1305-s390x.pl-add-vx-code-pa.patch
Patch11:        0004-s390x-assembly-pack-fix-formal-interface-bug-in-chac.patch
Patch12:        0005-s390x-assembly-pack-import-chacha-from-cryptogams-re.patch
Patch13:        0006-s390x-assembly-pack-import-poly-from-cryptogams-repo.patch
# PATCH-FIX-UPSTREAM bsc#1152695 jsc#SLE-7861 Support for CPACF enhancements - part 1 (crypto)
Patch16:        openssl-s390x-assembly-pack-add-OPENSSL_s390xcap-environment.patch
Patch17:        openssl-s390x-assembly-pack-add-support-for-pcc-and-kma-inst.patch
Patch18:        openssl-s390x-assembly-pack-add-OPENSSL_s390xcap-man-page.patch
Patch19:        openssl-s390x-assembly-pack-update-OPENSSL_s390xcap-3.patch
Patch20:        openssl-s390xcpuid.pl-fix-comment.patch
Patch21:        openssl-assembly-pack-accelerate-scalar-multiplication.patch
Patch22:        openssl-Enable-curve-spefific-ECDSA-implementations-via-EC_M.patch
Patch23:        openssl-s390x-assembly-pack-accelerate-ECDSA.patch
Patch24:        openssl-OPENSSL_s390xcap.pod-list-msa9-facility-bit-155.patch
Patch25:        openssl-s390x-assembly-pack-cleanse-only-sensitive-fields.patch
Patch26:        openssl-s390x-assembly-pack-fix-OPENSSL_s390xcap-z15-cpu-mas.patch
Patch27:        openssl-s390x-assembly-pack-fix-msa3-stfle-bit-detection.patch
Patch28:        openssl-Fix-9bf682f-which-broke-nistp224_method.patch
# FIPS patches
Patch30:        openssl-1.1.1-fips.patch
Patch31:        openssl-1.1.1-fips-post-rand.patch
Patch32:        openssl-1.1.1-fips-crng-test.patch
Patch33:        openssl-1.1.0-issuer-hash.patch
Patch34:        openssl-fips-run_selftests_only_when_module_is_complete.patch
Patch35:        openssl-ship_fips_standalone_hmac.patch
Patch36:        openssl-fips_mode.patch
Patch37:        openssl-1.1.1-evp-kdf.patch
Patch38:        openssl-1.1.1-ssh-kdf.patch
Patch40:        openssl-fips-selftests_in_nonfips_mode.patch
Patch41:        openssl-fips-clearerror.patch
Patch42:        openssl-fips-ignore_broken_atexit_test.patch
Patch45:        openssl-fips-add-SHA3-selftest.patch
Patch46:        openssl-fips_selftest_upstream_drbg.patch
Patch47:        openssl-unknown_dgst.patch
# PATCH-FIX-UPSTREAM jsc#SLE-7403 Support for CPACF enhancements - part 2 (crypto)
Patch50:        openssl-s390x-assembly-pack-accelerate-X25519-X448-Ed25519-and-Ed448.patch
Patch51:        openssl-s390x-fix-x448-and-x448-test-vector-ctime-for-x25519-and-x448.patch
# PATCH-FIX-UPSTREAM bsc#1175844 FIPS: (EC)Diffie-Hellman requirements
# from SP800-56Arev3 SLE-15-SP2
Patch52:        openssl-DH.patch
Patch53:        openssl-kdf-selftest.patch
Patch54:        openssl-kdf-tls-selftest.patch
Patch55:        openssl-kdf-ssh-selftest.patch
Patch56:        openssl-fips-DH_selftest_shared_secret_KAT.patch
# PATCH-FIX-UPSTREAM bsc#1192442 FIPS: missing KAT for HKDF/TLS 1.3/IPSEC IKEv2
Patch57:        openssl-fips-kdf-hkdf-selftest.patch
Patch58:        openssl-1.1.1-system-cipherlist.patch
# PATCH-FIX-OPENSUSE jsc#SLE-15832 Centralized Crypto Compliance Configuration
Patch59:        openssl-1_1-seclevel.patch
Patch60:        openssl-1_1-use-seclevel2-in-tests.patch
Patch61:        openssl-1_1-disable-test_srp-sslapi.patch
# PATCH-FIX-UPSTREAM jsc#SLE-18136 POWER10 performance enhancements for cryptography
Patch69:        openssl-1_1-Optimize-ppc64.patch
# PATCH-FIX-UPSTREAM jsc#SLE-19742 Backport Arm improvements from OpenSSL 3
Patch70:        openssl-1_1-Optimize-RSA-armv8.patch
Patch71:        openssl-1_1-Optimize-AES-XTS-aarch64.patch
Patch72:        openssl-1_1-Optimize-AES-GCM-uarchs.patch
# PATCH-FIX-SUSE bsc#1185320 FIPS: move the HMAC-SHA2-256 used for integrity test
Patch73:        openssl-FIPS-KAT-before-integrity-tests.patch
# PATCH-FIX-SUSE bsc#1182959 FIPS: Fix function and reason error codes
Patch74:        openssl-1_1-FIPS-fix-error-reason-codes.patch
#PATCH-FIX-SUSE bsc#1190652 FIPS: Add release number to version string
Patch75:        openssl-1_1-fips-bsc1190652_release_num_in_version_string.patch
# PATCH-FIX-SUSE bsc#1180995 Default to RFC7919 groups in FIPS mode
Patch76:        openssl-1_1-paramgen-default_to_rfc7919.patch
# PATCH-FIX-SUSE bsc#1194187 bsc#1004463 Add engines section in openssl.cnf
Patch77:        openssl-1_1-use-include-directive.patch
# PATCH-FIX-SUSE bsc#1197280 FIPS: Additional PBKDF2 requirements for KAT
Patch78:        openssl-1_1-FIPS-PBKDF2-KAT-requirements.patch
Patch79:        bsc1185319-FIPS-KAT-for-ECDSA.patch
Patch80:        bsc1198207-FIPS-add-hash_hmac-drbg-kat.patch
Patch82:        openssl-1_1-shortcut-test_afalg_aes_cbc.patch
# PATCH-FIX-SUSE bsc#1190653 FIPS: Provide methods to zeroize all unprotected SSPs and key components
Patch84:        openssl-1_1-Zeroization.patch
# PATCH-FIX-SUSE bsc#1190651 FIPS: Provide a service-level indicator
Patch85:        openssl-1_1-ossl-sli-000-fix-build-error.patch
Patch86:        openssl-1_1-ossl-sli-001-fix-faults-preventing-make-update.patch
Patch87:        openssl-1_1-ossl-sli-002-ran-make-update.patch
Patch88:        openssl-1_1-ossl-sli-003-add-sli.patch
# PATCH-FIX-SUSE bsc#1202148 FIPS: Port openssl to use jitterentropy
Patch89:        openssl-1_1-jitterentropy-3.4.0.patch
# PATCH-FIX-SUSE bsc#1203046 FIPS: Fix memory leak when FIPS mode is enabled
Patch90:        openssl-1.1.1-fips-fix-memory-leaks.patch
# PATCH-FIX-FEDORA bsc#1201293 FIPS: RAND api should call into FIPS DRBG
Patch91:        openssl-1_1-FIPS_drbg-rewire.patch
# PATCH-FIX-FEDORA bsc#1203069 FIPS: Add KAT for the RAND_DRBG implementation
Patch92:        openssl-1_1-fips-drbg-selftest.patch
# PATCH-FIX-SUSE bsc#1121365, bsc#1190888, bsc#1193859, bsc#1198471, bsc#1198472
# FIPS: List only approved digest and pubkey algorithms
Patch93:        openssl-1_1-fips-list-only-approved-digest-and-pubkey-algorithms.patch
# PATCH-FIX-SUSE bsc#1190651 FIPS: Provide a service-level indicator
Patch94:        openssl-1_1-ossl-sli-004-allow-aes-xts-256.patch
Patch95:        openssl-1_1-ossl-sli-005-EC_group_order_bits.patch
Patch96:        openssl-1_1-ossl-sli-006-rsa_pkcs1_padding.patch
Patch97:        openssl-1_1-ossl-sli-007-pbkdf2-keylen.patch
# PATCH-FIX-UPSTREAM jsc#PED-512
# POWER10 performance enhancements for cryptography
Patch98:        openssl-1_1-AES-GCM-performance-optimzation-with-stitched-method.patch
Patch99:        openssl-1_1-Fixed-counter-overflow.patch
Patch100:       openssl-1_1-chacha20-performance-optimizations-for-ppc64le-with-.patch
Patch101:       openssl-1_1-Fixed-conditional-statement-testing-64-and-256-bytes.patch
Patch102:       openssl-1_1-Fix-AES-GCM-on-Power-8-CPUs.patch
# PATCH-FIX-OPENSUSE bsc#1205042 Set OpenSSL 3.0 as the default openssl
Patch103:       openssl-1_1-openssl-config.patch
# PATCH-FIX-SUSE bsc#1207994 FIPS Make jitterentropy calls thread-safe
Patch104:       openssl-1_1-serialize-jitterentropy-calls.patch
# PATCH-FIX-SUSE bsc#1208998 FIPS: PBKDF2 requirements for openssl
Patch105:       openssl-1_1-ossl-sli-008-pbkdf2-salt_pass_iteration.patch
# PATCH-FIX-SUSE bsc#1212623 openssl s_client does not honor ocsp revocation status
Patch106:       openssl-s_client-check-ocsp-status.patch
# PATCH-FIX-SUSE bsc#1213517 Dont pass zero length input to EVP_Cipher
Patch107:       openssl-dont-pass-zero-length-input-to-EVP_Cipher.patch
#PATCH-FIX-SUSE bsc#1215215 FIPS: Add "fips" to version string
Patch108:       openssl-1_1-fips-bsc1215215_fips_in_version_string.patch
# PATCH-FIX-UPSTREAM jsc#PED-5086, jsc#PED-3514
# POWER10 performance enhancements for cryptography
Patch109:       openssl-ec-Use-static-linkage-on-nistp521-felem_-square-mul-.patch
Patch110:       openssl-ec-56-bit-Limb-Solinas-Strategy-for-secp384r1.patch
Patch111:       openssl-ec-powerpc64le-Add-asm-implementation-of-felem_-squa.patch
Patch112:       openssl-ecc-Remove-extraneous-parentheses-in-secp384r1.patch
Patch113:       openssl-powerpc-ecc-Fix-stack-allocation-secp384r1-asm.patch
Patch114:       openssl-Improve-performance-for-6x-unrolling-with-vpermxor-i.patch
# PATCH-FIX-UPSTREAM: bsc#1216922 CVE-2023-5678 Generating excessively long X9.42 DH keys or
# checking excessively long X9.42 DH keys or parameters may be very slow
Patch115:       openssl-CVE-2023-5678.patch
# PATCH-FIX-OPENSUSE skip SHA1 test in FIPS mode
Patch116:       openssl-Skip_SHA1-test-in-FIPS-mode.patch
# PATCH-FIX-UPSTREAM: bsc#1219243 CVE-2024-0727: denial of service via null dereference
Patch117:       openssl-CVE-2024-0727.patch
# PATCH-FIX-UPSTREAM: bsc#1222548 CVE-2024-2511: Unbounded memory growth with session handling in TLSv1.3
Patch118:       openssl-CVE-2024-2511.patch
# PATCH-FIX-UPSTREAM bsc#1225551 CVE-2024-4741: use After Free with SSL_free_buffers
Patch119:       openssl-CVE-2024-4741.patch
# PATCH-FIX-UPSTREAM: bsc#1227138 CVE-2024-5535: SSL_select_next_proto buffer overread
Patch120:       openssl-CVE-2024-5535.patch
Patch121:       reproducibledate.patch
BuildRequires:  jitterentropy-devel >= 3.4.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
Requires:       libjitterentropy3 >= 3.4.0
Provides:       ssl
Requires:       libopenssl1_1 = %{version}-%{release}
# Needed for clean upgrade path, boo#1070003
Obsoletes:      openssl-1_0_0
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      openssl-1_1_0
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
Requires:       crypto-policies
%endif
# ulp-macros is available according to SUSE version.
%ifarch x86_64
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1540
BuildRequires:  ulp-macros
%endif
%endif
%ifarch ppc64le
%if 0%{?sle_version} >= 150700 || 0%{?suse_version} >= 1570
BuildRequires:  gcc13
BuildRequires:  ulp-macros
%endif
%endif

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl1_1
Summary:        Secure Sockets and Transport Layer Security
Group:          Productivity/Networking/Security
Recommends:     ca-certificates-mozilla
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
Requires:       crypto-policies
%endif
Conflicts:      %{name} < %{version}-%{release}
# Merge back the hmac files bsc#1185116
Provides:       libopenssl1_1-hmac = %{version}-%{release}
Obsoletes:      libopenssl1_1-hmac < %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0-hmac
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-hmac

%description -n libopenssl1_1
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl-1_1-devel
Summary:        Development files for OpenSSL
Group:          Development/Libraries/C and C++
Requires:       jitterentropy-devel >= 3.4.0
Requires:       libopenssl1_1 = %{version}
Requires:       pkgconfig(zlib)
Recommends:     %{name} = %{version}
Conflicts:      ssl-devel
Provides:       ssl-devel
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl-1_1_0-devel
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-devel

%description -n libopenssl-1_1-devel
This subpackage contains header files for developing applications
that want to make use of the OpenSSL C API.

%package doc
Summary:        Additional Package Documentation
Group:          Productivity/Networking/Security
Conflicts:      openssl-doc
Provides:       openssl-doc = %{version}
Obsoletes:      openssl-doc < %{version}
BuildArch:      noarch

%description doc
This package contains optional documentation provided in addition to
this package's base documentation.

%prep
%autosetup -p1 -n %{_rname}-%{version}

cp apps/openssl.cnf apps/openssl-1_1.cnf

%build
%ifarch armv5el armv5tel
export MACHINE=armv5el
%endif
%ifarch armv6l armv6hl
export MACHINE=armv6l
%endif

# In ppc64le we need gcc-13 for userspace livepatching until we have the
# required -fpatchable-functions-entry patch merged into the mainline
%ifarch ppc64le
%if 0%{?sle_version} >= 150700 || 0%{?suse_version} >= 1570
export CC=gcc-13
export CXX=g++-13
%endif
%endif

./config \
    no-idea \
    no-afalgeng \
    enable-rfc3779 \
%ifarch x86_64 aarch64 ppc64le
    enable-ec_nistp_64_gcc_128 \
%endif
    enable-camellia \
    zlib \
    no-ec2m \
    --prefix=%{_prefix} \
    --libdir=%{_lib} \
    --openssldir=%{ssletcdir} \
    %{optflags} \
    %{?cflags_livepatching} \
    -Wa,--noexecstack \
    -Wl,-z,relro,-z,now \
    -fno-common \
    -DTERMIO \
    -DPURIFY \
    -D_GNU_SOURCE \
    -DOPENSSL_NO_BUF_FREELISTS \
    $(getconf LFS_CFLAGS) \
    -Wall \
    --with-rand-seed=getrandom \
    --system-ciphers-file=%{_sysconfdir}/crypto-policies/back-ends/openssl.config

# Show build configuration
perl configdata.pm --dump

util/mkdef.pl crypto update
%make_build depend
%make_build all

%check
export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
LD_LIBRARY_PATH=`pwd` make test -j1

# Create the hmac files required to run the regression tests in FIPS mode
LD_LIBRARY_PATH=`pwd` %{buildroot}%{_bindir}/fips_standalone_hmac \
 libssl.so.%{maj_min} > .libssl.so.%{maj_min}.hmac
LD_LIBRARY_PATH=`pwd` %{buildroot}%{_bindir}/fips_standalone_hmac \
 libcrypto.so.%{maj_min} > .libcrypto.so.%{maj_min}.hmac
OPENSSL_FORCE_FIPS_MODE=1 LD_LIBRARY_PATH=`pwd` make TESTS='-test_pem \
		       -test_hmac -test_mdc2 -test_dh -test_dsa -test_genrsa \
		       -test_mp_rsa -test_enc -test_enc_more -test_passwd -test_req \
		       -test_verify -test_evp -test_evp_extra -test_pkey_meth_kdf \
		       -test_bad_dtls -test_comp -test_key_share -test_renegotiation \
		       -test_sslcbcpadding -test_sslcertstatus -test_sslextension \
		       -test_sslmessages -test_sslrecords -test_sslsessiontick \
		       -test_sslsigalgs -test_sslsignature -test_sslskewith0p \
		       -test_sslversions -test_sslvertol -test_tls13alerts \
		       -test_tls13cookie -test_tls13downgrade -test_tls13hrr \
		       -test_tls13kexmodes -test_tls13messages -test_tls13psk \
		       -test_tlsextms -test_ca -test_cipherlist -test_cms \
		       -test_dtls_mtu -test_ssl_new -test_ssl_old -test_bio_enc \
		       -test_sslapi -test_tls13ccs -test_ec' test -j1

# show ciphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%{?pack_ipa_dumps}
%make_install %{?_smp_mflags}
# kill static libs
rm -f %{buildroot}%{_libdir}/lib*.a

# Rename the openssl CLI to openssl-1_1
mv %{buildroot}%{_bindir}/openssl %{buildroot}%{_bindir}/openssl-1_1

# Install the openssl-1_1.cnf config file
install -m 644 apps/openssl-1_1.cnf %{buildroot}%{_sysconfdir}/ssl/openssl-1_1.cnf

# remove the cnf.dist
rm -f %{buildroot}%{_sysconfdir}/ssl/openssl-1_1.cnf.dist
rm -f %{buildroot}%{_sysconfdir}/ssl/ct_log_list.cnf
rm -f %{buildroot}%{_sysconfdir}/ssl/ct_log_list.cnf.dist
ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl

mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/
# Create the two directories into which packages will drop their configuration
# files.
mkdir %{buildroot}/%{sslengcnf}
mkdir %{buildroot}/%{sslengdef}

# avoid file conflicts with man pages from other packages
#
pushd %{buildroot}/%{_mandir}
# some man pages now contain spaces. This makes several scripts go havoc, among them /usr/sbin/Check.
# replace spaces by underscores
#for i in man?/*\ *; do mv -v "$i" "${i// /_}"; done
which readlink &>/dev/null || function readlink { ( set +x; target=$(file $1 2>/dev/null); target=${target//* }; test -f $target && echo $target; ) }
for i in man?/*; do
    if test -L $i ; then
        LDEST=`readlink $i`
        rm -f $i ${i}ssl
        ln -sf ${LDEST}ssl ${i}ssl
    else
        mv $i ${i}ssl
        fi
    case "$i" in
        *.1)
        # these are the pages mentioned in openssl(1). They go into the main package.
        echo %doc %{_mandir}/${i}ssl%{?ext_man} >> $OLDPWD/filelist;;
        *)
        # the rest goes into the openssl-doc package.
        echo %doc %{_mandir}/${i}ssl%{?ext_man} >> $OLDPWD/filelist.doc;;
    esac
done
popd

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} \;

# Place showciphers.c for %%doc macro
cp %{SOURCE5} .

# the hmac hashes:
#
# this is a hack that re-defines the __os_install_post macro
# for a simple reason: the macro strips the binaries and thereby
# invalidates a HMAC that may have been created earlier.
# solution: create the hashes _after_ the macro runs.
#
# this shows up earlier because otherwise the expand of
# the macro is too late.
# remark: This is the same as running
#   openssl dgst -sha256 -hmac 'ppaksykemnsecgtsttplmamstKMEs'
%{expand:%%global __os_install_post {%__os_install_post

# Point linker to the newly installed libcrypto in order to avoid BuildRequiring itself (libopenssl1_1)
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"

%{buildroot}%{_bindir}/fips_standalone_hmac \
  %{buildroot}%{_libdir}/libssl.so.%{maj_min} > \
    %{buildroot}%{_libdir}/.libssl.so.%{maj_min}.hmac

# As fips_standalone_hmac now uses the very same library it checksums,
# the libcrypto hmac needs to be saved to a temporary file, otherwise
# the library will detect the empty hmac and abort due to a wrong checksum
%{buildroot}%{_bindir}/fips_standalone_hmac \
  %{buildroot}%{_libdir}/libcrypto.so.%{maj_min} > \
    %{buildroot}%{_libdir}/.libcrypto.so.%{maj_min}.temphmac

# rename the temporary checksum to its proper name
mv %{buildroot}%{_libdir}/.libcrypto.so.%{maj_min}.temphmac %{buildroot}%{_libdir}/.libcrypto.so.%{maj_min}.hmac
unset LD_LIBRARY_PATH

}}

%pre
# Migrate old engines.d to engines1.1.d.rpmsave
if [ ! -L %{ssletcdir}/engines.d ] && [ -d %{ssletcdir}/engines.d ]; then
    mkdir %{ssletcdir}/engines1.1.d.rpmsave ||:
    mv -v %{ssletcdir}/engines.d/* %{ssletcdir}/engines1.1.d.rpmsave ||:
    rmdir %{ssletcdir}/engines.d ||:
fi

# Migrate old engdef.d to engdef1.1.d.rpmsave
if [ ! -L %{ssletcdir}/engdef.d ] && [ -d %{ssletcdir}/engdef.d ]; then
    mkdir %{ssletcdir}/engdef1.1.d.rpmsave ||:
    mv -v %{ssletcdir}/engdef.d/* %{ssletcdir}/engdef1.1.d.rpmsave ||:
    rmdir %{ssletcdir}/engdef.d ||:
fi

%posttrans
# Restore engines1.1.d.rpmsave to engines1.1.d
if [ -d %{ssletcdir}/engines1.1.d.rpmsave ]; then
    mv -v %{ssletcdir}/engines1.1.d.rpmsave/* %{ssletcdir}/engines1.1.d ||:
    rmdir %{ssletcdir}/engines1.1.d.rpmsave ||:
fi

# Restore engdef1.1.d.rpmsave to engdef1.1.d
if [ -d %{ssletcdir}/engdef1.1.d.rpmsave ]; then
    mv -v %{ssletcdir}/engdef1.1.d.rpmsave/* %{ssletcdir}/engdef1.1.d ||:
    rmdir %{ssletcdir}/engdef1.1.d.rpmsave ||:
fi

# Move engines1_1.d to engines1.1.d
if [ -d %{ssletcdir}/engines1_1.d ]; then
    mv -v %{ssletcdir}/engines1_1.d/* %{ssletcdir}/engines1.1.d ||:
    rmdir %{ssletcdir}/engines1_1.d ||:
fi

# Move engdef1_1.d to engdef1.1.d
if [ -d %{ssletcdir}/engdef1_1.d ]; then
    mv -v %{ssletcdir}/engdef1_1.d/* %{ssletcdir}/engdef1.1.d ||:
    rmdir %{ssletcdir}/engdef1_1.d ||:
fi

%post -n libopenssl1_1 -p /sbin/ldconfig
%postun -n libopenssl1_1 -p /sbin/ldconfig

%files -n libopenssl1_1
%license LICENSE
%{_libdir}/libssl.so.%{maj_min}
%{_libdir}/libcrypto.so.%{maj_min}
%{_libdir}/.libssl.so.%{maj_min}.hmac
%{_libdir}/.libcrypto.so.%{maj_min}.hmac
%{_libdir}/engines-%{maj_min}

%files -n libopenssl-1_1-devel
%{_includedir}/%{_rname}/
%{_includedir}/ssl
%{_libdir}/libssl.so
%{_libdir}/libcrypto.so
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc

%files doc -f filelist.doc
%doc doc/* demos
%doc showciphers.c

%files -f filelist
%doc CHANGE* NEWS README
%dir %{ssletcdir}
%config (noreplace) %{ssletcdir}/openssl-1_1.cnf
%attr(700,root,root) %{ssletcdir}/private
%dir %{sslengcnf}
%dir %{sslengdef}
%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%{_bindir}/c_rehash-1_1
%{_bindir}/fips_standalone_hmac
%{_bindir}/openssl-1_1

%changelog
