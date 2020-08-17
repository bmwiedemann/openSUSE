#
# spec file for package qore-json-module
#
# Copyright (c) 2020 SUSE LLC
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


%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-json-module
Version:        1.7
Release:        0
Summary:        JSON module for Qore
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
URL:            https://qore.org
Source:         https://github.com/qorelanguage/module-json/releases/download/v%{version}/qore-json-module-%{version}.tar.bz2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.8.5
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}

%description
This package contains the json module for the Qore Programming Language.

JSON is a concise human-readable data serialization format.

%prep
%setup -q

%build
# Remove -m32 and -m64 options except for x86* and ppc*
%ifnarch %{ix86} x86_64 ppc64 ppc64le
sed -i 's/-m32//g;s/-m64//g' configure
%endif
# FIXME: you should use the %%configure macro
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=%{_prefix} --disable-debug
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/doc/qore-json-module
%make_install

%files
%{_datadir}/qore-modules
%{_libdir}/qore-modules
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES

%package doc
Summary:        JSON module for Qore

%description doc
This package contains the HTML documentation and example programs for the Qore
json module.

%files doc
%doc docs/json/html docs/JsonRpcHandler/html examples/ test/

%changelog
