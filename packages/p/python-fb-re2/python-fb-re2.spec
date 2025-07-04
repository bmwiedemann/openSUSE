#
# spec file for package python-fb-re2
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
Name:           python-fb-re2
Version:        1.0.7
Release:        0
Summary:        Python wrapper for Google's RE2
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/facebook/pyre2
Source:         https://github.com/facebook/pyre2/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM cpp17.patch gh#facebook/pyre2#25
Patch0:         cpp17.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  re2-devel
%python_subpackages

%description
Python wrapper for Google's RE2

%prep
%autosetup -p1 -n pyre2-%{version}
# fix tests on py312
sed -i 's/assertRaisesRegexp/assertRaisesRegex/g' tests/test_match.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/_re2*.so
%{python_sitearch}/re2.py
%{python_sitearch}/fb_re2-%{version}*-info
%pycache_only %{python_sitearch}/__pycache__

%changelog
