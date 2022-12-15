#
# spec file for package mozilla-nss
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2006-2022 Wolfgang Rosenauer
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


%global nss_softokn_fips_version 3.85
%define NSPR_min_version 4.35
%define nspr_ver %(rpm -q --queryformat '%%{VERSION}' mozilla-nspr)
%define nssdbdir %{_sysconfdir}/pki/nssdb
Name:           mozilla-nss
Version:        3.85
Release:        0
%define underscore_version 3_85
Summary:        Network Security Services
License:        MPL-2.0
Group:          System/Libraries
URL:            https://www.mozilla.org/projects/security/pki/nss/
Source:         https://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_%{underscore_version}_RTM/src/nss-%{version}.tar.gz
# hg clone https://hg.mozilla.org/projects/nss nss-%%{version}/nss ; cd nss-%%{version}/nss ; hg up NSS_%%{underscore_version}_RTM
#Source:         nss-%%{version}.tar.gz
Source1:        nss.pc.in
Source3:        nss-config.in
Source4:        %{name}-rpmlintrc
Source5:        baselibs.conf
Source6:        setup-nsssysinit.sh
Source7:        cert9.db
Source8:        key4.db
Source9:        pkcs11.txt
#Source10:       PayPalEE.cert
Source11:       nss-util.pc.in
Source13:       nss-util-config.in
Source99:       %{name}.changes
Patch1:         nss-opt.patch
Patch2:         system-nspr.patch
Patch3:         nss-no-rpath.patch
Patch4:         add-relro-linker-option.patch
Patch5:         malloc.patch
Patch6:         bmo-1400603.patch
Patch7:         nss-sqlitename.patch
Patch9:         nss-fips-use-getrandom.patch
Patch10:        nss-fips-dsa-kat.patch
Patch11:        nss-fips-pairwise-consistency-check.patch
Patch12:        nss-fips-rsa-keygen-strictness.patch
Patch13:        nss-fips-cavs-keywrap.patch
Patch14:        nss-fips-cavs-kas-ffc.patch
Patch15:        nss-fips-cavs-kas-ecc.patch
Patch16:        nss-fips-gcm-ctr.patch
Patch17:        nss-fips-constructor-self-tests.patch
Patch18:        nss-fips-cavs-general.patch
Patch19:        nss-fips-cavs-dsa-fixes.patch
Patch20:        nss-fips-cavs-rsa-fixes.patch
Patch21:        nss-fips-approved-crypto-non-ec.patch
Patch22:        nss-fips-zeroization.patch
Patch23:        nss-fips-tls-allow-md5-prf.patch
Patch24:        nss-fips-use-strong-random-pool.patch
Patch25:        nss-fips-detect-fips-mode-fixes.patch
Patch26:        nss-fips-combined-hash-sign-dsa-ecdsa.patch
Patch27:        nss-fips-aes-keywrap-post.patch
Patch37:        nss-fips-fix-missing-nspr.patch
Patch38:        nss-fips-stricter-dh.patch
Patch40:        nss-fips-180-3-csp-clearing.patch
Patch41:        nss-fips-pbkdf-kat-compliance.patch
Patch42:        nss-fips-tests-skip.patch
Patch44:        nss-fips-tests-enable-fips.patch
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
# aarch64 + gcc4.8 fails to build on SLE-12 due to undefined references
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(nspr) >= %{NSPR_min_version}
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Requires:       libfreebl3 >= %{nss_softokn_fips_version}
Requires:       libsoftokn3 >= %{nss_softokn_fips_version}
Requires:       mozilla-nspr >= %{NSPR_min_version}
%if "%{_lib}" == "lib64"
Requires:       libnssckbi.so()(64bit)
%else
Requires:       libnssckbi.so
%endif
%ifnarch %sparc
%if ! 0%{?qemu_user_space_build}
%define run_testsuite 1
%endif
%endif

%description
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v3,
TLS v1.0, v1.1, v1.2, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards.

%package devel
Summary:        Network (Netscape) Security Services development files
Group:          Development/Libraries/C and C++
Requires:       libfreebl3
Requires:       libsoftokn3
Requires:       mozilla-nss = %{version}-%{release}
Requires:       pkgconfig(nspr) >= %{NSPR_min_version}

%description devel
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v3,
TLS v1.0, v1.1, v1.2, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards.

%package tools
Summary:        Tools for developing, debugging, and managing applications that use NSS
Group:          System/Management
Requires(pre):  mozilla-nss >= %{version}

