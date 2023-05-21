#
# spec file
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

%{?sle15_python_module_pythons}
Name:           python-asdf-astropy%{psuffix}
Version:        0.4.0
Release:        0
Summary:        ASDF serialization support for astropy
License:        BSD-3-Clause
URL:            https://github.com/astropy/asdf-astropy
Source:         https://files.pythonhosted.org/packages/source/a/asdf-astropy/asdf-astropy-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module packaging >= 19}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf >= 2.13
Requires:       python-asdf-coordinates-schemas >= 0.1
Requires:       python-asdf-transform-schemas >= 0.2.2
Requires:       python-astropy >= 5.0.4
Requires:       python-numpy >= 1.20
Requires:       python-packaging >= 19
%if 0%{?python_version_nodots} < 39
Requires:       python-importlib_resources >= 3
%endif
%if %{with test}
BuildRequires:  %{python_module asdf-astropy = %{version}}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
%endif
BuildArch:      noarch
%python_subpackages

%description
ASDF serialization support for astropy

%prep
%autosetup -p1 -n asdf-astropy-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest -n auto
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/asdf_astropy
%{python_sitelib}/asdf_astropy-%{version}.dist-info
%endif

%changelog
