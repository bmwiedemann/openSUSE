#
# spec file for package python-immutables
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-immutables
Version:        0.19
Release:        0
Summary:        Immutable collections for Python
License:        Apache-2.0
URL:            https://github.com/MagicStack/immutables
Source:         https://files.pythonhosted.org/packages/source/i/immutables/immutables-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.3 if %python-base < 3.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %python_version_nodots < 38
Requires:       python-typing-extensions >= 3.7.4.3
%endif
%python_subpackages

%description
Immutable collections for Python.

%prep
%autosetup -p1 -n immutables-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitearch}/immutables/*.[ch]
%fdupes %{buildroot}%{$python_sitearch}
}

%check
export IMMU_SKIP_MYPY_TESTS=1
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/immutables
%{python_sitearch}/immutables-%{version}*-info

%changelog
