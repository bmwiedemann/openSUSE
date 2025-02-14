#
# spec file for package python-pylsqpack
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
Name:           python-pylsqpack
Version:        0.3.19
Release:        0
Summary:        Python ls-qpack QPACK library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aiortc/pylsqpack
Source:         https://files.pythonhosted.org/packages/source/p/pylsqpack/pylsqpack-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python wrapper for the ls-qpack QPACK library.

%prep
%setup -q -n pylsqpack-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pylsqpack
%{python_sitearch}/pylsqpack-%{version}.dist-info

%changelog
