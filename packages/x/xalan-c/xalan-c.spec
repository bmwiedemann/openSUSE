#
# spec file for package xalan-c
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


%define _libname libxalan-c112
Name:           xalan-c
Version:        1.12
Release:        0
Summary:        An XSLT Transformation Engine in C++
License:        Apache-2.0
Group:          Productivity/Publishing/XML
URL:            https://apache.github.io/xalan-c/
Source:         https://downloads.apache.org/xalan/xalan-c/sources/xalan_c-%{version}.tar.gz
BuildRequires:  Xerces-c-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
Provides:       Xalan-C = 1.11
Obsoletes:      Xalan-C < 1.11

%description
Xalan is an XSL processor for transforming XML documents into HTML,
text, or other XML document types. Xalan-C++ represents an almost
complete and robust C++ reference implementation of the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath).

%package -n %{_libname}
Summary:        An XSLT Transformation Engine in C++
Group:          System/Libraries
Provides:       libXalan-c111 = 1.11
Obsoletes:      libXalan-c111 < 1.11

%description -n %{_libname}
Xalan is an XSL processor for transforming XML documents into HTML,
text, or other XML document types. Xalan-C++ represents an almost
complete and robust C++ reference implementation of the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath).

%package -n libxalan-c-devel
Summary:        An XSLT Transformation Engine in C++ - Development Files
Group:          Development/Libraries/C and C++
Requires:       %{_libname} = %{version}
Provides:       Xalan-c-devel = %{version}
Obsoletes:      Xalan-c-devel < %{version}
Provides:       libXalan-c-devel = %{version}
Obsoletes:      libXalan-c-devel < %{version}

%description -n libxalan-c-devel
Xalan is an XSL processor for transforming XML documents into HTML,
text, or other XML document types. Xalan-C++ represents an almost
complete and a robust C++ reference implementation of the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath).

This package contains files needed for development with Xalanc

%prep
%setup -q -n xalan_c-%{version}

%build
%cmake
%cmake_build

%if 0
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
export RPM_OPT_FLAGS
chmod a+x runConfigure
chmod a+x conf*
./runConfigure -p linux -c gcc -x g++ -t default -m inmem -b "%{__isa_bits}" -P %{_prefix} -C --libdir="%{_libdir}"
%make_build
%endif

%install
%cmake_install

%post   -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc KEYS NOTICE
%{_bindir}/Xalan

%files -n %{_libname}
%{_libdir}/libxalan*.so.*

%files -n libxalan-c-devel
%{_includedir}/xalanc/
%{_libdir}/libxalan*.so
%{_libdir}/cmake/XalanC
%{_libdir}/pkgconfig/xalan-c.pc

%changelog
