#
# spec file for package python-elasticsearch-dsl
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-elasticsearch-dsl
Version:        7.2.1
Release:        0
Summary:        Python client for Elasticsearch
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/elasticsearch/elasticsearch-dsl-py
Source:         https://github.com/elastic/elasticsearch-dsl-py/archive/%{version}.tar.gz#/elasticsearch-dsl-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-elasticsearch >= 7.0.0
Requires:       python-python-dateutil
Requires:       python-six
Suggests:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage < 5.0.0}
BuildRequires:  %{python_module elasticsearch >= 7.0.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python client for Elasticsearch.

%prep
%setup -q -n elasticsearch-dsl-py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS Changelog.rst README
%license LICENSE
%{python_sitelib}/*

%changelog
