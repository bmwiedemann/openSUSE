#
# spec file for package python-pytest-echo
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
Name:           python-pytest-echo
Version:        1.7.1
Release:        0
Summary:        Pytest plugin for echoing build environment attributes
License:        MIT
URL:            https://github.com/pytest-dev/pytest-echo
Source:         https://files.pythonhosted.org/packages/source/p/pytest-echo/pytest-echo-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest >= 2.2}
# /SECTION
%python_subpackages

%description
pytest plugin with mechanisms for echoing environment variables,
package version and generic attributes.

%prep
%setup -q -n pytest-echo-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv pytest_echo.py /tmp/pytest_echo.py
%pytest
mv /tmp/pytest_echo.py pytest_echo.py

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
