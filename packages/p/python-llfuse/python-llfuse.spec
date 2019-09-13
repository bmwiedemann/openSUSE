#
# spec file for package python-llfuse
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
%bcond_without python2
Name:           python-llfuse
Version:        1.3.6
Release:        0
Summary:        Python Bindings for the low-level FUSE API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/python-llfuse/python-llfuse
Source:         https://github.com/python-llfuse/python-llfuse/archive/release-%{version}.tar.gz#/python-llfuse-release-%{version}.tar.gz
Patch0:         fix-test-for-fusermount.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%setup -q -n python-llfuse-release-%{version}
%patch0 -p1
dos2unix README.rst

%build
%python_expand $python setup.py build_cython
# fix-char-cast-to-unsigned-int
sed -i 's|udata, i, padding_char);|udata, i, (unsigned char)padding_char);|' src/llfuse.c
sed -i 's|udata, uoffset+i, chars\[i\]);|udata, uoffset+i, (unsigned char)chars\[i\]);|' src/llfuse.c

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Note: There are some tests that are skipped because the user that
# runs rpmbuild should be able to run fusermount but there's no way
# to add it to the trusted group.
%pytest_arch

%files %{python_files}
%doc Changes.rst README.rst
%license LICENSE
%{python_sitearch}

%changelog
