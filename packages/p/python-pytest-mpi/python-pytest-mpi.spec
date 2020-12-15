#
# spec file for package python-pytest-mpi
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


%define modname pytest_mpi
# Module supports only python3
%define skip_python2 1
Name:           python-pytest-mpi
Version:        0.4
Release:        0
Summary:        MPI plugin for pytest
License:        BSD-3-Clause
URL:            https://pytest-mpi.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mpi/pytest-mpi-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-sybil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mpi4py}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil}
BuildRequires:  openmpi2
# /SECTION
%python_subpackages

%description
mpi plugin for pytest to collect information from openmpi-based tests.

%prep
%setup -q -n pytest-mpi-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=${PATH}:%{_libdir}/mpi/gcc/openmpi2/bin
source %{_libdir}/mpi/gcc/openmpi2/bin/mpivars.sh
# include `-p pytester` as pytester needs to be manually activated (see https://pytest-mpi.readthedocs.io/en/latest/contributing.html)
# Also see gh#aragilar/pytest-mpi#14 for two failing tests disabled here
%pytest -v -p pytester -k 'not test_mpi_with_mpi and not test_mpi_only_mpi'

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
