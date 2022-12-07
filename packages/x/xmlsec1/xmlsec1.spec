#
# spec file for package xmlsec1
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%global libname    libxmlsec1-1
%global libopenssl libxmlsec1-openssl1
%global libgcrypt  libxmlsec1-gcrypt1
%global libgnutls  libxmlsec1-gnutls1
%global libnss     libxmlsec1-nss1
Name:           xmlsec1
Version:        1.2.37
Release:        0
Summary:        Library providing support for "XML Signature" and "XML Encryption" standards
License:        MIT
URL:            https://www.aleksey.com/xmlsec/
Source0:        https://www.aleksey.com/xmlsec/download/xmlsec1-%{version}.tar.gz
Source1:        https://www.aleksey.com/xmlsec/download/xmlsec1-%{version}.sig#/xmlsec1-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source99:       xmlsec1-rpmlintrc
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
# Needed certutil for tests
BuildRequires:  mozilla-nss-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
Recommends:     %{libopenssl}

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package -n %{libname}
Summary:        Library providing support for "XML Signature" and "XML Encryption" standards

%description -n %{libname}
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package -n %{libgcrypt}
Summary:        GCrypt crypto plugin for XML Security Library
Requires:       %{libname} = %{version}

%description -n %{libgcrypt}
GCrypt plugin for XML Security Library provides GCrypt based crypto services
for the xmlsec library.

%package -n %{libgnutls}
Summary:        GNUTls crypto plugin for XML Security Library
Requires:       %{libname} = %{version}

%description -n %{libgnutls}
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library.

%package -n %{libnss}
Summary:        NSS crypto plugin for XML Security Library
Requires:       %{libname} = %{version}

%description -n %{libnss}
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library.

%package -n %{libopenssl}
Summary:        OpenSSL crypto plugin for XML Security Library
Requires:       %{libname} = %{version}

%description -n %{libopenssl}
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package devel
Summary:        Libraries, includes for XML Signatures/Encryption
Requires:       %{libname} = %{version}
Requires:       libxml2-devel >= 2.6.0
Requires:       libxslt-devel >= 1.1.0
Requires:       openssl-devel >= 0.9.6
Requires:       zlib-devel

%description devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package openssl-devel
Summary:        OpenSSL crypto plugin for XML Security Library
Requires:       %{libopenssl} = %{version}
Requires:       %{name}-devel = %{version}

%description openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL

%package gcrypt-devel
Summary:        GCrypt crypto plugin for XML Security Library
Requires:       %{libgcrypt} = %{version}
Requires:       %{name}-devel = %{version}

%description gcrypt-devel
Libraries, includes, etc. for developing XML Security applications with GCrypt.

%package gnutls-devel
Summary:        GNUTls crypto plugin for XML Security Library
Requires:       %{libgnutls} = %{version}
Requires:       %{name}-devel = %{version}
Requires:       %{name}-openssl-devel = %{version}
Requires:       gnutls-devel >= 1.0.20
Requires:       libgcrypt-devel >= 1.2.0

%description gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls.

%package nss-devel
Summary:        NSS crypto plugin for XML Security Library
Requires:       %{libnss} = %{version}
Requires:       %{name}-devel = %{version}
Requires:       mozilla-nspr-devel
Requires:       mozilla-nss-devel >= 3.2

%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS.

%prep
%autosetup -p1

%build
# Allow for deprecations
export CFLAGS="-Wno-error=deprecated-declarations"
export CXXFLAGS="-Wno-error=deprecated-declarations"
%configure \
    --disable-static \
    --disable-silent-rules \
    --enable-werror \
    --disable-md5
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# move installed docs to include them in -devel package via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_datadir}/doc/xmlsec1/* __tmp_doc
rmdir %{buildroot}%{_datadir}/doc/xmlsec1

%check
# Relax the crypto policies for the test-suite
export GNUTLS_SYSTEM_PRIORITY_FILE=/dev/null
%make_build -j1 check check-keys check-dsig check-enc

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n %{libgcrypt} -p /sbin/ldconfig
%postun -n %{libgcrypt} -p /sbin/ldconfig
%post -n %{libgnutls} -p /sbin/ldconfig
%postun -n %{libgnutls} -p /sbin/ldconfig
%post -n %{libnss} -p /sbin/ldconfig
%postun -n %{libnss} -p /sbin/ldconfig
%post -n %{libopenssl} -p /sbin/ldconfig
%postun -n %{libopenssl} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md ChangeLog
%{_mandir}/man1/xmlsec1.1%{?ext_man}
%{_bindir}/xmlsec1

%files -n %{libname}
%license COPYING
%{_libdir}/libxmlsec1.so.*

%files -n %{libgcrypt}
%license COPYING
%{_libdir}/libxmlsec1-gcrypt.so.*
%{_libdir}/libxmlsec1-gcrypt.so

%files -n %{libgnutls}
%license COPYING
%{_libdir}/libxmlsec1-gnutls.so.*
%{_libdir}/libxmlsec1-gnutls.so

%files -n %{libnss}
%license COPYING
%{_libdir}/libxmlsec1-nss.so.*
%{_libdir}/libxmlsec1-nss.so

%files -n %{libopenssl}
%license COPYING
%{_libdir}/libxmlsec1-openssl.so.*
%{_libdir}/libxmlsec1-openssl.so

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS
%doc HACKING __tmp_doc/*
%{_bindir}/xmlsec1-config
%dir %{_includedir}/xmlsec1
%dir %{_includedir}/xmlsec1/xmlsec
%{_includedir}/xmlsec1/xmlsec/*.h
%{_libdir}/libxmlsec1.so
%{_libdir}/pkgconfig/xmlsec1.pc
%{_libdir}/xmlsec1Conf.sh
%{_datadir}/aclocal/xmlsec1.m4
%{_mandir}/man1/xmlsec1-config.1%{?ext_man}

%files openssl-devel
%license COPYING
%{_includedir}/xmlsec1/xmlsec/openssl/
%{_libdir}/pkgconfig/xmlsec1-openssl.pc

%files gcrypt-devel
%license COPYING
%{_includedir}/xmlsec1/xmlsec/gcrypt/
%{_libdir}/pkgconfig/xmlsec1-gcrypt.pc

%files gnutls-devel
%license COPYING
%{_includedir}/xmlsec1/xmlsec/gnutls/
%{_libdir}/pkgconfig/xmlsec1-gnutls.pc

%files nss-devel
%license COPYING
%{_includedir}/xmlsec1/xmlsec/nss/
%{_libdir}/pkgconfig/xmlsec1-nss.pc

%changelog
