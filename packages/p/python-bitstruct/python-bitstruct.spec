#
# spec file for package python-bitstruct
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-bitstruct
Version:        8.20.0
Release:        0
Summary:        Interpret strings as packed binary data
License:        MIT
URL:            https://github.com/eerimoq/bitstruct
Source:         https://files.pythonhosted.org/packages/source/b/bitstruct/bitstruct-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module is intended to have a similar interface as the python struct
module, but working on bits instead of primitive data types (char, int, ...).

%prep
%setup -q -n bitstruct-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -v tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/bitstruct*

%changelog
