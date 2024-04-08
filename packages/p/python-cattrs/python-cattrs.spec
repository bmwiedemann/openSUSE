#
# spec file for package python-cattrs
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


%{?sle15_python_module_pythons}
Name:           python-cattrs
Version:        23.2.3
Release:        0
Summary:        Composable complex class support for attrs and dataclasses
License:        MIT
URL:            https://github.com/python-attrs/cattrs
Source:         https://files.pythonhosted.org/packages/source/c/cattrs/cattrs-%{version}.tar.gz
Requires:       python-exceptiongroup
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.1}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 20}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cbor2}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module immutables}
BuildRequires:  %{python_module msgpack >= 1.0.2}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module ujson}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 20
Requires:       python-cbor2
Requires:       python-typing_extensions
Suggests:       python-ujson
Suggests:       python-orjson
Suggests:       python-msgpack
Suggests:       python-PyYAML
Suggests:       python-tomlkit
Suggests:       python-cbor2
Suggests:       python-pymongo
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
