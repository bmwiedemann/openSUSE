#
# spec file for package openssl-1_0_0
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


# hide steam subpackage provides
%global __provides_exclude_from ^%{steamlibdir}/.*$
# Add path where to store steam patched library
%define steamprefix	%{_prefix}/lib/steam
%define steamlibdir	%{_prefix}/lib/steam/%{_lib}
%define cavs_dir %{_libexecdir}/%{name}/cavs
%define ssletcdir %{_sysconfdir}/ssl
%define num_version 1.0.0
%define _rname  openssl
Name:           openssl-1_0_0
Version:        1.0.2u
Release:        0
Summary:        Secure Sockets and Transport Layer Security
License:        OpenSSL
Group:          Productivity/Networking/Security
URL:            https://www.openssl.org/
Source:         https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz
# to get mtime of file:
Source1:        %{name}.changes
Source2:        baselibs.conf
Source10:       README.SUSE
Source11:       README-FIPS.txt
Source42:       https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz.asc
# https://www.openssl.org/about/
# http://pgp.mit.edu:11371/pks/lookup?op=get&search=0xA2D29B7BF295C759#/openssl.keyring
Source43:       %{_rname}.keyring
Source98:       openssl-1_0_0-rpmlintrc
Source99:       showciphers.c
Patch0:         merge_from_0.9.8k.patch
Patch1:         openssl-1.0.0-c_rehash-compat.diff
Patch2:         openssl-engines-path.patch
# PATCH-FIX-SUSE: version the library ld info; taken from debian
Patch3:         openssl-1.0.0-version.patch
Patch4:         openssl-1.0.2a-padlock64.patch
# PATCH-FIX-UPSTREAM http://rt.openssl.org/Ticket/Attachment/WithHeaders/20049
Patch5:         openssl-fix-pod-syntax.diff
Patch6:         openssl-truststore.patch
Patch7:         compression_methods_switch.patch
Patch9:         openssl-1.0.2a-default-paths.patch
Patch10:        openssl-pkgconfig.patch
Patch13:        openssl-1.0.2a-ipv6-apps.patch
Patch14:        openssl-riscv64-config.patch
# FIPS patches:
Patch15:        openssl-1.0.2i-fips.patch
Patch16:        openssl-1.0.2a-fips-ec.patch
Patch17:        openssl-1.0.2a-fips-ctor.patch
Patch18:        openssl-1.0.2i-new-fips-reqs.patch
Patch19:        openssl-gcc-attributes.patch
Patch26:        0001-Axe-builtin-printf-implementation-use-glibc-instead.patch
Patch33:        openssl-no-egd.patch
Patch34:        openssl-fips-hidden.patch
Patch35:        openssl-1.0.1e-add-suse-default-cipher.patch
Patch37:        openssl-1.0.1e-add-test-suse-default-cipher-suite.patch
Patch38:        openssl-missing_FIPS_ec_group_new_by_curve_name.patch
# FIPS patches from SLE-12
Patch41:        openssl-fips-dont_run_FIPS_module_installed.patch
Patch50:        openssl-fips_disallow_x931_rand_method.patch
Patch51:        openssl-fips_disallow_ENGINE_loading.patch
Patch53:        openssl-rsakeygen-minimum-distance.patch
Patch54:        openssl-urandom-reseeding.patch
Patch55:        openssl-fips-rsagen-d-bits.patch
Patch56:        openssl-fips-selftests_in_nonfips_mode.patch
Patch57:        openssl-fips-fix-odd-rsakeybits.patch
Patch58:        openssl-fips-clearerror.patch
Patch59:        openssl-fips-dont-fall-back-to-default-digest.patch
Patch61:        openssl-fipslocking.patch
Patch63:        openssl-randfile_fread_interrupt.patch
Patch70:        openssl-fips-xts_nonidentical_key_parts.patch
Patch71:        openssl-fips_add_cavs_tests.patch
Patch73:        openssl-fips-OPENSSL_s390xcap.patch
Patch74:        openssl-fips_cavs_helpers_run_in_fips_mode.patch
Patch75:        openssl-fips_cavs_pad_with_zeroes.patch
Patch76:        openssl-fips_cavs_aes_keywrap.patch
Patch77:        openssl-fips-run_selftests_only_when_module_is_complete.patch
Patch78:        0001-Set-FIPS-thread-id-callback.patch
Patch79:        openssl-CVE-2018-0737-fips.patch
Patch80:        openssl-One_and_Done.patch
# OpenSSL Security Advisory [16 February 2021] [bsc#1182333,CVE-2021-23840] [bsc#1182331,CVE-2021-23841]
Patch81:        openssl-CVE-2021-23840.patch
Patch82:        openssl-CVE-2021-23841.patch
Patch83:        openssl-1.0.0-pic-pie.patch
Patch84:        openssl-DH.patch
Patch85:        openssl-add_rfc3526_rfc7919.patch
# OpenSSL Security Advisory [17 August 2021] bsc#1189521 CVE-2021-3712
Patch86:        CVE-2021-3712-ASN1_STRING-issues.patch
# OpenSSL Security Advisory bsc#1199166 CVE-2022-1292
Patch87:        openssl-CVE-2022-1292.patch
Patch88:        openssl-1_0_0-Fix-file-operations-in-c_rehash.patch
Patch89:        openssl-1_0_0-paramgen-default_to_rfc7919.patch
# PATCH-FIX-UPSTREAM bsc#1201627 Update further expiring certificates that affect tests
Patch90:        openssl-Update-further-expiring-certificates.patch
# PATCH-FIX-UPSTREAM bsc#1179491 CVE-2020-1971 EDIPARTYNAME NULL pointer de-reference
Patch91:        openssl-CVE-2020-1971.patch
#PATCH-FIX-UPSTREAM bsc#1207534 CVE-2022-4304 Timing Oracle in RSA Decryption
Patch92:        openssl-CVE-2022-4304.patch
#PATCH-FIX-UPSTREAM bsc#1207536 CVE-2023-0215 Use-after-free following BIO_new_NDEF()
Patch93:        openssl-CVE-2023-0215-1of4.patch
#Patch openssl-CVE-2023-0215-2of4.patch because this type of tests are not present
Patch94:        openssl-CVE-2023-0215-3of4.patch
Patch95:        openssl-CVE-2023-0215-4of4.patch
#PATCH-FIX-UPSTREAM bsc#1207533 CVE-2023-0286 Address type confusion related to X.400 address processing
Patch96:        openssl-CVE-2023-0286.patch
# PATCH-FIX-SUSE bsc#1202062 FIPS: Fix DH key generation in FIPS mode
Patch97:        openssl-fips_fix_DH_key_generation.patch
# PATCH-FIX-UPSTREAM: bsc#1209624, CVE-2023-0464 Excessive Resource Usage Verifying X.509 Policy Constraints
Patch98:        openssl-CVE-2023-0464.patch
# PATCH-FIX-UPSTREAM: bsc#1209878, CVE-2023-0465 Invalid certificate policies in leaf certificates are silently ignored
Patch99:        openssl-CVE-2023-0465.patch
# PATCH-FIX-UPSTREAM: bsc#1209873, CVE-2023-0466 Certificate policy check not enabled
Patch100:       openssl-CVE-2023-0466.patch
# PATCH-FIX-UPSTREAM: bsc#1211430, CVE-2023-2650 Possible DoS translating ASN.1 object identifiers
Patch101:       openssl-CVE-2023-2650.patch
# PATCH-FIX-UPSTREAM: bsc#1213487 CVE-2023-3446 DH_check() excessive time with over sized modulus
Patch102:       openssl-CVE-2023-3446.patch
# PATCH-FIX-UPSTREAM bsc#1213853 CVE-2023-3817 Excessive time spent checking DH q parameter value
Patch103:       openssl-1_0-CVE-2023-3817.patch
# PATCH-FIX-UPSTREAM: bsc#1216922 CVE-2023-5678 Generating excessively long X9.42 DH keys or
# checking excessively long X9.42 DH keys or parameters may be very slow
Patch104:       openssl-CVE-2023-5678.patch
# PATCH-FIX-UPSTREAM: bsc#1219243 CVE-2024-0727: denial of service via null dereference
Patch105:       openssl-CVE-2024-0727.patch
# steam patches
Patch150:       openssl-fix-cpuid_setup.patch
# compat patches to build with soversion 10 (bsc#1175429)
Patch200:       openssl-1.0.2e-rpmbuild.patch
BuildRequires:  bc
BuildRequires:  ed
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
Provides:       ssl
Conflicts:      openssl(cli)
Provides:       openssl(cli)

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl1_0_0
Summary:        Secure Sockets and Transport Layer Security
Group:          Productivity/Networking/Security
Recommends:     ca-certificates-mozilla
# Merge back the hmac files bsc#1185116
Provides:       libopenssl1_0_0-hmac = %{version}-%{release}
Obsoletes:      libopenssl1_0_0-hmac < %{version}-%{release}

