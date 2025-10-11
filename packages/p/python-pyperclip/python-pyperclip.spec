#
# spec file for package python-pyperclip
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pyperclip
Version:        1.11.0
Release:        0
Summary:        A clipboard module for Python
License:        BSD-3-Clause
URL:            https://github.com/asweigart/pyperclip
Source0:        https://files.pythonhosted.org/packages/source/p/pyperclip/pyperclip-%{version}.tar.gz
# PATCH-FIX-UPSTREAM tests are broken with 1.9.0 release https://github.com/asweigart/pyperclip/issues/263
Patch:          tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       xclip
Requires:       xsel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A clipboard module for Python. It only handles plain text.

%prep
%autosetup -p1 -n pyperclip-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/pyperclip
%{python_sitelib}/pyperclip-%{version}.dist-info

%changelog
