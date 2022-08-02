#
# spec file for package mxml
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


%define library_name libmxml1

Name:           mxml
Version:        3.3.1
Release:        0
Summary:        Small XML Parsing Library
# The Mini-XML library is licensed under the Apache License Version 2.0 with an
# exception to allow linking against GPL2/LGPL2-only software.
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.msweet.org/mxml
Source:         https://github.com/michaelrsweet/mxml/releases/download/v%{version}/mxml-%{version}.tar.gz
Source1:        https://github.com/michaelrsweet/mxml/releases/download/v%{version}/mxml-%{version}.tar.gz.sig
# key from https://www.msweet.org/pgp.html
Source2:        mxml.keyring
Source10:       baselibs.conf
BuildRequires:  pkgconfig

%description
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
nonstandard libraries.

This package holds the commandline tools for mxml.

%package -n %{library_name}
Summary:        Shared library for mxml
Group:          System/Libraries

%description -n %{library_name}
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
nonstandard libraries.

This package holds the shared library for mxml.

%package devel
Summary:        Development files for mxml
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}
Suggests:       mxml-doc = %{version}

%description devel
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
nonstandard libraries.

This package holds the development files for mxml.

%package doc
Summary:        Documentation for mxml
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
nonstandard libraries.

This package holds the HTML documentation for mxml.

%prep
%setup -q

%build
%configure --enable-threads --enable-shared --with-docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install DSTROOT=%{buildroot}
rm -v %{buildroot}%{_libdir}/libmxml.a

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%{_libdir}/libmxml.so.1*

%files devel
%{_includedir}/mxml.h
%{_libdir}/libmxml.so
%{_libdir}/pkgconfig/mxml.pc
%{_mandir}/man3/mxml.3%{?ext_man}

%files doc
%{_docdir}/%{name}

%changelog
