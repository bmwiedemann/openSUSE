#
# spec file for package python-bitstring
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
Name:           python-bitstring
Version:        3.1.7
Release:        0
Summary:        Python module for the construction, analysis and modification of binary data
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/scott-griffiths/bitstring
Source:         https://github.com/scott-griffiths/bitstring/archive/bitstring-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Bitstring is a pure Python module to aid
the creation and analysis of binary data.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with functions or slice notation.
They can also be read from, searched and replaced, and navigated in,
similar to a file or stream.

%prep
%setup -q -n bitstring-bitstring-%{version}
dos2unix README.rst
sed -i '1{\@^#!%{_bindir}/env python@d}' bitstring.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd test
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
