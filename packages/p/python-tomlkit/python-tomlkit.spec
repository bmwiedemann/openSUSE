#
# spec file for package python-tomlkit
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%{?pythons_for_pypi}
%endif
%{?sle15_python_module_pythons}
Name:           python-tomlkit%{psuffix}
Version:        0.15.1
Release:        0
Summary:        Style preserving TOML library
License:        MIT
URL:            https://github.com/sdispater/tomlkit
Source:         https://files.pythonhosted.org/packages/source/t/tomlkit/tomlkit-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomlkit = %{version}}
%endif
BuildArch:      noarch
%python_subpackages

%description
Style preserving TOML library

%prep
%setup -q -n tomlkit-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/tomlkit
%{python_sitelib}/tomlkit-%{version}*-info
%endif

%changelog
