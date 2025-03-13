#
# spec file for package python-spyder-notebook
#
# Copyright (c) 2025 SUSE LLC
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


%define pythons python3
Name:           python-spyder-notebook
Version:        0.6.1
Release:        0
Summary:        Jupyter notebook integration with Spyder
License:        MIT
URL:            https://github.com/spyder-ide/spyder-notebook
Source:         https://files.pythonhosted.org/packages/source/s/spyder-notebook/spyder_notebook-%{version}.tar.gz
Source1:        https://github.com/spyder-ide/spyder-notebook/raw/v%{version}/spyder_notebook/widgets/tests/test.ipynb
# PATCH-FIX-UPSTREAM gh#spyder-ide/spyder-notebook#481
Patch0:         support-python-312.patch
# TODO: use local-npm-registry
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-QDarkStyle
Requires:       python-QtPy
Requires:       python-nbformat
Requires:       python-notebook >= 7
Requires:       python-requests
Requires:       python-tornado
Requires:       python-traitlets
Requires:       (python-spyder >= 6 with python-spyder < 7)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module PyQt6-WebEngine}
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module QDarkStyle}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module notebook >= 7.2 with %python-notebook < 8}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module spyder >= 6 with %python-spyder < 7}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module traitlets}
# /SECTION
%python_subpackages

%description
Spyder plugin to use Jupyter notebooks inside Spyder. Currently it supports
basic functionality such as creating new notebooks, opening any notebook in
your filesystem and saving notebooks at any location.

You can also use Spyder's file switcher to easily switch between notebooks and
open an IPython console connected to the kernel of a notebook to inspect its
variables in the Variable Explorer.

%prep
%autosetup -p1 -n spyder_notebook-%{version}
cp %{SOURCE1} spyder_notebook/widgets/tests/
chmod -x spyder_notebook/utils/templates/welcome-dark.html

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_find_lang spyder_notebook

%check
export PYTEST_QT_API=pyqt6
%pytest -k "not test_config_dialog"

%files %{python_files} -f %{python_prefix}-spyder_notebook.lang
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/spyder_notebook
%{python_sitelib}/spyder_notebook-%{version}.dist-info

%changelog
