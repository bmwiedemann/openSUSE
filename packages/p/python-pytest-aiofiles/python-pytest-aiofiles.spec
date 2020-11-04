#
# spec file for package python-pytest-aiofiles
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
%define skip_python2 1
Name:           python-pytest-aiofiles
Version:        0.2.0
Release:        0
Summary:        Pytest fixtures for writing aiofiles tests with pyfakefs
License:        AGPL-3.0-or-later
URL:            https://github.com/buhman/pytest-aiofiles
Source:         https://files.pythonhosted.org/packages/source/p/pytest-aiofiles/pytest-aiofiles-%{version}.tar.gz
# https://github.com/buhman/pytest-aiofiles/pull/3
Source1:        LICENSE
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiofiles >= 0.3.1
Requires:       python-pyfakefs >= 3.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiofiles >= 0.3.1}
BuildRequires:  %{python_module asynctest >= 0.10.0}
BuildRequires:  %{python_module pyfakefs >= 3.1}
BuildRequires:  %{python_module pytest-asyncio >= 0.5.0}
# /SECTION
%python_subpackages

%description
pytest fixtures for writing aiofiles tests with pyfakefs

%prep
%setup -q -n pytest-aiofiles-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not urandom and not test_fake_open'

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
