#
# spec file for package qore-yaml-module
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
%define src_name module-yaml-release-%{qore_version}
%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-yaml-module
# for version base see CMakeLists.txt, tags are done for each qore release
Version:        0.7.0+qore%{qore_version}
Release:        0
Summary:        YAML module for Qore
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-yaml/archive/refs/tags/release-%{qore_version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libyaml-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.9.0
Requires:       qore-module(abi)%{?_isa} = %{module_api}
Suggests:       %{name}-doc = %{version}

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
autoreconf -fi
%configure \
%ifarch x86_64 ppc64 ppc64le s390x
  --enable-64bit \
%endif
  --disable-debug
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/doc/qore-yaml-module
%make_install
# Documentation needs the new built modules
export QORE_MODULE_DIR=%{buildroot}/%{_libdir}/qore-modules:%{buildroot}%{_datadir}/qore-modules
make html-local
%make_install install-html-local
%fdupes %{buildroot}%{_datadir}/qore-yaml-module

%files
%license COPYING.LGPL COPYING.MIT
%{_libdir}/qore-modules/*
%{_datadir}/qore-modules/*

%files doc
%doc README RELEASE-NOTES
%doc %{_datadir}/qore-yaml-module

%changelog
