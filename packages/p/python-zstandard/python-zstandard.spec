#
# spec file for package python-zstandard
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


%{?sle15_python_module_pythons}
Name:           python-zstandard
Version:        0.22.0
Release:        0
Summary:        Zstandard bindings for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/indygreg/python-zstandard
Source:         https://files.pythonhosted.org/packages/source/z/zstandard/zstandard-%{version}.tar.gz
Patch0:         feature-detection.patch
Patch1:         fix-zstd-1.5.7.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libzstd-devel = 1.5.7
BuildRequires:  python-rpm-macros
Requires:       libzstd1 = 1.5.7
Requires:       python-cffi >= 1.11
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.11}
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
%python_build --system-zstd

%install
%python_install
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
