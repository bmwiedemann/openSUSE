#
# spec file for package python-pydantic-extra-types
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


Name:           python-pydantic-extra-types
Version:        2.11.2
Release:        0
Summary:        Extra Pydantic types
License:        MIT
URL:            https://github.com/pydantic/pydantic-extra-types
Source:         https://files.pythonhosted.org/packages/source/p/pydantic_extra_types/pydantic_extra_types-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-tests-for-pydantic-2.13.patch gh#pydantic/pydantic-extra-types#394 -- adjust tests for the description member pydantic 2.13 adds to the Coordinate schema
Patch0:         fix-tests-for-pydantic-2.13.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.5.2}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 2.5.2
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module annotated-types}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module jsonschema >= 4.0.0}
BuildRequires:  %{python_module pendulum}
BuildRequires:  %{python_module phonenumbers}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module semver >= 3.0.2}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module uuid-utils}
# /SECTION
%python_subpackages

%description
A growing collection of extra field types and validators for Pydantic 2,
such as colors, coordinates, country and currency codes, phone numbers,
payment card numbers, MAC addresses, semantic versions and more.

%prep
%autosetup -p1 -n pydantic_extra_types-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/test_cron.py, tests/test_ulid.py and tests/test_json_schema.py import
# optional type backends not packaged in Factory -- cron-converter (cron type)
# and python-ulid (ulid type) -- so they cannot be collected.
%pytest --ignore tests/test_cron.py --ignore tests/test_ulid.py --ignore tests/test_json_schema.py

%files %{python_files}
%license LICENSE
%doc README.md HISTORY.md
%{python_sitelib}/pydantic_extra_types
%{python_sitelib}/pydantic_extra_types-%{version}.dist-info

%changelog
