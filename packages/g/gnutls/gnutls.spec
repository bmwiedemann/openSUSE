#
# spec file for package gnutls
#
# Copyright (c) 2020 SUSE LLC
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


%define gnutls_sover 30
%define gnutlsxx_sover 28
%define gnutls_dane_sover 0
# unbound isn't in SLE (bsc#1086428)
%if 0%{?is_opensuse}
%bcond_without dane
%else
%bcond_with dane
%endif
%bcond_with tpm
%bcond_without guile
Name:           gnutls
Version:        3.6.15
Release:        0
Summary:        The GNU Transport Layer Security Library
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.gnutls.org/
Source0:        ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch1:         gnutls-3.5.11-skip-trust-store-tests.patch
Patch4:         gnutls-3.6.6-set_guile_site_dir.patch
Patch6:         gnutls-temporarily_disable_broken_guile_reauth_test.patch
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  datefudge
BuildRequires:  fdupes
BuildRequires:  fipscheck
BuildRequires:  gcc-c++
# The test suite calls /usr/bin/ss from iproute2. It's our own duty to ensure we have it present
BuildRequires:  iproute2
BuildRequires:  libidn2-devel
BuildRequires:  libnettle-devel >= 3.4.1
BuildRequires:  libtasn1-devel >= 4.9
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  makeinfo
BuildRequires:  p11-kit-devel >= 0.23.1
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(autoopts)
%if 0%{?suse_version} <= 1320
BuildRequires:  net-tools
%else
BuildRequires:  net-tools-deprecated
%endif
%if %{with tpm}
BuildRequires:  trousers-devel
%endif
%if %{with dane}
Requires:       libgnutls-dane%{gnutls_dane_sover} = %{version}
%if 0%{?suse_version} <= 1320
BuildRequires:  unbound-devel
%else
BuildRequires:  libunbound-devel
%endif
%endif
%if %{with guile}
BuildRequires:  guile-devel
%endif

%description
The GnuTLS library provides a secure layer over a reliable transport
layer. Currently the GnuTLS library implements the proposed standards
of the IETF's TLS working group.

%package -n libgnutls%{gnutls_sover}
Summary:        The GNU Transport Layer Security Library
# install libopenssl and libopenssl-hmac close together (bsc#1090765)
License:        LGPL-2.1-or-later
Group:          System/Libraries
Suggests:       libgnutls%{gnutls_sover}-hmac = %{version}-%{release}

%description -n libgnutls%{gnutls_sover}
The GnuTLS library provides a secure layer over a reliable transport
layer. Currently the GnuTLS library implements the proposed standards
of the IETF's TLS working group.

%package -n libgnutls%{gnutls_sover}-hmac
Summary:        Checksums of the GNU Transport Layer Security Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       libgnutls%{gnutls_sover} = %{version}-%{release}

%description -n libgnutls%{gnutls_sover}-hmac
FIPS SHA256 checksums of the libgnutls library.

%package -n libgnutls-dane%{gnutls_dane_sover}
Summary:        DANE support for the GNU Transport Layer Security Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgnutls-dane%{gnutls_dane_sover}
The GnuTLS project aims to develop a library that provides a secure
layer over a reliable transport layer.
This package contains the "DANE" part of gnutls.

%package -n libgnutlsxx%{gnutlsxx_sover}
Summary:        C++ API for the GNU Transport Layer Security Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgnutlsxx%{gnutlsxx_sover}
The GnuTLS library provides a secure layer over a reliable transport
layer. Currently the GnuTLS library implements the proposed standards
of the IETF's TLS working group.

%package -n libgnutls-devel
Summary:        Development package for the GnuTLS C API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgnutls%{gnutls_sover} = %{version}
Requires(pre):  %{install_info_prereq}
Provides:       gnutls-devel = %{version}-%{release}

%description -n libgnutls-devel
Files needed for software development using gnutls.

%package -n libgnutls-dane-devel
Summary:        Development package for GnuTLS DANE component
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libgnutls-dane%{gnutls_dane_sover} = %{version}

%description -n libgnutls-dane-devel
Files needed for software development using gnutls.

%package -n libgnutlsxx-devel
Summary:        Development package for the GnuTLS C++ API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libgnutls-devel = %{version}
Requires:       libgnutlsxx%{gnutlsxx_sover} = %{version}
Requires:       libstdc++-devel
Requires(pre):  %{install_info_prereq}

%description -n libgnutlsxx-devel
Files needed for software development using gnutls.

%package guile
Summary:        Guile wrappers for gnutls
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       guile

%description guile
GnuTLS Wrappers for GNU Guile, a dialect of Scheme.

%prep
%autosetup -p1

%build
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE"
export CXXFLAGS="%{optflags} -fPIE"
#autoreconf -fiv
%configure \
        gl_cv_func_printf_directive_n=yes \
        gl_cv_func_printf_infinite_long_double=yes \
        --disable-static \
        --disable-rpath \
        --disable-silent-rules \
	--with-default-trust-store-dir=%{_localstatedir}/lib/ca-certificates/pem \
        --with-sysroot=/%{?_sysroot} \
%if %{without tpm}
        --without-tpm \
%endif
%if %{with dane}
        --with-unbound-root-key-file=%{_localstatedir}/lib/unbound/root.key \
%else
        --disable-libdane \
%endif
        --enable-fips140-mode \
	%{nil}
