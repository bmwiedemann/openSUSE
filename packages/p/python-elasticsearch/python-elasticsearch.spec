#
# spec file for package python-elasticsearch
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-elasticsearch
# DO NOT UPDATE until the compatible version of
# python-elasticsearch-dsl is available
Version:        8.17.0
Release:        0
Summary:        Python client for Elasticsearch
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/elastic/elasticsearch-py
Source:         https://github.com/elastic/elasticsearch-py/archive/refs/tags/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Make-pyarrow-dependency-optional-for-tests.patch gh#elastic/elasticsearch-py#2733
Patch1:         0001-Make-pyarrow-dependency-optional-for-tests.patch
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module elastic-transport}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module urllib3 >= 1.21.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-elastic-transport
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module PyYAML >= 5.4}
BuildRequires:  %{python_module aiohttp >= 3 with %python-aiohttp < 4}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests >= 2.4 with %python-requests < 3}
# /SECTION
%python_subpackages

%description
Official low-level client for Elasticsearch. Its goal is to provide common
ground for all Elasticsearch-related code in Python; because of this it tries
to be opinion-free and very extendable.

%prep
%autosetup -p1 -n elasticsearch-py-%{version}
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip some flaky tests that fails in OBS
donttest="test_sniff_uses_sniff_timeout or test_sniff_on_node_failure_triggers"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc CODE_OF_CONDUCT.md CHANGELOG.md README.md
%{python_sitelib}/elasticsearch
%{python_sitelib}/elasticsearch-%{version}*-info

%changelog
