#
# spec file for package qore-yaml-module
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


%define src_name module-yaml-%{version}
%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-yaml-module
Version:        0.7
Release:        0
Summary:        YAML module for Qore
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-yaml/archive/refs/tags/v%{version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libyaml-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= %{qore_version}
Requires:       qore-module(abi)%{?_isa} = %{module_api}
Suggests:       %{name}-doc = %{version}
# Version schema changed, remove with 0.7.1 release
Obsoletes:      %{name} = 0.7.0+qore1.0.10
Obsoletes:      %{name} = 0.7.0+qore0.9.15

%description
This package contains the yaml module for the Qore Programming Language.

YAML is a flexible and concise human-readable data serialization format.

%package doc
Summary:        Documentation and examples for the Qore yaml module
Group:          Development/Languages/Misc
Requires:       %{name} = %{version}

%description doc
This package contains the HTML documentation and example programs for the Qore
yaml module.

%prep
%setup -q -n %{src_name}
find examples -type f|xargs chmod 644

%build
%cmake
%cmake_build docs

%install
%cmake_install
%fdupes %{__builddir}/html

%files
%license COPYING.LGPL COPYING.MIT
%{_libdir}/qore-modules/*
%{_datadir}/qore-modules/*

%files doc
%doc README RELEASE-NOTES
%doc %{__builddir}/html

%changelog
