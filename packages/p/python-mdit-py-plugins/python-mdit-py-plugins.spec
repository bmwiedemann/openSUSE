#
# spec file for package python-mdit-py-plugins
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
Name:           python-mdit-py-plugins
Version:        0.4.1
Release:        0
Summary:        Collection of plugins for markdown-it-py
License:        MIT
URL:            https://mdit-py-plugins.readthedocs.io/
Source:         https://github.com/executablebooks/mdit-py-plugins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module markdown-it-py}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  fdupes
#Source:         https://files.pythonhosted.org/packages/source/m/mdit-py-plugins/mdit-py-plugins-%%{version}.tar.gz
BuildRequires:  python-rpm-macros
Requires:       python-markdown-it-py
BuildArch:      noarch
%python_subpackages

%description
Collection of core plugins for markdown-it-py.

%prep
%autosetup -p1 -n mdit-py-plugins-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md CHANGELOG.md docs/index.md
%license LICENSE
%{python_sitelib}/mdit_py_plugins/
%{python_sitelib}/mdit_py_plugins-%{version}*-info

%changelog
