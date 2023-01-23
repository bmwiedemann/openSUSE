#
# spec file for package python-cattrs
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


Name:           python-cattrs
Version:        22.2.0
Release:        0
Summary:        Composable complex class support for attrs and dataclasses
License:        MIT
URL:            https://github.com/python-attrs/cattrs
Source:         https://github.com/python-attrs/cattrs/archive/refs/tags/v%{version}.tar.gz#/cattrs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 20}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module immutables}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ujson}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 20
Suggests:       python-exceptiongroup
Suggests:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
Composable complex class support for attrs and dataclasses.

%prep
%setup -q -n cattrs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/cattr
%{python_sitelib}/cattrs
%{python_sitelib}/cattrs*info/

%changelog
