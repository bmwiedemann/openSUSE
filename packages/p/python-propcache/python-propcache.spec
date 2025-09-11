#
# spec file for package python-propcache
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-propcache
Version:        0.3.2
Release:        0
Summary:        Accelerated property cache
License:        Apache-2.0
URL:            https://github.com/aio-libs/propcache
Source:         https://files.pythonhosted.org/packages/source/p/propcache/propcache-%{version}.tar.gz
Patch0:         reproducible.patch
# PATCH-FIX-UPSTREAM https://github.com/aio-libs/propcache/commit/b97e7e37cbe8329e2a4d8383166c094f471a0d6a Test on Python 3.14
Patch1:         py314.patch
BuildRequires:  %{python_module Cython >= 3.0.11}
BuildRequires:  %{python_module covdefaults}
BuildRequires:  %{python_module expandvars}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 47}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Accelerated property cache

%prep
%autosetup -p1 -n propcache-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
find %{_builddir} -name ".gitignore" -delete
find %{_builddir} -name ".TEMPLATE.rst" -delete
}

%check
%pytest_arch

%files %{python_files}
%doc CHANGES CHANGES.rst CHANGES/README.rst README.rst
%license LICENSE
%{python_sitearch}/propcache
%{python_sitearch}/propcache-%{version}.dist-info

%changelog
