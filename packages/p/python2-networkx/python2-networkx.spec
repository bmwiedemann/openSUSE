#
# spec file for package python2-networkx
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
%define         oldpython python
%define         skip_python3 1
Name:           python2-networkx
Version:        2.2
Release:        0
Summary:        Python package for the study of complex networks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://networkx.github.io/
Source:         https://files.pythonhosted.org/packages/source/n/networkx/networkx-%{version}.zip
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module decorator >= 3.4.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nose >= 0.10.1}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python2-decorator >= 3.4.0
Recommends:     python2-PyYAML
Recommends:     python2-matplotlib
Recommends:     python2-pydot
Recommends:     python2-pygraphviz
Recommends:     python2-pyparsing
Recommends:     python2-scipy
BuildArch:      noarch
Provides:       %{oldpython}-networkx = %{version}
%python_subpackages

%description
NetworkX (NX) is a Python package for the creation, manipulation, and study of the structure, dynamics,
and functions of complex networks.

Features:
 * Includes standard graph-theoretic and statistical physics functions
 * Exchange of network algorithms between applications, disciplines, and platforms
 * Includes many classic graphs and synthetic networks
 * Nodes and edges can be "anything" (e.g. time-series, text, images, XML records)
 * Exploits existing code from high-quality legacy software in C, C++, Fortran, etc.
 * Unit-tested

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module networkx-doc = %{version}}

%description -n %{name}-doc
Documentation and examples for %{name}.

%prep
%setup -q -n networkx-%{version}

%build
%python_build

%install
%python_install

# Move docs into correct directory if necessary
if [ "%{_docdir}" != "%{_datadir}/doc" ] ; then
    mkdir -p %{buildroot}%{_docdir}/
    mv %{buildroot}%{_datadir}/doc/networkx-%{version} %{buildroot}%{_docdir}/
fi

%fdupes %{buildroot}%{_docdir}

%{python_expand pushd %{buildroot}%{$python_sitelib}
# Fix wrong-script-interpreter
find networkx -name '*test*.py' -exec sed -i "s|#!%{_bindir}/env python|#!%__$python|" {} +
find networkx -name '*test*.py' -exec grep -q '#!%__$python' {} \; -exec chmod a+x {} +
# Deduplicating files can generate a RPMLINT warning for pyc mtime
find networkx -name '*test*.py' -exec $python -m compileall -d %{$python_sitelib} {} \;
find networkx -name '*test*.py' -exec $python -O -m compileall -d %{$python_sitelib} {} \;
rm -f _current_flavor
%fdupes .
popd
}

%check
# test excluded because it leads to crashes on i586, gh#networkx/networkx#3304
%python_exec setup.py nosetests -v -e 'test_subgraph_centrality_big_graph'

%files %{python_files}
%license LICENSE.txt
%doc README.rst CONTRIBUTING.rst
%{python_sitelib}/networkx/
%{python_sitelib}/networkx-%{version}-py*.egg-info

%files -n %{name}-doc
%license LICENSE.txt
%{_docdir}/networkx-%{version}/

%changelog
