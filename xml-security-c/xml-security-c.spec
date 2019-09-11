#
# spec file for package xml-security-c
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libvers 20
Name:           xml-security-c
Version:        2.0.2
Release:        0
Summary:        Apache XML security C++ library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://santuario.apache.org/
Source0:        http://www.apache.org/dist/santuario/c-library/%{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/dist/santuario/c-library/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - 'bool' can't be converted to pointer in c++11
BuildRequires:  gcc-c++
BuildRequires:  libxalan-c-devel
BuildRequires:  libxerces-c-devel >= 3.2
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache XML project's
Xerces-C XML Parser and Xalan-C XSLT processor. The latter is used for processing
XPath and XSLT transforms.

%package -n xml-security-c-bin
Summary:        Utilities for XML security C++ library
Group:          Development/Libraries/C and C++

%description -n xml-security-c-bin
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache XML project's
Xerces-C XML Parser and Xalan-C XSLT processor. The latter is used for processing
XPath and XSLT transforms.

This package contains the utility programs.

%package -n libxml-security-c%{libvers}
Summary:        Apache XML security C++ library
Group:          Development/Libraries/C and C++
Provides:       xml-security-c = %{version}-%{release}
Obsoletes:      xml-security-c < %{version}-%{release}

%description -n libxml-security-c%{libvers}
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache XML project's
Xerces-C XML Parser and Xalan-C XSLT processor. The latter is used for processing
XPath and XSLT transforms.

This package contains just the shared library.

%package -n libxml-security-c-devel
Summary:        Development files for the Apache C++ XML security library
Group:          Development/Libraries/C and C++
Requires:       libxerces-c-devel
Requires:       libxml-security-c%{libvers} = %{version}-%{release}
Requires:       openssl-devel
Provides:       xml-security-c-devel = %{version}-%{release}
Obsoletes:      xml-security-c-devel < %{version}-%{release}

%description -n libxml-security-c-devel
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache XML project's
Xerces-C XML Parser and Xalan-C XSLT processor. The latter is used for processing
XPath and XSLT transforms.

This package includes files needed for development with xml-security-c.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/libxml-security-c.la

%post -n libxml-security-c%{libvers} -p /sbin/ldconfig
%postun -n libxml-security-c%{libvers} -p /sbin/ldconfig

%files -n xml-security-c-bin
%license LICENSE.txt
%doc CHANGELOG.txt
%{_bindir}/*

%files -n libxml-security-c%{libvers}
%license LICENSE.txt
%doc CHANGELOG.txt
%{_libdir}/*.so.*

%files -n libxml-security-c-devel
%license LICENSE.txt
%doc CHANGELOG.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/xml-security-c.pc

%changelog
