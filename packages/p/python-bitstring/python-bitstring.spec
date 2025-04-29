#
# spec file for package python-bitstring
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


Name:           python-bitstring
Version:        4.3.1
Release:        0
Summary:        Python module for the construction, analysis and modification of binary data
License:        MIT
URL:            https://github.com/scott-griffiths/bitstring
Source:         https://github.com/scott-griffiths/bitstring/archive/bitstring-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bitarray >= 3.0
BuildRequires:  %{python_module bitarray >= 3.0}
BuildRequires:  %{python_module gfloat}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-benchmark}
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
%autosetup -p1 -n bitstring-bitstring-%{version}
sed -i '1{\@^#!%{_bindir}/env python@d}' bitstring/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/bitstring
%{python_sitelib}/bitstring-4.3.1.dist-info

%changelog
