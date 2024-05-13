#
# spec file for package softhsm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Summary:        Software version of a PKCS#11 Hardware Security Module
License:        BSD-2-Clause
Group:          Productivity/Security
Name:           softhsm
Version:        2.5.0
Release:        0
Url:            http://www.opendnssec.org/
Source:         https://dist.opendnssec.org/source/%{name}-%{version}.tar.gz
Source1:        softhsm.module
# taken from coolkey which is not build on all arches we build on
Source2:        softhsm2-pk11install.c
Patch3:         softhsm-rsakeys.patch
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mozilla-nss-devel
BuildRequires:  mozilla-nss-tools
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3
BuildRequires:  sqlite3-devel >= 3.4.2
BuildRequires:  pkgconfig(zlib)
Requires(pre): shadow
Requires:       mozilla-nss-tools
Requires:       p11-kit

%global softhsm_module "SoftHSM PKCS #11 Module"
%global nssdb %{_sysconfdir}/pki/nssdb

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM. SoftHSM is
designed to meet the requirements of OpenDNSSEC, but can also work together
with other cryptographic products because of the PKCS#11 interface.

%package devel
Summary:        Development package of softhsm that includes the header files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}, openssl-devel, sqlite3-devel

%description devel
The devel package contains the libsofthsm include files

%prep
%setup -q
%patch3 -p1

# remove softhsm/ subdir auto-added to --libdir
sed -i "s:full_libdir/softhsm:full_libdir:g" configure
sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
sed -i "s:libdir)/@PACKAGE@:libdir):" Makefile.in

%build
autoreconf --install
%configure --libdir=%{_libdir}/pkcs11 --with-openssl=%{_prefix} --enable-ecc --disable-gost \
           --with-migrate --enable-visibility

make %{?_smp_mflags}
# install our copy of pk11install taken from coolkey package
cp %{SOURCE2} .
gcc $(pkg-config --cflags nss) %{optflags} -c softhsm2-pk11install.c
# Some environment variables prevent linking from being done, therefore clean up the env.
env -i PATH=/usr/sbin:/usr/bin:/sbin:/bin gcc $(pkg-config --libs nss) -lpthread  -lsoftokn3 -ldl -lz %{optflags} softhsm2-pk11install.o -o softhsm2-pk11install

%check
make check

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -D %{SOURCE1} %{buildroot}/%{_datadir}/p11-kit/modules/softhsm.module

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

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/softhsm2.conf
%doc LICENSE README.md NEWS
%dir %{_libdir}/pkcs11
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%dir %{_libdir}/softhsm
%{_bindir}/*
%{_libdir}/pkcs11/libsofthsm2.so
%{_libdir}/softhsm/libsofthsm.so
%attr(0664,root,root) %{_datadir}/p11-kit/modules/softhsm.module
%attr(0664,root,root) %{_datadir}/p11-kit/modules/softhsm2.module
%attr(0770,ods,ods) %dir %{_var}/lib/softhsm
%attr(0770,ods,ods) %dir %{_var}/lib/softhsm/tokens
%{_mandir}/*/*
%{_bindir}/softhsm2-pk11install

%files devel
%defattr(-,root,root)
%attr(0755,root,root) %dir %{_includedir}/softhsm
%{_includedir}/softhsm/*.h

%pre
getent group ods >/dev/null || groupadd -r ods
getent passwd ods >/dev/null || \
    useradd -r -g ods -d /%{_sharedstatedir}/softhsm -s /sbin/nologin \
    -c "softhsm private keys owner" ods
exit 0

%post
isThere=`modutil -rawlist -dbdir %{nssdb} | grep %{softhsm_module} || echo NO`
if [ "$isThere" == "NO" ]; then
      softhsm2-pk11install -p %{nssdb} 'name=%{softhsm_module} library=libsofthsm2.so'
fi

if [ $1 -eq 0 ]; then
   modutil -delete %{softhsm_module} -dbdir %{nssdb} -force || :
fi

%changelog
