#
# spec file for package python-ijson
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


%bcond_without ijson_testsuite

%{?sle15_python_module_pythons}
Name:           python-ijson
Version:        3.4.0.post0
Release:        0
Summary:        Iterative JSON parser with a standard Python iterator interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ICRAR/ijson
Source:         https://files.pythonhosted.org/packages/source/i/ijson/ijson-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%if %{with ijson_testsuite}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
%endif
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-asyncio
BuildRequires:  pkgconfig(yajl)
%python_subpackages

%description
Iterative JSON parser with a standard Python iterator interface.

%prep
%setup -q -n ijson-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with ijson_testsuite}
%check
%pytest_arch -v
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/ijson
%{python_sitearch}/ijson-%{version}*-info

%changelog
