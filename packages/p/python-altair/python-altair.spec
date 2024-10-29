#
# spec file for package python-altair
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-altair
Version:        5.2.0
Release:        0
Summary:        Declarative statistical visualization library for Python
License:        BSD-3-Clause
URL:            https://github.com/altair-viz/altair
Source:         https://github.com/altair-viz/altair/archive/refs/tags/v%{version}.tar.gz#/altair-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module anywidget if %python-base >= 3.10}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jsonschema >= 3}
BuildRequires:  %{python_module jupyter_ipython if %python-base >= 3.10}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
##BuildRequires:  %%{python_module vl-convert-python}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module typing-extensions if %python-base < 3.11}
BuildRequires:  %{python_module vega_datasets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-jsonschema >= 3
Requires:       python-numpy
Requires:       python-packaging
Requires:       python-pandas >= 0.25
Requires:       python-toolz
%if 0%{?python_version_nodots} < 311
Requires:       python-typing-extensions
%endif
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
donttest="test_examples or test_to_url"
# vega requires vl-convert-python, not packaged
donttest="$donttest or test_vegalite_compiler or with_format_vega"
# anywidget and jupyter_ipython not available anymore in python39
python39_ignore="--ignore tests/test_jupyter_chart.py"
python39_donttest=" or test_check_renderer_options or test_display_options"
%pytest -k "not ($donttest ${$python_donttest})" ${$python_ignore}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/altair/
%{python_sitelib}/altair-%{version}.dist-info/

%changelog
