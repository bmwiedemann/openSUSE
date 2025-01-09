#
# spec file for package python-elasticsearch-dsl
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
Name:           python-elasticsearch-dsl
Version:        8.17.0
Release:        0
Summary:        Python client for Elasticsearch
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/elasticsearch/elasticsearch-dsl-py
Source:         https://github.com/elastic/elasticsearch-dsl-py/archive/refs/tags/v%{version}.tar.gz#/elasticsearch-dsl-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# gh#elastic/elasticsearch-dsl-py#1569
Requires:       python-elasticsearch >= 8.0.0
Requires:       python-elastic-transport >= 8.0.0
Requires:       python-python-dateutil
Requires:       python-typing_extensions
Suggests:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module elasticsearch >= 8.0.0}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module nltk}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module sqlite3}
# /SECTION
%python_subpackages

%description
Python client for Elasticsearch.

%prep
%autosetup -p1 -n elasticsearch-dsl-py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires nltk wordnet
%pytest --ignore tests/test_integration/test_examples/_async/test_vectors.py --ignore tests/test_integration/test_examples/_sync/test_vectors.py

%files %{python_files}
%doc AUTHORS Changelog.rst README
%license LICENSE
%{python_sitelib}/elasticsearch_dsl
%{python_sitelib}/elasticsearch_dsl-%{version}.dist-info

%changelog
