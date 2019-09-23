#
# spec file for package mxml
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


Name:           mxml
Version:        2.11
Release:        0
Summary:        Small XML Parsing Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.msweet.org/mxml
Source:         https://github.com/michaelrsweet/mxml/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig

%description
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
nonstandard libraries.

This package holds the commandline tools for mxml.

%define library_name libmxml1

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
%configure --enable-shared --with-docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install DSTROOT=%{buildroot}
rm -v %{buildroot}%{_libdir}/libmxml.a

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files
%{_bindir}/mxmldoc
%{_mandir}/man1/mxmldoc.1%{?ext_man}

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
