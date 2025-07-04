#
# spec file for package python-pilkit
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


%{?sle15_python_module_pythons}
Name:           python-pilkit
Version:        3.0
Release:        0
Summary:        A collection of utilities and processors for the Python Imaging Libary
License:        BSD-3-Clause
URL:            https://github.com/matthewwithanm/pilkit/
Source:         https://files.pythonhosted.org/packages/source/p/pilkit/pilkit-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PILKit is a collection of utilities for working with PIL (the Python Imaging
Library).

One of its main features is a set of **processors** which expose a simple
interface for performing manipulations on PIL images.

%prep
%setup -q -n pilkit-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/pilkit
%{python_sitelib}/pilkit-%{version}*-info

%changelog
