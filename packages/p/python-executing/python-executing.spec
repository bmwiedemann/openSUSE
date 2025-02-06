#
# spec file for package python-executing
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
Name:           python-executing%{psuffix}
Version:        2.1.0
Release:        0
Summary:        Get the currently executing AST node of a frame, and other information
License:        MIT
URL:            https://github.com/alexmojaki/executing
Source:         https://files.pythonhosted.org/packages/source/e/executing/executing-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/alexmojaki/executing/pull/86 fix: backward compatibility fix for changed source positions in 3.12.6
Patch0:         new-python-312.patch
# PATCH-FIX-UPSTREAM https://github.com/alexmojaki/executing/pull/94 fix: check for pytest compatibility
Patch1:         pytest.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 4.0.0}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module asttokens}
%if 0%{?suse_version} > 1600
BuildRequires:  %{python_module ipython}
%endif
BuildRequires:  %{python_module littleutils}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
%endif
%python_subpackages

%description
Get the currently executing AST node of a frame, and other information

%prep
%autosetup -p1 -n executing-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}

# Don't have ipython build requirement in Leap
%if 0%{?suse_version} <= 1600
%pytest -k "not test_ipython"
%else
%pytest
%endif

%endif

%if %{without test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/executing
%{python_sitelib}/executing-%{version}.dist-info
%endif

%changelog
