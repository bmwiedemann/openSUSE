#
# spec file for package python-zstandard
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
Name:           python-zstandard
Version:        0.25.0
Release:        0
Summary:        Zstandard bindings for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/indygreg/python-zstandard
Source:         https://files.pythonhosted.org/packages/source/z/zstandard/zstandard-%{version}.tar.gz
Patch0:         feature-detection.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libzstd-devel >= 1.5.6
BuildRequires:  python-rpm-macros
Requires:       libzstd1 >= 1.5.6
%if 0%{?python_version_nodots} >= 314
Requires:       python-cffi >= 2.0.0
%else
Requires:       python-cffi >= 1.17
%endif
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 2.0.0}
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Zstandard bindings for Python

%prep
%autosetup -p1 -n zstandard-%{version}

%build
export CFLAGS="%{optflags}"
%define py_setup_args "--system-zstd"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# remove srcdir for tests collection of installed lib
mv zstandard zstandard.moved
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/zstandard
%{python_sitearch}/zstandard-%{version}*-info

%changelog
