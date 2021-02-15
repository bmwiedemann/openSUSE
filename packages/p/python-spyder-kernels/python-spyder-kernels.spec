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
Name:           python-spyder-kernels
Version:        1.10.1
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
# despite listed upstream (introduced by us in gh#spyder-ide/spyder-kernels#119) mock is not used anymore
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module dask-distributed}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel >= 5.1.3}
BuildRequires:  %{python_module ipython >= 7.6.0}
BuildRequires:  %{python_module jupyter_client >= 5.3.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module wurlitzer >= 1.0.3}
BuildRequires:  %{python_module matplotlib if (%python-base without python36-base)}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module pandas if (%python-base without python36-base)}
BuildRequires:  %{python_module scipy if (%python-base without python36-base)}
BuildRequires:  %{python_module xarray if (%python-base without python36-base)}
# /SECTION
Requires:       python-cloudpickle
Requires:       python-ipykernel >= 5.1.3
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
# no python36-numpy and related packages in Tumbleweed
python36_donttest=" or test_matplotlib_inline or test_umr_reload_modules"
python36_ignorefiles=" --ignore spyder_kernels/console/tests/test_console_kernel.py \
                       --ignore spyder_kernels/utils/tests/test_iofuncs.py \
                       --ignore spyder_kernels/utils/tests/test_nsview.py"

%pytest -k "not (${donttest} ${$python_donttest})" ${$python_ignorefiles} -ra

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/spyder_kernels
%{python_sitelib}/spyder_kernels-%{version}*-info

%changelog
