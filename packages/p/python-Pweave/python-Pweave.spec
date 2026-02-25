#
# spec file for package python-Pweave
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-Pweave
Version:        0.30.3
Release:        0
Summary:        Scientific reports with embedded python computations
License:        BSD-3-Clause
URL:            https://github.com/mpastell/Pweave
Source:         https://files.pythonhosted.org/packages/source/P/Pweave/Pweave-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/mpastell/Pweave/pull/167 Adjust for API changes in Python-Markdown 3.0
Patch0:         markdown.patch
# PATCH-FIX-OPENSUSE Replace use of IPythonInputSplitter with TransformerManager
Patch1:         support-ipython-9.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown
Requires:       python-Pygments
Requires:       python-ipykernel
Requires:       python-ipython
Requires:       python-jupyter_client
Requires:       python-nbconvert
Requires:       python-nbformat
Recommends:     python-Sphinx
Recommends:     python-matplotlib
Recommends:     python-scipy
Recommends:     python-sphinx_rtd_theme
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%autosetup -p1 -n Pweave-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pweave
%python_clone -a %{buildroot}%{_bindir}/ptangle
%python_clone -a %{buildroot}%{_bindir}/pypublish
%python_clone -a %{buildroot}%{_bindir}/pweave-convert

%post
%python_install_alternative pweave
%python_install_alternative ptangle
%python_install_alternative pypublish
%python_install_alternative pweave-convert

%postun
%python_uninstall_alternative pweave
%python_uninstall_alternative ptangle
%python_uninstall_alternative pypublish
%python_uninstall_alternative pweave-convert

%check
# tests.test_readers.test_url - online
# Formatters/publish Layout changes with updates in jupyter
# Failing test for testFIR_FilterExampleTex is gh#mpastell/Pweave#168
%pytest -k 'not (test_url or testFormatters or test_publish or testFIR_FilterExampleTex)'

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/pweave
%python_alternative %{_bindir}/ptangle
%python_alternative %{_bindir}/pypublish
%python_alternative %{_bindir}/pweave-convert
%{python_sitelib}/pweave
%{python_sitelib}/[Pp]weave-%{version}.dist-info

%changelog
