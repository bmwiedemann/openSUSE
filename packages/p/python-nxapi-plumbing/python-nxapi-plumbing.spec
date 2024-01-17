#
# spec file for package python-nxapi-plumbing
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


Name:           python-nxapi-plumbing
Version:        0.5.2
Release:        0
Summary:        A library for managing Cisco devices through NX-API using XML or jsonrpc
License:        Apache-2.0
URL:            https://github.com/ktbyers/nxapi-plumbing
Source:         https://github.com/ktbyers/nxapi-plumbing/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         python-nxapi-plumbing-fix-broken-test.patch
Patch1:         remove-future-requirement.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-requests >= 2.7.0
Requires:       python-scp
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
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
%autosetup -p1 -n nxapi-plumbing-%{version}
sed -i 's/\r$//' README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/nxapi_plumbing
%{python_sitelib}/nxapi_plumbing-%{version}.dist-info

%changelog
