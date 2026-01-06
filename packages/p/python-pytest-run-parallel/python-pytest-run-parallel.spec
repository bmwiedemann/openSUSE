#
# spec file for package python-pytest-run-parallel
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pytest-run-parallel
Version:        0.8.1
Release:        0
Summary:        A simple pytest plugin to run tests concurrently
License:        MIT
URL:            https://github.com/Quansight-Labs/pytest-run-parallel
Source:         https://files.pythonhosted.org/packages/source/p/pytest-run-parallel/pytest_run_parallel-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.4.0}
BuildRequires:  %{python_module pytest-order}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module hypothesis}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 8.4.0
Suggests:       python-psutil >= 6.1.1
BuildArch:      noarch
%python_subpackages

%description
A simple pytest plugin to run tests concurrently

%prep
%autosetup -p1 -n pytest_run_parallel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_run_parallel
%{python_sitelib}/pytest_run_parallel-%{version}.dist-info

%changelog
