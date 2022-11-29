#
# spec file for package python-elasticsearch-dsl
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


Name:           python-elasticsearch-dsl
Version:        7.4.0
Release:        0
Summary:        Python client for Elasticsearch
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/elasticsearch/elasticsearch-dsl-py
Source:         https://github.com/elastic/elasticsearch-dsl-py/archive/refs/tags/v%{version}.tar.gz#/elasticsearch-dsl-%{version}.tar.gz
# https://github.com/elastic/elasticsearch-dsl-py/issues/1596
# PATCH-FEATURE-UPSTREAM python-elasticsearch-dsl-no-mock.patch gh#elastic/elasticsearch-dsl-py#1596 mcepl@suse.com
# Use unittest.mock instead of the external package (merged to master, not yet released)
Patch0:         python-elasticsearch-dsl-no-mock.patch
# PATCH-FEATURE-UPSTREAM drop-python2-support.patch gh#elastic/elasticsearch-dsl-py@f7f85a5db8f2
Patch1:         drop-python2-support.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# gh#elastic/elasticsearch-dsl-py#1569
Requires:       (python-elasticsearch >= 7.0.0 with python-elasticsearch < 8)
Requires:       python-python-dateutil
Suggests:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module elasticsearch >= 7.0.0 with %python-elasticsearch < 8.0.0}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
Python client for Elasticsearch.

%prep
%autosetup -p1 -n elasticsearch-dsl-py-%{version}

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
%{python_sitelib}/elasticsearch_dsl/
%{python_sitelib}/elasticsearch_dsl-%{version}*-info/

%changelog
