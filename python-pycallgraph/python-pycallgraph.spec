#
# spec file for package python-pycallgraph
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
Name:           python-pycallgraph
Version:        1.0.1
Release:        0
Summary:        Python application flow visualizer
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://pycallgraph.slowchop.com/
Source:         https://files.pythonhosted.org/packages/source/p/pycallgraph/pycallgraph-%{version}.tar.gz
# Three very small files missing from sdist
Source1:        https://raw.githubusercontent.com/gak/pycallgraph/develop/test/helpers.py
Source2:        https://raw.githubusercontent.com/gak/pycallgraph/develop/test/calls.py
Source3:        https://raw.githubusercontent.com/gak/pycallgraph/develop/test/conftest.py
BuildRequires:  %{python_module modernize}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  python-rpm-macros
Requires:       graphviz
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python Call Graph is a Python module that creates call graph
visualizations for Python applications.

%prep
%setup -q -n pycallgraph-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} test/
# Avoid needing a useless test helper module.
sed -i '/import fix_path/d' test/helpers.py

sed -i '/use_2to3/d' setup.py
python-modernize -w -n --no-diffs pycallgraph/ test/

# test_no_stdlib fails due to https://github.com/gak/pycallgraph/issues/193
# low impact as nothing breaks, only stdlib functions are not excluded
# from the output graph.  This improves the logic a little, but a large
# rewrite is needed to do it properly.
sed -i 's/sysconfig.get_python_lib()/sysconfig.get_python_lib(plat_specific=True)/' pycallgraph/tracer.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pycallgraph

%check

%python_exec setup.py test

%post
%python_install_alternative pycallgraph

%postun
%python_uninstall_alternative pycallgraph

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pycallgraph
%{python_sitelib}/*

%changelog
