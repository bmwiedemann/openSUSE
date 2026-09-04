#
# spec file for package python-pydata-sphinx-theme
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


%define skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-pydata-sphinx-theme
Version:        0.21.0
Release:        0
Summary:        Bootstrap-based Sphinx theme from the PyData community
License:        BSD-3-Clause
URL:            https://github.com/pydata/pydata-sphinx-theme
Source:         https://files.pythonhosted.org/packages/source/p/pydata-sphinx-theme/pydata_sphinx_theme-%{version}.tar.gz#/pydata-sphinx-theme-%{version}.tar.gz
# package-lock.json file generated with command:
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source1:        package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source2:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx-theme-builder}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
Requires:       python-Babel
Requires:       python-Jinja2
Requires:       python-Sphinx
Requires:       python-accessible-pygments
Requires:       python-beautifulsoup4
Requires:       python-docutils
Requires:       python-pygments
Requires:       python-requests
Suggests:       python-beautifulsoup4
Suggests:       python-codecov
Suggests:       python-docutils
Suggests:       python-jupyter_sphinx
Suggests:       python-numpy
Suggests:       python-numpydoc
Suggests:       python-pandas
Suggests:       python-plotly
Suggests:       python-recommonmark
Suggests:       python-Sphinx
Suggests:       python-xarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module accessible-pygments}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
BuildRequires:  nodejs-default
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-packaging
BuildRequires:  yarn

# /SECTION
%python_subpackages

%description
Bootstrap-based Sphinx theme from the PyData community

%prep
%autosetup -p1 -n pydata_sphinx_theme-%{version}
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml
local-npm-registry %{_sourcedir} install --include=dev --include=peer

%build
export STB_USE_SYSTEM_NODE=1
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export NODE_OPTIONS=--openssl-legacy-provider

# nodeenv generated with python3, no need to generate a different
# nodeenv for each flavor
python%python_bin_suffix -m nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/pydata_sphinx_theme/theme/pydata_sphinx_theme/static/.gitignore
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No python-playwrite optional dependency gh#pydata/pydata-sphinx-theme#1541
donttest="test_pygments_fallbacks"
%pytest -k "not $donttest"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pydata_sphinx_theme
%{python_sitelib}/pydata_sphinx_theme-%{version}*info

%changelog
