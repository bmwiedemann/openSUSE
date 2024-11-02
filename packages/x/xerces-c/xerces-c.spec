#
# spec file for package xerces-c
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


%define libname libxerces-c-3_3
Name:           xerces-c
Version:        3.3.0
Release:        0
Summary:        A Validating XML Parser
License:        Apache-2.0
URL:            https://xerces.apache.org/xerces-c/
Source0:        https://www.apache.org/dist/xerces/c/3/sources/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/dist/xerces/c/3/sources/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libcurl)

%description
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards ( DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).

%package doc
Summary:        Documentation for %{name}

%description doc
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards ( DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).

This package contains just documentation.

%package -n %{libname}
Summary:        Shared libraries for Xerces-c - a validating XML parser
Provides:       Xerces-c = %{version}
Obsoletes:      Xerces-c < %{version}

%description -n %{libname}
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards ( DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).

This package contains shared libraries.

%package -n libxerces-c-devel
Summary:        A validating XML parser - Development Files
Requires:       %{libname} = %{version}
Provides:       Xerces-c-devel = %{version}
Obsoletes:      Xerces-c-devel < %{version}
Provides:       libXerces-c-devel = %{version}
Obsoletes:      libXerces-c-devel < %{version}

%description -n libxerces-c-devel
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents.

This package includes files needed for development with Xerces-c

%prep
%setup -q -n xerces-c-%{version}

%build
%configure \
    --enable-transcoder-gnuiconv \
    --enable-netaccessor-curl \
    --disable-static \
    --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm doc/Makefile*
%fdupes -s doc

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc CREDITS KEYS NOTICE README
%{_bindir}/*

%files doc
%license LICENSE
%doc CREDITS KEYS NOTICE README
%doc doc/*

%files -n %{libname}
%{_libdir}/libxerces-c-*.so

%files -n libxerces-c-devel
%{_includedir}/xercesc
%{_libdir}/libxerces-c.so
%{_libdir}/pkgconfig/xerces-c.pc

%changelog
