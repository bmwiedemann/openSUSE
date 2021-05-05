#
# spec file for package python-mpld3
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


# No numpy for py3.6
%define skip_python36 1
%define modname mpld3
# Tests are not designed to be non-interactively run, see README.md
%bcond_with     test
Name:           python-mpld3
Version:        0.5.2
Release:        0
Summary:        D3 Viewer for Matplotlib
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://mpld3.github.com
Source:         https://files.pythonhosted.org/packages/source/m/mpld3/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2 >= 2.7}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module matplotlib >= 2.2}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.7
Requires:       python-matplotlib >= 2.2
Requires:       python-pandas
Recommends:     jupyter-notebook
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module diffimg}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
%endif
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
%setup -q -n mpld3-%{version}

# Fix a bunch of inappropriate exec perms
chmod a-x notebooks/*.ipynb \
          LICENSE \
          *.md \
          mpld3/js/*.js \
          mpld3.egg-info/*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export HIDE_PLOTS=True
%python_expand nosetests-%{$python_bin_suffix} mpld3/tests/*.py
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS.md README.md
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%files -n %{name}-doc
%doc examples/ notebooks/

%changelog
