#
# spec file for package openssl-3
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define ssletcdir %{_sysconfdir}/ssl
%define sover 3
%define _rname openssl
%define man_suffix 3ssl

%bcond_with lto
%if %{without lto}
%define _lto_cflags %{nil}
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%global sle_needs_crypto_policies 1
%endif

%if 0%{?suse_version} > 1600
%global openssl_test_flags HARNESS_JOBS=${RPM_BUILD_NCPUS}
%endif

# Enable userspace livepatching.
%define livepatchable 1

Name:           openssl-3
Version:        3.5.3
Release:        0
Summary:        Secure Sockets and Transport Layer Security
License:        Apache-2.0
URL:            https://www.openssl.org/
Source:         https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz
Source1:        https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz.asc
# https://keys.openpgp.org/search?q=openssl@openssl.org
# BA54 73A2 B058 7B07 FB27 CF2D 2160 94DF D0CB 81EF
Source2:        %{_rname}.keyring
# to get mtime of file:
Source3:        %{name}.changes
Source4:        baselibs.conf
Source5:        showciphers.c
Source6:        openssl-TESTS-Disable-default-provider-crypto-policies.patch
# PATCH-FIX-OPENSUSE: Do not install html docs as it takes ages
Patch1:         openssl-no-html-docs.patch
Patch2:         openssl-truststore.patch
Patch3:         openssl-pkgconfig.patch
Patch4:         openssl-ppc64-config.patch
Patch5:         openssl-no-date.patch
# PATCH-FIX-FEDORA Add crypto-policies support
Patch6:         openssl-Add-support-for-PROFILE-SYSTEM-system-default-cipher.patch
# PATCH-FIX-FEDORA Add FIPS_mode compatibility macro and flag support
Patch7:         openssl-Add-FIPS_mode-compatibility-macro.patch
Patch8:         openssl-Add-Kernel-FIPS-mode-flag-support.patch
# PATCH-FIX-FEDORA Load FIPS the provider and set FIPS properties implicitly
Patch9:         openssl-Force-FIPS.patch
# PATCH-FIX-FEDORA Disable the fipsinstall command-line utility
Patch10:        openssl-disable-fipsinstall.patch
# PATCH-FIX-FEDORA Instructions to load legacy provider in openssl.cnf
Patch11:        openssl-load-legacy-provider.patch
# PATCH-FIX-FEDORA Embed the FIPS hmac
Patch12:        openssl-FIPS-embed-hmac.patch
# PATCH-FIX-FEDORA bsc#1221786 FIPS: Use of non-Approved Elliptic Curves
Patch13:        openssl-Add-changes-to-ectest-and-eccurve.patch
Patch14:        openssl-Disable-explicit-ec.patch
Patch15:        openssl-skipped-tests-EC-curves.patch
# PATCH-FIX-FEDORA bsc#1221753 bsc#1221760 bsc#1221822 FIPS: Extra public/private key checks required by FIPS-140-3
Patch16:        openssl-FIPS-140-3-keychecks.patch
# PATCH-FIX-FEDORA bsc#1221760 FIPS: Execute KATS before HMAC verification
Patch17:        openssl-FIPS-early-KATS.patch
# PATCH-FIX-FEDORA bsc#1221365 bsc#1221824 FIPS: Service Level Indicator is needed
Patch19:        openssl-FIPS-limit-rsa-encrypt.patch
Patch20:        openssl-FIPS-Expose-a-FIPS-indicator.patch
# PATCH-FIX-FEDORA bsc#1221760 FIPS: Execute KATS before HMAC verification
Patch21:        openssl-FIPS-Use-OAEP-in-KATs-support-fixed-OAEP-seed.patch
Patch22:        openssl-rand-Forbid-truncated-hashes-SHA-3-in-FIPS-prov.patch
# PATCH-FIX-FEDORA bsc#1221365 bsc#1221365 FIPS: Service Level Indicator is needed
Patch23:        openssl-FIPS-Remove-X9.31-padding-from-FIPS-prov.patch
# PATCH-FIX-FEDORA bsc#1221827 FIPS: Recommendation for Password-Based Key Derivation
Patch24:        openssl-pbkdf2-Set-minimum-password-length-of-8-bytes.patch
# PATCH-FIX-FEDORA bsc#1221365 FIPS: Service Level Indicator is needed
Patch25:        openssl-FIPS-RSA-disable-shake.patch
# PATCH-FIX-FEDORA bsc#1221824 FIPS: NIST SP 800-56Brev2 Section 6.4.1.2.1
Patch26:        openssl-FIPS-RSA-encapsulate.patch
# PATCH-FIX-FEDORA bsc#1221821 FIPS: Disable FIPS 186-4 Domain Parameters
Patch27:        openssl-DH-Disable-FIPS-186-4-type-parameters-in-FIPS-mode.patch
# PATCH-FIX-SUSE bsc#1221824 FIPS: Add check for SP 800-56Brev2 Section 6.4.1.2.1
Patch28:        openssl-FIPS-Add-SP800-56Br2-6.4.1.2.1-3.c-check.patch
# PATCH-FIX-SUSE bsc#1221753 FIPS: Enforce error state
Patch29:        openssl-FIPS-Enforce-error-state.patch
# PATCH-FIX-FEDORA Adapt pairwise tests
Patch30:        openssl-skip-quic-pairwise.patch
# PATCH-FIX-FEDORA Fix broken selftests in fips provider init
Patch31:        openssl-FIPS-Fix-encoder-decoder-negative-test.patch
Patch32:        openssl-FIPS-SUSE-FIPS-module-version.patch
Patch33:        openssl-FIPS-EC-disable-weak-curves.patch
Patch34:        openssl-FIPS-NO-DSA-Support.patch
Patch35:        openssl-FIPS-NO-DES-support.patch
Patch36:        openssl-FIPS-NO-Kmac.patch
Patch37:        openssl-FIPS-NO-PQ-ML-SLH-DSA.patch
# PATCH-FIX-SUSE Use the shared jitterentropy library instead of static
Patch38:        openssl-shared-jitterentropy.patch
# PATCH-FIX-SUSE Disable dubious broken test
Patch39:        openssl-disable-75-test_quicapi-test.patch
# PATCH-FIX-FEDORA bsc#1221365 FIPS: Service Level Indicator is needed
Patch40:        openssl-FIPS-enforce-EMS-support.patch
# PATCH-FIX-FEDORA bsc#1221787 FIPS: Selectively disallow SHA1 signatures
Patch41:        openssl-Allow-disabling-of-SHA1-signatures.patch
# PATCH-FIX-FEDORA bsc#1221365 FIPS: Deny SHA-1 signature verification in FIPS provider
Patch42:        openssl-FIPS-Deny-SHA-1-sigver-in-FIPS-provider.patch
# PATCH-FIX-FEDORA FIPS: Allow SHA1 in seclevel 2 if rh-allow-sha1-signatures = yes
Patch43:        openssl-FIPS-Allow-SHA1-in-seclevel-2-if-rh-allow-sha1-signatures.patch
# PATCH-FIX-FEDORA FIPS: Fix the speed command in FIPS mode for KMAC
Patch44:        openssl-FIPS-Fix-openssl-speed-KMAC.patch
# PATCH-FIX-SUSE Fix a bogus warning caused by -Wfree-nonheap-object
Patch45:        openssl-Fix-Wfree-nonheap-object-warning.patch
# PATCH-FIX-UPSTREAM bsc#1250232 CVE-2025-9230: Fix out-of-bounds read & write in RFC 3211 KEK Unwrap
Patch46:        openssl-CVE-2025-9230.patch
# PATCH-FIX-UPSTREAM bsc#1250233 CVE-2025-9231: Fix timing side-channel in SM2 algorithm on 64 bit ARM
Patch47:        openssl-CVE-2025-9231.patch
# PATCH-FIX-UPSTREAM bsc#1250234 CVE-2025-9232: Fix out-of-bounds read in HTTP client no_proxy handling
Patch48:        openssl-CVE-2025-9232.patch
# PATCH-FIX-UPSTREAM bsc#1256839 CVE-2026-22795: Missing ASN1_TYPE validation in PKCS#12 parsing
# PATCH-FIX-UPSTREAM bsc#1256840 CVE-2026-22796: ASN1_TYPE Type Confusion in the PKCS7_digest_from_attributes() function
Patch50:        openssl-CVE-2026-22795.patch
# PATCH-FIX-UPSTREAM bsc#1256837 CVE-2025-69420: Missing ASN1_TYPE validation in TS_RESP_verify_response() function
Patch51:        openssl-CVE-2025-69420.patch
# PATCH-FIX-UPSTREAM bsc#1256838 CVE-2025-69421: NULL Pointer Dereference in PKCS12_item_decrypt_d2i_ex function
Patch52:        openssl-CVE-2025-69421.patch
# PATCH-FIX-UPSTREAM bsc#1256836 CVE-2025-69419: Out of bounds write in PKCS12_get_friendlyname() UTF-8 function
Patch53:        openssl-CVE-2025-69419.patch
# PATCH-FIX-UPSTREAM bsc#1256833 CVE-2025-66199: TLS 1.3 CompressedCertificate excessive memory allocation
Patch54:        openssl-CVE-2025-66199.patch
# PATCH-FIX-UPSTREAM bsc#1256834 CVE-2025-68160: Heap out-of-bounds write in BIO_f_linebuffer on short writes
Patch55:        openssl-CVE-2025-68160.patch
# PATCH-FIX-UPSTREAM bsc#1256835 CVE-2025-69418: Unauthenticated/unencrypted trailing bytes with low-level OCB function calls
Patch56:        openssl-CVE-2025-69418.patch
# PATCH-FIX-UPSTREAM bsc#1256832 CVE-2025-15469: 'openssl dgst' one-shot codepath silently truncates inputs greater than 16MB
Patch57:        openssl-CVE-2025-15469.patch
# PATCH-FIX-UPSTREAM bsc#1256830 CVE-2025-15467: Stack buffer overflow in CMS AuthEnvelopedData parsing
Patch58:        openssl-CVE-2025-15467.patch
Patch59:        openssl-CVE-2025-15467-comments.patch
Patch60:        openssl-CVE-2025-15467-test.patch
# PATCH-FIX-UPSTREAM bsc#1256829 CVE-2025-11187: Improper validation of PBMAC1 parameters in PKCS#12 MAC verification
Patch61:        openssl-CVE-2025-11187.patch
# PATCH-FIX-UPSTREAM bsc#1256831 CVE-2025-15468: NULL dereference in SSL_CIPHER_find() function on unknown cipher ID
Patch62:        openssl-CVE-2025-15468.patch

