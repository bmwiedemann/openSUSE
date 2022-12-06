#
# spec file for package python-cstruct
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           python-cstruct
Version:        5.2
Release:        0
Summary:        C-style structs for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/andreax79/python-cstruct
Source:         https://github.com/andreax79/python-cstruct/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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

%build
%python_build

%install
%python_install
%python_expand find %{buildroot}%{$python_sitelib} -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc changelog.txt README.md
%{python_sitelib}/cstruct
%{python_sitelib}/cstruct-%{version}*-info

%changelog
