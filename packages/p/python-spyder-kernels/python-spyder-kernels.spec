#
# spec file for package python-spyder-kernels
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


# flaky for obs, only test locally
%bcond_with dasktest
Name:           python-spyder-kernels
Version:        2.4.1
Release:        0
Summary:        Jupyter kernels for Spyder's console
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-kernels
# PyPI tarballs do not include the tests: https://github.com/spyder-ide/spyder-kernels/issues/66
Source:         https://github.com/spyder-ide/spyder-kernels/archive/v%{version}.tar.gz#/spyder-kernels-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel >= 6.16.1 with %python-ipykernel < 7}
BuildRequires:  %{python_module ipython >= 7.31.1 with %python-ipython < 9}
BuildRequires:  %{python_module jupyter_client >= 7.3.4 with %python-jupyter_client < 8}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 22.1}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module wurlitzer >= 1.0.3}
BuildRequires:  %{python_module xarray}
%if %{with dasktest}
BuildRequires:  %{python_module dask-distributed}
%endif
# /SECTION
Requires:       python-cloudpickle
Requires:       python-pyzmq >= 22.1
Requires:       python-wurlitzer >= 1.0.3
Requires:       (python-ipykernel >= 6.16.1 with python-ipykernel < 7)
Requires:       (python-ipython >= 7.31.1 with python-ipython < 9)
Requires:       (python-jupyter_client >= 7.3.4 with python-jupyter_client < 8)
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
%autosetup -p1 -n spyder-kernels-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if ! %{with dasktest}
donttest=("-k" "not test_dask_multiprocessing")
%endif
%pytest "${donttest[@]}"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/spyder_kernels
%{python_sitelib}/spyder_kernels-%{version}*-info

%changelog
