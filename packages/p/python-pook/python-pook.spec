#
# spec file for package python-pook
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


# requires python-aiohttp
%{?sle15_python_module_pythons}
Name:           python-pook
Version:        1.1.1
Release:        0
Summary:        HTTP traffic mocking and expectations
License:        MIT
URL:            https://github.com/h2non/pook
Source:         https://files.pythonhosted.org/packages/source/p/pook/pook-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Requires:       python-furl >= 0.5.6
Requires:       python-jsonschema >= 2.5.1
Requires:       python-xmltodict >= 0.11.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module furl >= 0.5.6}
BuildRequires:  %{python_module jsonschema >= 2.5.1}
BuildRequires:  %{python_module mocket >= 1.6.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module urllib3 >= 1.19.1}
BuildRequires:  %{python_module xmltodict >= 0.10.2}
# /SECTION
%python_subpackages

%description
HTTP traffic mocking and expectations.

%prep
%autosetup -p1 -n pook-%{version}
rm -f setup.cfg pytest.ini tox.ini

# Assist unittest on Python 2
touch tests/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%{python_expand  #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m pytest -v tests/unit
$python -m pytest -v tests/integration/engines/pytest_suite.py
export PYTHONPATH=%{buildroot}%{$python_sitelib}:.
$python -m unittest tests.integration.engines.unittest_suite
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pook
%{python_sitelib}/pook-%{version}*-info

%changelog
