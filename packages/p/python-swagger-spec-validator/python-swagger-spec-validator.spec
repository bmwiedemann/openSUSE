#
# spec file for package python-swagger-spec-validator
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-swagger-spec-validator
Version:        3.0.4
Release:        0
Summary:        Validation of Swagger specifications
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/Yelp/swagger_spec_validator
Source:         https://github.com/Yelp/swagger_spec_validator/archive/refs/tags/v%{version}.tar.gz#/swagger-spec-validator-%{version}.tar.gz
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-jsonschema
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
Swagger Spec Validator is a Python library that validates Swagger Specs against
the Swagger 1.2 or Swagger 2.0 specification. The validator aims to check for
full compliance with the Specification.

%prep
%autosetup -p1 -n swagger_spec_validator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/swagger_spec_validator-%{version}*-info
%{python_sitelib}/swagger_spec_validator

%changelog
