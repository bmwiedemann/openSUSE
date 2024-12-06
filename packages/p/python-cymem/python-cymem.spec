#
# spec file for package python-cymem
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
Name:           python-cymem
Version:        2.0.10
Release:        0
Summary:        Manage calls to calloc/free through Cython
License:        MIT
URL:            https://github.com/explosion/cymem
Source:         https://files.pythonhosted.org/packages/source/c/cymem/cymem-%{version}.tar.gz
BuildRequires:  %{python_module Cython3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
# cymem: A Cython Memory Helper

cymem provides two small memory-management helpers for Cython. They make it
easy to tie memory to a Python object's life-cycle, so that the memory is freed
when the object is garbage collected.

## Overview

The most useful is `cymem.Pool`, which acts as a thin wrapper around the calloc
function:

```python
from cymem.cymem cimport Pool
cdef Pool mem = Pool()
data1 = <int*>mem.alloc(10, sizeof(int))
data2 = <float*>mem.alloc(12, sizeof(float))
```

The `Pool` object saves the memory addresses internally, and frees them when the
object is garbage collected. Typically you'll attach the `Pool` to some cdef'd
class. This is particularly handy for deeply nested structs, which have
complicated initialization functions. Just pass the `Pool` object into the
initializer, and you don't have to worry about freeing your struct at all —
all of the calls to `Pool.alloc` will be automatically freed when the `Pool`
expires.

%prep
%autosetup -p1 -n cymem-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/cymem
%{python_sitearch}/cymem-%{version}.dist-info

%changelog
