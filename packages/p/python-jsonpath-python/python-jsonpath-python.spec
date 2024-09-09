#
# spec file for package python-jsonpath-python
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-jsonpath-python
Version:        1.0.6
Release:        0
Summary:        A more powerful JSONPath implementation in modern Python
License:        MIT
URL:            https://github.com/zhangxianbing/jsonpath-python
Source:         https://files.pythonhosted.org/packages/source/j/jsonpath-python/jsonpath-python-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A more powerful JSONPath implementation in modern Python.

Features

* Light. (No need to install third-party dependencies.)
* Support filter operator, including multi-selection,
  inverse-selection filtering.
* Support sorter operator, including sorting by
  multiple fields, ascending and descending order.
* Support basic semantics of JSONPath.
* Support output modes: VALUE, PATH.

%prep
%autosetup -p1 -n jsonpath-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/jsonpath
%{python_sitelib}/jsonpath_python-%{version}.dist-info

%changelog
