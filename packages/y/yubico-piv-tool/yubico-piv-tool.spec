#
# spec file for package yubico-piv-tool
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


%define sover  2
Name:           yubico-piv-tool
Version:        2.3.0
Release:        0
Summary:        Yubico YubiKey NEO CCID Manager
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/yubico-piv-tool/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubico-piv-tool/Releases/%{name}-%{version}.tar.gz.sig
Source3:        yubico-piv-tool.keyring
Patch1:         pthread-link.patch
BuildRequires:  c++_compiler
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  gengetopt
BuildRequires:  help2man
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  valgrind
BuildRequires:  pkgconfig(openssl)
Requires:       libykcs11-%{sover} = %{version}
Requires:       libykpiv%{sover} = %{version}

%description
This is a command line tool to interact with the PIV applet on a YubiKey NEO.
Among other functions it supports, generating keys on device, importing keys
and certificates and creating certificate requests.

%package     -n libykpiv%{sover}
Summary:        Yubikey NEO PIV applet library
Group:          System/Libraries
Requires:       pcsc-ccid

%description -n libykpiv%{sover}
This is a low-level library to interact the PIV applet on a YubiKey NEO

%package     -n libykcs11-%{sover}
Summary:        Yubikey NEO PKCS#11 applet library
Group:          System/Libraries
Requires:       pcsc-ccid

%description -n libykcs11-%{sover}
This is a PKCS#11 module that allows to communicate with the PIV application running on a YubiKey

%package     -n libykpiv-devel
Summary:        Development files for the Yubikey NEO PIV applet library
Group:          Development/Libraries/C and C++
Requires:       libykpiv%{sover} = %{version}

%description -n libykpiv-devel
This package contains the header file needed to develop applications that use
Yubikey NEO PIV applet library.

%package     -n libykcs11-devel
Summary:        Development files for the Yubikey NEO PKCS#11 applet library
Group:          Development/Libraries/C and C++
Requires:       libykcs11-%{sover} = %{version}

%description -n libykcs11-devel
This package contains the header file needed to develop applications that use
Yubikey NEO PKCS#11 applet library.

%prep
%setup -q
%autopatch -p1

%build
%cmake -DBUILD_STATIC_LIB=OFF
%cmake_build

%check
cd build
make test

%install
%cmake_install

%post -n libykpiv%{sover} -p /sbin/ldconfig
%postun -n libykpiv%{sover} -p /sbin/ldconfig
%post -n libykcs11-%{sover} -p /sbin/ldconfig
%postun -n libykcs11-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n libykpiv%{sover}
%{_libdir}/libykpiv.so.%{sover}*

%files -n libykcs11-%{sover}
%{_libdir}/libykcs11.so.%{sover}*

%files -n libykpiv-devel
%dir %{_includedir}/ykpiv/
%{_includedir}/ykpiv/*
%{_libdir}/libykpiv.so
%{_libdir}/pkgconfig/ykpiv.pc

%files -n libykcs11-devel
%{_libdir}/libykcs11.so
%{_libdir}/pkgconfig/ykcs11.pc

%changelog
