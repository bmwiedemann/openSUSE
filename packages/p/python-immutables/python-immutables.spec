#
# spec file for package python-immutables
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
Name:           python-immutables
Version:        0.21
Release:        0
Summary:        Immutable collections for Python
License:        Apache-2.0
URL:            https://github.com/MagicStack/immutables
Source:         https://files.pythonhosted.org/packages/source/i/immutables/immutables-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Immutable collections for Python.

%prep
%autosetup -p1 -n immutables-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export IMMU_SKIP_MYPY_TESTS=1
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/immutables
%{python_sitearch}/immutables-%{version}.dist-info

%changelog
