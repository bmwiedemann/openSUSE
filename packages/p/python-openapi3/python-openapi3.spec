#
# spec file for package python-openapi3
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-openapi3
Version:        1.8.2
Release:        0
Summary:        Client and Validator of OpenAPI 3 Specifications
License:        BSD-3-Clause
URL:            https://github.com/dorthu/openapi3
Source:         https://github.com/Dorthu/openapi3/archive/refs/tags/%{version}.tar.gz#/openapi3-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support pydantic v2 RootModel changes
Patch0:         support-new-pydantic.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module hypercorn}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module uvloop}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Client and Validator of OpenAPI 3 Specifications

%prep
%autosetup -p1 -n openapi3-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# fastapi has moved on, and this ... hasn't
%pytest --ignore tests/fastapi_test.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/openapi3
%{python_sitelib}/openapi3-%{version}.dist-info

%changelog
