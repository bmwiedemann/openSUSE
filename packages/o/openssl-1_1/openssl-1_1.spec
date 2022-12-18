#
# spec file for package openssl-1_1
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


%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
# Enable livepatching support for SLE15-SP4 onwards. It requires
# compiler support introduced there.
%define livepatchable 1

# Set variables for livepatching.
%define _other %{_topdir}/OTHER
%define tar_basename %{_rname}-livepatch-%{version}-%{release}
%define tar_package_name %{tar_basename}.%{_arch}.tar.xz
%define clones_dest_dir %{tar_basename}/%{_arch}
%else
# Unsupported operating system.
%define livepatchable 0
%endif

%ifnarch x86_64
# Unsupported architectures must have livepatch disabled.
%define livepatchable 0
%endif

%define ssletcdir %{_sysconfdir}/ssl
%define maj_min 1.1
%define _rname  openssl
Name:           openssl-1_1
# Don't forget to update the version in the "openssl" package!
Version:        1.1.1s
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
Patch39:        openssl-fips-dont_run_FIPS_module_installed.patch
Patch40:        openssl-fips-selftests_in_nonfips_mode.patch
Patch41:        openssl-fips-clearerror.patch
Patch42:        openssl-fips-ignore_broken_atexit_test.patch
Patch43:        openssl-keep_EVP_KDF_functions_version.patch
Patch44:        openssl-fips_fix_selftests_return_value.patch
Patch45:        openssl-fips-add-SHA3-selftest.patch
Patch46:        openssl-fips_selftest_upstream_drbg.patch
Patch47:        openssl-unknown_dgst.patch
# PATCH-FIX-UPSTREAM jsc#SLE-7403 Support for CPACF enhancements - part 2 (crypto)
Patch50:        openssl-s390x-assembly-pack-accelerate-X25519-X448-Ed25519-and-Ed448.patch
Patch51:        openssl-s390x-fix-x448-and-x448-test-vector-ctime-for-x25519-and-x448.patch
Patch52:        openssl-1.1.1-system-cipherlist.patch
# PATCH-FIX-OPENSUSE jsc#SLE-15832 Centralized Crypto Compliance Configuration
Patch53:        openssl-1_1-seclevel.patch
Patch54:        openssl-1_1-use-seclevel2-in-tests.patch
Patch55:        openssl-1_1-disable-test_srp-sslapi.patch
Patch56:        openssl-add_rfc3526_rfc7919.patch
Patch57:        openssl-1_1-use-include-directive.patch
#PATCH-FIX-UPSTREAM jsc#SLE-18136 POWER10 performance enhancements for cryptography
Patch69:        openssl-1_1-Optimize-ppc64.patch
#PATCH-FIX-UPSTREAM jsc#SLE-19742 Backport Arm improvements from OpenSSL 3
Patch70:        openssl-1_1-Optimize-RSA-armv8.patch
Patch71:        openssl-1_1-Optimize-AES-XTS-aarch64.patch
Patch72:        openssl-1_1-Optimize-AES-GCM-uarchs.patch
#PATCH-FIX-SUSE bsc#1182959 FIPS: Fix function and reason error codes
Patch73:        openssl-1_1-FIPS-fix-error-reason-codes.patch
#PATCH-FIX-SUSE bsc#1180995 Default to RFC7919 groups in FIPS mode
Patch74:        openssl-1_1-paramgen-default_to_rfc7919.patch
# PATCH-FIX-UPSTREAM jsc#PED-512
# POWER10 performance enhancements for cryptography
Patch75:        openssl-1_1-AES-GCM-performance-optimzation-with-stitched-method.patch
Patch76:        openssl-1_1-Fixed-counter-overflow.patch
Patch77:        openssl-1_1-chacha20-performance-optimizations-for-ppc64le-with-.patch
Patch78:        openssl-1_1-Fixed-conditional-statement-testing-64-and-256-bytes.patch
Patch79:        openssl-1_1-Fix-AES-GCM-on-Power-8-CPUs.patch

Requires:       libopenssl1_1 = %{version}-%{release}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
Requires:       crypto-policies
%endif
Conflicts:      ssl
Provides:       ssl
Provides:       openssl(cli)
# Needed for clean upgrade path, boo#1070003
Obsoletes:      openssl-1_0_0
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      openssl-1_1_0

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl1_1
Summary:        Secure Sockets and Transport Layer Security
License:        OpenSSL
Group:          Productivity/Networking/Security
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
Requires:       crypto-policies
%endif
Recommends:     ca-certificates-mozilla
# install libopenssl and libopenssl-hmac close together (bsc#1090765)
Suggests:       libopenssl1_1-hmac = %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0
Conflicts:      %{name} < %{version}-%{release}

