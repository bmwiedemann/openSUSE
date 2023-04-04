#
# spec file for package python-threadpoolctl
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


Name:           python-threadpoolctl
Version:        3.1.0
Release:        0
Summary:        Thread-pool Controls
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/joblib/threadpoolctl
Source:         https://files.pythonhosted.org/packages/source/t/threadpoolctl/threadpoolctl-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python helpers to limit the number of threads used in native
libraries that handle their own internal threadpool (BLAS
and OpenMP implementations).

%prep
%setup -q -n threadpoolctl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/threadpoolctl.py
%pycache_only %{python_sitelib}/__pycache__/threadpoolctl.*.py*
%{python_sitelib}/threadpoolctl-%{version}*info

%changelog
