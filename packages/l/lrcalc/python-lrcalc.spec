#
# spec file for package python-lrcalc
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-lrcalc
Version:        2.1
Release:        0
Summary:        Python interface to the Littlewood-Richardson Calculator
License:        GPL-3.0-or-later
URL:            https://sites.math.rutgers.edu/~asbuch/lrcalc/
Source0:        https://sites.math.rutgers.edu/~asbuch/lrcalc/lrcalc-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  liblrcalc-devel = %{version}
BuildRequires:  fdupes
BuildRequires:  gcc
%python_subpackages

%description
Python interface to the Littlewood-Richardson Calculator (lrcalc).

%prep
%autosetup -p1 -n lrcalc-%{version}
sed -i "s/version='.*'/version='%{version}'/" python/setup.py

%build
cd python
%pyproject_wheel

%install
cd python
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import lrcalc; print(lrcalc.mult((2,1),(2,1)))"

%files %{python_files}
%license COPYING LICENSE
%doc README python/README.Python
%{python_sitearch}/lrcalc*.so
%{python_sitearch}/lrcalc-%{version}*-info

%changelog
