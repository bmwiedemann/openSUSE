#
# spec file for package python-openapi-spec-validator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-openapi-spec-validator
Version:        0.2.7
Release:        0
Summary:        Python module for validating OpenAPI Specs against Swagger and OAS3
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/p1c2u/openapi-spec-validator
Source:         https://github.com/p1c2u/openapi-spec-validator/archive/%{version}.tar.gz
Patch0:         openapi-spec-validator-skip-urls.patch
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-pathlib2
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-jsonschema
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-pathlib2
%endif
%python_subpackages

%description
OpenAPI Spec Validator is a Python library that validates
OpenAPI Specs against the OpenAPI 2.0 (aka Swagger) and
OpenAPI 3.0.0 specification. The validator aims to check
for full compliance with the Specification.

%prep
%setup -q -n openapi-spec-validator-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/openapi-spec-validator
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative openapi-spec-validator

%postun
%python_uninstall_alternative openapi-spec-validator

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/openapi-spec-validator
%{python_sitelib}/*

%changelog
