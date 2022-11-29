#
# spec file for package python-fastapi
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


#
# spec file for package python-fastapi
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fastapi
Version:        0.88.0
Release:        0
Summary:        FastAPI framework
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tiangolo/fastapi
Source:         https://files.pythonhosted.org/packages/source/f/fastapi/fastapi-%{version}.tar.gz
Patch0:         python-fastapi-disable-broken-tests.patch
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.0.0
Requires:       python-starlette >= 0.21.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 1.1.2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module SQLAlchemy >= 1.3.18}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module anyio >= 3.2.1}
BuildRequires:  %{python_module databases}
BuildRequires:  %{python_module email-validator >= 1.1.1}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.14.0}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module peewee >= 3.13.0}
BuildRequires:  %{python_module pydantic >= 1.0.0}
BuildRequires:  %{python_module pytest >= 5.4.3}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module python-multipart >= 0.0.5}
BuildRequires:  %{python_module requests >= 2.24.0}
BuildRequires:  %{python_module starlette >= 0.22.0}
BuildRequires:  %{python_module trio}
# /SECTION
%python_subpackages

%description
Python FastAPI framework.

%prep
%setup -q -n fastapi-%{version}
%autopatch -p1

# Requires orjson
rm tests/test_default_response_class.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# These two tests require orjson
%pytest -rs -W ignore::DeprecationWarning -k 'not (test_get_custom_response and (test_tutorial001 or test_tutorial001b))' tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*fastapi*/

%changelog
