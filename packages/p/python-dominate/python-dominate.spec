#
# spec file for package python-dominate
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-dominate
Version:        2.9.1
Release:        0
Summary:        Python library for creating and manipulating HTML documents
License:        GPL-3.0-only
URL:            https://github.com/Knio/dominate/
Source:         https://files.pythonhosted.org/packages/source/d/dominate/dominate-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#Knio/dominate#202
Patch0:         support-python-313.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 2.7.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Dominate is a Python library for creating and manipulating HTML
documents using an elegant DOM API.

It allows you to write HTML pages in pure Python very concisely,
which eliminates the need to learn another template language, and
lets you take advantage of the more powerful features of Python.

%prep
%autosetup -p1 -n dominate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/dominate
%{python_sitelib}/dominate-%{version}.dist-info

%changelog
