#
# spec file for package python-pytest-html
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-pytest-html
Version:        4.1.1
Release:        0
Summary:        Pytest plugin for generating HTML reports
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-html
Source:         https://files.pythonhosted.org/packages/source/p/pytest-html/pytest_html-%{version}.tar.gz
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source10:       package-lock.json
Source11:       node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
# PATCH-FIX-OPENSUSE drop-assertpy-dep.patch
Patch1:         drop-assertpy-dep.patch
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  local-npm-registry
BuildRequires:  npm
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 3.0.0
Requires:       python-pytest >= 7.0.0
Requires:       python-pytest-metadata >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 3.0.0}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module pytest-metadata >= 3.0.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
%python_subpackages

%description
A plugin for pytest that generates a HTML report for test results.

%prep
%autosetup -p1 -n pytest_html-%{version}
rm package-lock.json
local-npm-registry %{_sourcedir} install --also=dev
sed -i '/npm ci/d' scripts/npm.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest --ignore testing/test_integration.py --ignore testing/test_e2e.py

%files %{python_files}
%license LICENSE
%doc docs/changelog.rst README.rst
%{python_sitelib}/pytest_html
%{python_sitelib}/pytest_html-%{version}*-info

%changelog
