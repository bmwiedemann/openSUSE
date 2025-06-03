#
# spec file for package python-pluginbase
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


Name:           python-pluginbase
Version:        1.0.1
Release:        0
Summary:        Module for the development of flexible plugin systems
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/pluginbase
Source:         https://files.pythonhosted.org/packages/source/p/pluginbase/pluginbase-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PluginBase is a module for Python that enables the development of
flexible plugin systems.

%prep
%setup -q -n pluginbase-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd tests
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pluginbase.py
%{python_sitelib}/pluginbase-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/pluginbase*

%changelog
