#
# spec file for package python-sphinx-book-theme
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
%define modname sphinx-book-theme
Name:           python-sphinx-book-theme
Version:        0.1.3
Release:        0
Summary:        Jupyter Book: Create an online book with Jupyter Notebooks
License:        BSD-3-Clause
URL:            https://github.com/executablebooks/sphinx-book-theme
Source0:        https://files.pythonhosted.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz
Source98:       python-sphinx-book-theme-rpmlintrc
Source99:       add_lang_files.lua
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4 >= 4.6.1
Requires:       python-click
Requires:       python-docutils >= 0.15
Requires:       python-pydata-sphinx-theme
Requires:       python-PyYAML
Requires:       python-Sphinx >= 2
Suggests:       python-ablog
Suggests:       python-coverage
Suggests:       python-folium
Suggests:       python-importlib-resources >= 3.0
Suggests:       python-ipywidgets
Suggests:       python-matplotlib
Suggests:       python-myst-nb
Suggests:       python-myst_nb
Suggests:       python-nbclient
Suggests:       python-numpy
Suggests:       python-pandas
Suggests:       python-plotly
Suggests:       python-pre-commit
Suggests:       python-pytest
Suggests:       python-pytest-cov
Suggests:       python-pytest-regressions
Suggests:       python-sphinx-autobuild
Suggests:       python-sphinx-copybutton
Suggests:       python-sphinx-design
Suggests:       python-sphinx-thebe
Suggests:       python-sphinx-togglebutton >= 0.2.1
Suggests:       python-sphinx_thebe
Suggests:       python-sphinxcontrib-bibtex
Suggests:       python-sphinxext-opengraph
Suggests:       python-web-compile
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4 >= 4.6.1}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module docutils >= 0.15}
BuildRequires:  %{python_module pydata-sphinx-theme >= 0.6.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx >= 2}
# /SECTION
%python_subpackages

%description
Jupyter Book: Create an online book with Jupyter Notebooks

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/sphinx_book_theme*

%changelog
