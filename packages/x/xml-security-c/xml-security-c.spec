#
# spec file for package xml-security-c
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


%define libvers 30
Name:           xml-security-c
Version:        3.0.0
Release:        0
Summary:        Apache XML security C++ library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://shibboleth.net
Source0:        https://shibboleth.net/downloads/xml-security-c/3.0.0/%{name}-%{version}.tar.bz2
Source1:        https://shibboleth.net/downloads/xml-security-c/3.0.0/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  libxalan-c-devel >= 1.11
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
Requires:       libxalan-c-devel >= 1.11
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
%autopatch -p1

%build
%configure \
  --disable-static
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/libxml-security-c.la

%post -n libxml-security-c%{libvers} -p /sbin/ldconfig
%postun -n libxml-security-c%{libvers} -p /sbin/ldconfig

%files -n xml-security-c-bin
%license LICENSE.txt
%{_bindir}/*

%files -n libxml-security-c%{libvers}
%license LICENSE.txt
%{_libdir}/*.so.*

%files -n libxml-security-c-devel
%license LICENSE.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/xml-security-c.pc

%changelog
