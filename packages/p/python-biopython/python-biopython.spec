#
# spec file for package python-biopython
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Tests require a network connection
%bcond_with test
%define skip_python2 1
%define skip_python36 1
Name:           python-biopython
Version:        1.80
Release:        0
Summary:        Python Tools for Computational Molecular Biology
License:        BSD-3-Clause AND MIT
URL:            https://biopython.org/
Source0:        https://files.pythonhosted.org/packages/source/b/biopython/biopython-%{version}.tar.gz
Source100:      python-biopython-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-xml
Recommends:     python-matplotlib
Recommends:     python-mysql
Recommends:     python-networkx
Recommends:     python-psycopg2
Recommends:     python-pydot
Recommends:     python-pygraphviz
Recommends:     python-rdflib
Recommends:     python-reportlab
%python_subpackages

%description
The Biopython Project is an international association of developers of freely
available Python tools for computational molecular biology.

%prep
%setup -q -n biopython-%{version}
find -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'
# Example scripts cannot be in a subdirectory
mv -v Doc/examples examples

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
export LANG=en_US.UTF-8
%pytest
%endif

%files %{python_files}
%doc CONTRIB.rst DEPRECATED.rst NEWS.rst README.rst
%doc Doc/ examples/
%license LICENSE.rst
%{python_sitearch}/Bio/
%{python_sitearch}/BioSQL/
%{python_sitearch}/biopython-%{version}-py*.egg-info

%changelog
