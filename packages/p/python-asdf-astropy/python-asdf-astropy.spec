#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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

%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-asdf-astropy%{psuffix}
Version:        0.2.1
Release:        0
Summary:        ASDF serialization support for astropy
License:        BSD-3-Clause
URL:            https://github.com/astropy/asdf-astropy
Source:         https://files.pythonhosted.org/packages/source/a/asdf-astropy/asdf_astropy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM asdf-astropy-pr84-fixtests.patch -- gh#astropy/asdf-astropy#84
Patch1:         https://github.com/astropy/asdf-astropy/pull/84.patch#/asdf-astropy-pr84-fixtests.patch
BuildRequires:  %{python_module packaging >= 16.0}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm}
%if 0%{suse_version} >= 1550
BuildRequires:  %{python_module tomli}
%else
BuildRequires:  %{python_module toml}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf >= 2.8.0
Requires:       python-asdf-coordinates-schemas
Requires:       python-asdf-transform-schemas >= 0.2.2
Requires:       python-astropy >= 5.0.4
Requires:       python-numpy
Requires:       python-packaging >= 16.0
%if 0%{?python_version_nodots} < 39
Requires:       python-importlib_resources >= 3
%endif
%if %{with test}
BuildRequires:  %{python_module asdf-astropy = %{version}}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
%endif
BuildArch:      noarch
%python_subpackages

%description
ASDF serialization support for astropy

%prep
%autosetup -p1 -n asdf_astropy-%{version}
sed -i 's/--color=yes//' setup.cfg

%build
%python_build

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/asdf_astropy
%{python_sitelib}/asdf_astropy-%{version}*-info
%endif

%changelog
