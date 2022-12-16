#
# spec file for package gnutls
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


%define gnutls_sover 30
%define gnutlsxx_sover 30
%define gnutls_dane_sover 0
# unbound isn't in SLE (bsc#1086428)
%if 0%{?is_opensuse}
%bcond_without dane
%else
%bcond_with dane
%endif
# Enable Linux kernel AF_ALG based acceleration
%if 0%{?suse_version} >= 1550
# disable for now, as our OBS builds do not work with it. Marcus 20220511
#bcond_without kcapi
%bcond_with kcapi
%else
%bcond_with kcapi
%endif
%bcond_with tpm
%bcond_without guile
Name:           gnutls
Version:        3.7.8
Release:        0
Summary:        The GNU Transport Layer Security Library
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://www.gnutls.org/
Source0:        https://www.gnupg.org/ftp/gcrypt/gnutls/v3.7/%{name}-%{version}.tar.xz
Source1:        https://www.gnupg.org/ftp/gcrypt/gnutls/v3.7/%{name}-%{version}.tar.xz.sig
# https://gnutls.org/gnutls-release-keyring.gpg
Source2:        gnutls.keyring
Source3:        baselibs.conf
# Suppress a false positive on the .hmac file
Source4:        gnutls.rpmlintrc
Patch0:         gnutls-3.5.11-skip-trust-store-tests.patch
Patch1:         gnutls-FIPS-TLS_KDF_selftest.patch
Patch2:         gnutls-FIPS-disable-failing-tests.patch
Patch3:         gnutls_ECDSA_signing.patch
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%ifnarch s390 s390x
#PATCH-FIX-SUSE bsc#1202146 FIPS: Port gnutls to use jitterentropy
Patch4:         gnutls-FIPS-jitterentropy.patch
#PATCH-FIX-SUSE bsc#1202146 FIPS: Set error state when jent init failed in FIPS mode
Patch5:         gnutls-FIPS-Set-error-state-when-jent-init-failed.patch
%endif
%endif
#PATCH-FIX-SUSE bsc#1190698 FIPS: SLI gnutls_pbkdf2: verify keylengths and allow SHA only
Patch6:         gnutls-FIPS-SLI-pbkdf2-verify-keylengths-only-SHA.patch
#PATCH-FIX-UPSTREAM bsc#1203779 Make XTS key check failure not fatal
Patch7:         gnutls-Make-XTS-key-check-failure-not-fatal.patch
Patch8:         gnutls-disable-flaky-test-dtls-resume.patch
#PATCH-FIX-OPENSUSE bsc#1199881 Verify only the libgnutls library HMAC
Patch9:         gnutls-verify-library-HMAC.patch
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  datefudge
BuildRequires:  fdupes
BuildRequires:  fipscheck
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
# The test suite calls /usr/bin/ss from iproute2. It's our own duty to ensure we have it present
BuildRequires:  iproute2
BuildRequires:  libidn2-devel
BuildRequires:  libnettle-devel >= 3.6
BuildRequires:  libtasn1-devel >= 4.9
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  makeinfo
BuildRequires:  p11-kit-devel >= 0.23.1
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(autoopts)
BuildRequires:  pkgconfig(zlib)
%if %{with kcapi}
BuildRequires:  pkgconfig(libkcapi)
%endif
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
BuildRequires:  guile-devel > 1.8
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  crypto-policies
Requires:       crypto-policies
BuildRequires:  jitterentropy-devel >= 3.4.0
Requires:       libjitterentropy3 >= 3.4.0
%endif

%description
The GnuTLS library provides a secure layer over a reliable transport
layer. Currently the GnuTLS library implements the proposed standards
of the IETF's TLS working group.

%package -n libgnutls%{gnutls_sover}
Summary:        The GNU Transport Layer Security Library
# install libgnutls and libgnutls-hmac close together (bsc#1090765)
License:        LGPL-2.1-or-later
Group:          System/Libraries
Suggests:       libgnutls%{gnutls_sover}-hmac = %{version}-%{release}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif

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

%if %{with dane}
%package -n libgnutls-dane%{gnutls_dane_sover}
Summary:        DANE support for the GNU Transport Layer Security Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgnutls-dane%{gnutls_dane_sover}
The GnuTLS project aims to develop a library that provides a secure
layer over a reliable transport layer.
This package contains the "DANE" part of gnutls.
%endif

%package -n libgnutlsxx%{gnutlsxx_sover}
Summary:        C++ API for the GNU Transport Layer Security Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif

%description -n libgnutlsxx%{gnutlsxx_sover}
The GnuTLS library provides a secure layer over a reliable transport
layer. Currently the GnuTLS library implements the proposed standards
of the IETF's TLS working group.

%package -n libgnutls-devel
Summary:        Development package for the GnuTLS C API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       gnutls = %{version}
Requires:       libgnutls%{gnutls_sover} = %{version}
Provides:       gnutls-devel = %{version}-%{release}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif

%description -n libgnutls-devel
Files needed for software development using gnutls.

%if %{with dane}
%package -n libgnutls-dane-devel
Summary:        Development package for GnuTLS DANE component
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libgnutls-dane%{gnutls_dane_sover} = %{version}

