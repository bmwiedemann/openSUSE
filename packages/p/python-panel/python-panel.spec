#
# spec file for package python-panel
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%global skip_python39 1
Name:           python-panel%{psuffix}
Version:        1.4.1
Release:        0
Summary:        A high level app and dashboarding solution for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/holoviz/panel
Source0:        https://files.pythonhosted.org/packages/py3/p/panel/panel-%{version}-py3-none-any.whl
Source99:       python-panel-rpmlintrc
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module bokeh >= 3.4.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module param >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 2.0.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm >= 4.48.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros
Requires:       python-Markdown
Requires:       python-bleach
Requires:       python-bokeh >= 3.2.0
Requires:       python-linkify-it-py
Requires:       python-markdown-it-py
Requires:       python-mdit-py-plugins
Requires:       python-pandas >= 1.2
Requires:       python-param >= 2.0.0
Requires:       python-pyviz_comms >= 2.0.0
Requires:       python-requests
Requires:       python-tqdm >= 4.48.0
Requires:       python-typing_extensions
Requires:       python-xyzservices >= 2021.09.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     jupyter-panel
Recommends:     python-Pillow
Recommends:     python-holoviews >= 1.16.0
Recommends:     python-jupyterlab
Recommends:     python-matplotlib
Recommends:     python-plotly
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module altair}
BuildRequires:  %{python_module asyncio}
BuildRequires:  %{python_module diskcache}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module holoviews >= 1.16.0}
BuildRequires:  %{python_module ipympl}
BuildRequires:  %{python_module ipython >= 7.0}
BuildRequires:  %{python_module panel = %{version}}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module plotly >= 4.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module streamz}
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
Requires:       python3dist(panel) = %{version}
Suggests:       python3-panel

%description -n jupyter-panel
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

This package contains the notebook and server extension configuration common
to all Python flavors.

%prep
%setup -q -c -T
%if %{with test}
%python_expand mkdir -p build && unzip %{SOURCE0} -d build/
%endif

%build
# not needed

%if ! %{with test}
%install
%pyproject_install %{SOURCE0}
%python_clone -a %{buildroot}%{_bindir}/panel
%python_expand %fdupes %{buildroot}%{$python_sitelib}
cp %{buildroot}%{python_sitelib}/panel-%{version}.dist-info/LICENSE.txt .
%endif

%if %{with test}
%check
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
# DISABLE TESTS REQUIRING NETWORK ACCESS
donttest="test_loading_a_image_from_url"
donttest="$donttest or test_png_native_size_embed"
donttest="$donttest or test_png_embed_scaled_fixed_size"
donttest="$donttest or (test_png_scale_ and True)"
donttest="$donttest or (test_png_stretch_ and True)"
donttest="$donttest or (test_svg_native_size and True)"
donttest="$donttest or (test_svg_scaled_fixed_size and True)"
donttest="$donttest or (test_svg_scale_ and True)"
donttest="$donttest or (test_svg_stretch_ and True)"
# flaky async test
donttest="$donttest or test_server_async_callbacks"
# flaky timeout
donttest="$donttest or test_server_thread_pool_change_event or test_server_on_load_after_init"
# upstream skips it for win and osx, we skip it because it (flakily) terminates everything on aarch64
donttest="$donttest or (test_terminal and test_subprocess)"
# file sample.pdf missing
donttest="$donttest or test_pdf_local_file"
# Don't test on 32-bit: asyncio is too flaky
[ $(getconf LONG_BIT) -eq 32 ] && exit 0
#
%pytest build/panel -n auto -rsfE -k "not ($donttest)"
%endif

%post
%python_install_alternative panel

%postun
%python_uninstall_alternative panel

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%python_alternative %{_bindir}/panel
%{python_sitelib}/panel
%{python_sitelib}/panel-%{version}.dist-info

%files -n jupyter-panel
%license LICENSE.txt
%{_jupyter_config} %{_jupyter_servextension_confdir}/panel-client-jupyter.json
%{_jupyter_config} %{_jupyter_server_confdir}/panel-client-jupyter.json
%endif

%changelog