# ulp-macros is available according to SUSE version.
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1540
BuildRequires:  ulp-macros
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
Requires:       libopenssl3 = %{version}-%{release}
Requires:       openssl
Provides:       ssl
# Needed for clean upgrade path, boo#1070003
Obsoletes:      openssl-1_0_0
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      openssl-1_1_0
%{?suse_build_hwcaps_libs}
%if 0%{?sle_needs_crypto_policies}
Requires:       crypto-policies
%endif
BuildRequires:  jitterentropy-devel >= 3.4.0

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl3
Summary:        Secure Sockets and Transport Layer Security
Recommends:     ca-certificates-mozilla
Conflicts:      %{name} < %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0
%if 0%{?sle_needs_crypto_policies}
Requires:       crypto-policies
%endif
# Merge back the hmac files bsc#1185116
Provides:       libopenssl3-hmac = %{version}-%{release}
Obsoletes:      libopenssl3-hmac < %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0-hmac
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-hmac

%description -n libopenssl3
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl-3-devel
Summary:        Development files for OpenSSL
Requires:       jitterentropy-devel >= 3.4.0
Requires:       libopenssl3 = %{version}
Requires:       pkgconfig(zlib)
Recommends:     %{name} = %{version}
Provides:       ssl-devel
Conflicts:      ssl-devel
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl-1_1_0-devel
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-devel

