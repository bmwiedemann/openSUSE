#
# spec file for package python-hypothesis-jsonschema
#
# Copyright (c) 2026 SUSE LLC
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

# Upstream doesn't have git tags so use parent tag from pypi
%define parent_tag 0.23.1
Name:           python-hypothesis-jsonschema
Version:        0.23.1+gitfa38b03
Release:        0
Summary:        Generate test data from JSON schemata with Hypothesis
License:        MPL-2.0
URL:            https://github.com/python-jsonschema/hypothesis-jsonschema
Source0:        hypothesis-jsonschema-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module hypothesis >= 6.84.3}
BuildRequires:  %{python_module jsonschema >= 4.18.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-hypothesis >= 6.84.3
Requires:       python-jsonschema >= 4.18.0
BuildArch:      noarch
%python_subpackages

%description
Generate test data from JSON schemata with Hypothesis

%prep
%autosetup -p1 -n hypothesis-jsonschema-%{version}
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# incompatible with new jsonschema versions
skiptests="test_invalid_schemas_are_invalid"
skiptests+=" or test_cannot_generate_for_empty_test_suite_schema"
%pytest -k "not ($skiptests) and not (test_can_generate_for_real_large_schema and Draft and 8)"

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/hypothesis[-_]jsonschema
%{python_sitelib}/hypothesis[-_]jsonschema-%{parent_tag}.dist-info

%changelog
