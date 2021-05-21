#
# spec file for package python-spyder-kernels
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
%define skip_python2 1
%define skip_python36 1
Name:           python-spyder-kernels
Version:        2.0.3
Release:        0
Summary:        Jupyter kernels for Spyder's console
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-kernels
# PyPI tarballs do not include the tests: https://github.com/spyder-ide/spyder-kernels/issues/66
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module dask-distributed}
BuildRequires:  %{python_module decorator < 5}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel >= 5.3.0}
BuildRequires:  %{python_module ipython >= 7.6.0}
BuildRequires:  %{python_module jupyter_client >= 5.3.4}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module wurlitzer >= 1.0.3}
BuildRequires:  %{python_module xarray}
# /SECTION
Requires:       python-cloudpickle
Requires:       python-decorator < 5
Requires:       python-ipykernel >= 5.3.0
Requires:       python-ipython >= 7.6.0
Requires:       python-jupyter_client >= 5.3.4
Requires:       python-pyzmq >= 17
Requires:       python-wurlitzer >= 1.0.3
BuildArch:      noarch

%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package provides Jupyter kernels for use with the consoles
of Spyder. These can launched either through Spyder itself or
in an independent Python session, and allow for interactive or
file-based execution of Python code in different environments,
all inside the IDE.

%prep
%setup -q -n spyder-kernels-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# flaky for obs
donttest="test_dask_multiprocessing"

%pytest -k "not (${donttest})" -ra

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/spyder_kernels
%{python_sitelib}/spyder_kernels-%{version}*-info

%changelog
