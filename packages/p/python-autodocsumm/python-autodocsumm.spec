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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-autodocsumm
Version:        0.2.11
Release:        0
Summary:        Extended sphinx autodoc including automatic autosummaries
License:        Apache-2.0
URL:            https://github.com/Chilipp/autodocsumm
Source:         https://github.com/Chilipp/autodocsumm/archive/v%{version}.tar.gz#/autodocsumm-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n autodocsumm-%{version}
# Remove guard from Sphinx version
sed -i 's/,<5.0//' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/autodocsumm
%{python_sitelib}/autodocsumm-%{version}*-info

%changelog
