#
# spec file for package python-jupyterlab
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


%define distversion 4.3.5
Name:           python-jupyterlab
Version:        4.3.5
Release:        0
Summary:        Environment for interactive and reproducible computing
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab
Source0:        https://files.pythonhosted.org/packages/source/j/jupyterlab/jupyterlab-%{version}.tar.gz
Source99:       python-jupyterlab-rpmlintrc
BuildRequires:  %{python_module Jinja2 >= 3.0.3}
BuildRequires:  %{python_module async_lru >= 1.0.0}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.25.0}
BuildRequires:  %{python_module importlib-metadata >= 4.8.3 if %python-base < 3.10}
BuildRequires:  %{python_module importlib-resources >= 1.4 if %python-base < 3.9}
BuildRequires:  %{python_module ipykernel >= 6.5.0}
BuildRequires:  %{python_module jupyter-lsp >= 2.0.0}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module jupyter_server >= 2.4.0 with %python-jupyter_server < 3}
BuildRequires:  %{python_module jupyterlab_server >= 2.27.1 with %python-jupyterlab_server < 3}
BuildRequires:  %{python_module notebook_shim >= 0.2}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module tomli >= 1.2.2 if %python-base < 3.11}
BuildRequires:  %{python_module tornado >= 6.2.0}
BuildRequires:  %{python_module traitlets}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       jupyter-jupyterlab = %{version}
Requires:       python-Jinja2 >= 3.0.3
Requires:       python-async_lru >= 1.0.0
Requires:       python-httpx >= 0.25.0
Requires:       python-ipykernel >= 6.5.0
Requires:       python-jupyter-lsp >= 2.0.0
Requires:       python-jupyter_core
Requires:       python-notebook_shim >= 0.2
Requires:       python-packaging
Requires:       python-setuptools >= 40.1
Requires:       python-tornado >= 6.2.0
Requires:       python-traitlets
Requires:       (python-importlib-metadata >= 4.8.3 if python-base < 3.10)
Requires:       (python-importlib-resources >= 1.4 if python-base < 3.9)
Requires:       (python-jupyter_server >= 2.4.0 with python-jupyter_server < 3)
Requires:       (python-jupyterlab_server >= 2.27.1 with python-jupyterlab_server < 3)
Requires:       (python-tomli >= 1.2.2 if python-base < 3.11)
Suggests:       python-jupyter-collaboration >= 1
Provides:       python-jupyter_jupyterlab = %{version}
Obsoletes:      python-jupyter_jupyterlab < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jupyterlab-server-test}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-check-links}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-jupyter >= 0.5.3}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module virtualenv}
# /SECTION
%python_subpackages

%description
An extensible environment for interactive and reproducible computing,
based on the Jupyter Notebook and Architecture.

JupyterLab is the next-generation user interface for Project Jupyter
offering all the familiar building blocks of the classic Jupyter
Notebook (notebook, terminal, text editor, file browser, rich outputs,
etc.).

%package     -n jupyter-jupyterlab
Summary:        Environment for interactive and reproducible computing
Group:          Development/Languages/Python
Requires:       jupyter-jupyterlab-filesystem
Requires:       nodejs >= 10
Requires:       npm >= 10
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(jupyterlab) = %{distversion}
Suggests:       python3-jupyterlab
Provides:       jupyter-jupyterlab-discovery = 6
Obsoletes:      jupyter-jupyterlab-discovery < 6

%description -n jupyter-jupyterlab
An extensible environment for interactive and reproducible computing,
based on the Jupyter Notebook and Architecture.

JupyterLab is the next-generation user interface for Project Jupyter
offering all the familiar building blocks of the classic Jupyter
Notebook (notebook, terminal, text editor, file browser, rich outputs,
etc.).

%prep
%autosetup -p1 -n jupyterlab-%{version}
sed -i -e 's|^#!%{_bindir}/env node|#!%{_bindir}/node|' jupyterlab/staging/yarn.js
chmod a+x jupyterlab/staging/yarn.js
find jupyterlab -name yarn.lock -delete
find jupyterlab -name .yarnrc.yml -delete

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
%fdupes %{buildroot}%{$python_sitelib}
}
%fdupes %{buildroot}%{_jupyter_prefix}
%python_clone -a %{buildroot}%{_bindir}/jupyter-lab
%python_clone -a %{buildroot}%{_bindir}/jupyter-labextension
%python_clone -a %{buildroot}%{_bindir}/jupyter-labhub
%python_clone -a %{buildroot}%{_bindir}/jlpm

%check
# This is only a rudimentary set of tests which we can run offline using pytest directly. The full test
# suite would use jlpm which needs online connection through npm:
# https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html#build-and-run-the-tests
# Disable build checks that pull in remote resources with npm
donttest="$donttest or (TestExtension and test_app_dir)"
donttest="$donttest or (TestExtension and test_build)"
donttest="$donttest or (TestExtension and test_disable_extension)"
donttest="$donttest or (TestExtension and test_enable_extension)"
donttest="$donttest or (TestExtension and test_list_extension)"
donttest="$donttest or (TestExtension and test_link)"
donttest="$donttest or (TestExtension and test_unlink)"
donttest="$donttest or (TestExtension and test_install)"
donttest="$donttest or (TestExtension and test_uninstall)"
donttest="$donttest or (TestExtension and test_update)"
donttest="$donttest or (TestAppHandlerRegistry and test_get_registry)"
donttest="$donttest or (TestAppHandlerRegistry and test_populate_staging)"
donttest="$donttest or (TestAppHandlerRegistry and test_yarn_config)"
donttest="$donttest or (TestBuildAPI and test_build)"
%pytest -k "not (${donttest:4} ${$python_donttest})"

%post
%python_install_alternative jupyter-lab jupyter-labextension jupyter-labhub jlpm

%postun
%python_uninstall_alternative jupyter-lab

%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyterlab/
%{python_sitelib}/jupyterlab-%{version}.dist-info/
%python_alternative %{_bindir}/jupyter-lab
%python_alternative %{_bindir}/jupyter-labextension
%python_alternative %{_bindir}/jupyter-labhub
%python_alternative %{_bindir}/jlpm

%files -n jupyter-jupyterlab
%license LICENSE
%{_jupyter_config} %{_jupyter_servextension_confdir}/jupyterlab.json
%{_jupyter_config} %{_jupyter_server_confdir}/jupyterlab.json
%{_jupyter_lab_dir}
%{_datadir}/applications/jupyterlab.desktop
%{_datadir}/icons/hicolor/scalable/apps/jupyterlab.svg

%changelog
