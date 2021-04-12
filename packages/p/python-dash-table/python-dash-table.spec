#
# spec file for package python-dash-table-test
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
# Upstream cannot tag the release version, due to a Julia bug,
# but we need the github archive for the test files
# https://github.com/plotly/dash-table/issues/850
# get this from the master branch (dev is the default but does not have the full package)
%define commit 6dba4d539674b91a073a5e13dd344654390ce4f7
Name:           python-dash-table%{psuffix}
Version:        4.11.3
Release:        0
Summary:        Dash table
License:        MIT
URL:            https://github.com/plotly/dash-table
Source:         https://github.com/plotly/dash-table/archive/%{commit}.tar.gz#/dash-table-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module dash}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
An interactive DataTable for Dash.

%prep
%setup -q -n dash-table-%{commit}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest tests/unit
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/dash_table/
%{python_sitelib}/dash_table-%{version}*-info
%endif

%changelog
