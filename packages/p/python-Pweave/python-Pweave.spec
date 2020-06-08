#
# spec file for package python-Pweave
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-Pweave
Version:        0.30.3
Release:        0
Summary:        Scientific reports with embedded python computations
License:        BSD-3-Clause
URL:            https://github.com/mpastell/Pweave
Source:         https://files.pythonhosted.org/packages/source/P/Pweave/Pweave-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown
Requires:       python-Pygments
Requires:       python-certifi
Requires:       python-jupyter_client
Requires:       python-jupyter_ipykernel
Requires:       python-jupyter_ipython
Requires:       python-jupyter_nbconvert
Requires:       python-jupyter_nbformat
Recommends:     python-Sphinx
Recommends:     python-matplotlib
Recommends:     python-scipy
Recommends:     python-sphinx_rtd_theme
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module jupyter_ipykernel}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module jupyter_nbconvert}
BuildRequires:  %{python_module jupyter_nbformat}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Pweave is a scientific report generator and a literate programming
tool for Python. Pweave can capture the results and plots from data
analysis and works well with NumPy, SciPy and matplotlib. It is able
to run python code from source document and include the results and
capture matplotlib plots in the output.

Pweave is good for creating reports, tutorials, presentations etc.
with embedded python code It can also be used to make websites together
with e.g. Sphinx or rest2web.

%prep
%setup -q -n Pweave-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests.test_readers.test_url - online
# Formatters/publish Layout changes with updates in jupyter
%pytest -k 'not (test_url or testFormatters or test_publish)'

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{_bindir}/pweave
%{_bindir}/ptangle
%{_bindir}/pypublish
%{_bindir}/pweave-convert
%{python_sitelib}/*

%changelog
