#
# spec file for package python-nxapi-plumbing
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-nxapi-plumbing
Version:        0.5.2
Release:        0
Summary:        A library for managing Cisco devices through NX-API using XML or jsonrpc
License:        Apache-2.0
URL:            https://github.com/ktbyers/nxapi-plumbing
Source:         https://github.com/ktbyers/nxapi-plumbing/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         python-nxapi-plumbing-fix-broken-test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Requires:       python-lxml
Requires:       python-requests >= 2.7.0
Requires:       python-scp
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module scp}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A low-level library for managing Cisco devices through NX-API using JSON-RPC and XML.

%prep
%setup -q -n nxapi-plumbing-%{version}
%patch0 -p1
sed -i 's/\r$//' README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
