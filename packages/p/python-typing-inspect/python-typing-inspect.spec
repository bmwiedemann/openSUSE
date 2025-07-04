#
# spec file for package python-typing-inspect
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
Name:           python-typing-inspect
Version:        0.9.0
Release:        0
Summary:        Python runtime inspection utilities for typing
License:        MIT
URL:            https://github.com/ilevkivskyi/typing_inspect
Source:         https://files.pythonhosted.org/packages/source/t/typing_inspect/typing_inspect-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mypy_extensions >= 0.3.0
Requires:       python-typing_extensions >= 3.7.4
Suggests:       python-typing >= 3.7.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mypy_extensions >= 0.3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 3.7.4}
# /SECTION
%python_subpackages

%description
Python runtime inspection utilities for typing module.

%prep
%autosetup -p1 -n typing_inspect-%{version}

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
%{python_sitelib}/typing_inspect.py
%pycache_only %{python_sitelib}/__pycache__/typing_inspect.*.pyc
%{python_sitelib}/typing_inspect-%{version}.dist-info

%changelog
