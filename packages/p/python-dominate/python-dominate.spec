#
# spec file for package python-dominate
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
Name:           python-dominate
Version:        2.5.2
Release:        0
Summary:        Python library for creating and manipulating HTML documents
License:        GPL-3.0-only
URL:            http://github.com/Knio/dominate/
Source:         https://files.pythonhosted.org/packages/source/d/dominate/dominate-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 2.7.3}
BuildRequires:  %{python_module setuptools}
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
%setup -q -n dominate-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
