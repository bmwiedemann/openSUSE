#
# spec file for package python-pyperclip
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
Name:           python-pyperclip
Version:        1.7.0
Release:        0
Summary:        A clipboard module for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/asweigart/pyperclip
Source0:        https://pypi.io/packages/source/p/pyperclip/pyperclip-%{version}.tar.gz
# https://github.com/asweigart/pyperclip/issues/17
Source1:        https://raw.githubusercontent.com/asweigart/pyperclip/master/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       xclip
Requires:       xsel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
A clipboard module for Python. It only handles plain text.

%prep
%setup -q -n pyperclip-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE.txt
%{python_sitelib}/pyperclip
%{python_sitelib}/pyperclip-%{version}-py%{py_ver}.egg-info

%changelog
