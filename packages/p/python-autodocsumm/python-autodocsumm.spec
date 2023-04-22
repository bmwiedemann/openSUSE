#
# spec file for package python-autodocsumm
#
# Copyright (c) 2023 SUSE LLC
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
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-autodocsumm
Version:        0.2.9
Release:        0
Summary:        Extended sphinx autodoc including automatic autosummaries
License:        GPL-2.0-only
URL:            https://github.com/Chilipp/autodocsumm
Source:         https://github.com/Chilipp/autodocsumm/archive/v%{version}.tar.gz#/autodocsumm-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 2.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 2.2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Extended sphinx autodoc including automatic autosummaries

%prep
%setup -q -n autodocsumm-%{version}
# Remove guard from Sphinx version
sed -i 's/,<5.0//' setup.py

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/autodocsumm
%{python_sitelib}/autodocsumm-%{version}*-info

%changelog
