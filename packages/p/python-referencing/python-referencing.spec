#
# spec file for package python-referencing
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-referencing%{psuffix}
Version:        0.36.2
Release:        0
Summary:        JSON Referencing + Python
License:        MIT
URL:            https://github.com/python-jsonschema/referencing
# only use tarball created by tar_scm service,
# as PyPi does not include the suite git submodule
# and github tarballs do not include the .git directory
# required by hatch_vcs and setuptools_scm
#
# using obs_scm does **not** work...
Source:         referencing-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
# runtime dependencies
BuildRequires:  %{python_module attrs >= 24.3.0}
BuildRequires:  %{python_module rpds-py >= 0.22.3}
BuildRequires:  %{python_module typing_extensions >= 4.4.0 if %python-base < 3.13}
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.3.3}
BuildRequires:  %{python_module jsonschema-specifications}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module packaging >= 24.2}
BuildRequires:  %{python_module pytest-subtests >= 0.14.1}
# /SECTION
%endif
BuildRequires:  fdupes
Requires:       python-attrs >= 22.2.0
Requires:       python-rpds-py >= 0.7.0
Requires:       python-typing_extensions >= 4.4.0
BuildArch:      noarch
%python_subpackages

%description
JSON Referencing + Python

%prep
%setup -q -n referencing-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if %{without test}
%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING
%{python_sitelib}/referencing/
%{python_sitelib}/referencing-%{version}.dist-info/
%endif

%changelog
