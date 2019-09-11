#
# spec file for package python-zstd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-zstd
Version:        1.4.1.0
Release:        0
Summary:        ZSTD Bindings for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source:         https://files.pythonhosted.org/packages/source/z/zstd/zstd-%{version}.tar.gz
Patch0:         test-external.patch
Patch1:         test-once.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libzstd) >= 1.4.1
%python_subpackages

%description
ZSTD Bindings for Python.

%prep
%setup -q -n zstd-%{version}
%patch0 -p1
%patch1 -p1
rm -rf zstd/
# do not test the version matching, we don't really need exact version of
# zstd here
rm tests/test_version.py
sed -i -e '/test_version/d' tests/__init__.py

%build
export CFLAGS="%{optflags}"
%python_build --legacy --pyzstd-legacy --external

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
