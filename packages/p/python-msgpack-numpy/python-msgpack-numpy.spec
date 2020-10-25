#
# spec file for package python-msgpack-numpy
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-msgpack-numpy
Version:        0.4.7.1
Release:        0
Summary:        Numpy data serialization library using msgpack
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lebedov/msgpack-numpy
Source:         https://files.pythonhosted.org/packages/source/m/msgpack-numpy/msgpack-numpy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack >= 0.5.2
Requires:       python-numpy >= 1.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module msgpack >= 0.5.2}
BuildRequires:  %{python_module numpy >= 1.9.0}
# /SECTION
%python_subpackages

%description
This package provides encoding and decoding routines that enable the
serialization and deserialization of numerical and array data types
provided by numpy using the highly efficient msgpack format.
Serialization of Python's native complex data types is also supported.

%prep
%setup -q -n msgpack-numpy-%{version}
sed -i -e '/^#!\//, 1d' msgpack_numpy.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -B tests.py

%files %{python_files}
%doc AUTHORS.md CHANGES.md README.md
%license LICENSE.md
%{python_sitelib}/msgpack_numpy-%{version}-py*.egg-info
%{python_sitelib}/msgpack_numpy.*
%pycache_only %{python_sitelib}/__pycache__

%changelog
