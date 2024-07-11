#
# spec file for package python-dm-tree
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


Name:           python-dm-tree
Version:        0.1.8
Release:        0
Summary:        Tree is a library for working with nested data structures
License:        Apache-2.0
URL:            https://github.com/deepmind/tree
Source:         https://files.pythonhosted.org/packages/source/d/dm-tree/dm-tree-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/google-deepmind/tree/pull/50
Patch0:         remove-abseil.patch
# PATCH-FIX-UPSTREAM Based on https://github.com/google-deepmind/tree/pull/73
Patch1:         use-system-pybind11.patch
# PATCH-FIX-OPENSUSE Set debug build so we get symbols
Patch2:         set-debug.patch
BuildRequires:  python-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module absl-py >= 0.6.1}
BuildRequires:  %{python_module attrs >= 18.2.0}
BuildRequires:  %{python_module numpy >= 1.15.4}
BuildRequires:  %{python_module wrapt >= 1.11.2}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
%python_subpackages

%description
Tree is a library for working with nested data structures.

%prep
%autosetup -p1 -n dm-tree-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/tree/{,__pycache__/}tree_test.*

%check
tmp=$(mktemp -d)
cp tree/tree_test.py $tmp
pushd $tmp
%pytest_arch tree_test.py
popd

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/tree
%{python_sitearch}/dm_tree-%{version}.dist-info

%changelog
