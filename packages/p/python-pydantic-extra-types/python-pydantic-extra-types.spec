#
# spec file for package python-pydantic-extra-types
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


Name:           python-pydantic-extra-types
Version:        2.11.1
Release:        0
Summary:        Extra Pydantic types
License:        MIT
URL:            https://github.com/pydantic/pydantic-extra-types
Source:         https://files.pythonhosted.org/packages/source/p/pydantic_extra_types/pydantic_extra_types-%{version}.tar.gz
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
# The test suite (incl. tests/test_json_schema.py) imports optional type
# backends not packaged in Factory -- cron-converter (cron type) and
# python-ulid (ulid type) -- so pytest cannot even collect. Fall back to an
# import smoke test of the core, dependency-free types.
%python_expand PYTHONDONTWRITEBYTECODE=1 $python -c "import pydantic_extra_types; from pydantic_extra_types import mac_address, coordinate, isbn"

%files %{python_files}
%license LICENSE
%doc README.md HISTORY.md
%{python_sitelib}/pydantic_extra_types
%{python_sitelib}/pydantic_extra_types-%{version}.dist-info

%changelog
