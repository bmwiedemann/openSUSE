#
# spec file for package python-graphviz
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-graphviz
Version:        0.20.1
Release:        0
Summary:        Python interface for Graphviz
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/xflr6/graphviz
Source:         https://files.pythonhosted.org/packages/source/g/graphviz/graphviz-%{version}.zip
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module pytest-mock >= 3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  noto-sans-fonts
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
%autosetup -n graphviz-%{version}
sed -i '/--cov/d' setup.cfg
sed -i '/^mock_use_standalone_module/d' setup.cfg

# Fix wrong-file-end-of-line-encoding
dos2unix LICENSE.txt README.rst docs/*.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/graphviz
%{python_sitelib}/graphviz-%{version}*-info

%changelog
