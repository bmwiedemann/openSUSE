#
# spec file for package python-cattrs
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


%{?sle15_python_module_pythons}
Name:           python-cattrs
Version:        26.1.0
Release:        0
Summary:        Composable complex class support for attrs and dataclasses
License:        MIT
URL:            https://github.com/python-attrs/cattrs
Source:         https://files.pythonhosted.org/packages/source/c/cattrs/cattrs-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 25.4.0}
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module cbor2 >= 5.4.6}
BuildRequires:  %{python_module hypothesis >= 6.135.26}
BuildRequires:  %{python_module immutables >= 0.21}
BuildRequires:  %{python_module msgpack >= 1.0.5}
BuildRequires:  %{python_module msgspec >= 0.19.0}
BuildRequires:  %{python_module orjson >= 3.11.3}
BuildRequires:  %{python_module pymongo >= 4.4.0}
BuildRequires:  %{python_module pytest >= 8.4.1}
BuildRequires:  %{python_module pytest-benchmark >= 5.1.0}
BuildRequires:  %{python_module tomli-w >= 1.1.0}
BuildRequires:  %{python_module tomlkit >= 0.11.8}
BuildRequires:  %{python_module typing_extensions >= 4.14.0}
BuildRequires:  %{python_module ujson >= 5.10.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 25.4.0
%if %python_version_nodots < 311
Requires:       python-exceptiongroup >= 1.1.1
%endif
Requires:       python-typing_extensions >= 4.14.0
Suggests:       python-cbor2 >= 5.4.6
Suggests:       python-ujson >= 5.10.0
Suggests:       python-orjson >= 3.11.3
Suggests:       python-msgpack >= 1.0.5
Suggests:       python-PyYAML >= 6.0
Suggests:       python-tomlkit >= 0.11.8
Suggests:       python-tomli-w >= 1.1.0
Suggests:       python-pymongo >= 4.4.0
BuildArch:      noarch
%python_subpackages

%description
Composable complex class support for attrs and dataclasses.

%prep
%autosetup -p1 -n cattrs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md HISTORY.md CONTRIBUTING.md
%license LICENSE
%{python_sitelib}/cattr
%{python_sitelib}/cattrs
%{python_sitelib}/cattrs-%{version}.dist-info

%changelog
