#
# spec file for package python-fuse
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-fuse%{psuffix}
Version:        1.0.9
Release:        0
Summary:        Python bindings for FUSE
License:        LGPL-2.1-only
URL:            https://github.com/libfuse/python-fuse
Source0:        https://github.com/libfuse/python-fuse/archive/v%{version}.tar.gz#/python-fuse-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module fuse = %{version}}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  fdupes
BuildRequires:  fuse-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for FUSE (User space File System)

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/Other

%description -n %{name}-doc
HTML Documentation and examples for %name.

%prep
%autosetup -p1 -n python-fuse-%{version}

%build
%if %{without test}
export CFLAGS="%{optflags}"
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
# gh#libfuse/python-fuse#94
%pytest tests -k 'not test_fioc'
%endif

%if %{without test}
%files %{python_files}
%license COPYING
%{python_sitearch}/fuse.py
%pycache_only %{python_sitearch}/__pycache__/fuse*.py*
%{python_sitearch}/fuseparts
%{python_sitearch}/fuse_python-%{version}.dist-info

%files -n %{name}-doc
%doc README.* FAQ AUTHORS example
%endif

%changelog
