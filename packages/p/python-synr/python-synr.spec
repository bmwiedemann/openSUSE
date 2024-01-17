#
# spec file for package python-synr
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-synr
Version:        0.6.0
Release:        0
Summary:        A consistent AST for Python
License:        Apache-2.0
URL:            https://synr.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/s/synr/synr-%{version}.tar.gz
Source1:        https://github.com/octoml/synr/raw/v%{version}/tests/test_synr.py
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires:       python-attrs
BuildArch:      noarch
%python_subpackages

%description
A library for a stable Abstract Syntax Tree for Python.

%prep
%setup -q -n synr-%{version}
mkdir tests
cp %{SOURCE1} tests

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/synr
%{python_sitelib}/synr-%{version}*-info

%changelog
