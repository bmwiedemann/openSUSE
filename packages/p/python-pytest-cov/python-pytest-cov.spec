#
# spec file for package python-pytest-cov
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
Name:           python-pytest-cov
Version:        2.11.1
Release:        0
Summary:        Pytest plugin for coverage reporting
License:        MIT
URL:            https://github.com/schlamar/pytest-cov
Source:         https://files.pythonhosted.org/packages/source/p/pytest-cov/pytest-cov-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pytest-dev/pytest-cov#453 work with coverage 5.4
Patch0:         https://github.com/pytest-dev/pytest-cov/pull/453.patch#/pytest-cov-pr453-coverage54.patch
BuildRequires:  %{python_module coverage >= 5.2.1}
BuildRequires:  %{python_module fields}
BuildRequires:  %{python_module process-tests}
BuildRequires:  %{python_module pytest >= 4.6.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage >= 5.2.1
Requires:       python-pytest >= 4.6.0
BuildArch:      noarch
%python_subpackages

%description
This plugin produces coverage reports.  It supports centralised testing
and distributed testing in both load and each modes.  It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%prep
%autosetup -p1 -n pytest-cov-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
# test_dist_missing_data - needs internet access
# test_central_subprocess_change_cwd_with_pythonpath - needs pytest cov in venv which is not doable in OBS build
export PYTHONDONTWRITEBYTECODE=1
echo "import site;site.addsitedir(\"$(pwd)/src\")" > tests/sitecustomize.py
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}:$PWD/tests py.test-%{$python_bin_suffix} -v -k 'not (test_dist_missing_data or test_central_subprocess_change_cwd_with_pythonpath)'

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/pytest-cov.pth
%{python_sitelib}/pytest_cov
%{python_sitelib}/pytest_cov-%{version}-py%{python_version}.egg-info

%changelog
