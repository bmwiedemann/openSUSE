#
# spec file for package gpgme
#
# Copyright (c) 2021 SUSE LLC
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
%define psuffix %{nil}
%bcond_without python2
%bcond_without python3
%bcond_with qt
%else
%define psuffix qt
%bcond_with python2
%bcond_with python3
%bcond_without qt
%endif
%{!?python_module:%define python_module() python-%{**} python3-{**}}
Name:           gpgme%{psuffix}
Version:        1.15.1
Release:        0
Summary:        Programmatic library interface to GnuPG
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://www.gnupg.org/related_software/gpgme/
Source:         ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source2:        baselibs.conf
# https://www.gnupg.org/signature_key.html
Source3:        gpgme.keyring
# used to have a fixed timestamp
Source99:       gpgme.changes
BuildRequires:  gcc-c++
BuildRequires:  gpg2 >= 2.0.10
BuildRequires:  libassuan-devel >= 2.4.2
BuildRequires:  libgpg-error-devel >= 1.36
BuildRequires:  pkgconfig
BuildRequires:  swig
%if %{with python2} || %{with python3}
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
%endif
%if %{with qt}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
%endif
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
%define python_sitearch %python3_sitearch
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
%package -n python2-gpg
Summary:        Python 2 bindings for GPGME, a library for accessing GnuPG
Group:          Development/Languages/Python
Provides:       python-gpg = %{version}-%{release}
Obsoletes:      python-gpg < %{version}-%{release}

%description -n python2-gpg
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the bindings to use the library from Python 2 applications.

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

%package -n libqgpgme7
Summary:        Programmatic Qt library interface to GnuPG
Group:          System/Libraries
Requires:       gpg2

%description -n libqgpgme7
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the Qt bindings.

%package -n libqgpgme-devel
Summary:        Development files for libqgpgme, a Qt library for accessing GnuPG
Group:          Development/Libraries/C and C++
Requires:       libgpgme-devel = %{version}
Requires:       libgpgmepp-devel = %{version}
Requires:       libqgpgme7 = %{version}

%description -n libqgpgme-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level crypto API for
encryption, decryption, signing, signature verification, and key
management.

This package contains the bindings to use the library in Qt C++ applications.

%prep
%setup -q -n gpgme-%{version}

%ifarch %{ix86}
sed -i -e '/t-callbacks.py/d' lang/python/tests/Makefile.{am,in}
%endif

%build
build_timestamp=$(date -u +%{Y}-%{m}-%{dT}%{H}:%{M}+0000 -r %{SOURCE99})
languages="cl cpp"

%if %{with python2} || %{with python3}
languages="${languages} python"
%endif

%if %{with qt}
languages="cpp qt"
%endif

%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-fd-passing \
	--enable-languages="${languages}" \
	--enable-build-timestamp="${build_timestamp}"
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
chmod -x %{buildroot}%{_libdir}/cmake/Gpgmepp/*.cmake

%if %{with qt}
rm -r %{buildroot}%{_bindir}
rm -r %{buildroot}%{_datadir}/aclocal/gpgme*
rm -r %{buildroot}%{_includedir}/gpgme*
rm -r %{buildroot}%{_infodir}/gpgme*
rm -r %{buildroot}%{_libdir}/cmake/Gpgmepp
rm -r %{buildroot}%{_libdir}/libgpgme*
rm -r %{buildroot}%{_libdir}/pkgconfig/gpgme*
%endif

%check
%if ! 0%{?qemu_user_space_build}
%make_build check
%endif

%if %{with qt}
%post -n libqgpgme7 -p /sbin/ldconfig
%postun -n libqgpgme7 -p /sbin/ldconfig
%endif

%if !%{with qt}
%post -n libgpgme11 -p /sbin/ldconfig
%postun -n libgpgme11 -p /sbin/ldconfig
%post -n libgpgmepp6 -p /sbin/ldconfig
%postun -n libgpgmepp6 -p /sbin/ldconfig
%endif

%if !%{with qt}
%files
%license COPYING COPYING.LESSER
%doc AUTHORS ChangeLog ChangeLog-2011 README NEWS THANKS TODO VERSION
%{_bindir}/gpgme-tool
%{_bindir}/gpgme-json
%{_datadir}/common-lisp
%{_datadir}/common-lisp/source
%{_infodir}/gpgme*

%files -n libgpgme11
%{_libdir}/libgpgme.so.*

%files -n libgpgme-devel
%{_libdir}/libgpgme.so
%{_bindir}/gpgme-config
%{_datadir}/aclocal/gpgme.m4
%{_includedir}/gpgme.h
%{_libdir}/pkgconfig/gpgme.pc
%{_libdir}/pkgconfig/gpgme-glib.pc

%files -n libgpgmepp6
%{_libdir}/libgpgmepp.so.*

%files -n libgpgmepp-devel
%{_libdir}/libgpgmepp.so
%{_includedir}/gpgme++
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Gpgmepp
%{_libdir}/cmake/Gpgmepp/GpgmeppConfig*.cmake
%endif

%if %{with python2} && ! 0%{?python_subpackage_only}
%files -n python2-gpg
%{python_sitearch}/gpg*
%endif

%if %{with python3} || ( 0%{?python_subpackage_only} && %{with python2} )
%files %{python_files gpg}
%{python_sitearch}/gpg*
%endif

%if %{with qt}
%files -n libqgpgme7
%{_libdir}/libqgpgme.so.*

%files -n libqgpgme-devel
%{_includedir}/qgpgme/
%{_includedir}/QGpgME/
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/QGpgme
%{_libdir}/cmake/QGpgme/*.cmake
%{_libdir}/libqgpgme.so
%endif

%changelog