%description -n libopenssl1_0_0
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl10
Summary:        Secure Sockets and Transport Layer Security
Group:          Productivity/Networking/Security

%description -n libopenssl10
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

This package contains libcrypto.so.10 and libssl.so.10 symlinks and
provided capabilities usually provided by other distributions for
compatibility with third party packages.

%package -n libopenssl1_0_0-steam
Summary:        Secure Sockets and Transport Layer Security for steam
Group:          Productivity/Networking/Security

%description -n libopenssl1_0_0-steam
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

This subpackage is providing special patched edition for steam

%package -n libopenssl-1_0_0-devel
Summary:        Development files for OpenSSL
Group:          Development/Libraries/C and C++
Requires:       libopenssl1_0_0 = %{version}
Requires:       pkgconfig(zlib)
Recommends:     %{name} = %{version}
# we need to have around only the exact version we are able to operate with
Conflicts:      libopenssl-devel < %{version}
Conflicts:      libopenssl-devel > %{version}
Conflicts:      ssl-devel
Provides:       ssl-devel

%description -n libopenssl-1_0_0-devel
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

%package cavs
Summary:        CAVS testing framework and utilities
Group:          Productivity/Networking/Security
Requires:       libopenssl1_0_0 = %{version}-%{release}

%description cavs
Includes the Composite Application Validation System (CAVS)
testing framework and utilities.

