#
# spec file for package python-elasticsearch
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
%bcond_without  test
Name:           python-elasticsearch
Version:        7.0.2
Release:        0
Summary:        Python client for Elasticsearch
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/elastic/elasticsearch-py
Source:         https://github.com/elastic/elasticsearch-py/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nosexcover}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module requests >= 2.0.0}
BuildRequires:  %{python_module urllib3 >= 1.21.1}
%endif
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS Changelog.rst README
%{python_sitelib}/*

%changelog
