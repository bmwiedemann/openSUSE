#
# spec file for package python-qsymm
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


%define skip_python2 1
%define skip_python36 1
%define modname qsymm
Name:           python-qsymm
Version:        1.3.0
Release:        0
Summary:        Symmetry finder and symmetric Hamiltonian generator
License:        BSD-2-Clause
URL:            https://gitlab.kwant-project.org/qt/qsymm
Source:         https://files.pythonhosted.org/packages/source/q/qsymm/qsymm-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-scipy
Requires:       python-sympy
Requires:       python-tinyarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sympy}
BuildRequires:  %{python_module tinyarray}
# /SECTION
%python_subpackages

%description
qsymm is a Python library that automatically generates model
Hamiltonians from symmetry constraints and finds the full symmetry
group of your Hamiltonian.

%prep
%setup -q -n qsymm-%{version}
sed -i -e '/pytest-runner/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# 3 tests randomply fail
# test_check_symmetry test_cont_finder test_disc_finder
%pytest -k 'not (test_check_symmetry or test_cont_finder or test_disc_finder)'

%files %{python_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
