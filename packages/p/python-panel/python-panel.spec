#
# spec file for package python-panel
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

# too flaky server-side. Test it locally
%bcond_with servertests

# truncate trailing suffix
%define distversion 1.5.5
Name:           python-panel%{psuffix}
Version:        1.5.5
Release:        0
Summary:        A high level app and dashboarding solution for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/holoviz/panel
Source0:        https://files.pythonhosted.org/packages/source/p/panel/panel-%{version}.tar.gz
# package-lock.json file generated with procedure:
# - delete old package-lock.json in panel subdirectory
# - add '"typescript": "^5.1.0"' to package.json devDependencies
# - npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source10:       package-lock.json
# node_modules generated using "osc service mr" with https://github.com/openSUSE/obs-service-node_modules
Source11:       node_modules.spec.inc
Source99:       python-panel-rpmlintrc
%include        %{_sourcedir}/node_modules.spec.inc
# PATCH-FEATURE-OPENSUSE opensuse-js-fixes.patch boo#1231254 gh#openSUSE/obs-service-node_modules#41
Patch0:         opensuse-js-fixes.patch
# PATCH-FIX-UPSTREAM manual-asyncio-loop.patch https://github.com/holoviz/panel/pull/7591
Patch1:         manual-asyncio-loop.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module bokeh >= 3.5.0 with %python-bokeh < 3.7}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module param >= 2.1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyviz-comms >= 2.0.0}
BuildRequires:  %{python_module requests}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
Requires:       python-Markdown
Requires:       python-bleach
Requires:       python-linkify-it-py
Requires:       python-markdown-it-py
Requires:       python-mdit-py-plugins
Requires:       python-packaging
Requires:       python-pandas >= 1.2
Requires:       python-pyviz_comms >= 2.0.0
Requires:       python-requests
Requires:       python-tqdm
Requires:       python-typing_extensions
Requires:       (python-bokeh >= 3.5.0 with python-bokeh < 3.7)
Requires:       (python-param >= 2.1 with python-param < 3)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     jupyter-panel
Recommends:     python-Pillow
Recommends:     python-holoviews >= 1.18.0
Recommends:     python-jupyterlab
Recommends:     python-matplotlib
Recommends:     python-plotly
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module panel = %{version}}
##
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module altair}
BuildRequires:  %{python_module diskcache}
BuildRequires:  %{python_module holoviews >= 1.16.0}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module streamz}
BuildRequires:  esbuild
BuildRequires:  unzip
# Tests segfault
# BuildRequires:  %%{python_module vtk}
%endif
%python_subpackages

%description
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

%package     -n jupyter-panel
Summary:        Jupyter notebook and server cofiguration for python-panel
Group:          Development/Languages/Python
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(panel) = %{distversion}
Requires:       jupyter-bokeh
Suggests:       python3-panel

%description -n jupyter-panel
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

This package contains the notebook and server extension configuration common
to all Python flavors.

%prep
%autosetup -p1 -n panel-%{version}
# no color for pytest
sed -i '/addopts/ s/--color=yes//' pyproject.toml
sed -i /asyncio_default_fixture_loop_scope/d pyproject.toml
rm panel/.eslintrc.js
for p in panel/tests/io/reload_module.py
do \
    [ -f $p -a ! -s $p ] || exit 1 && echo "# Empty module" > $p
done
# Resources are already bundled in sdist
sed -i 's|bundle_resources()$|assert os.path.exists("panel/dist/bundled/font-awesome")|' hatch_build.py
pushd panel
rm package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --include=peer
popd

%if ! %{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/panel
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
# test_compile tries to build and write next to the imported module: permission denied
export PYTHONPATH=":x"
# no network connection in obs
deselectmark=(-m "not internet")
# no multiflavor playwright
ignorefiles=(--ignore scripts/panelite/test/test_utils.py --ignore scripts/panelite/test/test_panelite.py)
# upstream skips it for win and osx, we skip it because it (flakily) terminates everything on aarch64
donttest="(test_terminal and test_subprocess)"
# file sample.pdf missing
donttest="$donttest or test_pdf_local_file"
%if !%{with servertests}
# flaky async tests
donttest="$donttest or test_server"
%endif
%pytest -n auto -rsfE -k "not ($donttest)" "${deselectmark[@]}" "${ignorefiles[@]}" -p no:unraisableexception
%endif

%post
%python_install_alternative panel

%postun
%python_uninstall_alternative panel

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/panel
%{python_sitelib}/panel
%{python_sitelib}/panel-%{version}.dist-info

%files -n jupyter-panel
%license LICENSE.txt
%{_jupyter_config} %{_jupyter_servextension_confdir}/panel-client-jupyter.json
%{_jupyter_config} %{_jupyter_server_confdir}/panel-client-jupyter.json
%endif

%changelog
