#
# spec file for package python-cPyparsing
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


Name:           python-cPyparsing
Version:        2.4.7.2.4.3
Release:        0
Summary:        Cython implementation of PyParsing
License:        Apache-2.0
URL:            https://github.com/evhub/cpyparsing
Source:         https://files.pythonhosted.org/packages/source/c/cPyparsing/cpyparsing-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Cython implementation of PyParsing created for use in Coconut and Undebt.

%prep
%setup -q -n cpyparsing-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python ./tests/cPyparsing_test.py

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/cPyparsing.cpython-*-*-linux-gnu.so
%{python_sitearch}/cpyparsing-%{version}.dist-info

%changelog
