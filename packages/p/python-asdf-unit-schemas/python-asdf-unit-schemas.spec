#
# spec file for package python-asdf-unit-schemas
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif


Name:           python-asdf-unit-schemas%{psuffix}
Version:        0.1.0
Release:        0
Summary:        ASDF schemas for units
License:        BSD-3-Clause
URL:            https://github.com/asdf-format/asdf-unit-schemas
Source:         https://files.pythonhosted.org/packages/source/a/asdf_unit_schemas/asdf_unit_schemas-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-importlib_resources >= 3 if python-base < 3.9)
Requires:       python-asdf-standard >= 1.0.1
Provides:       python-asdf_unit_schemas = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module asdf-astropy}
BuildRequires:  %{python_module asdf-unit-schemas = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
%endif
%python_subpackages

%description
This package provides ASDF schemas for validating unit tags.

%prep
%autosetup -p1 -n asdf_unit_schemas-%{version}
sed -i /addopts/d pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/asdf_unit_schemas
%{python_sitelib}/asdf_unit_schemas-%{version}.dist-info
%endif

%changelog
