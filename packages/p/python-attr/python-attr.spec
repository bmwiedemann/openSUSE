#
# spec file for package python-attr
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
Name:           python-attr
Version:        0.3.2
Release:        0
Summary:        Python module for setting attributes of target functions or classes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/denis-ryzhkov/attr
Source:         https://files.pythonhosted.org/packages/source/a/attr/attr-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A decorator to set attributes of target function or class in a DRY way.

%prep
%setup -q -n attr-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec dry_attr.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/attr.py
%{python_sitelib}/dry_attr.py
%{python_sitelib}/attr-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/*attr*

%changelog