%description -n libopenssl-3-devel
This subpackage contains header files for developing applications
that want to make use of the OpenSSL C API.

%package -n libopenssl-3-fips-provider
Summary:        OpenSSL FIPS provider
Requires:       libjitterentropy3 >= 3.4.0
Requires:       libopenssl3 >= %{version}
BuildRequires:  fipscheck
BuildRequires:  jitterentropy-devel >= 3.4.0

%description -n libopenssl-3-fips-provider
This package contains the OpenSSL FIPS provider.

%package doc
Summary:        Manpages and additional documentation for openssl
Conflicts:      libopenssl-3-devel < %{version}-%{release}
Conflicts:      openssl-doc
Provides:       openssl-doc = %{version}
Obsoletes:      openssl-doc < %{version}
BuildArch:      noarch

%description doc
This package contains optional documentation provided in addition to
this package's base documentation.

%prep
%autosetup -p1 -n %{_rname}-%{version}

%build
%ifarch armv5el armv5tel
export MACHINE=armv5el
%endif
%ifarch armv6l armv6hl
export MACHINE=armv6l
%endif

./Configure \
    enable-camellia \
%ifarch x86_64 aarch64 ppc64le
    enable-ec_nistp_64_gcc_128 \
%endif
    enable-fips \
    enable-fips-jitter \
    enable-jitter \
    enable-ktls \
    enable-pie \
    enable-rfc3779 \
    enable-seed \
    no-afalgeng \
    no-atexit \
    no-ec2m \
    no-mdc2 \
    zlib \
    --prefix=%{_prefix} \
    --libdir=%{_lib} \
    --openssldir=%{ssletcdir} \
    %{optflags} \
    %{?cflags_livepatching} \
    -Wa,--noexecstack \
    -Wl,-z,relro,-z,now \
    -fno-common \
    -DTERMIOS \
    -DPURIFY \
    -D_GNU_SOURCE \
    -DOPENSSL_PEDANTIC_ZEROIZATION \
    '-DSUSE_OPENSSL_RELEASE="\"%{release}\""' \
    -DOPENSSL_NO_BUF_FREELISTS \
    $(getconf LFS_CFLAGS) \
    -Wall \
    --system-ciphers-file=%{_sysconfdir}/crypto-policies/back-ends/openssl.config