%description -n libopenssl1_1
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl-1_1-devel
Summary:        Development files for OpenSSL
License:        OpenSSL
Group:          Development/Libraries/C and C++
Requires:       libopenssl1_1 = %{version}
Requires:       pkgconfig(zlib)
Recommends:     %{name} = %{version}
# we need to have around only the exact version we are able to operate with
Conflicts:      libopenssl-devel < %{version}
Conflicts:      libopenssl-devel > %{version}
Conflicts:      ssl-devel
Provides:       ssl-devel
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl-1_1_0-devel
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-devel

%description -n libopenssl-1_1-devel
This subpackage contains header files for developing applications
that want to make use of the OpenSSL C API.

%package -n libopenssl1_1-hmac
Summary:        HMAC files for FIPS-140-2 integrity checking of the openssl shared libraries
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
Requires:       libopenssl1_1 = %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0-hmac
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-hmac

%description -n libopenssl1_1-hmac
The FIPS compliant operation of the openssl shared libraries is NOT
possible without the HMAC hashes contained in this package!

%package doc
Summary:        Additional Package Documentation
License:        OpenSSL
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

%build
%ifarch armv5el armv5tel
export MACHINE=armv5el
%endif
%ifarch armv6l armv6hl
export MACHINE=armv6l
%endif

./config \
    no-idea \
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
%if %{livepatchable}
    -fpatchable-function-entry=16,14 -fdump-ipa-clones \
%endif
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
make depend %{?_smp_mflags}
make all %{?_smp_mflags}

%check
export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
#export HARNESS_VERBOSE=1
#export OPENSSL_FORCE_FIPS_MODE=1
LD_LIBRARY_PATH=`pwd` make test -j1

# show ciphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%if %{livepatchable}

# Ipa-clones are files generated by gcc which logs changes made across
# functions, and we need to know such changes to build livepatches
# correctly. These files are intended to be used by the livepatch
# developers and may be retrieved by using `osc getbinaries`.
#
# Create list of ipa-clones.
find . -name "*.ipa-clones" ! -empty | sed 's/^\.\///g' | sort > ipa-clones.list

# Create ipa-clones destination folder and move clones there.
mkdir -p ipa-clones/%{clones_dest_dir}
while read f; do
  _dest=ipa-clones/%{clones_dest_dir}/$f
  mkdir -p ${_dest%/*}
  cp $f $_dest
done < ipa-clones.list

# Create tar package with the clone files.
tar cfJ %{tar_package_name} -C ipa-clones %{tar_basename}

# Copy tar package to the OTHERS folder
cp %{tar_package_name} %{_other}

%endif # livepatchable

%make_install %{?_smp_mflags}
# kill static libs
rm -f %{buildroot}%{_libdir}/lib*.a
# remove the cnf.dist
rm -f %{buildroot}%{_sysconfdir}/ssl/openssl.cnf.dist
ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/
# Create the two directories into which packages will drop their configuration
# files.
mkdir %{buildroot}/%{ssletcdir}/engines.d/
mkdir %{buildroot}/%{ssletcdir}/engdef.d/

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

%post -n libopenssl1_1 -p /sbin/ldconfig
%postun -n libopenssl1_1 -p /sbin/ldconfig

%files -n libopenssl1_1
%license LICENSE
%{_libdir}/libssl.so.%{maj_min}
%{_libdir}/libcrypto.so.%{maj_min}
%{_libdir}/engines-%{maj_min}

%files -n libopenssl1_1-hmac
%{_libdir}/.libssl.so.%{maj_min}.hmac
%{_libdir}/.libcrypto.so.%{maj_min}.hmac

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
%config (noreplace) %{ssletcdir}/openssl.cnf
%attr(700,root,root) %{ssletcdir}/private
%dir %{ssletcdir}/engines.d
%dir %{ssletcdir}/engdef.d
%{ssletcdir}/ct_log_list.cnf
%{ssletcdir}/ct_log_list.cnf.dist

%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%{_bindir}/c_rehash
%{_bindir}/fips_standalone_hmac
%{_bindir}/%{_rname}

%changelog
