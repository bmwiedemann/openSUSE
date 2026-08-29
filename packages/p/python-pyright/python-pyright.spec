#
# spec file for package python-pyright
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


%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
%{?sle15_python_module_pythons}
Name:           python-pyright
Version:        1.1.411
Release:        0
Summary:        Command line wrapper for pyright
License:        MIT
URL:            https://github.com/RobertCraigie/pyright-python
Source0:        https://github.com/RobertCraigie/pyright-python/archive/refs/tags/v%{version}.tar.gz#/pyright-%{version}.tar.gz
Source1:        generate-package-json.py
Source10:       package.json
Source11:       package-lock.json
Source12:       node_modules.spec.inc
# PATCH-FIX-OPENSUSE system-node.patch -- Use system Node.js and the vendored npm payload
Patch0:         system-node.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-subprocess}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       nodejs >= 14.0.0
Requires:       nodejs-common
BuildArch:      noarch
%include %{_sourcedir}/node_modules.spec.inc
# SECTION test requirements
BuildRequires:  %{python_module typing_extensions >= 4.1}
# /SECTION
%python_subpackages

%description
Command line wrapper for pyright

%prep
%autosetup -p1 -n pyright-python-%{version}
cp -p %{SOURCE10} package.json
cp -p %{SOURCE11} package-lock.json
local-npm-registry %{_sourcedir} install --omit=dev --omit=optional --ignore-scripts --no-audit --no-fund --update-notifier=false
test "$(node -p "require('./node_modules/pyright/package.json').version")" = "%{version}"
! find node_modules/pyright -type f \( -name "*.node" -o -name "*.dll" -o -name "*.exe" \) -print -quit | grep -q .
rm -rf src/pyright/dist
mv node_modules/pyright src/pyright/dist
# Fix env-script-interpreter rpmlint error
sed -i 's|#!/usr/bin/env node|#!/usr/bin/node|' src/pyright/dist/*.js
rm -rf node_modules package.json package-lock.json
find . -name \*.pyi -empty -print -delete

%build
%pyproject_wheel

%check
# NOTE: disable test_main.py, test_node.py, and test_langserver.py as the tests
# required internet access, by attempting to download the version
# file from the main server at
# https://raw.githubusercontent.com/microsoft/pylance-release/main/releases/{pylance_version}.json
%pytest --ignore tests/test_main.py --ignore tests/test_langserver.py --ignore tests/test_node.py
%python_expand PYTHONPATH=src $python -m pyright --version | grep -Fx "pyright %{version}"

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyright
%python_clone -a %{buildroot}%{_bindir}/pyright-python
%python_clone -a %{buildroot}%{_bindir}/pyright-langserver
%python_clone -a %{buildroot}%{_bindir}/pyright-python-langserver
%python_group_libalternatives pyright pyright-python pyright-langserver pyright-python-langserver
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{_bindir}

%pre
%python_libalternatives_reset_alternative pyright

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyright
%python_alternative %{_bindir}/pyright-python
%python_alternative %{_bindir}/pyright-langserver
%python_alternative %{_bindir}/pyright-python-langserver
%{python_sitelib}/pyright
%{python_sitelib}/pyright-%{version}.dist-info

%changelog