# Show build configuration
perl configdata.pm --dump

# Do not run this in a production package the FIPS symbols must be patched-in
# util/mkdef.pl crypto update

%make_build depend
%make_build all

%check
# Relax the crypto-policies requirements and disable the default
# provider for the test suite regression tests
patch -p1 < %{SOURCE6}
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
# export HARNESS_VERBOSE=yes
# Embed HMAC into fips provider for test run
OPENSSL_CONF=/dev/null LD_LIBRARY_PATH=. apps/openssl dgst -binary -sha256 -mac HMAC -macopt hexkey:f4556650ac31d35461610bac4ed81b1a181b2d8a43ea2854cbae22ca74560813 < providers/fips.so > providers/fips.so.hmac
objcopy --update-section .rodata1=providers/fips.so.hmac providers/fips.so providers/fips.so.mac
mv providers/fips.so.mac providers/fips.so

# Run the tests in non FIPS mode
LD_LIBRARY_PATH="$PWD" make test %{?_smp_mflags} %{?openssl_test_flags}

# Run the tests also in FIPS mode
# OPENSSL_FORCE_FIPS_MODE=1 LD_LIBRARY_PATH="$PWD" make TESTS='-test_evp_fetch_prov -test_tsa' test -j16 || :

# Add generation of HMAC checksum of the final stripped library
# We manually copy standard definition of __spec_install_post
# and add hmac calculation/embedding to fips.so
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    OPENSSL_CONF=/dev/null LD_LIBRARY_PATH=. apps/openssl dgst -binary -sha256 -mac HMAC -macopt hexkey:f4556650ac31d35461610bac4ed81b1a181b2d8a43ea2854cbae22ca74560813 < %{buildroot}%{_libdir}/ossl-modules/fips.so > %{buildroot}%{_libdir}/ossl-modules/fips.so.hmac \
    objcopy --update-section .rodata1=%{buildroot}%{_libdir}/ossl-modules/fips.so.hmac %{buildroot}%{_libdir}/ossl-modules/fips.so %{buildroot}%{_libdir}/ossl-modules/fips.so.mac \
    mv %{buildroot}%{_libdir}/ossl-modules/fips.so.mac %{buildroot}%{_libdir}/ossl-modules/fips.so \
    rm %{buildroot}%{_libdir}/ossl-modules/fips.so.hmac \
%{nil}

# show ciphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%{?pack_ipa_dumps}
%make_install %{?_smp_mflags} MANSUFFIX=%{man_suffix}