make %{?_smp_mflags}

# the hmac hashes:
#
# this is a hack that re-defines the __os_install_post macro
# for a simple reason: the macro strips the binaries and thereby
# invalidates a HMAC that may have been created earlier.
# solution: create the hashes _after_ the macro runs.
#
# this shows up earlier because otherwise the %%expand of
# the macro is too late.
# remark: This is the same as running
#   openssl dgst -sha256 -hmac 'orboDeJITITejsirpADONivirpUkvarP'
%{expand:%%global __os_install_post {%__os_install_post
%{_bindir}/fipshmac %{buildroot}%{_libdir}/libgnutls.so.%{gnutls_sover}
}}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/locale/en@{,bold}quot
# Do not package static libs and libtool files
find %{buildroot} -type f -name "*.la" -delete -print

# install docs
mkdir -p %{buildroot}%{_docdir}/libgnutls-devel/
cp doc/gnutls.html doc/*.png %{buildroot}%{_docdir}/libgnutls-devel/
mkdir -p %{buildroot}%{_docdir}/libgnutls-devel/reference
cp doc/reference/html/* %{buildroot}%{_docdir}/libgnutls-devel/reference/
mkdir -p %{buildroot}%{_docdir}/libgnutls-devel/examples
cp doc/examples/*.{c,h} %{buildroot}%{_docdir}/libgnutls-devel/examples/

# PNG files are replaced with the compressed files and that breaks
# deduplication, this is workaround
find %{buildroot}%{_datadir} -name '*.png' -exec gzip -n -9 {} +
rm -rf %{buildroot}%{_datadir}/doc/gnutls
%fdupes -s %{buildroot}%{_datadir}

%find_lang libgnutls --all-name

%check
%if ! 0%{?qemu_user_space_build}
make %{?_smp_mflags} check || {
    find -name test-suite.log -print -exec cat {} +
    exit 1
}
%endif

%post -n libgnutls%{gnutls_sover} -p /sbin/ldconfig
%postun -n libgnutls%{gnutls_sover} -p /sbin/ldconfig

%if %{with dane}
%post -n libgnutls-dane%{gnutls_dane_sover} -p /sbin/ldconfig
%postun -n libgnutls-dane%{gnutls_dane_sover} -p /sbin/ldconfig
%endif

%post -n libgnutlsxx%{gnutlsxx_sover} -p /sbin/ldconfig
%postun -n libgnutlsxx%{gnutlsxx_sover} -p /sbin/ldconfig
%post -n libgnutls-devel
%install_info --info-dir=%{_infodir} %{_infodir}/gnutls.info.gz

%preun -n libgnutls-devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnutls.info.gz

%files -f libgnutls.lang
%license LICENSE
%doc THANKS README.md NEWS ChangeLog AUTHORS doc/TODO
%{_bindir}/certtool
%{_bindir}/gnutls-cli
%{_bindir}/gnutls-cli-debug
%{_bindir}/gnutls-serv
%{_bindir}/ocsptool
%{_bindir}/psktool
%{_bindir}/p11tool
%{_bindir}/srptool
%if %{with dane}
%{_bindir}/danetool
%endif
%if %{with tpm}
%{_bindir}/tpmtool
%endif
%{_mandir}/man1/*

%files -n libgnutls%{gnutls_sover}
%{_libdir}/libgnutls.so.%{gnutls_sover}*

%files -n libgnutls%{gnutls_sover}-hmac
%{_libdir}/.libgnutls.so.%{gnutls_sover}*.hmac

%if %{with dane}
%files -n libgnutls-dane%{gnutls_dane_sover}
%{_libdir}/libgnutls-dane.so.%{gnutls_dane_sover}*
%endif

%files -n libgnutlsxx%{gnutlsxx_sover}
%{_libdir}/libgnutlsxx.so.%{gnutlsxx_sover}*

%files -n libgnutls-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/abstract.h
%{_includedir}/%{name}/crypto.h
%{_includedir}/%{name}/compat.h
%{_includedir}/%{name}/dtls.h
%{_includedir}/%{name}/gnutls.h
%{_includedir}/%{name}/openpgp.h
%{_includedir}/%{name}/ocsp.h
%{_includedir}/%{name}/pkcs7.h
%{_includedir}/%{name}/pkcs11.h
%{_includedir}/%{name}/pkcs12.h
%{_includedir}/%{name}/self-test.h
%{_includedir}/%{name}/socket.h
%{_includedir}/%{name}/x509.h
%{_includedir}/%{name}/x509-ext.h
%{_includedir}/%{name}/tpm.h
%{_includedir}/%{name}/system-keys.h
%{_includedir}/%{name}/urls.h
%{_libdir}/libgnutls.so
%{_libdir}/pkgconfig/gnutls.pc
%{_mandir}/man3/*
%{_infodir}/*%{ext_info}
%doc %{_docdir}/libgnutls-devel

%if %{with dane}
%files -n libgnutls-dane-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/dane.h
%{_libdir}/pkgconfig/gnutls-dane.pc
%{_libdir}/libgnutls-dane.so
%endif

%files -n libgnutlsxx-devel
%{_libdir}/libgnutlsxx.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/gnutlsxx.h

%if %{with guile}
%files guile
%{_libdir}/guile/*
%{_datadir}/guile/gnutls*
%endif

%changelog
