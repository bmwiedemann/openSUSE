#
# spec file for package libp11
#
# Copyright (c) 2025 SUSE LLC
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


# the libname depends on what version openssl it is linked against
%if 0%{?suse_version} < 1500
# libp11.so.2 for openssl 1.0 - suse_version < 1500
%define libname libp11-2
%else
# libp11.so.3 for openssl 1.1 - suse_version >= 1500
%define libname libp11-3
%endif
Name:           libp11
Version:        0.4.16
Release:        0
Summary:        Library Implementing a Small Layer on Top of PKCS#11 API
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://github.com/OpenSC/libp11
Source0:        https://github.com/OpenSC/libp11/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/OpenSC/libp11/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}-rpmlintrc
Source4:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# Required for testing
BuildRequires:  opensc
# For pgrep
BuildRequires:  procps
BuildRequires:  softhsm
# The engine_pkcs11 library has been merged into version 0.4.0 and later.
# (It existed only in security:chipcard OBS repository.
Obsoletes:      engine_pkcs11 <= 0.2.2

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

The official name for PKCS#11 is "RSA Security Inc. PKCS #11
Cryptographic Token Interface (Cryptoki)".

Libp11 source code includes the official header files (version 2.20)
and thus is "derived from the RSA Security Inc. PKCS #11 Cryptographic
Token Interface (Cryptoki)".

%package -n %{libname}
Summary:        Library Implementing a Small Layer on Top of PKCS#11 API
Group:          Productivity/Security
# RH has renamed libp11 to openssl-pkcs11 since 0.4.7-4, in order to keep
# compatibility we need to provide openssl-pkcs11 (jsc#PED-12017)
Provides:       openssl-pkcs11 = %{version}-%{release}

%description -n %{libname}
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

The official name for PKCS#11 is "RSA Security Inc. PKCS #11
Cryptographic Token Interface (Cryptoki)".

Libp11 source code includes the official header files (version 2.20)
and thus is "derived from the RSA Security Inc. PKCS #11 Cryptographic
Token Interface (Cryptoki)".

%package -n openssl-engine-%{name}
Summary:        Library Implementing a Small Layer on Top of PKCS#11 API
Group:          Productivity/Security
# IBM dropped support for the openssl-ibmpkcs11 and will contribute to
# libp11 project instead. (jsc#PED-3327)
Provides:       openssl-ibmpkcs11 = 1.0.1
Obsoletes:      openssl-ibmpkcs11 <= 1.0.1

%description -n openssl-engine-%{name}
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

The official name for PKCS#11 is "RSA Security Inc. PKCS #11
Cryptographic Token Interface (Cryptoki)".

Libp11 source code includes the official header files (version 2.20)
and thus is "derived from the RSA Security Inc. PKCS #11 Cryptographic
Token Interface (Cryptoki)".

%package -n openssl-provider-%{name}
Summary:        Library Implementing a Small Layer on Top of PKCS#11 API
Group:          Productivity/Security

%description -n openssl-provider-%{name}
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

The official name for PKCS#11 is "RSA Security Inc. PKCS #11
Cryptographic Token Interface (Cryptoki)".

Libp11 source code includes the official header files (version 2.20)
and thus is "derived from the RSA Security Inc. PKCS #11 Cryptographic
Token Interface (Cryptoki)".

%package devel
Summary:        Library Implementing a Small Layer on Top of PKCS#11 API
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       openssl-devel

%description devel
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

The official name for PKCS#11 is "RSA Security Inc. PKCS #11
Cryptographic Token Interface (Cryptoki)".

Libp11 source code include the official header files (version 2.20) and
thus is "derived from the RSA Security Inc. PKCS #11 Cryptographic
Token Interface (Cryptoki)".

%prep
%autosetup -p1
# Since the library name changes based on used openssl, we have to create baselibs.conf dynamically
echo %{libname} > %{_sourcedir}/baselibs.conf

%build
autoreconf -fiv
%configure \
    --disable-static \
    --disable-silent-rules \
    --docdir=%{_docdir}/%{libname}
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name} %{buildroot}%{_docdir}/%{libname}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_docdir}

%check
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc %{_docdir}/%{libname}
%{_libdir}/libp11.so.*

%files -n openssl-engine-%{name}
%if 0%{?suse_version} > 1325
%{_libdir}/engines-*
%else
%{_libdir}/engines
%endif

%files -n openssl-provider-%{name}
%{_libdir}/ossl-modules

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
