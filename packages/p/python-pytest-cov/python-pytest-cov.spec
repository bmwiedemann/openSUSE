#
# spec file for package python-pytest-cov
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%bcond_without test
%define psuffix -%{flavor}
%else
%bcond_with test
%define psuffix %{nil}
%endif
%{?sle15_python_module_pythons}
Name:           python-pytest-cov%{psuffix}
Version:        7.0.0
Release:        0
Summary:        Pytest plugin for coverage reporting
License:        MIT
URL:            https://github.com/pytest-dev/pytest-cov
Source:         https://files.pythonhosted.org/packages/source/p/pytest-cov/pytest_cov-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pytest-dev/pytest-cov/pull/722 match coverage 7.10.7 warnings
Patch0:         0001-match-coverage-7.10.7-warnings.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
%if %{with test}
BuildRequires:  %{python_module coverage >= 7.10.6}
BuildRequires:  %{python_module fields}
BuildRequires:  %{python_module process-tests}
BuildRequires:  %{python_module pytest-cov = %{version}}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module virtualenv}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage >= 7.10.6
Requires:       python-pluggy >= 1.2
Requires:       python-pytest >= 6.2.5
BuildArch:      noarch
%python_subpackages

%description
This plugin produces coverage reports.  It supports centralised testing
and distributed testing in both load and each modes.  It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%prep
%autosetup -p1 -n pytest_cov-%{version}

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/
%endif

%check
%if %{with test}
echo "import site;site.addsitedir(\"$(pwd)/src\")" > tests/sitecustomize.py
# test_dist_missing_data - needs internet access
# test_central_subprocess_change_cwd_with_pythonpath - needs pytest cov in venv which is not doable in OBS build
donttest="test_dist_missing_data or test_central_subprocess_change_cwd_with_pythonpath"
# test_celery - requires testcontainers, not packaged
donttest+=" or test_celery"
# Broken with new version of coverage
donttest+=" or test_subprocess_with_path_aliasing or test_central_subprocess"
donttest+=" or test_dist_subprocess_not_collocated or test_cleanup_on_sigterm"
donttest+=" or test_append_coverage_subprocess or test_dist_subprocess_collocated"
# Broken with Python 3.14 https://github.com/pytest-dev/pytest-cov/issues/719
donttest+=" or test_contexts"
%pytest -v -k "not (${donttest})"
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/pytest_cov
%{python_sitelib}/pytest_cov-%{version}.dist-info
%endif

%changelog
