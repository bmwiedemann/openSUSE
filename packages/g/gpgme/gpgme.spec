#
# spec file for package gpgme
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


%define psuffix %{nil}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_without python3
%bcond_with qt
%endif
%if "%{flavor}" == "qt"
%define psuffix qt
%bcond_with python3
%bcond_without qt
%endif
%if "%{flavor}" == "qt6"
%define psuffix qt6
%bcond_with python3
%bcond_without qt6
%endif

%if 0%{suse_version} >= 1550 || "%{?pythons}" == "python311"
%bcond_without replace_distutils
%else
# Keep deprecated distutils for Python 3.6 on 15.x
%bcond_with replace_distutils
%endif

Name:           gpgme%{psuffix}
Version:        1.24.0
Release:        0
Summary:        Programmatic library interface to GnuPG
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://www.gnupg.org/related_software/gpgme/
Source:         https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source2:        baselibs.conf
# https://www.gnupg.org/signature_key.html
Source3:        https://gnupg.org/signature_key.asc#/gpgme.keyring
# used to have a fixed timestamp
Source99:       gpgme.changes
# PATCH-FIX-OPENSUSE gpgme-suse-nobetasuffix.patch code@bnavigator.de -- remove "-unknown" betasuffix boo#1205197
Patch2:         gpgme-suse-nobetasuffix.patch
Patch3:         python313.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gpg2 >= 2.4.1
BuildRequires:  libassuan-devel >= 2.4.2
BuildRequires:  libgpg-error-devel >= 1.47
BuildRequires:  pkgconfig
BuildRequires:  swig
%if %{with python3}
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
%if %{with replace_distutils}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 62.4}
BuildRequires:  %{python_module wheel}
%endif
%endif
%if %{with qt}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
%endif
%if %{with qt6}
%if 0%{?suse_version} < 1550
# The default compiler is too old for Qt6, use the newest
# version available in the :Update repo
BuildRequires:  gcc12-c++
BuildRequires:  gcc12-PIE
%endif
BuildRequires:  pkgconfig(Qt6Core) >= 6.4.0
BuildRequires:  pkgconfig(Qt6Test)
%endif
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
%define python_sitearch %python3_sitearch
%define python_version %python3_version
%define python_files() -n python3-%{**}
%endif

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management. It uses GnuPG as its back-end.

%package -n libgpgme11
Summary:        Programmatic library interface to GnuPG
Group:          System/Libraries
Requires:       gpg2

%description -n libgpgme11
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management. It uses GnuPG as its back-end.

%package -n libgpgme-devel
Summary:        Development files for GPGME, a C library for accessing GnuPG
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgpg-error-devel
Requires:       libgpgme11 = %{version}
%requires_ge    libassuan-devel
Provides:       gpgme-devel = %{version}
Obsoletes:      gpgme-devel < %{version}

%description -n libgpgme-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This subpackage contains the headers needed for building applications
making use of libgpgme.

%package -n libgpgmepp6
Summary:        Programmatic C++ library interface to GnuPG
Group:          System/Libraries
Requires:       gpg2

%description -n libgpgmepp6
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the C++ bindings.

%package -n libgpgmepp-devel
Summary:        Development files for libgpgmepp, a C++ library for accessing GnuPG
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgpg-error-devel
Requires:       libgpgme-devel = %{version}
Requires:       libgpgmepp6 = %{version}
# This avoids requiring CMake at build time for the default flavor
Provides:       cmake(Gpgmepp) = %{version}
%requires_ge    libassuan-devel

%description -n libgpgmepp-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This subpackage contains the headers needed for building applications
making use of libgpgmepp.

%if 0%{?python_subpackage_only}
%package -n python-gpg
Summary:        Python %{python_version} bindings for GPGME, a library for accessing GnuPG
Group:          Development/Languages/Python

%description -n python-gpg
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the bindings to use the library from Python %{python_version} applications.

%else

%package -n python3-gpg
Summary:        Python 3 bindings for GPGME, a library for accessing GnuPG
Group:          Development/Languages/Python

%description -n python3-gpg
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the bindings to use the library from Python 3 applications.
%endif

%package -n libqgpgme15
Summary:        Programmatic Qt 5 library interface to GnuPG
Group:          System/Libraries
Requires:       gpg2

%description -n libqgpgme15
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the Qt 5 bindings.

%package -n libqgpgme-devel
Summary:        Development files for libqgpgme, a Qt 5 library for accessing GnuPG
Group:          Development/Libraries/C and C++
Requires:       libgpgme-devel = %{version}
Requires:       libgpgmepp-devel = %{version}
Requires:       libqgpgme15 = %{version}

%description -n libqgpgme-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the bindings to use the library in Qt 5 C++ applications.

%package -n libqgpgmeqt6-15
Summary:        Programmatic Qt 6 library interface to GnuPG
Group:          System/Libraries
Requires:       gpg2

%description -n libqgpgmeqt6-15
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the Qt 6 bindings.

%package -n libqgpgmeqt6-devel
Summary:        Development files for libqgpgmeqt6, a Qt library for accessing GnuPG
Group:          Development/Libraries/C and C++
Requires:       libgpgme-devel = %{version}
Requires:       libgpgmepp-devel = %{version}
Requires:       libqgpgmeqt6-15 = %{version}
# The include folders have the same name in both libqgpgme-devel and libqgpgmeqt6-devel
Conflicts:      libqgpgme-devel

