#
# spec file for package python-objgraph
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
Name:           python-objgraph
Version:        3.6.1
Release:        0
Summary:        Python module to draw object reference graphs with graphviz
License:        MIT
Group:          Development/Languages/Python
URL:            http://mg.pov.lt/objgraph/
Source:         https://files.pythonhosted.org/packages/source/o/objgraph/objgraph-%{version}.tar.gz
# see https://github.com/mgedmin/objgraph/issues/80
Patch1:         python313.patch
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  python-rpm-macros
Requires:       graphviz-gd
Requires:       graphviz-gnome
Requires:       python-graphviz
BuildArch:      noarch
%python_subpackages

%description
objgraph is a module for visual exploration of Python object graphs.

graphviz is needed if pretty graphs are desired.
xdot can be used for interactive use.

%prep
%autosetup -p1 -n objgraph-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst CHANGES.rst HACKING.rst
%license LICENSE
%{python_sitelib}/objgraph.py
%pycache_only %{python_sitelib}/__pycache__/objgraph*
%{python_sitelib}/objgraph-%{version}.dist-info

%changelog
