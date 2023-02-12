#
# spec file for package qore-linenoise-module
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


%define src_name module-linenoise-%{version}
%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-linenoise-module
Version:        1.0.1
Release:        0
Summary:        Linenoise module for Qore
License:        LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-linenoise/archive/refs/tags/v%{version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  qore >= 1.12.4
BuildRequires:  qore-stdlib >= 1.12.4
BuildRequires:  qore-devel >= 1.12.4
Requires:       qore-module(abi)%{?_isa} = %{module_api}
Suggests:       %{name}-doc = %{version}

%description
The linenoise module provides readline-like functionality to Qore,
allowing qore programs to manage comfortable user input in the command line.

%package doc
Summary:        Documentation and examples for the Qore linenoise module
Group:          Development/Languages/Misc
Requires:       %{name} = %{version}

%description doc
This package contains the HTML documentation and example programs for the Qore
linenoise module.

%prep
%setup -q -n %{src_name}

%build
%cmake
%cmake_build docs

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING.LGPL COPYING.MIT
%{_libdir}/qore-modules/*

%files doc
%doc README
%doc %{__builddir}/docs/linenoise/html

%changelog
