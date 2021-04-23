#
# spec file for package python-openapi-codec
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
Name:           python-openapi-codec
Version:        1.3.2
Release:        0
Summary:        OpenAPI codec for Core API
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/core-api/python-openapi-codec/
Source:         https://github.com/core-api/python-openapi-codec/archive/%{version}.tar.gz#/openapi-codec-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coreapi >= 2.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coreapi >= 2.2.0}
# /SECTION
%python_subpackages

%description
Python Core API codec for the Open API schema format, also known as "Swagger".

%prep
%setup -q -n python-openapi-codec-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
