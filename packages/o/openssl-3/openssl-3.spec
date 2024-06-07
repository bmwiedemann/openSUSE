#
# spec file for package openssl-3
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


%define ssletcdir %{_sysconfdir}/ssl
%define sover 3
%define _rname openssl
%define man_suffix 3ssl
%global sslengcnf %{ssletcdir}/engines%{sover}.d
%global sslengdef %{ssletcdir}/engdef%{sover}.d

# Enable userspace livepatching.
%define livepatchable 1

Name:           openssl-3
# Don't forget to update the version in the "openssl" meta-package!
Version:        3.1.4
Release:        0
Summary:        Secure Sockets and Transport Layer Security
License:        Apache-2.0
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
Source6:        openssl-Disable-default-provider-for-test-suite.patch
# PATCH-FIX-OPENSUSE: Do not install html docs as it takes ages
Patch1:         openssl-no-html-docs.patch
Patch2:         openssl-truststore.patch
Patch3:         openssl-pkgconfig.patch
Patch4:         openssl-DEFAULT_SUSE_cipher.patch
Patch5:         openssl-ppc64-config.patch
Patch6:         openssl-no-date.patch
# Add crypto-policies support
Patch7:         openssl-Add-support-for-PROFILE-SYSTEM-system-default-cipher.patch
Patch8:         openssl-crypto-policies-support.patch
# PATCH-FIX-UPSTREAM: bsc#1209430 Upgrade OpenSSL from 3.0.8 to 3.1.0 in TW
Patch9:         openssl-Add_support_for_Windows_CA_certificate_store.patch
# PATCH-FIX-FEDORA Add FIPS_mode compatibility macro and flag support
Patch10:        openssl-Add-FIPS_mode-compatibility-macro.patch
Patch11:        openssl-Add-Kernel-FIPS-mode-flag-support.patch
# PATCH-FIX-UPSTREAM jsc#PED-5086, jsc#PED-3514
# POWER10 performance enhancements for cryptography
Patch12:        openssl-ec-Use-static-linkage-on-nistp521-felem_-square-mul-.patch
Patch13:        openssl-ec-56-bit-Limb-Solinas-Strategy-for-secp384r1.patch
Patch14:        openssl-ec-powerpc64le-Add-asm-implementation-of-felem_-squa.patch
Patch15:        openssl-ecc-Remove-extraneous-parentheses-in-secp384r1.patch
Patch16:        openssl-powerpc-ecc-Fix-stack-allocation-secp384r1-asm.patch
Patch17:        openssl-Improve-performance-for-6x-unrolling-with-vpermxor-i.patch
# PATCH-FIX-UPSTREAM: bsc#1216922 CVE-2023-5678 Generating excessively long X9.42 DH keys or
# checking excessively long X9.42 DH keys or parameters may be very slow
Patch18:        openssl-CVE-2023-5678.patch
# PATCH-FIX-UPSTREAM https://github.com/openssl/openssl/pull/22971
Patch19:        openssl-Enable-BTI-feature-for-md5-on-aarch64.patch
# PATCH-FIX-UPSTREAM: bsc#1218690 CVE-2023-6129 - POLY1305 MAC implementation corrupts vector registers on PowerPC
Patch20:        openssl-CVE-2023-6129.patch
# PATCH-FIX-FEDORA Load FIPS the provider and set FIPS properties implicitly
Patch21:        openssl-Force-FIPS.patch
# PATCH-FIX-FEDORA Disable the fipsinstall command-line utility
Patch22:        openssl-disable-fipsinstall.patch
# PATCH-FIX-FEDORA Instructions to load legacy provider in openssl.cnf
Patch23:        openssl-load-legacy-provider.patch
# PATCH-FIX-FEDORA Embed the FIPS hmac
Patch24:        openssl-FIPS-embed-hmac.patch
# PATCH-FIX-UPSTREAM: bsc#1218810 CVE-2023-6237: Excessive time spent checking invalid RSA public keys
Patch25:        openssl-CVE-2023-6237.patch
# PATCH-FIX-SUSE bsc#1194187, bsc#1207472, bsc#1218933 - Add engines section in openssl.cnf
Patch26:        openssl-3-use-include-directive.patch
# PATCH-FIX-UPSTREAM: bsc#1219243 CVE-2024-0727: denial of service via null dereference
Patch27:        openssl-CVE-2024-0727.patch
# PATCH-FIX-UPSTREAM: bsc#1222548 CVE-2024-2511: Unbounded memory growth with session handling in TLSv1.3
Patch28:        openssl-CVE-2024-2511.patch
# PATCH-FIX-UPSTREAM: bsc#1224388 CVE-2024-4603: excessive time spent checking DSA keys and parameters
Patch29:        openssl-CVE-2024-4603.patch
# PATCH-FIX-UPSTREAM: bsc#1225291 NVMe/TCP TLS connection fails due to handshake failure
Patch30:        openssl-Fix-EVP_PKEY_CTX_add1_hkdf_info-behavior.patch
Patch31:        openssl-Handle-empty-param-in-EVP_PKEY_CTX_add1_hkdf_info.patch
BuildRequires:  pkgconfig
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
BuildRequires:  ulp-macros
%else
# Define ulp-macros macros as empty
%define cflags_livepatching ""
%define pack_ipa_dumps      echo "Livepatching is disabled in this build"
%endif
BuildRequires:  pkgconfig(zlib)
Requires:       libopenssl3 = %{version}-%{release}
Requires:       openssl
Provides:       ssl
# Needed for clean upgrade path, boo#1070003
Obsoletes:      openssl-1_0_0
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      openssl-1_1_0
%{?suse_build_hwcaps_libs}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif

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
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
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
Requires:       libopenssl3 >= %{version}
BuildRequires:  fipscheck

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
    no-mdc2 no-ec2m no-sm2 no-sm4 \
    enable-rfc3779 enable-camellia enable-seed \
