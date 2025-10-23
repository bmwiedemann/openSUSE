#
# spec file for package python-frozenlist
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
Name:           python-frozenlist
Version:        1.8.0
Release:        0
Summary:        Python list-like structure which implements MutableSequence
License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
Source:         https://files.pythonhosted.org/packages/source/f/frozenlist/frozenlist-%{version}.tar.gz
Patch1:         no-pytest-cov.patch
# PATCH-FIX-OPENSUSE - avoid embedding random tmp dir in .so
Patch2:         reproducible.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module expandvars}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python list-like structure which implements collections.abc.MutableSequence.

%prep
%autosetup -p1 -n frozenlist-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/frozenlist
%{python_sitearch}/frozenlist-%{version}*-info

%changelog
