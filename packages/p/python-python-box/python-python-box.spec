#
# spec file for package python-python-box
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


%{?sle15_python_module_pythons}
Name:           python-python-box
Version:        7.2.0
Release:        0
Summary:        Advanced Python dictionaries with dot notation access
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cdgriffith/Box
Source:         https://github.com/cdgriffith/Box/archive/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module msgpack >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml >= 0.17}
BuildRequires:  %{python_module toml >= 0.10.2}
# /SECTION
Requires:       python-msgpack >= 1.0.0
Requires:       python-ruamel.yaml >= 0.17
Requires:       python-toml >= 0.10.2
%python_subpackages

%description
Advanced Python dictionaries with dot notation access

%prep
%setup -q -n Box-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH='.'
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/box
%{python_sitelib}/python_box-%{version}.dist-info

%changelog
