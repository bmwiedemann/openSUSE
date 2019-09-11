#
# spec file for package xsd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xsd
Version:        4.0.0
Release:        0
Summary:        W3C XML schema to C++ data binding compiler
License:        SUSE-GPL-2.0-with-FLOSS-exception
Group:          Development/Languages/C and C++
# http://www.codesynthesis.com/products/xsd/license.xhtml
Url:            http://www.codesynthesis.com/products/xsd/
Source0:        http://www.codesynthesis.com/download/xsd/4.0/%{name}-%{version}+dep.tar.bz2
Source99:       xsd-rpmlintrc
# Rename xsd to xsdcxx
Patch0:         xsdcxx-rename.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libxerces-c-devel > 2.8.0
BuildRequires:  m4
Requires:       libxerces-c-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%description    doc
This package contains API documentation for xsd.

%prep
%setup -q -n %{name}-%{version}+dep
%patch0 -p1

%build
make verbose=1 CXXFLAGS="%{optflags}" %{?_smp_mflags}

%install
make install_prefix="%{buildroot}%{_prefix}"  install

# Rename xsd to xsdcxx to avoid conflicting with mono-web package.
mv %{buildroot}%{_bindir}/xsd %{buildroot}%{_bindir}/xsdcxx
mv %{buildroot}%{_datadir}/doc/xsd %{buildroot}%{_datadir}/doc/xsdcxx
mv %{buildroot}%{_mandir}/man1/xsd.1 %{buildroot}%{_mandir}/man1/xsdcxx.1

# Remove duplicate docs.
rm -rf %{buildroot}%{_datadir}/doc/libxsd

%fdupes -s %{buildroot}%{_datadir}/doc

%files
%defattr(-,root,root,-)
%doc README xsd/NEWS xsd/LICENSE xsd/GPLv2 xsd/FLOSSE
%{_bindir}/xsdcxx
%{_includedir}/xsd/
%{_mandir}/man1/xsdcxx.1*

%files doc
%defattr(-,root,root,-)
%doc %{_datadir}/doc/xsdcxx

%changelog
