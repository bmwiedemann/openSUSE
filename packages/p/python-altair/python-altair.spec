#
# spec file for package python-altair
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


Name:           python-altair
Version:        5.1.2
Release:        0
Summary:        Declarative statistical visualization library for Python
License:        BSD-3-Clause
URL:            https://github.com/altair-viz/altair
Source:         https://github.com/altair-viz/altair/archive/refs/tags/v%{version}.tar.gz#/altair-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module anywidget}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
##BuildRequires:  %%{python_module vl-convert-python}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module vega_datasets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-jsonschema
Requires:       python-numpy
Requires:       python-packaging
Requires:       python-pandas
Requires:       python-toolz
Requires:       python-typing-extensions
Recommends:     python-jupyter_ipython
Recommends:     python-pyarrow
Recommends:     python-vega_datasets
##Recommends:     python-vl-convert-python
BuildArch:      noarch
%python_subpackages

%description
This package provides a Python API for building statistical visualizations
in a declarative manner. This API contains no actual visualization rendering
code, but instead emits JSON data structures following the `Vega-Lite`_
specification. For convenience, Altair can optionally use `ipyvega`_ to
seamlessly display client-side renderings in the Jupyter notebook.

%prep
%setup -q -n altair-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# disable tests that require network
# vega requires vl-convert-python, not packaged
%pytest -k 'not (test_examples or test_vegalite_compiler or with_format_vega)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/altair/
%{python_sitelib}/altair-%{version}.dist-info/

%changelog