%prep
%setup -q -n %{_rname}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 26 -p1
%patch -P 33 -p1
%patch -P 34 -p1
%patch -P 35 -p1
%patch -P 37 -p1
%patch -P 38 -p1
%patch -P 41 -p1
%patch -P 50 -p1
%patch -P 51 -p1
%patch -P 53 -p1
%patch -P 54 -p1
%patch -P 55 -p1
%patch -P 56 -p1
%patch -P 57 -p1
%patch -P 58 -p1
%patch -P 59 -p1
%patch -P 61 -p1
%patch -P 63 -p1
%patch -P 70 -p1
%patch -P 71 -p1
%patch -P 73 -p1
%patch -P 74 -p1
%patch -P 75 -p1
%patch -P 76 -p1
%patch -P 77 -p1
# we don't have FIPS_crypto_threadid_set_callback
%patch -P 78 -R -p1
%patch -P 79 -p1
%patch -P 80 -p1
%patch -P 81 -p1
%patch -P 82 -p1
%patch -P 83 -p1
%patch -P 84 -p1
%patch -P 85 -p1
%patch -P 86 -p1
%patch -P 87 -p1
%patch -P 88 -p1
%patch -P 89 -p1
%patch -P 90 -p1
%patch -P 91 -p1
%patch -P 92 -p1
%patch -P 93 -p1
%patch -P 94 -p1
%patch -P 95 -p1
%patch -P 96 -p1
%patch -P 97 -p1
%patch -P 98 -p1
%patch -P 99 -p1
%patch -P 100 -p1
%patch -P 101 -p1
%patch -P 102 -p1
%patch -P 103 -p1
%patch -P 104 -p1
%patch -P 105 -p1

# clean up patching leftovers
find . -name '*.orig' -delete

cp -p %{SOURCE10} .
cp -p %{SOURCE11} .

# create copy for steam
mkdir ../steam
cp -aR * ../steam/

# apply steam patches
pushd ../steam > /dev/null
%patch -P 150 -p1
popd > /dev/null

# create copy to build compat .so.10 library
mkdir ../compat
cp -aR * ../compat/

# apply compat patches
pushd ../compat > /dev/null
%patch -P 200 -p1
sed -i -e "s/-Wl,--version-script=openssl.ld/-Wl,--default-symver,--version-script=openssl.ld/" Configure
popd > /dev/null

%build
%ifarch armv5el armv5tel
export MACHINE=armv5el
%endif
%ifarch armv6l armv6hl
export MACHINE=armv6l
%endif

for i in . ../steam ../compat; do
pushd $i
./config \
    threads shared no-rc5 no-idea \
    fips \
    no-ssl2 \
    no-ssl3 \
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
    %{optflags} -std=gnu99 \
    -Wa,--noexecstack \
    -Wl,-z,relro,-z,now \
    -fno-common \
    -DTERMIO \
    -DPURIFY \
    -D_GNU_SOURCE \
    -DOPENSSL_NO_BUF_FREELISTS \
    $(getconf LFS_CFLAGS) \
    -Wall

# Record mtime of changes file instead of build time to make build-compare work
%make_build -j1 PERL=perl -C crypto buildinf.h
CHANGES=`stat --format="%%y" %{SOURCE1}`
cat crypto/buildinf.h
sed -i -e "s|#define DATE .*|#define DATE \"built on: $CHANGES\"|" crypto/buildinf.h
cat crypto/buildinf.h

