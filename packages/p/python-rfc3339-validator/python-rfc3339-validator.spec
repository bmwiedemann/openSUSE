#
# spec file for package python-rfc3339-validator
#
# Copyright (c) 2023 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-rfc3339-validator
Version:        0.1.4
Release:        0
Summary:        A pure python RFC3339 validator
License:        MIT
URL:            https://github.com/naimetti/rfc3339-validator
Source:         https://files.pythonhosted.org/packages/source/r/rfc3339_validator/rfc3339_validator-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest >= 3}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module strict-rfc3339}
# /SECTION
%python_subpackages

%description
A pure python RFC3339 validator

%prep
%setup -q -n rfc3339_validator-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/rfc3339_validator.py
%pycache_only %{python_sitelib}/__pycache__/
%{python_sitelib}/rfc3339_validator-*.egg-info/

%changelog
