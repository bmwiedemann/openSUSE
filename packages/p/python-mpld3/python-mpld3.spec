#
# spec file for package python-mpld3
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


Name:           python-mpld3
Version:        0.5.9
Release:        0
Summary:        D3 Viewer for Matplotlib
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://mpld3.github.io
# SourceRepository: https://github.com/mpld3/mpld3
Source0:        https://files.pythonhosted.org/packages/source/m/mpld3/mpld3-%{version}.tar.gz
Source1:        https://github.com/mpld3/mpld3/raw/v%{version}/visualize_tests.py
# PATCH-FIX-UPSTREAM mpld3-pr516-dasharray.patch gh#mpld3/mpld3#516
Patch1:         mpld3-pr516-dasharray.patch
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-matplotlib
Recommends:     jupyter-notebook
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module diffimg}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is an interactive D3js-based viewer which brings matplotlib graphics to the browser.
Please visit http://mpld3.github.io for documentation and examples.

mpld3 provides a custom stand-alone javascript library built on D3, which
parses JSON representations of plots.  The mpld3 python module provides a
set of routines which parses matplotlib plots (using the mplexporter
framework) and outputs the JSON description readable by mpld3.js.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Python
Recommends:     python3-jupyter_ipython >= 2.0
Provides:       %{python_module %{name} = %{version}}

%description -n %{name}-doc
Documentation and examples for %{name}

%prep
%autosetup -p1 -n mpld3-%{version}
cp %{SOURCE1} .

# Fix a bunch of inappropriate exec perms
chmod a-x notebooks/*.ipynb \
          LICENSE \
          *.md \
          mpld3/js/*.js \
          examples/*.py \
          mpld3.egg-info/*

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export HIDE_PLOTS=True
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.md README.md
%{python_sitelib}/mpld3/
%{python_sitelib}/mpld3-%{version}.dist-info

%files -n %{name}-doc
%doc examples/ notebooks/

%changelog
