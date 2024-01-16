#
# spec file for package python-fuse
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


%{?sle15_python_module_pythons}
Name:           python-fuse
Version:        1.0.7
Release:        0
Summary:        Python bindings for FUSE
License:        LGPL-2.1-only
URL:            https://github.com/libfuse/python-fuse
Source:         https://github.com/libfuse/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#libfuse/python-fuse#58
Patch0:         no-more-distutils.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  fuse-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for FUSE (User space File System)

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Can not figured how to do it.

%files %{python_files}
%license COPYING
%doc README.* FAQ AUTHORS
%{python_sitearch}/fuse.py
%pycache_only %{python_sitearch}/__pycache__/fuse*.py*
%{python_sitearch}/fuseparts
%{python_sitearch}/fuse_python-%{version}.dist-info

%changelog
