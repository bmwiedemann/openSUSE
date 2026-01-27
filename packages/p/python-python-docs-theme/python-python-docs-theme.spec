#
# spec file for package python-python-docs-theme
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-python-docs-theme
Version:        2025.12
Release:        0
Summary:        The Sphinx theme for the CPython docs and related projects
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python/python-docs-theme
Source:         https://files.pythonhosted.org/packages/source/p/python-docs-theme/python_docs_theme-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 7.3
BuildArch:      noarch
%python_subpackages

%description
The Sphinx theme for the CPython docs and related projects

%prep
%setup -q -n python_docs_theme-%{version}
# the python311 exclusion wasn't really needed
sed -i 's/>=3.12/>=3.11/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/python_docs_theme
%{python_sitelib}/python_docs_theme-%{version}*-info

%changelog
