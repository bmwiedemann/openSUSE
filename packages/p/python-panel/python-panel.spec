#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-panel%{psuffix}
Version:        1.1.0
Release:        0
Summary:        A high level app and dashboarding solution for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://panel.holoviz.org
Source:         https://files.pythonhosted.org/packages/source/p/panel/panel-%{version}.tar.gz
Source99:       python-panel-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module bokeh >= 3.1.1 with %python-bokeh < 3.2}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module param >= 1.9.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyct >= 0.4.4}
BuildRequires:  %{python_module pyviz-comms >= 0.7.4}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm >= 4.48.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module altair}
BuildRequires:  %{python_module diskcache}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module folium}
BuildRequires:  %{python_module holoviews >= 1.16.0}
BuildRequires:  %{python_module ipympl}
BuildRequires:  %{python_module ipython >= 7.0}
BuildRequires:  %{python_module panel = %{version}}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module plotly >= 4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module streamz}
# Tests segfault
# BuildRequires:  %%{python_module vtk}
%endif
Requires:       jupyter-panel
Requires:       python-Markdown
Requires:       python-bleach
Requires:       python-linkify-it-py
Requires:       python-markdown-it-py < 3
Requires:       python-mdit-py-plugins
Requires:       python-pandas >= 1.2
Requires:       python-param >= 1.12.0
Requires:       python-pyviz_comms >= 0.7.4
Requires:       python-requests
Requires:       python-tqdm >= 4.48.0
Requires:       python-typing_extensions
Requires:       python-xyzservices >= 2021.09.1
Requires:       (python-bokeh >= 3.1.1 with python-bokeh  < 3.2.0)
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-Pillow
Recommends:     python-holoviews >= 1.16.0
Recommends:     python-jupyterlab
Recommends:     python-matplotlib
Recommends:     python-plotly
BuildArch:      noarch
%python_subpackages

%description
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

%package -n jupyter-panel
Summary:        Jupyter notebook and server cofiguration for python-panel
Group:          Development/Languages/Python

%description -n jupyter-panel
Panel is a Python library that lets you create custom interactive web apps and
dashboards by connecting user-defined widgets to plots, images, tables, or
text.

This package contains the notebook and server extension configuration common
to all Python flavors.

%prep
%autosetup -p1 -n panel-%{version}
# Do not try to rebuild the bundled npm stuff. We don't have network. Just use the shipped bundle.
sed -i '/def _build_paneljs/ a \    return' setup.py
for p in panel/tests/io/reload_module.py
do \
    [ -f $p -a ! -s $p ] || exit 1 && echo "# Empty module" > $p
done
for p in panel/dist/css/regular_table.css \
  panel/dist/bundled/perspective/@finos/perspective-viewer@1.9.3/dist/css/variables.css
do \
    [ -f $p -a ! -s $p ] || exit 1 && echo "// Empty css" > $p
done

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
%pytest -ra -k "not ($donttest)"
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
%_jupyter_config %{_jupyter_servextension_confdir}/panel-client-jupyter.json
%_jupyter_config %{_jupyter_server_confdir}/panel-client-jupyter.json

%endif

%changelog