%description -n libgnutls-dane-devel
Files needed for software development using gnutls.
%endif

%package -n libgnutlsxx-devel
Summary:        Development package for the GnuTLS C++ API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libgnutls-devel = %{version}
Requires:       libgnutlsxx%{gnutlsxx_sover} = %{version}
Requires:       libstdc++-devel

%description -n libgnutlsxx-devel
Files needed for software development using gnutls.

%if %{with guile}
%package guile
Summary:        Guile wrappers for gnutls
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       guile > 1.8

%description guile
GnuTLS Wrappers for GNU Guile, a dialect of Scheme.
%endif

%prep
%autosetup -p1

echo "SYSTEM=NORMAL" >> tests/system.prio

%build
export LDFLAGS="-pie -Wl,-z,now -Wl,-z,relro"
export CFLAGS="%{optflags} -fPIE"
export CXXFLAGS="%{optflags} -fPIE"
autoreconf -fiv

# Rename the internal .hmac file to include the so library version
sed -i "s/\.gnutls\.hmac/\.libgnutls\.so\.%{gnutls_sover}\.hmac/g" lib/Makefile.am lib/Makefile.in lib/fips.c

%configure \
        gl_cv_func_printf_directive_n=yes \
        gl_cv_func_printf_infinite_long_double=yes \
        --disable-static \
        --disable-rpath \
        --disable-gcc-warnings \
        --disable-silent-rules \
        %{?with_kcapi:--enable-afalg} \
        --with-default-trust-store-dir=%{_localstatedir}/lib/ca-certificates/pem \
        --with-system-priority-file=%{_sysconfdir}/crypto-policies/back-ends/gnutls.config \
        --with-default-priority-string="@SYSTEM" \
        --with-sysroot=/%{?_sysroot} \
%if %{without tpm}
        --without-tpm \
%endif
%if %{with dane}
        --with-unbound-root-key-file=%{_localstatedir}/lib/unbound/root.key \
%else
        --disable-libdane \
%endif
%if %{with guile}
        --enable-guile \
        --with-guile-extension-dir=%{_libdir}/guile/3.0 \
%else
        --disable-guile \
%endif
        --enable-fips140-mode \
        --with-fips140-module-name="GnuTLS version" \
        --with-fips140-module-version="%{version}-%{release}" \
        %{nil}
%make_build

%install
%make_install

# Compute the FIPS hmac using the brp-50-generate-fips-hmac script
# export BRP_FIPSHMAC_FILES=%%{buildroot}%%{_libdir}/libgnutls.so.%%{gnutls_sover}

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
# note: The FIPS hmac is now calculated with an internal tool since
#   commit a86c8e87189e23920ae622da5e572cb4e1a6e0ed
%{expand:%%global __os_install_post {%__os_install_post
./lib/fipshmac "%{buildroot}%{_libdir}/libgnutls.so.%{gnutls_sover}" > %{buildroot}%{_libdir}/.libgnutls.so.%{gnutls_sover}.hmac
sed -i "s^%{buildroot}/usr^^" %{buildroot}%{_libdir}/.libgnutls.so.%{gnutls_sover}.hmac
}}

rm -rf %{buildroot}%{_datadir}/locale/en@{,bold}quot
# Do not package static libs and libtool files
find %{buildroot} -type f -name "*.la" -delete -print

# install docs
mkdir -p %{buildroot}%{_docdir}/libgnutls-devel/
cp doc/gnutls.html doc/*.png %{buildroot}%{_docdir}/libgnutls-devel/
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
%make_build check GNUTLS_SYSTEM_PRIORITY_FILE=/dev/null || {
    find -name test-suite.log -print -exec cat {} +
    exit 1
}
#Run the regression tests also in FIPS mode
GNUTLS_FORCE_FIPS_MODE=1 make check %{?_smp_mflags} GNUTLS_SYSTEM_PRIORITY_FILE=/dev/null || {
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
%license LICENSE
%{_libdir}/libgnutls.so.%{gnutls_sover}*

%files -n libgnutls%{gnutls_sover}-hmac
%license LICENSE
%{_libdir}/.libgnutls.so.%{gnutls_sover}*.hmac

%if %{with dane}
%files -n libgnutls-dane%{gnutls_dane_sover}
%license LICENSE
%{_libdir}/libgnutls-dane.so.%{gnutls_dane_sover}*
%endif

%files -n libgnutlsxx%{gnutlsxx_sover}
%license LICENSE
%{_libdir}/libgnutlsxx.so.%{gnutlsxx_sover}*

%files -n libgnutls-devel
%license LICENSE
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
%license LICENSE
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/dane.h
%{_libdir}/pkgconfig/gnutls-dane.pc
%{_libdir}/libgnutls-dane.so
%endif

%files -n libgnutlsxx-devel
%license LICENSE
%{_libdir}/libgnutlsxx.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/gnutlsxx.h

%if %{with guile}
%files guile
%license LICENSE
%{_libdir}/guile/*
%{_datadir}/guile/site/*
%endif

%changelog
