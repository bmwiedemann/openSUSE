#
# spec file for package tpm2-pkcs11
#
# Copyright (c) 2023 SUSE LLC
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


%define so_ver  0
%define pythons python3
Name:           tpm2-pkcs11
Version:        1.9.0
Release:        0
Summary:        A PKCS#11 interface for TPM2 hardware
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-pkcs11
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  autoconf-archive >= 2017.03.21
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-generators
BuildRequires:  python3-PyYAML
BuildRequires:  python3-base
BuildRequires:  python3-cryptography
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-setuptools
BuildRequires:  python3-tpm2-pytss
BuildRequires:  tpm2.0-tools
BuildRequires:  pkgconfig(libcrypto) >= 1.0.2g
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tss2-esys) >= 2.0
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-tctildr)
BuildRequires:  pkgconfig(yaml-0.1)
%{?python_enable_dependency_generator}

%description
PKCS #11 is a Public-Key Cryptography Standard that defines a standard method to
access cryptographic services from tokens/devices such as hardware security
modules (HSM), smart cards, etc. This project uses a TPM2 device
as the cryptographic token.

%package -n libtpm2_pkcs11-0
Summary:        A PKCS#11 interface for TPM2 hardware
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libtpm2_pkcs11-0
PKCS #11 is a Public-Key Cryptography Standard that defines a standard method to
access cryptographic services from tokens/devices such as hardware security
modules (HSM), smart cards, etc. This project uses a TPM2 device
as the cryptographic token.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libtpm2_pkcs11-0 = %{version}
Provides:       libtpm2_pkcs11-devel = %{version}-%{release}

%description devel
Headers and libraries to build software against %{name}.

%prep
%autosetup

%build
autoreconf -fiv
%configure --disable-static
%make_build
cd tools
%python_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sysconfdir}/tpm2_pkcs11
cd tools
%python_install
%fdupes %{buildroot}

%post -n libtpm2_pkcs11-0 -p /sbin/ldconfig
%postun -n libtpm2_pkcs11-0 -p /sbin/ldconfig

%files
%license LICENSE
%doc docs/*
%dir %{_datadir}/p11-kit/modules
%dir %{_datadir}/p11-kit
%{_datadir}/p11-kit/modules/tpm2_pkcs11.module
%{_sysconfdir}/tpm2_pkcs11
%{_bindir}/tpm2_ptool
%{python_sitelib}/tpm2_pkcs11
%{python_sitelib}/*.egg-info

%files -n libtpm2_pkcs11-0
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/libtpm2_pkcs11.so.%{so_ver}*

%files devel
%dir %{_libdir}/pkcs11
%{_libdir}/pkgconfig/tpm2-pkcs11.pc
%{_libdir}/pkcs11/libtpm2_pkcs11.so

%changelog