%description tools
The NSS Security Tools allow developers to test, debug, and manage
applications that use NSS.

%package sysinit
Summary:        System NSS Initialization
Group:          System/Management
Requires:       mozilla-nss >= %{version}
Requires(post): coreutils

%description sysinit
Default Operation System module that manages applications loading
NSS globally on the system. This module loads the system defined
PKCS #11 modules for NSS and chains with other NSS modules to load
any system or user configured modules.

%package -n libfreebl3
Summary:        Freebl library for the Network Security Services
Group:          System/Libraries
Recommends:     libfreebl3-hmac = %{version}-%{release}

%description -n libfreebl3
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v3,
TLS v1.0, v1.1, v1.2, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards.

This package installs the freebl library from NSS.

%package -n libfreebl3-hmac
Summary:        Freebl library checksums for the Network Security Services
Group:          System/Libraries
Requires:       libfreebl3 = %{version}-%{release}

%description -n libfreebl3-hmac
Checksums for libraries contained in the libfreebl3 package
used in the FIPS 140-2 mode.

%package -n libsoftokn3
Summary:        Network Security Services Softoken Module
Group:          System/Libraries
Requires:       libfreebl3 = %{version}-%{release}
Recommends:     libsoftokn3-hmac = %{version}-%{release}

%description -n libsoftokn3
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v3,
TLS v1.0, v1.1, v1.2, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards.

Network Security Services Softoken Cryptographic Module

%package -n libsoftokn3-hmac
Summary:        Network Security Services Softoken Module checksums
Group:          System/Libraries
Requires:       libsoftokn3 = %{version}-%{release}

%description -n libsoftokn3-hmac
Checksums for libraries contained in the libsoftokn3 package
used in the FIPS 140-2 mode.

%package certs
Summary:        CA certificates for NSS
Group:          Productivity/Networking/Security

%description certs
This package contains the integrated CA root certificates from the
Mozilla project.

%prep
%setup -q -n nss-%{version}
cd nss
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if 0%{?suse_version} > 1110
%patch5 -p1
%endif
%patch6 -p1
%patch7 -p1
# FIPS patches
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch37 -p1
%patch38 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch44 -p1

# additional CA certificates
#cd security/nss/lib/ckfw/builtins
#cat %{SOURCE2} >> certdata.txt
#make generate

%build
%ifarch %arm
# LTO fails on neon errors
%global _lto_cflags %{nil}
%else
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%endif
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
export CC=gcc-9
# Yes, they use both...
export CXX=g++-9
export CCC=g++-9
%endif
cd nss
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -name '*.[ch]' -print -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

export NSS_ALLOW_SSLKEYLOGFILE=1
export NSS_ENABLE_WERROR=0
export NSS_NO_PKCS11_BYPASS=1
export FREEBL_NO_DEPEND=1
export FREEBL_LOWHASH=1
export NSPR_INCLUDE_DIR=`nspr-config --includedir`
export NSPR_LIB_DIR=`nspr-config --libdir`
export OPT_FLAGS="%{optflags} -fno-strict-aliasing -fPIE -pie"
export LIBDIR=%{_libdir}
%ifarch x86_64 s390x ppc64 ppc64le ia64 aarch64 riscv64
export USE_64=1
%endif
export NSS_DISABLE_GTESTS=1
export NSS_USE_SYSTEM_SQLITE=1
export NSS_ENABLE_FIPS_INDICATORS=1
export NSS_FIPS_MODULE_ID="\"SUSE Linux Enterprise NSS %{version}-%{release}\""
#export SQLITE_LIB_NAME=nsssqlite3
MAKE_FLAGS="BUILD_OPT=1"
make %{?_smp_mflags} nss_build_all $MAKE_FLAGS
# run testsuite
%if 0%{?run_testsuite}
export BUILD_OPT=1
export HOST="localhost"
export DOMSUF="localdomain"
export USE_IP=TRUE
export IP_ADDRESS="127.0.0.1"
cd tests
./all.sh
if grep "FAILED" ../../../tests_results/security/localhost.1/output.log ; then
  echo "Testsuite FAILED"
  exit 1
fi
%endif

