#
# spec file for package python-pysha3
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
%define skip_python311 1
Name:           python-pysha3
Version:        1.0.2
Release:        0
Summary:        Python SHA3 wrapper library
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/tiran/pysha3
Source:         https://files.pythonhosted.org/packages/source/p/pysha3/pysha3-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a python wrapper library for SHA-3 (keccak).

%prep
%setup -q -n pysha3-1.0.2

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# see tests.test_main
classes="SHA3_224Tests or SHA3_256Tests or SHA3_384Tests or SHA3_512Tests or\
         Shake_128Tests or Shake_256Tests or\
         Keccak_224Tests or Keccak_256Tests or Keccak_384Tests or Keccak_512Tests"
%pytest_arch -k "$classes" tests.py

%files %{python_files}
%doc CHANGES.txt README.txt
%license LICENSE
%{python_sitearch}/*

%changelog
