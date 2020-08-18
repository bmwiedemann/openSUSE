#
# spec file for package python-cstruct
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cstruct
Version:        1.8
Release:        0
License:        MIT
Summary:        C-style structs for Python
Url:            http://github.com/andreax79/python-cstruct
Group:          Development/Languages/Python
Source:         https://github.com/andreax79/python-cstruct/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Convert C struct definitions into Python classes with methods for
serializing/deserializing. The usage is very simple: create a class
subclassing cstruct.CStruct and add a C struct definition as a
string in the struct field. The C struct definition is parsed at
runtime and the struct format string is generated. The class offers
the method "unpack" for deserializing a string of bytes into a
Python object and the method "pack" for serializing the values into
a string.

%prep
%setup -q
sed -i -e '/^#!\//, 1d' \
  cstruct/__init__.py \
  cstruct/examples/fdisk.py \
  cstruct/examples/who.py \
  cstruct/tests/test_cstruct.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE 
%doc changelog.txt README.md
%{python_sitelib}/cstruct*

%changelog
