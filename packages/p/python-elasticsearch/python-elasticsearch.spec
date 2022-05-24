#
# spec file for package python-elasticsearch
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-elasticsearch
Version:        7.6.0
Release:        0
Summary:        Python client for Elasticsearch
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/elastic/elasticsearch-py
Source:         https://github.com/elastic/elasticsearch-py/archive/%{version}.tar.gz
# https://github.com/elastic/elasticsearch-py/issues/1983
Patch0:         python-elasticsearch-no-mock.patch
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 >= 1.21.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-urllib3 >= 1.21.1
BuildArch:      noarch
%python_subpackages

%description
Official low-level client for Elasticsearch. Its goal is to provide common
ground for all Elasticsearch-related code in Python; because of this it tries
to be opinion-free and very extendable.

%prep
%setup -q -n elasticsearch-py-%{version}
rm README.rst
sed -i 's/from nose.plugins.skip import SkipTest/from unittest import SkipTest/' test_elasticsearch/test_helpers.py
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs

%files %{python_files}
%license LICENSE
%doc AUTHORS Changelog.rst README
%{python_sitelib}/*

%changelog
