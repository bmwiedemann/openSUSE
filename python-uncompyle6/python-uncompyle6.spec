#
# spec file for package python-uncompyle6
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
Name:           python-uncompyle6
Version:        3.3.5
Release:        0
Summary:        Python cross-version byte-code decompiler
License:        GPL-3.0-only
Group:          Development/Languages/Python
Url:            https://github.com/rocky/python-uncompyle6/
Source:         https://files.pythonhosted.org/packages/source/u/uncompyle6/uncompyle6-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module spark_parser >= 1.8.7}
BuildRequires:  %{python_module xdis >= 4.0.2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-spark_parser >= 1.8.7
Requires:       python-xdis >= 4.0.2
BuildArch:      noarch

%python_subpackages

%description
A native Python cross-version decompiler and fragment decompiler.
The successor to decompyle, uncompyle, and uncompyle2.

%prep
%setup -q -n uncompyle6-%{version}
# invalid syntax on new pytest
rm pytest/test_function_call.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest pytest

%files %{python_files}
%license COPYING
%doc ChangeLog README README.rst
%python3_only %{_bindir}/uncompyle6
%python3_only %{_bindir}/pydisassemble
%{python_sitelib}/*

%changelog
