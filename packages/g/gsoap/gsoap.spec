#
# spec file for package gsoap
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


Name:           gsoap
%define lname	libgsoap-2_8_124
Version:        2.8.124
Release:        0
Summary:        Toolkit for SOAP/REST-based C/C++ server and client web service applications
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Development/Libraries/C and C++
URL:            http://www.genivia.com/dev.html

Source:         gsoap-%version.tar.xz
Source2:        sanitize_source.sh
Patch2:         gsoap-01-sharedlibs.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)

%description
gSOAP is a toolkit for C and C++ server and client Web service
applications, and is responsible for e.g. HTTP request handling and
the serialization of XML. It supports SOAP 1.1/1.2 RPC encoding and
document/literal styles, WSDL 1.1, MTOM/MIME/DIME attachments
(streaming), SOAP-over-UDP, request-response and one-way messaging.
It also supports WS-Addressing and WS-Security.

%package devel
Summary:        Development files for the gSOAP toolkit
Group:          Development/Libraries/C and C++
Obsoletes:      libgsoap-devel < %version-%release
Provides:       libgsoap-devel = %version-%release

%description devel
This package contains the runtime development programs, include
headers and development library symlinks for libgsoap.

%package -n %lname
Summary:        Runtime libraries for gSOAP
Group:          Development/Libraries/C and C++

%description -n %lname
gSOAP is a toolkit for C and C++ server and client Web service
applications, and is responsible for e.g. HTTP request handling and
the serialization of XML.

%package doc
Summary:        Runtime and development documentation for gsoap
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This subpackage contains the documentation for the gSOAP toolkit.

%prep
%setup -q
cmp gsoap/stdsoap2.cpp gsoap/stdsoap2.c
%patch -P 2 -p1
ln -fs stdsoap2.cpp gsoap/stdsoap2.c

%build
# GSOAP changes its ABI between 2.8.22 and 2.8.28 without updating the SONAMEs.
# Therefore, the full version must be present in the SONAME (and we can trigger
# this by updating the AC_INIT field in this instance).
#
perl -i -lpe 's{AC_INIT\(\[gsoap\], 2.8\)}{AC_INIT([gsoap], [%version])}' \
	configure.ac
# Rebuild configure - fix that utterly long mktime test.
# Also needed because Makefile.am and configure.ac are touched.
#
autoreconf -fi
%configure --enable-ipv6 --disable-static CFLAGS="%optflags -fcommon"
pushd gsoap/src/
# build prerequisites for parallel build first
make soapcpp2_yacc.c
popd
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
rm -f "$b/%_libdir"/*.la
mkdir -p "$b/%_defaultdocdir"
cp -a gsoap/doc "$b/%_defaultdocdir/%name"
find "$b" -type f -name "*inconsolata*" -exec chmod a-x "{}" "+"
%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files devel
%_bindir/*soap*
%_bindir/*wsdl*
%_datadir/%name/
%_includedir/*soap*
%_libdir/libgsoap.so
%_libdir/libgsoapck.so
%_libdir/libgsoapssl.so
%_libdir/libgsoap++.so
%_libdir/libgsoapck++.so
%_libdir/libgsoapssl++.so
%_libdir/pkgconfig/*gsoap*.pc

%files -n %lname
%_libdir/libgsoap*-%version.so

%files doc
%_defaultdocdir/%name/

%changelog
