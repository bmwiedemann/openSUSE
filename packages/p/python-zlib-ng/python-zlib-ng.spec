#
# spec file for package python-zlib-ng
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-zlib-ng%{psuffix}
Version:        0.5.1
Release:        0
License:        Python-2.0
Summary:        Faster zlib and gzip compatible compression and decompression
Group:          Development/Languages/Python
URL:            https://github.com/pycompression/python-zlib-ng
Source0:        https://files.pythonhosted.org/packages/source/z/zlib-ng/zlib_ng-%{version}.tar.gz
Source1:        https://github.com/pycompression/python-zlib-ng/archive/refs/tags/v%{version}.tar.gz#/zlib-ng-%{version}-gh.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioningit}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-ng-devel
Provides:       python-zlib_ng = %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module zlib-ng = %{version}}
%endif
%python_subpackages

%description
Faster zlib and gzip compatible compression and decompression by providing Python bindings for the zlib-ng library.

This package provides Python bindings for the zlib-ng library.

%prep
%setup -q -a1 -n zlib_ng-%{version}

%build
%if !%{with test}
export PYTHON_ZLIB_NG_LINK_DYNAMIC=1
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%pytest_arch
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/zlib_ng
%{python_sitearch}/zlib_ng-%{version}.dist-info
%endif

%changelog
