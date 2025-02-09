#
# spec file for package python-hatch-requirements-txt
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
Name:           python-hatch-requirements-txt%{psuffix}
Version:        0.4.1
Release:        0
Summary:        Hatchling plugin to read project dependencies from requirements.txt
License:        MIT
URL:            https://github.com/repo-helper/hatch-requirements-txt
Source:         https://github.com/repo-helper/hatch-requirements-txt/archive/refs/tags/v%{version}.tar.gz#/hatch_requirements_txt-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module hatch-requirements-txt = %{version}}
BuildRequires:  %{python_module pkginfo}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-hatchling >= 0.21.0
Requires:       python-packaging >= 21.3
BuildArch:      noarch
%python_subpackages

%description
Hatchling plugin to read project dependencies from requirements.txt

%prep
%autosetup -p1 -n hatch-requirements-txt-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Broken upstream
%pytest -k 'not (test_not_dynamic_but_filename_defined or test_not_dynamic_but_files_defined)'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/hatch_requirements_txt
%{python_sitelib}/hatch_requirements_txt-%{version}.dist-info
%endif

%changelog
