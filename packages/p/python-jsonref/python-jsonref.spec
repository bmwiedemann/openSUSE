#
# spec file for package python-jsonref
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jsonref
Version:        1.1.0
Release:        0
Summary:        An implementation of JSON Reference for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/gazpachoking/jsonref
Source:         https://files.pythonhosted.org/packages/source/j/jsonref/jsonref-%{version}.tar.gz
Patch1:         use-pdm-backend.patch
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
jsonref is a library for automatic dereferencing of JSON Reference
objects for Python (supporting 2.6+ including Python 3).

This library lets you use a data structure with JSON reference objects, as if
the references had been replaced with the referent data.

Features
* References are evaluated lazily. Nothing is dereferenced until it is used.
* Recursive references are supported, and create recursive python data
  structures.
References objects are actually replaced by lazy lookup proxy objects which are
almost completely transparent.
Complete docs can be found at http://jsonref.readthedocs.org/

%prep
%autosetup -p1 -n jsonref-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/jsonref.py
%{python_sitelib}/proxytypes.py
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/jsonref-%{version}.dist-info

%changelog
