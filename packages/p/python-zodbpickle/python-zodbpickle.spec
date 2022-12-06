#
# spec file for package python-zodbpickle
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-zodbpickle
Version:        2.6
Release:        0
Summary:        Fork of Python 3 pickle module
License:        Python-2.0 AND ZPL-2.1
Group:          Development/Libraries/Python
URL:            https://pypi.python.org/pypi/zodbpickle
Source:         https://files.pythonhosted.org/packages/source/z/zodbpickle/zodbpickle-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This package presents a uniform pickling interface for ZODB:
 * Under Python2, this package forks both Python 2.7’s pickle and
   cPickle modules, adding support for the protocol 3 opcodes.
   It also provides a new subclass of bytes, zodbpickle.binary,
   which Python2 applications can use to pickle binary values such
   that they will be unpickled as bytes under Py3k.
 * Under Py3k, this package forks the pickle module (and the
   supporting C extension) from both Python 3.2 and Python 3.3.
   The fork add support for the noload operations used by ZODB.

%prep
%setup -q -n zodbpickle-%{version}
rm -rf src/zodbpickle.egg-info

%build
%python_build

%install
%python_install
%{python_expand find %{buildroot}%{$python_sitearch} -name *.c -delete
  %fdupes %{buildroot}%{$python_sitearch}
}

%check
pushd src
mv zodbpickle{,_hide}
%pyunittest_arch -v zodbpickle_hide.tests.test_pickle.test_suite

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitearch}/*

%changelog
