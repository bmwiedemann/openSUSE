#
# spec file for package python-expandvars
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-expandvars
Version:        1.1.2
Release:        0
Summary:        Expand system variables Unix style
License:        MIT
URL:            https://github.com/sayanarijit/expandvars
Source:         https://files.pythonhosted.org/packages/source/e/expandvars/expandvars-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Expand system variables Unix style

This module is inspired by [GNU bash's variable expansion
features](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html).
It can be used as an alternative to Python's
[os.path.expandvars](https://docs.python.org/3/library/os.path.html#os.path.expandvars)
function.

%prep
%autosetup -p1 -n expandvars-%{version}
# remove coverage which also breaks with pytest 9
sed -i '/addopts = /d' pyproject.toml

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
%{python_sitelib}/expandvars.py
%pycache_only %{python_sitelib}/__pycache__/expandvars*
%{python_sitelib}/expandvars-%{version}.dist-info

%changelog
