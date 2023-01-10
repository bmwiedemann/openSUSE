#
# spec file for package python-greenlet
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2010 B1 Systems GmbH, Vohburg, Germany.
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


Name:           python-greenlet
Version:        1.1.3
Release:        0
Summary:        Lightweight in-process concurrent programming
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/python-greenlet/greenlet
Source0:        https://files.pythonhosted.org/packages/source/g/greenlet/greenlet-%{version}.tar.gz
Source9:        python-greenlet-rpmlintrc
# PATCH-FIX-OPENSUSE sphinx-6.0.0.patch
Patch0:         sphinx-6.0.0.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
%python_subpackages

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

%package devel
Summary:        C development headers for python-greenlet
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
This package contains header files required for C modules development.

%prep
%autosetup -p1 -n greenlet-%{version}

%build
export CFLAGS="%{optflags} -fno-tree-dominator-opts -fno-strict-aliasing"
%python_build

export PYTHONPATH=$PWD/src
cd docs && make html && rm _build/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CFLAGS="%{optflags} -fno-tree-dominator-opts -fno-strict-aliasing"
%pyunittest_arch discover -v greenlet.tests

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%doc docs/_build/html/
%license LICENSE*
%{python_sitearch}/greenlet*

%files %{python_files devel}
%doc AUTHORS
%license LICENSE*
%{_includedir}/python%{python_version}*/greenlet/

%changelog
