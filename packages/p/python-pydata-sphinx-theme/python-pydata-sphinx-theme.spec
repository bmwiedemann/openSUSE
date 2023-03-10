#
# spec file for package python-pydata-sphinx-theme
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pydata-sphinx-theme
Version:        0.13.1
Release:        0
Summary:        Bootstrap-based Sphinx theme from the PyData community
License:        BSD-3-Clause
URL:            https://github.com/pydata/pydata-sphinx-theme
Source:         pydata-sphinx-theme-%{version}.tar.gz
# Source: https://files.pythonhosted.org/packages/source/p/pydata-sphinx-theme/pydata_sphinx_theme-%%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        python-pydata-sphinx-theme-%{version}-vendor.tar.xz
Source2:        python-pydata-sphinx-theme-%{version}-vendor-licenses.txt
Source99:       prepare_vendor.sh
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx-theme-builder}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-beautifulsoup4
Requires:       python-docutils
Requires:       python-sphinx-theme-builder
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
BuildRequires:  %{python_module accessible-pygments}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module docutils}
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs19
BuildRequires:  nodejs19-devel
BuildRequires:  yarn

# /SECTION
%python_subpackages

%description
Bootstrap-based Sphinx theme from the PyData community

%prep
%autosetup -p1 -n pydata-sphinx-theme-%{version} -a1
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

# Create a node header tarball so we don't try to download it
mkdir -p node-v%{nodejs_version}/include
cp -a %{_includedir}/node19 node-v%{nodejs_version}/include/node
tar czf node-v%{nodejs_version}-headers.tar.gz node-v%{nodejs_version}
echo "tarball=\"$PWD/node-v%{nodejs_version}-headers.tar.gz\"" > .npmrc

%build
export STB_USE_SYSTEM_NODE=1
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/.package-cache"
export NODE_OPTIONS=--openssl-legacy-provider
yarn install --offline

# nodeenv generated with python3, no need to generate a different
# nodeenv for each flavor
python3 -m nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pydata_sphinx_theme*

%changelog
