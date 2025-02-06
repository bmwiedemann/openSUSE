#
# spec file for package python-inline-snapshot
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
Name:           python-inline-snapshot%{psuffix}
Version:        0.19.3
Release:        0
Summary:        Create and update inline snapshots in your Python code
License:        MIT
URL:            https://github.com/15r10nk/inline-snapshot/
Source:         https://files.pythonhosted.org/packages/source/i/inline-snapshot/inline_snapshot-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module black >= 23.3.0}
BuildRequires:  %{python_module click >= 8.1.4}
BuildRequires:  %{python_module dirty-equals >= 0.7.0}
BuildRequires:  %{python_module hypothesis >= 6.75.5}
BuildRequires:  %{python_module inline-snapshot = %{version}}
BuildRequires:  %{python_module mypy >= 1.2.0}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pyright >= 1.1.359}
BuildRequires:  %{python_module pytest-freezer >= 0.4.8}
BuildRequires:  %{python_module pytest-mock >= 3.14.0}
BuildRequires:  %{python_module pytest-subtests >= 0.11.0}
BuildRequires:  %{python_module pytest-xdist >= 3.6.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module time-machine >= 2.10.0}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-asttokens >= 2.0.5
Requires:       python-executing >= 2.0.0
Requires:       python-rich >= 13.7.1
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 2.0.0
%endif
Suggests:       python-black >= 23.3
Suggests:       python-click >= 8.1.4
Suggests:       python-dirty-equals >= 0.9
BuildArch:      noarch
%python_subpackages

%description
Create and update inline snapshots in your Python code.

%prep
%autosetup -p1 -n inline_snapshot-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
#NOTE: disable test_typing because the underlying pyright module uses
# nodeenv, which required https connection to nodejs.org. This is not
# possible in OBS.
%if %{with test}
%pytest -v -k 'not (test_typing or test_format_command_fail)'
%endif

%if %{without test}
%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/inline_snapshot
%{python_sitelib}/inline_snapshot-%{version}.dist-info
%endif

%changelog
