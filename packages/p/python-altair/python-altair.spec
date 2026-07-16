#
# spec file for package python-altair
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
Name:           python-altair
Version:        6.2.2
Release:        0
Summary:        Declarative statistical visualization library for Python
License:        BSD-3-Clause
URL:            https://github.com/altair-viz/altair
Source:         https://github.com/altair-viz/altair/archive/refs/tags/v%{version}.tar.gz#/altair-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module anywidget}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jsonschema >= 3}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module narwhals >= 2.4.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas >= 1.1.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module versioningit}
##BuildRequires:  %%{python_module vl-convert-python}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module typing-extensions >= 4.12 if %python-base < 3.15}
BuildRequires:  %{python_module vega_datasets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-jsonschema >= 3
Requires:       python-narwhals >= 2.4.0
Requires:       python-packaging
%if 0%{?python_version_nodots} < 315
Requires:       python-typing-extensions >= 4.12
%endif
Recommends:     python-jupyter_ipython
Recommends:     python-numpy
Recommends:     python-pandas >= 1.1.3
Recommends:     python-pyarrow
Recommends:     python-toolz
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
ignore="--ignore tests/test_datasets.py --ignore altair/datasets/_data.py"
donttest="test_examples or test_to_url or test_theme_remote_lambda"
# vega requires vl-convert-python, not packaged
# ... or polars, also not packaged
ignore+=" --ignore tests/test_toplevel.py"
ignore+=" --ignore tests/utils/test_data.py"
ignore+=" --ignore tests/utils/test_schemapi.py"
ignore+=" --ignore tests/vegalite/v6/test_api.py"
%pytest $ignore -k "not ($donttest ${$python_donttest})" tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/altair/
%{python_sitelib}/altair-%{version}.dist-info/

%changelog
