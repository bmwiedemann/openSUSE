#
# spec file for package python-pyls-spyder
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
Name:           python-pyls-spyder
Version:        0.1.1
Release:        0
Summary:        Spyder extensions for the python-language-server
License:        MIT
URL:            https://github.com/spyder-ide/pyls-spyder
# Use Github archive instead of PyPI sdist because of test files
Source:         %{url}/archive/v%{version}.tar.gz#/pyls-spyder-%{version}-gh.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-language-server}
# /SECTION
BuildRequires:  fdupes
Requires:       python-python-language-server
BuildArch:      noarch
%python_subpackages

%description
Spyder extensions for the python-language-server

%prep
%setup -q -n pyls-spyder-%{version}
# https://github.com/spyder-ide/pyls-spyder/pull/11
sed -i 's/from mock/from unittest.mock/' pyls_spyder/tests/test_plugin.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/pyls_spyder
%{python_sitelib}/pyls_spyder-%{version}*-info

%changelog