# Build the library
%make_build depend -j1
%make_build -j1
LD_LIBRARY_PATH=`pwd` make rehash -j1
popd > /dev/null
done

%check
export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
LD_LIBRARY_PATH=`pwd` make test -j1
# show cyphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE99} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
make MANDIR=%{_mandir} INSTALL_PREFIX=%{buildroot} install
# kill static libs
rm -f %{buildroot}%{_libdir}/lib*.a
# install hmac binary
install -m 0755 crypto/fips/fips_standalone_hmac %{buildroot}%{_bindir}/fips_standalone_hmac
ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/
# cavs tests
install -m 0755 -d %{buildroot}%{cavs_dir}
cp -a crypto/fips/fips_*{test,vs} %{buildroot}%{cavs_dir}

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

# Place showciphers.c for %doc macro
cp %{SOURCE99} .

# the hmac hashes:
#
# this is a hack that re-defines the __os_install_post macro
# for a simple reason: the macro strips the binaries and thereby
# invalidates a HMAC that may have been created earlier.
# solution: create the hashes _after_ the macro runs.
#
# this shows up earlier because otherwise the %%expand of
# the macro is too late.
# remark: This is the same as running
#   openssl dgst -sha256 -hmac 'ppaksykemnsecgtsttplmamstKMEs'
%{expand:%%global __os_install_post {%__os_install_post

%{buildroot}%{_bindir}/fips_standalone_hmac \
  %{buildroot}%{_libdir}/libssl.so.%{num_version} > \
    %{buildroot}%{_libdir}/.libssl.so.%{num_version}.hmac

%{buildroot}%{_bindir}/fips_standalone_hmac \
  %{buildroot}%{_libdir}/libcrypto.so.%{num_version} > \
    %{buildroot}%{_libdir}/.libcrypto.so.%{num_version}.hmac

}}

for engine in 4758cca atalla nuron sureware ubsec cswift chil aep gmp capi; do
rm %{buildroot}/%{_libdir}/engines-1.0/lib$engine.so
done

%ifnarch %{ix86} x86_64
rm %{buildroot}/%{_libdir}/engines-1.0/libpadlock.so
%endif

# install the steam content
pushd ../steam > /dev/null
install -D -m 0755 libcrypto.so.1.0.0 %{buildroot}%{steamlibdir}/libcrypto.so.1.0.0
install -D -m 0755 libssl.so.1.0.0 %{buildroot}%{steamlibdir}/libssl.so.1.0.0
popd > /dev/null

# install the compat content with soname 10 to keep
# compatibility with other distros (bsc#1175429)
pushd ../compat > /dev/null
install -D -m 0755 libcrypto.so.10 %{buildroot}%{_libdir}/libcrypto.so.10
install -D -m 0755 libssl.so.10 %{buildroot}%{_libdir}/libssl.so.10
popd > /dev/null

%post -n libopenssl1_0_0 -p /sbin/ldconfig
%postun -n libopenssl1_0_0 -p /sbin/ldconfig
%post -n libopenssl1_0_0-steam -p /sbin/ldconfig
%postun -n libopenssl1_0_0-steam -p /sbin/ldconfig
%post -n libopenssl10 -p /sbin/ldconfig
%postun -n libopenssl10 -p /sbin/ldconfig

%files -n libopenssl1_0_0
%license LICENSE
%{_libdir}/libssl.so.%{num_version}
%{_libdir}/libcrypto.so.%{num_version}
%{_libdir}/.libssl.so.%{num_version}.hmac
%{_libdir}/.libcrypto.so.%{num_version}.hmac
%dir %{_libdir}/engines-1.0
%{_libdir}/engines-1.0

%files -n libopenssl10
%license LICENSE
%{_libdir}/libssl.so.10
%{_libdir}/libcrypto.so.10

%files -n libopenssl1_0_0-steam
%license LICENSE
%dir %{steamprefix}
%dir %{steamlibdir}
/%{steamlibdir}/libssl.so.%{num_version}
/%{steamlibdir}/libcrypto.so.%{num_version}

%files -n libopenssl-1_0_0-devel
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

%files cavs
%{_libexecdir}/%{name}

%files -f filelist
%doc CHANGE* INSTAL*
%doc NEWS README README.SUSE README-FIPS.txt
%dir %{ssletcdir}
%config (noreplace) %{ssletcdir}/openssl.cnf
%attr(700,root,root) %{ssletcdir}/private
%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%{_bindir}/c_rehash
%{_bindir}/fips_standalone_hmac
%{_bindir}/%{_rname}

%changelog
