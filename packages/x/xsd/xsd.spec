#
# spec file for package xsd
#
# Copyright (c) 2023 SUSE LLC
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


Name:           xsd
Version:        4.1.0
Release:        0
Summary:        W3C XML schema to C++ data binding compiler
# http://www.codesynthesis.com/products/xsd/license.xhtml
License:        SUSE-GPL-2.0-with-FLOSS-exception
URL:            https://www.codesynthesis.com/products/xsd/
Source0:        https://codesynthesis.com/~boris/tmp/xsd/%{version}.a11/%{name}-%{version}.a11+dep.tar.bz2
Source1:        cxx-tree-guide.pdf
Source2:        cxx-parser-guide.pdf
Source3:        cxx-tree-manual.pdf
Source99:       xsd-rpmlintrc
# Rename xsd to xsdcxx
Patch0:         xsdcxx-rename.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libboost_headers-devel
BuildRequires:  libxerces-c-devel > 2.8.0
BuildRequires:  m4
Requires:       libxerces-c-devel

%description
CodeSynthesis XSD is an open-source, cross-platform W3C XML Schema to
C++ data binding compiler. Provided with an XML instance specification
(XML Schema), it generates C++ classes that represent the given
vocabulary as well as parsing and serialization code.
You can then access the data stored in XML using types and functions
that semantically correspond to your application domain rather than
dealing with intricacies of reading and writing XML.

%package        doc
Summary:        API documentation files for xsd
Group:          Documentation/Other
Requires:       xsd
BuildArch:      noarch

%description    doc
This package contains API documentation for xsd.

%prep
%autosetup -p1 -n %{name}-%{version}.a11+dep

%build
%make_build CXXFLAGS="%{optflags}"

%install
make install_prefix="%{buildroot}%{_prefix}" install

# Rename xsd to xsdcxx to avoid conflicting with mono-web package.
mv %{buildroot}%{_bindir}/xsd %{buildroot}%{_bindir}/xsdcxx
mv %{buildroot}%{_datadir}/doc/xsd %{buildroot}%{_datadir}/doc/xsdcxx
mv %{buildroot}%{_mandir}/man1/xsd.1 %{buildroot}%{_mandir}/man1/xsdcxx.1

# Remove duplicate docs.
rm -r %{buildroot}%{_datadir}/doc/libxsd

# the pdf creation relies on a double conversion, first to create a ps file, then a PDF
# the process produces unreproducible builds. Replace with pre-generated files
cp -f %{SOURCE1} %{buildroot}%{_datadir}/doc/xsdcxx/cxx/tree/cxx-tree-guide.pdf
cp -f %{SOURCE2} %{buildroot}%{_datadir}/doc/xsdcxx/cxx/tree/guide/cxx-parser-guide.pdf
cp -f %{SOURCE3} %{buildroot}%{_datadir}/doc/xsdcxx/cxx/tree/manual/cxx-tree-manual.pdf

%fdupes -s %{buildroot}%{_datadir}/doc

%files
%license xsd/LICENSE
%doc README xsd/NEWS xsd/GPLv2 xsd/FLOSSE
%{_bindir}/xsdcxx
%{_includedir}/xsd/
%{_mandir}/man1/xsdcxx.1%{?ext_man}

%files doc
%doc %{_datadir}/doc/xsdcxx

%changelog
