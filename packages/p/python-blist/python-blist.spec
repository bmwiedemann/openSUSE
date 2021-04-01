#
# spec file for package python-blist
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-blist
Version:        1.3.6
Release:        0
Summary:        A list-like type with better asymptotic performance
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://stutzbachenterprises.com/blist/
Source:         https://files.pythonhosted.org/packages/source/b/blist/blist-%{version}.tar.gz
Patch0:         0001-Fix-compatibility-for-Python-3.7.patch
# PATCH-FIX-UPSTREAM blist-pr91-py39.patch -- gh#DanielStutzbach/blist/pull/91.patch
Patch1:         https://github.com/DanielStutzbach/blist/pull/91.patch#/blist-pr91-py39.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The blist is a drop-in replacement for the Python list the provides
better performance when modifying large lists.  The blist package also
provides sortedlist, sortedset, weaksortedlist,
weaksortedset, sorteddict, and btuple types.

%prep
%autosetup -p1 -n blist-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand # arcane test suite setup: needs the built module in the same tree as the test files
mkdir blist-test-%{$python_bin_suffix}
pushd blist-test-%{$python_bin_suffix}
cp -r %{buildroot}%{$python_sitearch}/blist ./
cp -r ../blist/test blist/
cp ../test_blist.py ./
$python -m unittest -v test_blist.test_suite
popd
}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/blist-%{version}-py*.egg-info
%{python_sitearch}/blist/

%changelog
