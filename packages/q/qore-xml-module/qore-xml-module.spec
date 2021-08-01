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


%define qore_version 0.9.15
%define module_api   %(qore --latest-module-api 2>/dev/null)
%define src_name     module-xml-release-%{qore_version}
Name:           qore-xml-module
Version:        1.5.0+qore%{qore_version}
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
BuildRequires:  qore-devel >= 0.9
Requires:       %{_bindir}/env
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

%prep
%setup -q -n %{src_name}

%build
%cmake
%cmake_build
make %{?_smp_mflags} docs

%install
%cmake_install
%fdupes -s %{__builddir}/html
ls -ahlp %__builddir/html

%files
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES
%{_bindir}/soaputil
%{_datadir}/qore-modules
%{_libdir}/qore-modules

%files doc
%doc %{__builddir}/html examples

%changelog
