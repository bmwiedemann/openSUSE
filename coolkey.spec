#
# spec file for package coolkey
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


%define coolkey_module "CoolKey PKCS #11 Module"
%define nssdb %{_sysconfdir}/pki/nssdb
Name:           coolkey
Version:        1.1.0
Release:        0
Summary:        CoolKey and CAC PKCS #11 PKI Module for Smart Cards
License:        LGPL-2.1-only
Group:          Productivity/Security
URL:            https://www.dogtagpki.org/wiki/CoolKey
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
Source2:        baselibs.conf
# Patches imported from Fedora and CentOS:
# PATCH-FIX-SECURITY coolkey-cache-dir-move.patch sbrabec@suse.cz bnc304180 CVE-2007-4129 -- Fix file and directory permission flaw.
Patch1:         coolkey-cache-dir-move.patch
# PATCH-FIX-FEDORA coolkey-gcc43.patch bnc661643 sbrabec@suse.cz -- Fix for gcc-4.3.
Patch2:         coolkey-gcc43.patch
# PATCH-FEATURE-FEDORA coolkey-latest.patch bnc661643 sbrabec@suse.cz -- The head branch patch.
Patch3:         coolkey-latest.patch
# PATCH-FIX-FEDORA coolkey-simple-bugs.patch bnc661643 sbrabec@suse.cz -- Fix imported from Fedora, mostly merging former SUSE fixes.
Patch4:         coolkey-simple-bugs.patch
# PATCH-FIX-FEDORA coolkey-thread-fix.patch bnc661643 sbrabec@suse.cz -- Fix threading.
Patch5:         coolkey-thread-fix.patch
# PATCH-FEATURE-FEDORA coolkey-cac.patch bnc661643 sbrabec@suse.cz -- Support for CAC cards.
Patch6:         coolkey-cac.patch
# PATCH-FIX-FEDORA coolkey-cac-1.patch bnc661643 sbrabec@suse.cz -- Fixes of CAC support patch.
Patch7:         coolkey-cac-1.patch
# PATCH-FIX-FEDORA coolkey-pcsc-lite-fix.patch bnc661643 sbrabec@suse.cz -- Port to the latest pcsc-lite.
Patch8:         coolkey-pcsc-lite-fix.patch
Patch9:         coolkey-fix-token-removal-failure.patch
Patch10:        coolkey-piv-ecc-el7.patch
Patch20:        coolkey-1.1.0-noapplet.patch
Patch21:        coolkey-1.1.0-fix-spurious-event.patch
Patch22:        coolkey-1.1.0-p15.patch
Patch23:        coolkey-1.1.0-p15-coverity.patch
Patch24:        coolkey-1.1.0-more-keys.patch
Patch25:        coolkey-1.1.0-fail-on-bad-mechanisms.patch
Patch26:        coolkey-1.1.0-max-cpu-bug.patch
Patch27:        coolkey-1.1.0-rhel7-alt-cac.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mozilla-nss-devel
BuildRequires:  mozilla-nss-sysinit
BuildRequires:  mozilla-nss-tools
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
#Requires:       pcsc-lite
# Requires: ifd-egate
Requires:       pcsc-ccid
# 390 does not have libusb or smartCards
ExcludeArch:    s390 s390x

%description
Linux Driver support for the CoolKey and CAC products. CoolKeys are
part of a complete PKI solution that provides smart card login, single
sign-on, secure messaging, and secure email access. In the complete
solution, users are issued CoolKeys by their employer, ISP, bank, or
other parties. When the user plugs the keys in for the first time, the
keys are automatically provisioned with certificates, keys, and a PIN,
unique for that user by the Red Hat Certificate System. Once the
CoolKey is provisioned, the user can take the key to any system and use
it to login (authenticate), send and receive signed and encrypted
email, or participate in secure messaging or IRC communication.
CoolKeys are based on JavaCard 1.2.

%package devel
Summary:        CoolKey and CAC PKCS #11 PKI Module for Smart Cards
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Linux Driver support for the CoolKey and CAC products.

CoolKeys are part of complete PKI solution that provides smart card
login, single sign-on, secure messaging, and secure email access. In
the complete solution, users are issued CoolKeys by their employer,
ISP, bank, or other agency. When the user plugs in the keys for the
first time, the keys are automatically provisioned with certificates,
keys, and a PIN unique to that user by the Red Hat Certificate System.
Once the CoolKey is provisioned, the user can take the key to any
system and use it to login (authenticate), send and receive signed and
encrypted email, or participate in secure messaging or IRC
communication.

CoolKeys are based on JavaCard 1.2.

%prep
%setup -q
%patch -P 1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5
%patch -P 6
%patch -P 7
%patch -P 8
%patch -P 9 -p1
%patch -P 10
%patch -P 20
%patch -P 21
%patch -P 22
%patch -P 23
%patch -P 24
%patch -P 25
%patch -P 26
%patch -P 27

%build
autoreconf -f -i
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure\
	--with-debug\
	--disable-dependency-tracking\
	--enable-pk11install
%make_build

%install
%make_install
ln -s pkcs11/libcoolkeypk11.so %{buildroot}/%{_libdir}

%triggerin -- mozilla-nss-sysinit mozilla-nss-tools
if [ -x %{_bindir}/pk11install -a -x %{_bindir}/modutil -a -f %{_sysconfdir}/pki/nssdb/pkcs11.txt ]; then
  isThere=`modutil -rawlist -dbdir dbm:%{nssdb} | grep %{coolkey_module} || echo NO`
  if [ "$isThere" = "NO" ]; then
      pk11install -l -p %{nssdb} 'name=%{coolkey_module} library=libcoolkeypk11.so' ||:
   fi
  isThere=`modutil -rawlist -dbdir sql:%{nssdb} | grep %{coolkey_module} || echo NO`
  if [ "$isThere" = "NO" ]; then
      pk11install -s -p %{nssdb} 'name=%{coolkey_module} library=libcoolkeypk11.so' ||:
   fi
fi

%post
/sbin/ldconfig
if [ -x %{_bindir}/pk11install -a -x %{_bindir}/modutil -a -f %{_sysconfdir}/pki/nssdb/pkcs11.txt ]; then
  isThere=`modutil -rawlist -dbdir dbm:%{nssdb} | grep %{coolkey_module} || echo NO`
  if [ "$isThere" = "NO" ]; then
      pk11install -l -p %{nssdb} 'name=%{coolkey_module} library=libcoolkeypk11.so' ||:
   fi
  isThere=`modutil -rawlist -dbdir sql:%{nssdb} | grep %{coolkey_module} || echo NO`
  if [ "$isThere" = "NO" ]; then
      pk11install -s -p %{nssdb} 'name=%{coolkey_module} library=libcoolkeypk11.so' ||:
   fi
fi

%postun
/sbin/ldconfig
if [ $1 -eq 0 -a -x %{_bindir}/modutil -a -f %{_sysconfdir}/pki/nssdb/pkcs11.txt ]; then
   modutil -delete %{coolkey_module} -dbdir dbm:%{nssdb} -force || :
   modutil -delete %{coolkey_module} -dbdir sql:%{nssdb} -force || :
fi

%files
%license LICENSE
%doc ChangeLog README
%{_bindir}/pk11install
%{_libdir}/libcoolkeypk11.so
%{_libdir}/pkcs11/*.so
%{_libdir}/libckyapplet.so.*
# FIXME: Find a common package owning this directory:
%dir %{_libdir}/pkcs11

%files devel
%{_libdir}/libckyapplet.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

%changelog
