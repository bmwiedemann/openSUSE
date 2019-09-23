#
# spec file for package python-pyfuse3
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
%define skip_python2 1
%define pname   pyfuse3
Name:           python-%{pname}
Version:        1.3.1
Release:        0
Summary:        Python Bindings for the low-level FUSE3 API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/libfuse/pyfuse3
Source:         https://github.com/libfuse/pyfuse3/archive/release-%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module contextvars >= 2.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  fuse3-devel >= 3.3.0
BuildRequires:  libattr-devel
BuildRequires:  python-rpm-macros
Recommends:     fuse3 >= 3.3.0
%python_subpackages

%description
pyfuse3 is a set of Python 3 bindings for libfuse 3. It provides an asynchronous API compatible with Trio and asyncio, and enables you to easily write a full-featured Linux filesystem in Python.

%prep
%setup -q -n %{pname}-release-%{version}

%build
%python_expand $python setup.py build_cython
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
