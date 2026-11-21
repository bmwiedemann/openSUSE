#
# spec file for package mxml
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         library_name lib%{name}4_2
%define         git_url https://github.com/michaelrsweet/mxml/releases/download
Name:           mxml
Version:        4.0.6
Release:        0
Summary:        Mini-XML - Tiny XML Parsing Library
# The Mini-XML library is licensed under the Apache License Version 2.0 with an
# exception to allow linking against GPL2/LGPL2-only software.
License:        Apache-2.0
URL:            https://www.msweet.org/mxml
Source0:        %{git_url}/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{git_url}/v%{version}/%{name}-%{version}.tar.gz.sig
# Key from https://www.msweet.org/pgp.html
Source2:        mxml.keyring

%description
Mini-XML is a small XML parsing library that you can use to read XML
data files or strings in your application without requiring large
non-standard libraries.

This package holds the commandline tools for mxml.

%package -n %{library_name}
Summary:        Mini-XML - Tiny XML Parsing Library

%description -n %{library_name}
Mini-XML is a small XML parsing library that you can use to read XML
data files or strings in your application without requiring large
non-standard libraries.

This package holds the shared library.

%package devel
Summary:        Development files for mxml
Requires:       %{library_name} = %{version}
Suggests:       %{name}-doc = %{version}

%description devel
Mini-XML is a small XML parsing library that you can use to read XML
data files or strings in your application without requiring large
non-standard libraries.

This package holds the development files for mxml.

%package doc
Summary:        Documentation for mxml
BuildArch:      noarch

%description doc
Mini-XML is a small XML parsing library that you can use to read XML
data files or strings in your application without requiring large
non-standard libraries.

This package holds the documentation for mxml.

%prep
%autosetup

%build
%configure --with-docdir=%{_docdir}/%{name} --disable-static
%make_build

%install
%make_install DOCFILES="doc/mxml.epub doc/mxml.html doc/mxml-cover.png README.md" \
              INSTALL_LIB='$(INSTALL) -s -m 755'

%check
./testmxml test.xml

%ldconfig_scriptlets -n %{library_name}

%files -n %{library_name}
%{_libdir}/lib%{name}4.so.*

%files devel
%license LICENSE NOTICE
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}4.so
%{_libdir}/pkgconfig/%{name}4.pc
%{_mandir}/man3/%{name}4.3%{?ext_man}

%files doc
%{_docdir}/%{name}

%changelog
