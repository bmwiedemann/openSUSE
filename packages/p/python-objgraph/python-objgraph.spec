#
# spec file for package python-objgraph
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
%define oldpython python
Name:           python-objgraph
Version:        3.4.1
Release:        0
Summary:        Python module to draw object reference graphs with graphviz
License:        MIT
Group:          Development/Languages/Python
URL:            http://mg.pov.lt/objgraph/
Source:         https://files.pythonhosted.org/packages/source/o/objgraph/objgraph-%{version}.tar.gz
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  python-rpm-macros
Requires:       graphviz-gd
Requires:       graphviz-gnome
Requires:       python-graphviz
Obsoletes:      %{oldpython}-objgraph-doc
BuildArch:      noarch
%python_subpackages

%description
objgraph is a module for visual exploration of Python object graphs.

graphviz is needed if pretty graphs are desired.
xdot can be used for interactive use.

%prep
%setup -q -n objgraph-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst CHANGES.rst HACKING.rst
%license LICENSE
%{python_sitelib}/*

%changelog
