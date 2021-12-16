#
# spec file for package python-pydyf
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Dr. Axel Braun <DocB@openSUSE.org>
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
%define         skip_python2 1

Name:           python-pydyf
Version:        0.1.2
Release:        0
Summary:        A low-level PDF generator
License:        BSD-3-Clause
URL:            https://www.courtbouillon.org/pydyf
Source:         https://files.pythonhosted.org/packages/source/p/pydyf/pydyf-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
## Testing
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pytest-isort}
BuildRequires:  gs

%python_subpackages

%description
A low-level PDF generator written in Python and based on PDF specification 1.7.

%prep
%setup -q -n pydyf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i 's:--flake8 --cov --no-cov-on-fail::' pyproject.toml
%pytest tests/test_pydyf.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
