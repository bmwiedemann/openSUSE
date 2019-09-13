#
# spec file for package libqca2
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


%bcond_with botan
%if 0%{?suse_version} > 1320
# Enable gcrypt plugin on TW
%bcond_without gcrypt
%else
%bcond_with gcrypt
%endif
%bcond_without nss
%bcond_without pkcs11
Name:           libqca2
Version:        2.2.1
Release:        0
Summary:        Qt Cryptographic Architecture 2
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://userbase.kde.org/QCA
Source:         https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE
Patch0:         qca-2.2.1-fixDSA.patch
BuildRequires:  ca-certificates
BuildRequires:  cmake >= 2.8.12
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gpg2
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtCore) >= 4.7
BuildRequires:  pkgconfig(openssl)
Requires:       gpg2 >= 2.0.0
%requires_eq    libqt4
%if %{with botan}
BuildRequires:  libbotan-devel
%endif
%if %{with gcrypt}
BuildRequires:  libgcrypt-devel >= 1.7
%endif
%if %{with nss}
BuildRequires:  pkgconfig(nss)
%endif
%if %{with pkcs11}
BuildRequires:  pkgconfig(libpkcs11-helper-1)
%endif

%description
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%package devel
Summary:        Development files for the Qt Cryptographic Architecture 2
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libqt4-devel

%description devel
This package provides a generic Qt cryptographic architecture,
including a library and a plugin for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES and AES.

%package plugin-cyrus-sasl
Summary:        Cyrus SASL plugin for the Qt Cryptographic Architecture 2
Group:          System/Libraries
Requires:       %{name} = %{version}

%description plugin-cyrus-sasl
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%package plugin-gcrypt
Summary:        Qt Cryptographic Architecture 2
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description plugin-gcrypt
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%package plugin-botan
Summary:        Botan plugin for the Qt Cryptographic Architecture 2
Group:          System/Libraries
Requires:       %{name} = %{version}
Provides:       %{name}:%{_libdir}/qt4/plugins/crypto/libqca-botan.so

%description plugin-botan
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%package plugin-nss
Summary:        NSS plugin for the Qt Cryptographic Architecture 2
Group:          System/Libraries
Requires:       %{name} = %{version}

%description plugin-nss
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%package plugin-pkcs11
Summary:        PKCS#11 support for the Qt Cryptographic Architecture 2
Group:          System/Libraries
Requires:       %{name} = %{version}

%description plugin-pkcs11
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%prep
%setup -q -n qca-%{version}
%patch0 -p1

%build
%cmake \
    -DQCA_PLUGINS_INSTALL_DIR=%{_libdir}/qt4/plugins/ \
    -DQCA_FEATURE_INSTALL_DIR=%{_datadir}/qt4/mkspecs/features/ \
    -DQT4_BUILD=ON \
    -DWITH_cyrus-sasl_PLUGIN=ON \
%if %{with gcrypt}
    -DWITH_gcrypt_PLUGIN=ON \
%endif
    -DWITH_gnupg_PLUGIN=ON \
    -DWITH_logger_PLUGIN=ON \
%if %{with botan}
    -DWITH_botan_PLUGIN=ON \
%endif
%if %{with nss}
    -DWITH_nss_PLUGIN=ON \
%endif
%if %{with pkcs11}
    -DWITH_pkcs11_PLUGIN=ON \
%endif
    -DWITH_ossl_PLUGIN=ON
make %{?_smp_mflags}

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README TODO
%{_bindir}/mozcerts
%{_libdir}/libqca.so.*
%dir %{_libdir}/qt4/plugins/crypto
%{_libdir}/qt4/plugins/crypto/libqca-logger.so
%{_libdir}/qt4/plugins/crypto/libqca-softstore.so
%{_libdir}/qt4/plugins/crypto/libqca-ossl.so
%{_libdir}/qt4/plugins/crypto/libqca-gnupg.so

%files devel
%{_bindir}/qcatool
%{_includedir}/QtCrypto
%{_datadir}/qt4/mkspecs/features/crypto.prf
%{_mandir}/man1/qcatool.1%{?ext_man}
%{_libdir}/libqca.so
%{_libdir}/pkgconfig/qca2.pc
%{_libdir}/cmake/Qca/

%files plugin-cyrus-sasl
%{_libdir}/qt4/plugins/crypto/libqca-cyrus-sasl.so

%if %{with gcrypt}
%files plugin-gcrypt
%{_libdir}/qt4/plugins/crypto/libqca-gcrypt.so
%endif

%if %{with botan}
%files plugin-botan
%{_libdir}/qt4/plugins/crypto/libqca-botan.so
%endif

%if %{with nss}
%files plugin-nss
%{_libdir}/qt4/plugins/crypto/libqca-nss.so
%endif

%if %{with pkcs11}
%files plugin-pkcs11
%{_libdir}/qt4/plugins/crypto/libqca-pkcs11.so
%endif

%changelog
