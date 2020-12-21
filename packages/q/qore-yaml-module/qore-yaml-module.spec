#
# spec file for package qore-yaml-module
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
Name:           qore-yaml-module
Version:        0.6
Release:        0
Summary:        YAML module for Qore
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/Misc
URL:            https://www.qore.org/
Source:         https://github.com/qorelanguage/module-yaml/releases/download/v%{version}/qore-yaml-module-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libyaml-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.8.5
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}

%description
This package contains the yaml module for the Qore Programming Language.

YAML is a flexible and concise human-readable data serialization format.

%package doc
Summary:        Documentation and examples for the Qore yaml module
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Development/Languages

%description doc
This package contains the HTML documentation and example programs for the Qore
yaml module.

%files doc
%doc docs/yaml docs/YamlRpcClient docs/YamlRpcHandler test examples

%prep
%setup -q
find examples -type f|xargs chmod 644

%build
%ifarch x86_64 ppc64 ppc64le s390x
c64=--enable-64bit
%endif
# FIXME: you should use the %%configure macro
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=%{_prefix} --disable-debug $c64
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/doc/qore-yaml-module
%make_install
%fdupes -s docs

%files
%{_libdir}/qore-modules
%{_datadir}/qore-modules
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES

%changelog
