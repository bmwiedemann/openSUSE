#
# spec file for package pkcs11-helper
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           pkcs11-helper
Version:        1.30.0
Release:        0
Summary:        Helper Library for the Use with Smart Cards and the PKCS#11 API
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/OpenSC/OpenSC/wiki
Source0:        https://github.com/OpenSC/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
pkcs11-helper allows using multiple PKCS#11 providers at the same
time and selecting keys by id, label or certificate subject.
Besides it covers the following topics: * Handling card removal
and card insert events:
* Handling card re-insert to a different slot
* Supporting session expiration serialization
* and much more All this is possible using a simple API.

%package -n libpkcs11-helper1
Summary:        Helper Library for the Use with Smart Cards and the PKCS#11 API
Group:          System/Libraries
# dropped empty package with 1.30.0, required by openvpn
Provides:       %{name} = %{version}

%description -n libpkcs11-helper1
pkcs11-helper allows using multiple PKCS#11 providers at the same time,
selecting keys by id, label or certificate subject, handling card
removal and card insert events, handling card re-insert to a different
slot, supporting session expiration serialization and much more, all
using a simple API.

%package devel
Summary:        Helper Library for the Use with Smart Cards and the PKCS#11 API
Group:          Development/Libraries/C and C++
Requires:       libpkcs11-helper1 = %{version}

%description devel
pkcs11-helper allows using multiple PKCS#11 providers at the same time,
selecting keys by id, label or certificate subject, handling card
removal and card insert events, handling card re-insert to a different
slot, supporting session expiration serialization and much more, all
using a simple API.

%prep
%autosetup -p1

%build
#autoreconf -fvi
# We use only openssl - disable all other engines
%configure \
  --disable-static \
  --enable-doc \
  --docdir=%{_docdir}/%{name} \
  --disable-crypto-engine-gnutls \
  --disable-crypto-engine-nss \
  --disable-crypto-engine-polarssl \
  --disable-crypto-engine-mbedtls \
  --disable-crypto-engine-cryptoapi
%make_build

%install
%make_install
cp -a AUTHORS ChangeLog THANKS %{buildroot}%{_docdir}/%{name}/
find %{buildroot} -type f -name "*.la" -delete -print
# installed via macro
find %{buildroot}%{_docdir} -type f -name "COPYING*" -delete -print

%ldconfig_scriptlets -n libpkcs11-helper1

%files -n libpkcs11-helper1
%license COPYING*
%{_libdir}/libpkcs11-helper.so.*
%{_mandir}/man8/*%{ext_man}
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/api

%files devel
%license COPYING*
%doc %{_docdir}/%{name}/api
%{_includedir}/pkcs11-helper-1.0
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4

%changelog
