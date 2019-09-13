#
# spec file for package python-nbval
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
Name:           python-nbval
Version:        0.9.2
Release:        0
Summary:        A pytest plugin to validate Jupyter notebooks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/computationalmodelling/nbval
Source:         https://files.pythonhosted.org/packages/source/n/nbval/nbval-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-coverage
Requires:       python-ipykernel
Requires:       python-jupyter_client
Requires:       python-nbdime
Requires:       python-nbformat
Requires:       python-pytest >= 2.8
Requires:       python-six
Recommends:     python-matplotlib
Recommends:     python-pytest-cov
Recommends:     python-pytest-timeout
Recommends:     python-sympy
Provides:       python-jupyter_nbval = %{version}
Obsoletes:      python-jupyter_nbval <= %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nbdime}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pyinotify}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sympy}
# /SECTION
%ifpython3
Provides:       jupyter-nbval = %{version}
%endif
%python_subpackages

%description
The plugin adds functionality to py.test to recognise and collect
Jupyter notebooks. The intended purpose of the tests is to determine
whether execution of the stored inputs match the stored outputs of
the .ipynb file. Whilst also ensuring that the notebooks are running
without errors.

The tests were designed to ensure that Jupyter notebooks (especially
those for reference and documentation), are executing consistently.

Each cell is taken as a test, a cell that doesn't reproduce the
expected output will fail.

%prep
%setup -q -n nbval-%{version}
sed -i 's/\r$//' README.md

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
