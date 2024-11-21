#
# spec file for package python-types-python-dateutil
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
Name:           python-types-python-dateutil
Version:        2.9.0.20241003
Release:        0
Summary:        Typing stubs for python-dateutil
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         https://files.pythonhosted.org/packages/source/t/types-python-dateutil/types-python-dateutil-%{version}.tar.gz
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
## Typing stubs for python-dateutil

This is a PEP 561 type stub package for the `python-dateutil` package. It
can be used by type-checking tools like

%prep
%autosetup -p1 -n types-python-dateutil-%{version}

%build
%pyproject_wheel

%check
%python_exec -m mypy dateutil-stubs

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/dateutil-stubs
%{python_sitelib}/types_python_dateutil-%{version}.dist-info

%changelog