%install
cd nss
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libexecdir}/nss
mkdir -p %{buildroot}%{_includedir}/nss3
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{nssdbdir}
pushd ../dist/Linux*
# copy headers
cp -rL ../public/nss/*.h %{buildroot}%{_includedir}/nss3
# copy some freebl include files we also want
for file in blapi.h alghmac.h cmac.h
do
  cp -L ../private/nss/$file %{buildroot}/%{_includedir}/nss3
done
# copy dynamic libs
cp -L  lib/libnss3.so \
       lib/libnssdbm3.so \
       lib/libnssdbm3.chk \
       lib/libnssutil3.so \
       lib/libnssckbi.so \
       lib/libnsssysinit.so \
       lib/libsmime3.so \
       lib/libsoftokn3.so \
       lib/libsoftokn3.chk \
       lib/libssl3.so \
       %{buildroot}%{_libdir}
cp -L  lib/libfreebl3.so \
       lib/libfreebl3.chk \
       lib/libfreeblpriv3.so \
       lib/libfreeblpriv3.chk \
       %{buildroot}/%{_libdir}
#cp -L  lib/libnsssqlite3.so \
#       %{buildroot}%{_libdir}
# copy static libs
cp -L  lib/libcrmf.a \
       lib/libfreebl.a \
       lib/libnssb.a \
       lib/libnssckfw.a \
       %{buildroot}%{_libdir}
# copy tools
cp -L  bin/certutil \
       bin/cmsutil \
       bin/crlutil \
       bin/nss-policy-check \
       bin/modutil \
       bin/pk12util \
       bin/signtool \
       bin/signver \
       bin/ssltap \
       %{buildroot}%{_bindir}
# copy unsupported tools
cp -L  bin/atob \
       bin/btoa \
       bin/derdump \
       bin/ocspclnt \
       bin/pp \
       bin/selfserv \
       bin/shlibsign \
       bin/strsclnt \
       bin/symkeyutil \
       bin/tstclnt \
       bin/vfyserv \
       bin/vfychain \
       %{buildroot}%{_libexecdir}/nss
# prepare pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
sed "s:%%LIBDIR%%:%{_libdir}:g
s:%%VERSION%%:%{version}:g
s:%%NSPR_VERSION%%:%{nspr_ver}:g" \
  %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/nss.pc
sed "s:%%LIBDIR%%:%{_libdir}:g
s:%%VERSION%%:%{version}:g
s:%%NSPR_VERSION%%:%{nspr_ver}:g" \
  %{SOURCE11} > %{buildroot}%{_libdir}/pkgconfig/nss-util.pc
# prepare nss-config file
popd
NSS_VMAJOR=`cat lib/nss/nss.h | grep "#define.*NSS_VMAJOR" | gawk '{print $3}'`
NSS_VMINOR=`cat lib/nss/nss.h | grep "#define.*NSS_VMINOR" | gawk '{print $3}'`
NSS_VPATCH=`cat lib/nss/nss.h | grep "#define.*NSS_VPATCH" | gawk '{print $3}'`
cat %{SOURCE3} | sed -e "s,@libdir@,%{_libdir},g" \
                     -e "s,@prefix@,%{_prefix},g" \
                     -e "s,@exec_prefix@,%{_prefix},g" \
                     -e "s,@includedir@,%{_includedir}/nss3,g" \
                     -e "s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g" \
                     -e "s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g" \
                     -e "s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g" \
                     > %{buildroot}/%{_bindir}/nss-config
chmod 755 %{buildroot}/%{_bindir}/nss-config
NSSUTIL_VMAJOR=`cat lib/util/nssutil.h | grep "#define.*NSSUTIL_VMAJOR" | awk '{print $3}'`
NSSUTIL_VMINOR=`cat lib/util/nssutil.h | grep "#define.*NSSUTIL_VMINOR" | awk '{print $3}'`
NSSUTIL_VPATCH=`cat lib/util/nssutil.h | grep "#define.*NSSUTIL_VPATCH" | awk '{print $3}'`
cat %{SOURCE13} | sed -e "s,@libdir@,%{_libdir},g" \
                     -e "s,@prefix@,%{_prefix},g" \
                     -e "s,@exec_prefix@,%{_prefix},g" \
                     -e "s,@includedir@,%{_includedir}/nss3,g" \
                     -e "s,@MOD_MAJOR_VERSION@,$NSSUTIL_VMAJOR,g" \
                     -e "s,@MOD_MINOR_VERSION@,$NSSUTIL_VMINOR,g" \
                     -e "s,@MOD_PATCH_VERSION@,$NSSUTIL_VPATCH,g" \
                     > %{buildroot}/%{_bindir}/nss-util-config
chmod 755 %{buildroot}/%{_bindir}/nss-util-config
# setup-nsssysinfo.sh
install -m 744 %{SOURCE6} %{buildroot}%{_sbindir}/
# create empty NSS database
#LD_LIBRARY_PATH=%{buildroot}/%{_lib}:%{buildroot}%{_libdir} %{buildroot}%{_bindir}/modutil -force -dbdir "sql:%{buildroot}%{nssdbdir}" -create
#LD_LIBRARY_PATH=%{buildroot}/%{_lib}:%{buildroot}%{_libdir} %{buildroot}%{_bindir}/certutil -N -d "sql:%{buildroot}%{nssdbdir}" -f /dev/null 2>&1 > /dev/null
#chmod 644 "%{buildroot}%{nssdbdir}"/*
#sed "s:%{buildroot}::g
#s/^library=$/library=libnsssysinit.so/
#/^NSS/s/\(Flags=internal\)\(,[^m]\)/\1,moduleDBOnly\2/" \
#  %{buildroot}%{nssdbdir}/pkcs11.txt > %{buildroot}%{nssdbdir}/pkcs11.txt.sed
#  mv %{buildroot}%{nssdbdir}/pkcs11.txt{.sed,}
# copy empty NSS database
install -m 644 %{SOURCE7} %{buildroot}%{nssdbdir}
install -m 644 %{SOURCE8} %{buildroot}%{nssdbdir}
install -m 644 %{SOURCE9} %{buildroot}%{nssdbdir}
# create shlib sigs after extracting debuginfo
%define __spec_install_post \
  %{?__debug_package:%{__debug_install_post}} \
  %{__arch_install_post} \
  %__os_install_post \
  LD_LIBRARY_PATH=:%{buildroot}%{_libdir} %{buildroot}%{_libexecdir}/nss/shlibsign -i %{buildroot}%{_libdir}/libsoftokn3.so \
  LD_LIBRARY_PATH=:%{buildroot}%{_libdir} %{buildroot}%{_libexecdir}/nss/shlibsign -i %{buildroot}%{_libdir}/libnssdbm3.so \
  LD_LIBRARY_PATH=:%{buildroot}%{_libdir} %{buildroot}%{_libexecdir}/nss/shlibsign -i %{buildroot}/%{_libdir}/libfreebl3.so \
  LD_LIBRARY_PATH=:%{buildroot}%{_libdir} %{buildroot}%{_libexecdir}/nss/shlibsign -i %{buildroot}/%{_libdir}/libfreeblpriv3.so \
%{nil}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libfreebl3 -p /sbin/ldconfig
%postun -n libfreebl3 -p /sbin/ldconfig
%post -n libsoftokn3 -p /sbin/ldconfig
%postun -n libsoftokn3 -p /sbin/ldconfig

%post sysinit
/sbin/ldconfig
# make sure the current config is enabled
%{_sbindir}/setup-nsssysinit.sh on

%preun sysinit
if [ $1 = 0 ]; then
  %{_sbindir}/setup-nsssysinit.sh off
fi

%postun sysinit -p /sbin/ldconfig

%files
%{_libdir}/libnss3.so
%{_libdir}/libnssutil3.so
%{_libdir}/libsmime3.so
%{_libdir}/libssl3.so
#%%{_libdir}/libnsssqlite3.so

%files devel
%defattr(644, root, root, 755)
%{_includedir}/nss3/
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%attr(755,root,root) %{_bindir}/nss-config
%attr(755,root,root) %{_bindir}/nss-util-config

%files tools
%{_bindir}/*
%exclude %{_sbindir}/setup-nsssysinit.sh
%{_libexecdir}/nss/
%exclude %{_bindir}/nss-config
%exclude %{_bindir}/nss-util-config

%files sysinit
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/nssdb
%config(noreplace) %{_sysconfdir}/pki/nssdb/*
%{_libdir}/libnsssysinit.so
%{_sbindir}/setup-nsssysinit.sh

%files -n libfreebl3
%{_libdir}/libfreebl3.so
%{_libdir}/libfreeblpriv3.so

%files -n libfreebl3-hmac
%{_libdir}/libfreebl3.chk
%{_libdir}/libfreeblpriv3.chk

%files -n libsoftokn3
%{_libdir}/libsoftokn3.so
%{_libdir}/libnssdbm3.so

%files -n libsoftokn3-hmac
%{_libdir}/libsoftokn3.chk
%{_libdir}/libnssdbm3.chk

%files certs
%{_libdir}/libnssckbi.so

%changelog
