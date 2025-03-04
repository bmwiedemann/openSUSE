#
# spec file for package python-pytest-mpi
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


%if 0%{?sle_version} && 0%{?sle_version} < 150300
  %define mpiver openmpi
%else
  %define mpiver openmpi4
%endif

%define modname pytest_mpi
Name:           python-pytest-mpi
Version:        0.6
Release:        0
Summary:        MPI plugin for pytest
License:        BSD-3-Clause
URL:            https://pytest-mpi.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mpi/pytest-mpi-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Recommends:     python-mpi4py
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  openmpi-macros-devel
BuildRequires:  %{mpiver}
BuildRequires:  %{python_module mpi4py}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil >= 3}
# /SECTION
%python_subpackages

%description
mpi plugin for pytest to collect information from openmpi-based tests.

%prep
%autosetup -p1 -n pytest-mpi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Exclude test_fixtures, it fails for i586 arch with Segmentation fault
donttest="test_fixtures"
%if "%{_arch}" == "s390x"
# Exclude some test_mpi_ that fails for s390x arch with Segmentation fault
donttest+=" or test_mpi_with_mpi or test_mpi_only_mpi or test_mpi_skip_under_mpi or test_mpi_xfail or test_mpi_xfail_under_mpi"
%endif
%setup_openmpi
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./ py%{$python_version_nodots}.XXX)
$python -m pytest -v -p pytester --runpytest=subprocess -k "not ($donttest)"
rm -fr ${PYTEST_DEBUG_TEMPROOT}
}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*.*-info/

%changelog
