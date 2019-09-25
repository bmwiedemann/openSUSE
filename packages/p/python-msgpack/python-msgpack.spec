#
# spec file for package python-msgpack
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-msgpack
Version:        0.6.2
Release:        0
Summary:        MessagePack (de)serializer
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/msgpack/msgpack-python
Source:         https://files.pythonhosted.org/packages/source/m/msgpack/msgpack-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# was renamed at 0.5.0
Provides:       python-msgpack-python = %{version}
Obsoletes:      python-msgpack-python < 0.5.0
%ifpython2
Provides:       %{oldpython}-msgpack-python = %{version}
Obsoletes:      %{oldpython}-msgpack-python < 0.5.0
%endif
%python_subpackages

%description
MessagePack (de)serializer for Python.

MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.

%prep
%setup -q -n msgpack-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/msgpack
%{python_sitearch}/msgpack-%{version}-py%{py_ver}.egg-info

%changelog
