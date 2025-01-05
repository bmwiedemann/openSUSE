#
# spec file for package softhsm
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


%global softhsm_module "SoftHSM PKCS #11 Module"
%global nssdb %{_sysconfdir}/pki/nssdb
%global upname SoftHSMv2
Name:           softhsm
Version:        2.6.1+git.1732869438.f7883c2
Release:        0
Summary:        Software version of a PKCS#11 Hardware Security Module
License:        BSD-2-Clause
#Git-Web:       https://github.com/opendnssec/SoftHSMv2
URL:            https://www.opendnssec.org/
Source0:        %{upname}-%{version}.tar.gz
# Source0:        https://dist.opendnssec.org/source/%%{name}-%%{version}.tar.gz
# Source1:        https://dist.opendnssec.org/source/%%{name}-%%{version}.tar.gz.sig
# taken from coolkey which is not build on all arches we build on
# https://github.com/dogtagpki/coolkey/blob/master/src/install/pk11install.c
# patched with patch from coolkey-1.1.0-fix-build-gcc14.patch from the coolkey pkg
Source2:        softhsm2-pk11install.c
Source5:        softhsm.module
Source6:        ods-user.conf
Source9:        softhsm.keyring
Source99:       fedora.changelog
# PATCH-FIX-UPSTREAM softhsm-openssl3-tests.patch gh#opendnssec/SoftHSMv2!633
# Make the patch compatible with OpenSSL 3
Patch1:         softhsm-openssl3-tests.patch
# PATCH-FIX-UPSTREAM softhsm-prevent-global-deleted-objects-access.patch gh#opendnssec/SoftHSMv2#742
Patch3:         softhsm-prevent-global-deleted-objects-access.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-3-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mozilla-nss-devel
BuildRequires:  mozilla-nss-tools
# Because of directory ownership
BuildRequires:  p11-kit
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3 >= 3.4.2
BuildRequires:  sqlite3-devel >= 3.4.2
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(zlib)
Requires:       mozilla-nss-tools
Requires:       p11-kit
Requires(pre):  shadow
%sysusers_requires

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM. SoftHSM is
designed to meet the requirements of OpenDNSSEC, but can also work together
with other cryptographic products because of the PKCS#11 interface.

%package devel
Summary:        Development package of softhsm
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel
Requires:       sqlite3-devel

%description devel
The devel package contains the libsofthsm include files

%prep
%autosetup -p1 -n %{upname}-%{version}
cp -p %{SOURCE99} .

./autogen.sh

# remove softhsm/ subdir auto-added to --libdir
sed -i "s:full_libdir/softhsm:full_libdir:g" configure
sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
sed -i "s:libdir)/@PACKAGE@:libdir):" Makefile.in
autoreconf -fiv

%build
# This package fails its testsuite with LTO enabled and needs further
# investigation
%define _lto_cflags %{nil}
autoreconf --install
%configure --libdir=%{_libdir}/pkcs11 --with-openssl=%{_prefix} --enable-ecc --enable-eddsa --disable-gost \
           --with-migrate --enable-visibility --with-p11-kit=%{_datadir}/p11-kit/modules/

%make_build
# install our copy of pk11install taken from coolkey package
cp %{SOURCE2} .
gcc $(pkg-config --cflags nss) %{optflags} -c softhsm2-pk11install.c
# Some environment variables prevent linking from being done, therefore clean up the env.
env -i PATH=%{_prefix}/sbin:%{_prefix}/bin:/sbin:/bin gcc $(pkg-config --libs nss) -lpthread  -lsoftokn3 -ldl -lz %{optflags} softhsm2-pk11install.o -o softhsm2-pk11install

%sysusers_generate_pre %{SOURCE6} ods ods-user.conf

%install
%make_install
install -D %{SOURCE5} %{buildroot}/%{_datadir}/p11-kit/modules/softhsm.module

rm %{buildroot}/%{_sysconfdir}/softhsm2.conf.sample
rm -f %{buildroot}/%{_libdir}/pkcs11/*a
mkdir -p %{buildroot}%{_includedir}/softhsm
cp src/lib/*.h %{buildroot}%{_includedir}/softhsm
mkdir -p %{buildroot}/%{_sharedstatedir}/softhsm/tokens
install -m0755 -D softhsm2-pk11install %{buildroot}/%{_bindir}/softhsm2-pk11install

# leave a softlink where softhsm-1 installed its library. Programs like
# opendnssec have that filename in their configuration file.
mkdir -p %{buildroot}/%{_libdir}/softhsm/
ln -s ../pkcs11/libsofthsm2.so %{buildroot}/%{_libdir}/softhsm/libsofthsm.so
# rhbz#1272423 NSS needs it to be in the search path too
( cd  %{buildroot}/%{_libdir} ; ln -s pkcs11/libsofthsm2.so)

install -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/ods-user.conf

%pre -f ods.pre

%check
for d in crypto data_mgr handle_mgr object_store session_mgr slot_mgr ; do
%make_build check  -C src/lib/$d
done

pushd src/lib/test
%make_build p11test
for t in TokenTests AsymWrapUnwrapTests DigestTests ForkTests \
         InitTests InfoTests SessionTests UserTests RandomTests \
         SignVerifyTests AsymEncryptDecryptTests DeriveTests \
         ObjectTests SymmetricAlgorithmTests ; do
./p11test $t || true
done
popd

%post
isThere=`modutil -rawlist -dbdir %{nssdb} | grep %{softhsm_module} || echo NO`
if [ "$isThere" == "NO" ]; then
      softhsm2-pk11install -p %{nssdb} 'name=%{softhsm_module} library=libsofthsm2.so'
fi

if [ $1 -eq 0 ]; then
   modutil -delete %{softhsm_module} -dbdir %{nssdb} -force || :
fi

%clean

%files
%config(noreplace) %{_sysconfdir}/softhsm2.conf
%license LICENSE
%doc README.md FIPS-NOTES.md NEWS fedora.changelog
%{_bindir}/softhsm2-dump-file
%{_bindir}/softhsm2-keyconv
%{_bindir}/softhsm2-migrate
%{_bindir}/softhsm2-pk11install
%{_bindir}/softhsm2-util
%dir %{_libdir}/softhsm
%{_libdir}/pkcs11/libsofthsm2.so
%{_libdir}/softhsm/libsofthsm.so
%{_datadir}/p11-kit/modules/softhsm.module
%{_datadir}/p11-kit/modules/softhsm2.module
%attr(0750,ods,ods) %dir %{_sharedstatedir}/softhsm
%attr(1770,ods,ods) %dir %{_sharedstatedir}/softhsm/tokens
%{_mandir}/man1/softhsm2-dump-file.1%{?ext_man}
%{_mandir}/man1/softhsm2-keyconv.1%{?ext_man}
%{_mandir}/man1/softhsm2-migrate.1%{?ext_man}
%{_mandir}/man1/softhsm2-util.1%{?ext_man}
%{_mandir}/man5/softhsm2.conf.5%{?ext_man}
%{_sysusersdir}/ods-user.conf

%files devel
%attr(0755,root,root) %dir %{_includedir}/softhsm
%{_includedir}/softhsm/*.h
%{_libdir}/libsofthsm2.so

%changelog
