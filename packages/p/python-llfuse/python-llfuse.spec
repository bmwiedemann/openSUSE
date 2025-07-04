#
# spec file for package python-llfuse
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
Name:           python-llfuse
Version:        1.5.1
Release:        0
Summary:        Python Bindings for the low-level FUSE API
License:        LGPL-2.1-or-later
URL:            https://github.com/python-llfuse/python-llfuse
Source:         https://github.com/python-llfuse/python-llfuse/archive/release-%{version}.tar.gz#/python-llfuse-release-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlite3}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  fuse-devel >= 2.8.0
BuildRequires:  libattr-devel
BuildRequires:  python-rpm-macros
Recommends:     fuse
%if %{with python2}
BuildRequires:  python2-contextlib2
%endif
%ifpython2
Requires:       python-contextlib2
%endif
Obsoletes:      %{name}-docs
%python_subpackages

%description
LLFUSE is a set of Python bindings for the low level FUSE API. It requires at
least FUSE 2.8.0 and supports both Python 2.x and 3.x.

LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well.

%prep
%autosetup -p1 -n python-llfuse-release-%{version}
dos2unix README.rst

%build
%python_expand $python setup.py build_cython
# fix-char-cast-to-unsigned-int
sed -i 's|udata, i, padding_char);|udata, i, (unsigned char)padding_char);|' src/llfuse.c
sed -i 's|udata, uoffset+i, chars\[i\]);|udata, uoffset+i, (unsigned char)chars\[i\]);|' src/llfuse.c
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Note: There are some tests that are skipped because the user that
# runs rpmbuild should be able to run fusermount but there's no way
# to add it to the trusted group.
%pytest_arch

%files %{python_files}
%doc Changes.rst README.rst
%license LICENSE
%{python_sitearch}/llfuse.cpython-*-linux-gnu.so
%{python_sitearch}/llfuse-%{version}.dist-info

%changelog
