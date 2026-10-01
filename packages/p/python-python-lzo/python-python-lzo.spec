#
# spec file for package python-python-lzo
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


%{?sle15_python_module_pythons}
Name:           python-python-lzo
Version:        1.15
Release:        0
Summary:        Python bindings for the LZO data compression library
License:        GPL-2.0-only
URL:            https://github.com/jd-boyd/python-lzo
Source:         https://files.pythonhosted.org/packages/source/p/python-lzo/python-lzo-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#jd-boyd/python-lzo#78
Patch0:         support-python-312.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  lzo-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module provides Python bindings for the LZO data compression library.

LZO is a lossless data compression library. Decompression requires no
memory. Different compression levels can be used to achieve better
ratios at the expense of time.

%prep
%autosetup -p1 -n python-lzo-%{version}
dos2unix NEWS

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests

%files %{python_files}
%doc NEWS
%license COPYING
%{python_sitearch}/lzo.*so
%{python_sitearch}/python_lzo-%{version}.dist-info

%changelog
