#
# spec file for package python-subprocess32
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
# Note: this package is python 2.x-only.
%define skip_python3 1
Name:           python-subprocess32
Version:        3.5.4
Release:        0
Summary:        A backport of the subprocess module from Python 3.2/3.3 for use on 2.x
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/python-subprocess32
Source:         https://files.pythonhosted.org/packages/source/s/subprocess32/subprocess32-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  python-test
%endif
%python_subpackages

%description
This is a backport of the subprocess standard library module from
Python 3.2 & 3.3 for use on Python 2.

It includes bugfixes and some new features.  On POSIX systems it is
guaranteed to be reliable when used in threaded applications.
It includes timeout support from Python 3.3 but otherwise matches
3.2's API.  It has not been tested on Windows.

%prep
%setup -q -n subprocess32-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%check
%python_exec setup.py test -v

%files %{python_files}
%license LICENSE
%doc ChangeLog README.md
%{python_sitearch}/_posixsubprocess32.so
%pycache_only %{python_sitearch}/__pycache__/*
%{python_sitearch}/subprocess32.py*
%{python_sitearch}/subprocess32-%{version}-py*.egg-info

%changelog
