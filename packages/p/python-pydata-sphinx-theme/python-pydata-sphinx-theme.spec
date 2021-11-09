#
# spec file for package python-pydata-sphinx-theme
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
Name:           python-pydata-sphinx-theme
Version:        0.7.1
Release:        0
Summary:        Bootstrap-based Sphinx theme from the PyData community
License:        BSD-3-Clause
URL:            https://github.com/pydata/pydata-sphinx-theme
# Source:         https://files.pythonhosted.org/packages/source/p/pydata-sphinx-theme/pydata-sphinx-theme-%%{version}.tar.gz
Source:         pydata-sphinx-theme-%{version}.tar.gz
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-beautifulsoup4
Requires:       python-docutils
Suggests:       python-beautifulsoup4
Suggests:       python-codecov
Suggests:       python-docutils
Suggests:       python-jupyter_sphinx
Suggests:       python-numpy
Suggests:       python-numpydoc
Suggests:       python-pandas
Suggests:       python-plotly
Suggests:       python-recommonmark
Suggests:       python-Sphinx
Suggests:       python-xarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
# /SECTION
%python_subpackages

%description
Bootstrap-based Sphinx theme from the PyData community

%prep
%autosetup -p1 -n pydata-sphinx-theme-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pydata_sphinx_theme*

%changelog