rename so.%{sover} so.%{version} %{buildroot}%{_libdir}/*.so.%{sover}
for lib in %{buildroot}%{_libdir}/*.so.%{version} ; do
    chmod 755 ${lib}
    ln -sf $(basename ${lib}) %{buildroot}%{_libdir}/$(basename ${lib} .%{version})
    ln -sf $(basename ${lib}) %{buildroot}%{_libdir}/$(basename ${lib} .%{version}).%{sover}
done

# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Remove the cnf.dist
rm -f %{buildroot}%{ssletcdir}/openssl.cnf.dist
rm -f %{buildroot}%{ssletcdir}/ct_log_list.cnf.dist

# Remove unneeded NOTES files
for file in NOTES-ANDROID.md NOTES-DJGPP.md NOTES-NONSTOP.md NOTES-VMS.md NOTES-WINDOWS.md ; do
    rm -f %{_datadir}/packages/libopenssl-3-devel/${file}
done

# Make a copy of the default openssl.cnf file
cp %{buildroot}%{ssletcdir}/openssl.cnf %{buildroot}%{ssletcdir}/openssl-orig.cnf

# Create openssl ca-certificates dir required by nodejs regression tests [bsc#1207484]
mkdir -p %{buildroot}%{_localstatedir}/lib/ca-certificates/openssl
install -d -m 555 %{buildroot}%{_localstatedir}/lib/ca-certificates/openssl

# Remove the fipsmodule.cnf because FIPS module is loaded automatically in FIPS mode
rm -f %{buildroot}%{ssletcdir}/fipsmodule.cnf

ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/

# Add the FIPS module configuration from crypto-policies since SP6
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
ln -s %{_sysconfdir}/crypto-policies/back-ends/openssl_fips.config %{buildroot}%{ssletcdir}/fips_local.cnf
%endif

# Avoid file conflicts with man pages from other packages
pushd %{buildroot}/%{_mandir}
find . -type f -exec chmod 644 {} +
mv man5/config.5%{man_suffix} man5/openssl.cnf.5
popd

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} +

# Place showciphers.c for %%doc macro
cp %{SOURCE5} .

# Compute the FIPS hmac using the brp-50-generate-fips-hmac script
export BRP_FIPSHMAC_FILES="%{buildroot}%{_libdir}/libssl.so.%{sover} %{buildroot}%{_libdir}/libcrypto.so.%{sover}"

%post -p "/bin/bash"
if [ "$1" -gt 1 ] ; then
    # Check if the packaged default config file for openssl-3, called openssl.cnf,
    # is the original or if it has been modified and alert the user in that case
    # that a copy of the original file openssl-orig.cnf can be used if needed.
    cmp --silent %{ssletcdir}/openssl.cnf %{ssletcdir}/openssl-orig.cnf 2>/dev/null
    if [ "$?" -eq 1 ] ; then
        echo -e " The openssl-3 default config file openssl.cnf is different from" ;
        echo -e " the original one shipped by the package. A copy of the original" ;
        echo -e " file is packaged and named as openssl-orig.cnf if needed."
    fi
fi

%pre

%post -n libopenssl3 -p /sbin/ldconfig
%postun -n libopenssl3 -p /sbin/ldconfig

%files -n libopenssl3
%license LICENSE.txt
%attr(0755,root,root) %{_libdir}/libssl.so.%{version}
%{_libdir}/libssl.so.%{sover}
%attr(0755,root,root) %{_libdir}/libcrypto.so.%{version}
%{_libdir}/libcrypto.so.%{sover}
%{_libdir}/engines-%{sover}
%dir %{_libdir}/ossl-modules
%{_libdir}/ossl-modules/legacy.so
%{_libdir}/.libssl.so.%{sover}.hmac
%{_libdir}/.libcrypto.so.%{sover}.hmac
%dir %{ssletcdir}
%attr(700,root,root) %{ssletcdir}/private
%config %{ssletcdir}/openssl-orig.cnf
%config (noreplace) %{ssletcdir}/openssl.cnf
%config (noreplace) %{ssletcdir}/ct_log_list.cnf
%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%dir %{_localstatedir}/lib/ca-certificates/
%dir %{_localstatedir}/lib/ca-certificates/openssl

%files -n libopenssl-3-fips-provider
%{_libdir}/ossl-modules/fips.so
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
%config %{ssletcdir}/fips_local.cnf
%endif

%files -n libopenssl-3-devel
%doc NOTES*.md CONTRIBUTING.md HACKING.md AUTHORS.md ACKNOWLEDGEMENTS.md
%{_includedir}/%{_rname}/
%{_includedir}/ssl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/OpenSSL
%{_libdir}/cmake/OpenSSL/*.cmake

%files doc
%doc README.md
%doc doc/html/* doc/HOWTO/* demos
%doc showciphers.c
%{_mandir}/man3/*

%files
%license LICENSE.txt
%doc CHANGES.md NEWS.md README.md
%{_bindir}/%{_rname}
%{_bindir}/c_rehash
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%changelog
