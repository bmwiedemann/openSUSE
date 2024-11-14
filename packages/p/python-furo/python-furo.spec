#
# spec file for package python-furo
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


Name:           python-furo
Version:        2024.8.6
Release:        0
Summary:        Clean customisable Sphinx documentation theme
# This project is MIT.  Other files bundled with the documentation have the
# following licenses:
# - searchindex.js: BSD-2-Clause
# - _sources/kitchen-sink/*.rst.txt: CC-BY-SA-4.0
# - _sphinx_design_static/*: MIT
# - _static/basic.css: BSD-2-Clause
# - _static/check-solid.svg: MIT
# - _static/clipboard.min.js: MIT
# - _static/copy*: MIT
# - _static/debug.css: MIT
# - _static/demo*.png: MIT
# - _static/design*: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/pied-piper-admonition.css: MIT
# - _static/plus.png: BSD-2-Clause
# - _static/pygments.css: BSD-2-Clause
# - _static/readthedocs-dummy.js: MIT
# - _static/searchtools.js: BSD-2-Clause
# - _static/skeleton.css: MIT
# - _static/sphinx-design.min.css: MIT
# - _static/sphinx_highlight.js: BSD-2-Clause
# - _static/tabs.*: MIT
License:        MIT
URL:            https://pradyunsg.me/furo/
Source0:        https://files.pythonhosted.org/packages/source/f/furo/furo-%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        furo-%{version}-vendor.tar.xz
Source2:        furo-%{version}-vendor-licenses.txt
# Run without any arguments from this directory with the fresh Source0
Source99:       prepare_vendor.sh
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module doc}
BuildRequires:  %{python_module myst-parser}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module sphinx-design}
BuildRequires:  %{python_module sphinx-inline-tabs}
BuildRequires:  %{python_module sphinx-theme-builder >= 0.2.0a10}
BuildRequires:  %{python_module sphinxcontrib-copybutton}
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  npm-default
BuildRequires:  python-rpm-macros
BuildRequires:  rpmdevtools
BuildRequires:  yarn
Requires:       python-Sphinx >= 6.0
Requires:       python-beautifulsoup4
Requires:       python-pygments >= 2.7
Requires:       python-sphinx-basic-ng >= 1.0.0.beta2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 6.0}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module nodeenv}
BuildRequires:  %{python_module pygments >= 2.7}
BuildRequires:  %{python_module sphinx-basic-ng >= 1.0.0.beta2}
BuildRequires:  %{python_module urllib3}
# /SECTION
%python_subpackages

%description
Furo is a Sphinx theme, which is:
- Intentionally minimal --- the most important thing is the content, not
  the scaffolding around it.
- Responsive --- adapting perfectly to the available screen space, to
  work on all sorts of devices.
- Customizable --- change the color palette, font families, logo and
  more!
- Easy to navigate --- with carefully-designed sidebar navigation and
  inter-page links.
- Good looking content --- through clear typography and well-stylized
  elements.
- Good looking search --- helps readers find what they want quickly.
- Biased for smaller docsets --- intended for smaller documentation
  sets, where presenting the entire hierarchy in the sidebar is not
  overwhelming.}

%package -n %{name}-doc
Summary:        Documentation files for %{name}
Group:          Documentation/Other

%description -n %{name}-doc
HTML Documentation and examples for %{name}.

%prep
%autosetup -p1 -a1 -n furo-%{version}
cp -p %{SOURCE2} .

# Don't ship version control files
find . -name .gitignore -delete

# Substitute the installed nodejs version for the requested version
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%build
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Build documentation
export PYTHONPATH=%{buildroot}%{python3_sitelib}
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The tests require web access.  If any tests show up that can be run without a
# network, do this:
#%%pytest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/furo
%{python_sitelib}/furo-%{version}.dist-info

%files -n %{name}-doc
%doc README.md html/
%license LICENSE

%changelog
