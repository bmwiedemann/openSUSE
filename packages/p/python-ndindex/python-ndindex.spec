#
# spec file for package python-ndindex
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-ndindex
Version:        1.9.2
Release:        0
Summary:        A Python library for manipulating indices of ndarrays
License:        MIT
URL:            https://quansight-labs.github.io/ndindex/
Source:         https://files.pythonhosted.org/packages/source/n/ndindex/ndindex-%{version}.tar.gz
# PATCH-FIX-OPENSUSE custom-pytest.patch gh#Quansight-Labs/ndindex#150
Patch2:         custom-pytest.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base > 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sympy}
# /SECTION
%python_subpackages

%description
A Python library for manipulating indices of ndarrays.

%prep
%autosetup -p1 -n ndindex-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%ifarch %{ix86}
# flaky on 32bit
donttest=("-k" "not test_as_subindex_hypothesis")
%endif
# Remove from import path
mv ndindex noimport-ndindex
%pytest_arch --hypothesis-profile=obs --pyargs ndindex.tests "${donttest[@]}"
mv noimport-ndindex ndindex

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/ndindex
%{python_sitearch}/ndindex-%{version}.dist-info

%changelog
