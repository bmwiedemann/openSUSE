#
# spec file for package python-thriftpy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-thriftpy
Version:        0.3.9
Release:        0
Summary:        Pure python implementation of Apache Thrift
License:        MIT
Group:          Development/Languages/Python
URL:            https://thriftpy.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/t/thriftpy/thriftpy-%{version}.tar.gz
Source1:        LICENSE
Patch0:         tornado_5.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply >= 3.4
Recommends:     python-tornado >= 4.0
%if %{with test}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module tornado >= 4.0}
%endif
%python_subpackages

%description
ThriftPy is a pure python implementation of Apache Thrift in a
pythonic way.

%prep
%setup -q -n thriftpy-%{version}
cp %{SOURCE1} .
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitearch}/*

%changelog
