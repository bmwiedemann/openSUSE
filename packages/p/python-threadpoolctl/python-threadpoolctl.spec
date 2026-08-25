#
# spec file for package python-threadpoolctl
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
Name:           python-threadpoolctl
Version:        3.6.0
Release:        0
Summary:        Thread-pool Controls
License:        BSD-3-Clause
URL:            https://github.com/joblib/threadpoolctl
Source:         %{url}/archive/%{version}.tar.gz#/threadpoolctl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#joblib/threadpoolctl#226
Patch0:         support-flit-core-4.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python helpers to limit the number of threads used in native
libraries that handle their own internal threadpool (BLAS
and OpenMP implementations).

%prep
%autosetup -p1 -n threadpoolctl-%{version}

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
%pycache_only %{python_sitelib}/__pycache__/threadpoolctl.*.pyc
%{python_sitelib}/threadpoolctl-%{version}.dist-info

%changelog
