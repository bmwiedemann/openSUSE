#
# spec file for package qca
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define pkgname_suffix %{nil}
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt5"
  %define qt5 1
  %define pkgname_suffix -qt5
  %define qt_min_version 5.14
  %define _plugindir %{_libqt5_plugindir}
%endif
# %%elif requires rpm 4.15...
%if "%{flavor}" == "qt6"
  %define qt6 1
  %define pkgname_suffix -qt6
  %define qt_min_version 6.0
  %define _plugindir %{_qt6_pluginsdir}
%endif
#
%define _soversion 2
%define realversion 2.3.9
%bcond_without pkcs11
Name:           qca%{pkgname_suffix}
Version:        2.3.9
Release:        0
Summary:        Qt Cryptographic Architecture 2
License:        LGPL-2.1-or-later
URL:            https://userbase.kde.org/QCA
# Using git for now
Source0:        qca-%{version}.tar.xz
#Source0:        https://download.kde.org/stable/qca/%%{version}/qca-%%{version}.tar.xz
#Source1:        https://download.kde.org/stable/qca/%%{version}/qca-%%{version}.tar.xz.sig
Source2:        qca.keyring
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cmake
BuildRequires:  gpg2
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
%if %{with pkcs11}
BuildRequires:  pkcs11-helper-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if 0%{?qt5}
BuildRequires:  cmake(Qt5Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Network) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Test) >= %{qt_min_version}
%endif
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Network) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Test) >= %{qt_min_version}
%endif
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl) >= 1.1.1
Requires:       gpg2 >= 2.0.0
%if 0%{?qt5}
# The plugins used to be in the same package as the library
Obsoletes:      libqca-qt5 <= 2.3.2
%endif

%description
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%package -n libqca-%{flavor}-%{_soversion}
Summary:        QCA library
%if 0%{?qt5}
Provides:       libqca-qt5 = %{version}
Obsoletes:      libqca-qt5 < %{version}
%endif
Requires:       %{name} >= %{version}
Recommends:     %{name}-plugins

%description -n libqca-%{flavor}-%{_soversion}
The Qt cryptographic library.

%package devel
Summary:        Development files for the Qt Cryptographic Architecture 2
Requires:       libqca-%{flavor}-%{_soversion} = %{version}
%if 0%{?qt5}
Requires:       cmake(Qt5Core) >= %{qt_min_version}
Requires:       cmake(Qt5Network) >= %{qt_min_version}
Provides:       libqca-qt5-devel = %{version}
Obsoletes:      libqca-qt5-devel < %{version}
%endif
%if 0%{?qt6}
Requires:       cmake(Qt6Core) >= %{qt_min_version}
Requires:       cmake(Qt6Network) >= %{qt_min_version}
%endif

%description devel
This package provides a generic Qt cryptographic architecture,
including a library and a plugin for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES and AES.

%package plugins
Summary:        Various plugins for the Qt Cryptographic Architecture 2
%if 0%{?qt5}
Provides:       libqca-qt5-plugins = %{version}
Obsoletes:      libqca-qt5-plugins < %{version}
%endif

%description plugins
This package provides a generic Qt cryptographic architecture,
including a library and a plug-in for using all supported capabilities
of openssl, like SSL/TLS, X509, RSA, SHA1, MD5, Blowfish, 3DES, and
AES.

It can be extended by further plug-ins, for example, with qca-sasl for
SASL support.

%prep
%autosetup -p1 -n qca-%{version}
# Don't build examples
echo > examples/CMakeLists.txt

# The pgp test fails randomly
sed -i '/pgpunittest/d' unittest/CMakeLists.txt

%build
%if 0%{?qt5}
%cmake \
%else
%cmake_qt6 \
  -DBUILD_WITH_QT6=ON \
%endif
  -DBUILD_TESTS=ON \
  -DQCA_INSTALL_IN_QT_PREFIX=ON \
  -DQCA_BINARY_INSTALL_DIR:PATH="%{_bindir}" \
  -DQCA_MAN_INSTALL_DIR:PATH="%{_mandir}" \
  -DWITH_botan_PLUGIN=OFF

%if 0%{?qt5}
%cmake_build
%else
%qt6_build
%endif

%install
%if 0%{?qt5}
%cmake_install
%else
%qt6_install
%endif

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
%if 0%{?qt5}
export QT_PLUGIN_PATH=%{buildroot}%{_libqt5_plugindir}:%{_libqt5_plugindir}
%else
export QT_PLUGIN_PATH=%{buildroot}%{_qt6_pluginsdir}:%{_qt6_pluginsdir}
%endif
# The 'PGP' test fails randomly
%define _smp_mflags -j1
%ctest

%ldconfig_scriptlets -n libqca-%{flavor}-%{_soversion}

%files
%dir %{_plugindir}/crypto
%{_plugindir}/crypto/libqca-gcrypt.so
%{_plugindir}/crypto/libqca-gnupg.so
%{_plugindir}/crypto/libqca-logger.so
%{_plugindir}/crypto/libqca-ossl.so
%{_plugindir}/crypto/libqca-softstore.so

%files -n libqca-%{flavor}-%{_soversion}
%license COPYING
%doc README
%{_libdir}/libqca-%{flavor}.so.%{_soversion}
%{_libdir}/libqca-%{flavor}.so.%{realversion}

%files devel
%{_bindir}/mozcerts-%{flavor}
%{_bindir}/qcatool-%{flavor}
%{_includedir}/%{flavor}/Qca-%{flavor}/
%if 0%{?qt5}
%{_libdir}/%{flavor}/mkspecs/features/crypto.prf
%endif
%{_libdir}/cmake/Qca-%{flavor}/
%{_libdir}/libqca-%{flavor}.so
%if 0%{?qt5}
%{_libdir}/pkgconfig/qca2-%{flavor}.pc
%endif
%{_mandir}/man1/qcatool-%{flavor}.1%{?ext_man}

%files plugins
%{_plugindir}/crypto/libqca-cyrus-sasl.so
%{_plugindir}/crypto/libqca-nss.so
%if %{with pkcs11}
%{_plugindir}/crypto/libqca-pkcs11.so
%endif

%changelog
