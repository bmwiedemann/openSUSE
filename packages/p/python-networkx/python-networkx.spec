#
# spec file for package python-networkx
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-networkx
Version:        2.8.8
Release:        0
Summary:        Python package for the study of complex networks
License:        BSD-3-Clause
URL:            https://networkx.github.io/
Source:         https://files.pythonhosted.org/packages/source/n/networkx/networkx-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-matplotlib >= 3.4
Requires:       python-numpy >= 1.19
Requires:       python-pandas >= 1.3
Requires:       python-scipy >= 1.8
Recommends:     python-PyYAML
Recommends:     python-pydot >= 1.4.2
Recommends:     python-pygraphviz
Recommends:     python-pyparsing
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module lxml >= 4.6}
BuildRequires:  %{python_module matplotlib >= 3.4}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module pandas >= 1.3}
BuildRequires:  %{python_module pydot >= 1.4.2}
BuildRequires:  %{python_module pygraphviz >= 1.9}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.8}
# /SECTION
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
Provides:       %{python_module networkx-doc = %{version}}

%description -n %{name}-doc
Documentation and examples for %{name}.

%prep
%setup -q -n networkx-%{version}
%autopatch -p1

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
find networkx -name '*test*.py' -exec sed -i "s|#!%{_bindir}/env python$|#!%__$python|" {} +
find networkx -name '*test*.py' -exec sed -i "s|#!%{_bindir}/env python3$|#!%__$python|" {} +
find networkx -name '*test*.py' -exec grep -q '#!%__$python' {} \; -exec chmod a+x {} +
# Deduplicating files can generate a RPMLINT warning for pyc mtime
find networkx -name '*test*.py' -exec $python -m compileall -d %{$python_sitelib} {} \;
find networkx -name '*test*.py' -exec $python -O -m compileall -d %{$python_sitelib} {} \;
rm -f _current_flavor
%fdupes .
popd
}

%check
# gh#networkx/networkx#4030 we cannot use -n auto because
# TestKatzCentralityDirectedNumpy fails otherwise
# (pandas) test_from_adjacency_named fails on i586
%if 0%{?suse_version} < 1550
rm -v networkx/drawing/tests/test_pydot.py
%endif
%pytest -rs -k 'not test_from_adjacency_named and not test_asadpour_tsp'

%files %{python_files}
%license LICENSE.txt
%doc README.rst CONTRIBUTING.rst
%{python_sitelib}/networkx/
%{python_sitelib}/networkx-%{version}-py*.egg-info

%files -n %{name}-doc
%license LICENSE.txt
%doc %{_docdir}/networkx-%{version}/

%changelog
