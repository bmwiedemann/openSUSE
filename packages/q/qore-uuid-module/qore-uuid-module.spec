#
# spec file for package qore-uuid-module
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define qore_version 1.0.10
%define module_api   %(qore --latest-module-api 2>/dev/null)
%define src_name     module-uuid-release-%{qore_version}
Name:           qore-uuid-module
Version:        1.4.0+qore%{qore_version}
Release:        0
Summary:        UUID module for Qore
License:        LGPL-2.1+ or MIT
Group:          Development/Languages
URL:            https://qore.org
Source:         https://github.com/qorelanguage/module-uuid/archive/refs/tags/release-%{qore_version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libuuid-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= %{qore_version}
Requires:       qore-module(abi)%{?_isa} = %{module_api}

%description
This package contains the uuid module for the Qore Programming Language.

UUIDs are universally unique identifiers that can be used for any purpose.

%package doc
Summary:        Documentation and examples for the Qore UUID module
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
uuid module.

%prep
%setup -q -n %{src_name}

%build
%cmake
%make_build docs

%install
%cmake_install
%fdupes -s %{__builddir}/html

%files
%license COPYING*
%doc README RELEASE-NOTES AUTHORS
%{_libdir}/qore-modules

%files doc
%doc %{__builddir}/html

%changelog
