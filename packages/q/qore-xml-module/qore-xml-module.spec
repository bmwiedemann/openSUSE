#
# spec file for package qore-xml-module
#
# Copyright (c) 2021 SUSE LLC
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


%define qore_version 1.0.10
%define module_api   %(qore --latest-module-api 2>/dev/null)
%define src_name     module-xml-release-%{qore_version}
Name:           qore-xml-module
Version:        1.5.1+qore%{qore_version}
Release:        0
Summary:        XML module for Qore
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
URL:            https://qore.org
Source:         https://github.com/qorelanguage/module-xml/archive/refs/tags/release-%{qore_version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= %{qore_version}
Requires:       qore-module(abi)%{?_isa} = %{module_api}

%description
This package contains the xml module for the Qore Programming Language.

XML is a markup language for encoding information.

%package doc
Summary:        Documentation and examples for the Qore xml module
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
xml module.

%package tools
Summary:        User tools writen in Qore Programming Language
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Tools/Other
Requires:       %{name} = %{version}-%{release}

%description tools
This package contains the webdav server and soap utils.

%prep
%setup -q -n %{src_name}

%build
%cmake
%make_build docs

%install
%cmake_install
%fdupes -s %{__builddir}/html
# Fix scripts
find examples -name "*.q" -exec sed -i '1 s/env qore/qore/' \{\} +
for f in "%{buildroot}%{_bindir}/"{soaputil,webdav-server}; do sed -i '1 s/env qore/qore/' "$f"; done

%files
%license COPYING.LGPL COPYING.MIT
%{_datadir}/qore-modules
%{_libdir}/qore-modules

%files doc
%doc %{__builddir}/html examples

%files tools
%doc README RELEASE-NOTES
%{_bindir}/webdav-server
%{_bindir}/soaputil

%changelog
