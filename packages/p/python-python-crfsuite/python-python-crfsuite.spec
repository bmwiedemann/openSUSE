#
# spec file for package python-python-crfsuite
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


%{?sle15_python_module_pythons}
Name:           python-python-crfsuite
Version:        0.9.11
Release:        0
Summary:        Python binding for CRFsuite
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/scrapinghub/python-crfsuite
Source:         https://files.pythonhosted.org/packages/source/p/python_crfsuite/python_crfsuite-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python-crfsuite is a python binding to CRFsuite_.

%prep
%autosetup -p1 -n python_crfsuite-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pycrfsuite bak
%pytest_arch
mv bak pycrfsuite

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitearch}/pycrfsuite
%exclude %{python_sitearch}/pycrfsuite/*.cpp
%exclude %{python_sitearch}/pycrfsuite/*.hpp
%{python_sitearch}/python_crfsuite-%{version}*-info

%changelog
