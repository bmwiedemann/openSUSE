#
# spec file for package python-spyder-kernels
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.5.1
Release:        0
Summary:        Jupyter kernels for Spyder's console
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/spyder-ide/spyder-kernels
# PyPI tarballs do not include the tests: https://github.com/spyder-ide/spyder-kernels/issues/66
Source:         https://github.com/spyder-ide/spyder-kernels/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/spyder-ide/spyder-kernels/commit/5496e4596dabda05d8583e2533fcdb14ebde2c9c.patch#/fix-tests-pandas.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module ipykernel >= 4.8.2}
BuildRequires:  %{python_module jupyter_client >= 5.2.3}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module wurlitzer}
BuildRequires:  %{python_module xarray}
BuildRequires:  python-futures
# /SECTION
Requires:       python-cloudpickle
Requires:       python-ipykernel >= 4.8.2
Requires:       python-jupyter_client >= 5.2.3
Requires:       python-pyzmq >= 17
Requires:       python-wurlitzer
%ifpython2
Requires:       python-futures
%endif
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
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rf _build.python*
rm -rf build
%python_expand pytest-%{$python_bin_suffix}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
