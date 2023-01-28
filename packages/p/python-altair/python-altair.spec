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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-altair
Version:        4.2.2
Release:        0
Summary:        Declarative statistical visualization library for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/altair-viz/altair
Source:         https://files.pythonhosted.org/packages/source/a/altair/altair-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module vega_datasets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-entrypoints
Requires:       python-jsonschema
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-toolz
Requires:       python-typing
Recommends:     python-jupyter_ipython
Recommends:     python-vega_datasets
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# disable tests that require network
%pytest altair -k 'not test_examples'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/altair/
%{python_sitelib}/altair-%{version}*-info/

%changelog
