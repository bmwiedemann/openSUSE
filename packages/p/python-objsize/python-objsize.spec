#
# spec file for package python-objsize
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


Name:           python-objsize
Version:        0.7.0
Release:        0
Summary:        Calculate the size of Python's objects subtree in bytes (deep size)
License:        BSD-3-Clause
URL:            https://github.com/liran-funaro/objsize
Source:         https://github.com/liran-funaro/objsize/archive/refs/tags/%{version}.tar.gz#/objsize-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Traversal over Python's objects subtree and calculate the total size of the subtree in bytes (deep size).

The objsize Python package allows for the exploration and measurement of an object's complete memory usage
in bytes, including its child objects. This process, often referred to as deep size calculation, is achieved
through Python's internal Garbage Collection (GC) mechanism.

The objsize package is designed to ignore shared objects, such as None, types, modules, classes, functions,
and lambdas, because they are shared across many instances. One of the key performance features of objsize
is that it avoids recursive calls, ensuring a faster and safer execution.

%prep
%autosetup -p1 -n objsize-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/objsize
%{python_sitelib}/objsize-%{version}.dist-info

%changelog
