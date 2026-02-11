#
# spec file for package python-pytest_rerunfailures
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


%{?sle15_python_module_pythons}
Name:           python-pytest-rerunfailures
Version:        16.1
Release:        0
Summary:        A pytest plugin to re-run tests
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-rerunfailures
Source:         https://files.pythonhosted.org/packages/source/p/pytest-rerunfailures/pytest_rerunfailures-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 17.1
Requires:       python-pytest >= 8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.0}
BuildRequires:  %{python_module pytest-xdist >= 2.3.0}
# /SECTION
%python_subpackages

%description
The pytest-rerunfailures package is a plugin for Pytest that re-runs
tests to eliminate intermittent failures.

%prep
%setup -q -n pytest_rerunfailures-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/pytest-dev/pytest-rerunfailures/issues/267
donttest="test_run_session_teardown_once_after_reruns "
donttest+="or test_exception_matches_rerun_except_query "
donttest+="or test_exception_not_match_rerun_except_query "
donttest+="or test_exception_matches_only_rerun_query "
donttest+="or test_exception_match_only_rerun_in_dual_query"
%pytest -k "not (${donttest})"

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_rerunfailures.py
%pycache_only %{python_sitelib}/__pycache__/pytest_rerunfailures*pyc
%{python_sitelib}/pytest_rerunfailures-%{version}.dist-info

%changelog
