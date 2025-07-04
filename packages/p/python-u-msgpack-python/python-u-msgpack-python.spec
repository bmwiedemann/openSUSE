#
# spec file for package python-u-msgpack-python
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
Name:           python-u-msgpack-python
Version:        2.8.0
Release:        0
Summary:        A MessagePack serializer and deserializer
License:        MIT
URL:            https://github.com/vsergeev/u-msgpack-python
Source:         https://files.pythonhosted.org/packages/source/u/u-msgpack-python/u-msgpack-python-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
u-msgpack-python is a MessagePack serializer and
deserializer module written in pure Python, compatible with
Python 2, Python 3, in both the CPython and PyPy implementations of
Python. u-msgpack-python is fully compliant with the MessagePack
2017-09-17 specification. In particular, it supports the binary,
UTF-8 string, and application-defined extended types.

%prep
%setup -q -n u-msgpack-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec test_umsgpack.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/umsgpack
%{python_sitelib}/u_msgpack_python-%{version}.dist-info

%changelog
