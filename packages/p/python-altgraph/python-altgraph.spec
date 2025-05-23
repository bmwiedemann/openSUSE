#
# spec file for package python-altgraph
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
Name:           python-altgraph
Version:        0.17.4
Release:        0
Summary:        Python graph (network) package
License:        MIT
URL:            https://github.com/ronaldoussoren/altgraph/
Source:         https://files.pythonhosted.org/packages/source/a/altgraph/altgraph-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

%package     -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module altgraph-doc = %{version}}

%description -n %{name}-doc
Altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

%prep
%setup -q -n altgraph-%{version}

%build
%pyproject_wheel
cd doc && make html

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/altgraph
%{python_sitelib}/altgraph-%{version}*-info

%files -n %{name}-doc
%doc doc/_build/html/
%license LICENSE

%changelog
