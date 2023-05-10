#
# spec file for package python-pytest-plus
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pytest-plus
Version:        0.4.0
Release:        0
Summary:        Extension for pytest to enforce minimum tests pass
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pycontribs/pytest-plus
Source:         https://files.pythonhosted.org/packages/source/p/pytest-plus/pytest-plus-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 63.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6.0.1}
# /SECTION
Requires:       python-pytest >= 6.0.1
Suggests:       python-coverage >= 7.0.0
Suggests:       python-pytest-html
BuildArch:      noarch
%python_subpackages

%description
PyTest Plus extends pytest functionality to enforce PYTEST_REQPASS tests passed.

%prep
%setup -q -n pytest-plus-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
