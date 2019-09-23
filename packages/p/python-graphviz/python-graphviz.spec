#
# spec file for package python-graphviz
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
Name:           python-graphviz
Version:        0.13
Release:        0
Summary:        Python interface for Graphviz
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/xflr6/graphviz
Source:         https://files.pythonhosted.org/packages/source/g/graphviz/graphviz-%{version}.zip
BuildRequires:  %{python_module mock >= 2}
BuildRequires:  %{python_module pytest >= 3.4}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock >= 1.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  w3m
BuildRequires:  xdg-utils
Requires:       graphviz
Recommends:     xdg-utils
BuildArch:      noarch
%python_subpackages

%description
This package facilitates the creation and rendering of graph descriptions in
the DOT language of the Graphviz graph drawing software from Python.

It supports creating a graph object, assembling the graph by adding nodes and
edges, and retrieving its DOT source code string, saving the source code to a
file and rendering it with the Graphviz installation.

Using the view option/method, the resulting (PDF, PNG, SVG, etc.) file can be
inspected with its default application. Graphs can also be rendered and
displayed within IPython notebooks.

%prep
%setup -q -n graphviz-%{version}

# Fix wrong-file-end-of-line-encoding
dos2unix CHANGES.txt LICENSE.txt README.rst docs/*.rst

# Remove hardcoded pytest version
sed -i -e '/minversion/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt README.rst
%{python_sitelib}/graphviz
%{python_sitelib}/graphviz-%{version}-py*.egg-info

%changelog
