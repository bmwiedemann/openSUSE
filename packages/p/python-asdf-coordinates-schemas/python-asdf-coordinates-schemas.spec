#
# spec file for package python-asdf-coordinates-schemas
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-asdf-coordinates-schemas%{psuffix}
Version:        0.3.0
Release:        0
Summary:        ASDF coordinates schemas
License:        BSD-3-Clause
URL:            https://github.com/asdf-format/asdf-coordinates-schemas
Source:         https://files.pythonhosted.org/packages/source/a/asdf-coordinates-schemas/asdf_coordinates_schemas-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf >= 2.12.1
Requires:       python-asdf-standard >= 1.1.0
Provides:       python-asdf_coordinates_schemas = %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module asdf-astropy >= 0.2.0}
BuildRequires:  %{python_module asdf-coordinates-schemas = %{version}}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
ASDF coordinates schemas

%prep
%setup -q -n asdf_coordinates_schemas-%{version}
sed -i "/addopts = '--color=yes'/d" pyproject.toml

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# gh#asdf-format/asdf-coordinates-schemas#59
donttest="(galactocentric and test_example_0)"
%pytest -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/asdf_coordinates_schemas
%{python_sitelib}/asdf_coordinates_schemas-%{version}.dist-info
%endif

%changelog
