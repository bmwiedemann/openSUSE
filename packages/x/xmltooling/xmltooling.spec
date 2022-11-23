#
# spec file for package xmltooling
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


%define libvers 10
%define opensaml_version 3.2.1
%define pkgdocdir %{_docdir}/%{name}
Name:           xmltooling
Version:        3.2.2
Release:        0
Summary:        OpenSAML XML Processing library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://wiki.shibboleth.net/confluence/display/OpenSAML/XMLTooling-C
Source0:        http://shibboleth.net/downloads/c++-opensaml/%{opensaml_version}/%{name}-%{version}.tar.bz2
Source1:        http://shibboleth.net/downloads/c++-opensaml/%{opensaml_version}/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Patch0:         xmltooling-1.5.5-doxygen_timestamp.patch
BuildRequires:  automake
BuildRequires:  curl-devel >= 7.10.6
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  liblog4shib-devel >= 1.0.4
BuildRequires:  libtool
BuildRequires:  libxerces-c-devel >= 3.2
BuildRequires:  libxml-security-c-devel >= 2.0.0
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

%package -n libxmltooling%{libvers}
Summary:        OpenSAML XMLTooling library
Group:          System/Libraries
Provides:       xmltooling = %{version}-%{release}
Obsoletes:      xmltooling < %{version}-%{release}

%description -n libxmltooling%{libvers}
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package contains just the shared library.

%package -n libxmltooling-lite%{libvers}
Summary:        OpenSAML XMLTooling library
Group:          System/Libraries
Provides:       xmltooling = %{version}-%{release}
Obsoletes:      xmltooling < %{version}-%{release}

%description -n libxmltooling-lite%{libvers}
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package contains just the shared library.

%package -n libxmltooling-devel
Summary:        XMLTooling development Headers
Group:          Development/Libraries/C and C++
Requires:       curl-devel >= 7.10.6
Requires:       liblog4shib-devel >= 1.0.4
Requires:       libxerces-c-devel >= 3.2
Requires:       libxml-security-c-devel >= 2.0.0
Requires:       libxmltooling%{libvers} = %{version}-%{release}
Requires:       libxmltooling-lite%{libvers} = %{version}-%{release}
Requires:       openssl-devel
Provides:       xmltooling-devel = %{version}-%{release}
Obsoletes:      xmltooling-devel < %{version}-%{release}
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel >= 1.32.0
%endif

%description -n libxmltooling-devel
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package includes files needed for development with XMLTooling.

%package -n xmltooling-schemas
Summary:        XMLTooling schemas and catalog
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description -n xmltooling-schemas
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package includes XML schemas and related files.

%prep
%setup -q
%autopatch -p1

%build
# The default C++ standard used in GCC-11 is C++17,
# which does not support opensaml codebase.
CXXFLAGS="-std=c++11 %{optflags}"
export CXXFLAGS
autoreconf -fiv
%configure
%make_build

%install
make install DESTDIR=%{buildroot} pkgdocdir=%{pkgdocdir}
# Don't package unit tester if present.
rm -f %{buildroot}/%{_bindir}/xmltoolingtest
rm -f %{buildroot}/%{_libdir}/libxmltooling.la
rm -f %{buildroot}/%{_libdir}/libxmltooling-lite.la

%check
%make_build check

%post -n libxmltooling%{libvers} -p /sbin/ldconfig
%post -n libxmltooling-lite%{libvers} -p /sbin/ldconfig
%postun -n libxmltooling%{libvers} -p /sbin/ldconfig
%postun -n libxmltooling-lite%{libvers} -p /sbin/ldconfig

%files -n libxmltooling%{libvers}
%{_libdir}/libxmltooling.so.*

%files -n libxmltooling-lite%{libvers}
%{_libdir}/libxmltooling-lite.so.*

%files -n xmltooling-schemas
%dir %{_datadir}/xml/xmltooling
%{_datadir}/xml/xmltooling/*

%files -n libxmltooling-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/xmltooling.pc
%{_libdir}/pkgconfig/xmltooling-lite.pc

%doc %{pkgdocdir}

%changelog
