#
# spec file for package python-altgraph
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-altgraph
Version:        0.16.1
Release:        0
Summary:        Python graph (network) package
License:        MIT
URL:            https://bitbucket.org/ronaldoussoren/altgraph/
Source:         https://files.pythonhosted.org/packages/source/a/altgraph/altgraph-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
rm doc/_build/html/.buildinfo
sed -i 's/\r$//' doc/_build/html/_static/jquery.js

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.txt
%license LICENSE
%{python_sitelib}/*

%files -n %{name}-doc
%doc doc/_build/html/
%license LICENSE

%changelog