%description -n libqgpgmeqt6-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the bindings to use the library in Qt 6 C++ applications.

%prep
%autosetup -N -n gpgme-%{version}
%if %{with replace_distutils}
%patch -p1 -P2 -P3
%endif
%if 0%{suse_version} > 1500
# Note: rpm in 15.x does not know about the autopatch -m flag.
# Need to apply every additional patch explicitly, if any.
%autopatch -p1 -m4
%endif

%build
./autogen.sh
build_timestamp=$(date -u +%{Y}-%{m}-%{dT}%{H}:%{M}+0000 -r %{SOURCE99})
languages="cl cpp"

%if %{with python3}
languages="${languages} python"
%endif

%if %{with qt}
languages="cpp qt"
%endif

%if %{with qt6}
languages="cpp qt6"
%if 0%{?suse_version} < 1550
# Qt6 needs full c++-17 support
export CXX=g++-12 CC=gcc-12 CPP=cpp-12
%endif
%endif

%define _configure ../configure
mkdir build
pushd build
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-fd-passing \
	--enable-languages="${languages}" \
	--enable-build-timestamp="${build_timestamp}"
%make_build
popd

%install
pushd build
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
chmod -x %{buildroot}%{_libdir}/cmake/Gpgmepp/*.cmake

%if %{with qt} || %{with qt6}
rm -r %{buildroot}%{_bindir}
rm -r %{buildroot}%{_datadir}/aclocal/gpgme*
rm -r %{buildroot}%{_includedir}/gpgme*
rm -r %{buildroot}%{_infodir}/gpgme*
rm -r %{buildroot}%{_libdir}/cmake/Gpgmepp
rm -r %{buildroot}%{_libdir}/libgpgme*
rm -r %{buildroot}%{_libdir}/pkgconfig/gpgme*
rm -r %{buildroot}%{_mandir}/man1/gpgme-json.*
%endif
popd

%if %{with python3}
# Move the gpg directory out of the newly added egg upstream directory
%if 0%{?suse_version} > 1500
%python_expand mv %{buildroot}%{$python_sitearch}/gpg-%{version}*.egg/gpg %{buildroot}%{$python_sitearch}/gpg
%python_expand rm -rf %{buildroot}%{$python_sitearch}/gpg-%{version}*.egg
%endif
%endif

%check
GPGME_DEBUG=2:mygpgme.log %make_build check skip=%{?qt_skip:%{qt_skip}} || cat $(find -name mygpgme.log -type f)

%if %{with qt}
%ldconfig_scriptlets -n libqgpgme15
%endif

%if %{with qt6}
%ldconfig_scriptlets -n libqgpgmeqt6-15
%endif

%if %{without qt} && %{without qt6}
%ldconfig_scriptlets -n libgpgme11
%ldconfig_scriptlets -n libgpgmepp6
%endif

%if %{without qt} && %{without qt6}
%files
%license COPYING COPYING.LESSER LICENSES
%doc AUTHORS ChangeLog ChangeLog-2011 README NEWS THANKS TODO VERSION
%{_bindir}/gpgme-tool
%{_bindir}/gpgme-json
%{_datadir}/common-lisp
%{_datadir}/common-lisp/source
%{_infodir}/gpgme*
%{_mandir}/man1/gpgme-json.*

%files -n libgpgme11
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libgpgme.so.*

%files -n libgpgme-devel
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libgpgme.so
%{_bindir}/gpgme-config
%{_datadir}/aclocal/gpgme.m4
%{_includedir}/gpgme.h
%{_libdir}/pkgconfig/gpgme.pc
%{_libdir}/pkgconfig/gpgme-glib.pc

%files -n libgpgmepp6
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libgpgmepp.so.*

%files -n libgpgmepp-devel
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libgpgmepp.so
%{_includedir}/gpgme++
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Gpgmepp
%{_libdir}/cmake/Gpgmepp/GpgmeppConfig*.cmake
%{_libdir}/pkgconfig/gpgmepp.pc
%endif

%if %{with python3}
%files %{python_files gpg}
%license COPYING COPYING.LESSER LICENSES
%{python_sitearch}/gpg
%if 0%{?suse_version} <= 1500
%{python_sitearch}/gpg-%{version}*.egg-info
%endif
%endif

%if %{with qt}
%files -n libqgpgme15
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libqgpgme.so.*

%files -n libqgpgme-devel
%license COPYING COPYING.LESSER LICENSES
%{_includedir}/qgpgme-qt5/
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/QGpgme
%{_libdir}/cmake/QGpgme/*.cmake
%{_libdir}/libqgpgme.so
%endif

%if %{with qt6}
%files -n libqgpgmeqt6-15
%license COPYING COPYING.LESSER LICENSES
%{_libdir}/libqgpgmeqt6.so.*

%files -n libqgpgmeqt6-devel
%license COPYING COPYING.LESSER LICENSES
%{_includedir}/qgpgme-qt6/
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/QGpgmeQt6
%{_libdir}/cmake/QGpgmeQt6/*.cmake
%{_libdir}/libqgpgmeqt6.so
%endif

%changelog
