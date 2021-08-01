#
# spec file for package qore-json-module
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
%define module_api %(qore --latest-module-api 2>/dev/null)
%define src_name module-json-release-%{qore_version}
Name:           qore-json-module
Version:        1.8+qore%{qore_version}
Release:        0
Summary:        JSON module for Qore
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
URL:            https://qore.org
Source:         https://github.com/qorelanguage/module-json/archive/refs/tags/release-%{qore_version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.9.5
Requires:       qore-module(abi)%{?_isa} = %{module_api}

%description
This package contains the json module for the Qore Programming Language.

JSON is a concise human-readable data serialization format.

%package doc
Summary:        JSON module for Qore

%description doc
This package contains the HTML documentation and example programs for the Qore
json module.

%prep
%setup -q -n %{src_name}

%build
%cmake
%make_build docs

%install
%cmake_install

%files
%license COPYING.LGPL COPYING.MIT
%{_datadir}/qore-modules/*
%{_libdir}/qore-modules/*

%files doc
%doc README RELEASE-NOTES
%doc build/html/*

%changelog
