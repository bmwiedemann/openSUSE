#
# spec file for package libqca-qt5
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


%define _so 2
%bcond_without pkcs11
Name:           libqca-qt5
Version:        2.2.1
Release:        0
Summary:        Qt Cryptographic Architecture 2
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://userbase.kde.org/QCA
Source:         https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
Source1:        baselibs.conf
Source99:       libqca-qt5-rpmlintrc
# PATCH-FIX-OPENSUSE
Patch0:         qca-2.2.1-fixDSA.patch
BuildRequires:  ca-certificates
BuildRequires:  cmake >= 2.8.12
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gpg2
BuildRequires:  libdrm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.2.0
BuildRequires:  pkgconfig(openssl)
Requires:       gpg2 >= 2.0.0
Recommends:     %{name}-plugins
Provides:       libqca-qt5-2 = %{version}
Obsoletes:      libqca-qt5-2 < %{version}
%if %{with pkcs11}
BuildRequires:  pkcs11-helper-devel
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
Requires:       pkgconfig(Qt5Core) >= 5.2.0
Requires:       pkgconfig(Qt5Network) >= 5.2.0

%description devel
This package provides a generic Qt cryptographic architecture,
including a library and a plugin for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES and AES.

%package plugins
Summary:        Various plugins for the Qt Cryptographic Architecture 2
Group:          System/Libraries

%description plugins
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
      -DQT4_BUILD=OFF \
      -DBUILD_TESTS=OFF \
      -DQCA_INSTALL_IN_QT_PREFIX=ON \
      -DWITH_botan_PLUGIN=OFF \
      -DQCA_BINARY_INSTALL_DIR:PATH="%{_bindir}" \
      -DQCA_MAN_INSTALL_DIR:PATH="%{_mandir}" \
      -DQCA_SUFFIX=qt5
make %{?_smp_mflags}

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README TODO
%{_libdir}/libqca-qt5.so.*
%dir %{_libdir}/qt5/plugins/crypto
%{_libdir}/qt5/plugins/crypto/libqca-logger.so
%{_libdir}/qt5/plugins/crypto/libqca-softstore.so
%{_libdir}/qt5/plugins/crypto/libqca-ossl.so
%{_libdir}/qt5/plugins/crypto/libqca-gnupg.so
%{_libdir}/qt5/plugins/crypto/libqca-gcrypt.so

%files devel
%{_bindir}/qcatool-qt5
%{_bindir}/mozcerts-qt5
%{_includedir}/qt5/Qca-qt5/
%{_libdir}/qt5/mkspecs/features/crypto.prf
%{_mandir}/man1/qcatool-qt5.1%{?ext_man}
%{_libdir}/libqca-qt5.so
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_libdir}/cmake/Qca-qt5/

%files plugins
%{_libdir}/qt5/plugins/crypto/libqca-cyrus-sasl.so
%{_libdir}/qt5/plugins/crypto/libqca-nss.so
%if %{with pkcs11}
%{_libdir}/qt5/plugins/crypto/libqca-pkcs11.so
%endif

%changelog
