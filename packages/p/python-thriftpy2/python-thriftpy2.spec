#
# spec file for package python-thriftpy2
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
Name:           python-thriftpy2
Version:        0.4.5
Release:        0
Summary:        Pure python implementation of Apache Thrift
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Thriftpy/thriftpy2
Source:         https://github.com/Thriftpy/thriftpy2/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.28.4}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4.0}
BuildRequires:  %{python_module toro >= 0.6}
BuildRequires:  fdupes
BuildRequires:  python-gdbm
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dbm
BuildRequires:  python3-pytest-asyncio
Requires:       python-ply >= 3.4
Recommends:     python-tornado >= 4.0
Recommends:     python-toro >= 0.6
%python_subpackages

%description
ThriftPy is a pure python implementation of Apache Thrift in a
pythonic way.

%prep
%setup -q -n thriftpy2-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
cd tests
# the two tests fail in OBS on timeout
%pytest_arch -k 'not (test_able_to_communicate or test_zero_length_string)'

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitearch}/*

%changelog
