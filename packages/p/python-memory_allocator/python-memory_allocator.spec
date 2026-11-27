#
# spec file for package python-memory_allocator
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


Name:           python-memory_allocator
Version:        0.2.1
Release:        0
Summary:        An extension class to allocate memory easily with cython
License:        GPL-3.0-or-later
URL:            https://github.com/sagemath/memory_allocator
Source:         https://files.pythonhosted.org/packages/source/m/memory_allocator/memory_allocator-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Cython >= 3.0}
BuildRequires:  %{python_module meson-python >= 0.15.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  binutils
%python_subpackages

%description
# MemoryAllocator
An extension class to allocate memory easily with cython.

This extension class started as part of the [Sage](https://sagemath.org) software.

%prep
%autosetup -p1 -n memory_allocator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand strip %{buildroot}%{$python_sitearch}/memory_allocator/*.so

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test.py

%files %{python_files}
%doc AUTHORS README.md
%license LICENSE
%{python_sitearch}/memory_allocator
%{python_sitearch}/memory_allocator-%{version}.dist-info

%changelog
