#
# spec file for package python-humanreadable
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
Name:           python-humanreadable
Version:        0.4.1
Release:        0
Summary:        A Python library to convert from human-readable values to Python values
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/humanreadable
Source:         https://files.pythonhosted.org/packages/source/h/humanreadable/humanreadable-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typepy >= 1.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typepy >= 1.2.0}
# /SECTION
%python_subpackages

%description
humanreadable is a Python library to convert from human-readable
values to Python values.

%prep
%setup -q -n humanreadable-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/humanreadable*

%changelog