%ifarch x86_64 aarch64 ppc64le
    enable-ec_nistp_64_gcc_128 \
%endif
    enable-fips \
    enable-ktls \
    zlib \
    --prefix=%{_prefix} \
    --libdir=%{_lib} \
    --openssldir=%{ssletcdir} \
    %{optflags} \
    %{cflags_livepatching} \
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

# Do not run this in a production package the FIPS symbols must be patched-in
# util/mkdef.pl crypto update

%make_build depend
%make_build all

%check
# Relax the crypto-policies requirements for the regression tests
# Revert patch8 before running tests
patch -p1 -R < %{PATCH8}
# Revert openssl-3-use-include-directive.patch because these directories
# exists only in buildroot but not in build system and some tests are failing
# because of it.
patch -p1 -R < %{PATCH26}
# Disable the default provider for the test suite.
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
LD_LIBRARY_PATH="$PWD" make test -j16

# Run the tests also in FIPS mode
# OPENSSL_FORCE_FIPS_MODE=1 LD_LIBRARY_PATH="$PWD" make TESTS='-test_evp_fetch_prov -test_tsa' test -j16 || :

# Add generation of HMAC checksum of the final stripped library
# We manually copy standard definition of __spec_install_post
# and add hmac calculation/embedding to fips.so
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    OPENSSL_CONF=/dev/null LD_LIBRARY_PATH=. apps/openssl dgst -binary -sha256 -mac HMAC -macopt hexkey:f4556650ac31d35461610bac4ed81b1a181b2d8a43ea2854cbae22ca74560813 < $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so > $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.hmac \
    objcopy --update-section .rodata1=$RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.hmac $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.mac \
    mv $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.mac $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so \
    rm $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.hmac \
%{nil}

# show ciphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%{pack_ipa_dumps}
%make_install %{?_smp_mflags} MANSUFFIX=%{man_suffix}

rename so.%{sover} so.%{version} %{buildroot}%{_libdir}/*.so.%{sover}
for lib in %{buildroot}%{_libdir}/*.so.%{version} ; do
    chmod 755 ${lib}
    ln -sf $(basename ${lib}) %{buildroot}%{_libdir}/$(basename ${lib} .%{version})
    ln -sf $(basename ${lib}) %{buildroot}%{_libdir}/$(basename ${lib} .%{version}).%{sover}
done

# Remove static libraries
rm -f %{buildroot}%{_libdir}/lib*.a

# Remove the cnf.dist
rm -f %{buildroot}%{ssletcdir}/openssl.cnf.dist
rm -f %{buildroot}%{ssletcdir}/ct_log_list.cnf.dist

# Make a copy of the default openssl.cnf file
cp %{buildroot}%{ssletcdir}/openssl.cnf %{buildroot}%{ssletcdir}/openssl-orig.cnf

# Create openssl ca-certificates dir required by nodejs regression tests [bsc#1207484]
mkdir -p %{buildroot}%{_localstatedir}/lib/ca-certificates/openssl
install -d -m 555 %{buildroot}%{_localstatedir}/lib/ca-certificates/openssl

# Remove the fipsmodule.cnf because FIPS module is loaded automatically
rm -f %{buildroot}%{ssletcdir}/fipsmodule.cnf

ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/

# Create the two directories into which packages will drop their configuration
# files.
mkdir %{buildroot}/%{sslengcnf}
mkdir %{buildroot}/%{sslengdef}
# Create unversioned symbolic links to above directories
ln -s %{sslengcnf} %{buildroot}/%{ssletcdir}/engines.d
ln -s %{sslengdef} %{buildroot}/%{ssletcdir}/engdef.d

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
# Migrate old engines.d to engines1.1.d.rpmsave
if [ ! -L %{ssletcdir}/engines.d ] && [ -d %{ssletcdir}/engines.d ]; then
   mkdir %{ssletcdir}/engines1.1.d.rpmsave ||:
   mv %{ssletcdir}/engines.d %{ssletcdir}/engines1.1.d.rpmsave ||:
fi

# Migrate old engdef.d to engdef1.1.d.rpmsave
if [ ! -L %{ssletcdir}/engdef.d ] && [ -d %{ssletcdir}/engdef.d ]; then
   mkdir %{ssletcdir}/engdef1.1.d.rpmsave ||:
   mv %{ssletcdir}/engdef.d %{ssletcdir}/engdef1.1.d.rpmsave ||:
fi

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

%files -n libopenssl-3-fips-provider
%{_libdir}/ossl-modules/fips.so

%files -n libopenssl-3-devel
%doc NOTES*.md CONTRIBUTING.md HACKING.md AUTHORS.md ACKNOWLEDGEMENTS.md
%{_includedir}/%{_rname}/
%{_includedir}/ssl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc README.md
%doc doc/html/* doc/HOWTO/* demos
%doc showciphers.c
%{_mandir}/man3/*

%files
%license LICENSE.txt
%doc CHANGES.md NEWS.md FAQ.md README.md
%dir %{ssletcdir}
%config %{ssletcdir}/openssl-orig.cnf
%config (noreplace) %{ssletcdir}/openssl.cnf
%config (noreplace) %{ssletcdir}/ct_log_list.cnf
%attr(700,root,root) %{ssletcdir}/private
%dir %{sslengcnf}
%dir %{sslengdef}
# symbolic link to above directories
%{ssletcdir}/engines.d
%{ssletcdir}/engdef.d
%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%dir %{_localstatedir}/lib/ca-certificates/
%dir %{_localstatedir}/lib/ca-certificates/openssl
%{_bindir}/%{_rname}
%{_bindir}/c_rehash
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%changelog
