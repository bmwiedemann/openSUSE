#
# spec file for package python-lazy-object-proxy
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-lazy-object-proxy%{psuffix}
Version:        1.10.0
Release:        0
Summary:        Rebuild a new abstract syntax tree from Python's ast
License:        BSD-2-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/ionelmc/python-lazy-object-proxy
Source:         https://files.pythonhosted.org/packages/source/l/lazy-object-proxy/lazy-object-proxy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      python-lazy_object_proxy < %{version}-%{release}
Provides:       python-lazy_object_proxy = %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module lazy-object-proxy = %{version}}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A fast and thorough lazy object proxy that rebuilds a new abstract syntax tree
from Python's ast

%prep
%setup -q -n lazy-object-proxy-%{version}

%build
%if !%{with test}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%pytest tests
%endif

%if !%{with test}
%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst docs
%license LICENSE
%{python_sitearch}/lazy_object_proxy
%{python_sitearch}/lazy_object_proxy-%{version}*-info
%endif

%changelog
