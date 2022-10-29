#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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

%bcond_without libalternatives

Name:           python-voila%{psuffix}
Version:        0.4.0
Release:        0
Summary:        Plugin for serving read-only live Jupyter notebooks
License:        BSD-3-Clause
URL:            https://github.com/voila-dashboards/voila
# Need both source archives: PyPI wheel for the npm compiled JS static files, GitHub for the tests
Source0:        https://github.com/voila-dashboards/voila/archive/refs/tags/v%{version}.tar.gz#/voila-%{version}-gh.tar.gz
Source1:        https://files.pythonhosted.org/packages/py3/v/voila/voila-%{version}-py3-none-any.whl
Source99:       python-voila-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-voila = %{version}
Requires:       python-jupyter-core >= 4.11
Requires:       python-websockets >= 9.0
Requires:       (python-jupyter-client >= 6.1.3 with python-jupyter-client < 7.4.2)
Requires:       (python-jupyter-server >= 1.18 with python-jupyter-server < 2)
Requires:       (python-jupyterlab-server >= 2.3.0 with python-jupyterlab-server < 3)
Requires:       (python-nbclient >= 0.4.0 with python-nbclient < 0.8)
Requires:       (python-nbconvert >= 6.4.5 with python-nbconvert < 8)
Requires:       (python-traitlets >= 5.0.3 with python-traitlets < 6)
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module matplotlib-web}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module papermill}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module voila = %{version}}
%endif
%python_subpackages

%description
Voila serves live Jupyter notebook including Jupyter interactive widgets.

Unlike the usual HTML-converted notebooks, each user connecting to the Voila
tornado application gets a dedicated Jupyter kernel which can execute the
callbacks to changes in Jupyter interactive widgets.

By default, voila disallows execute requests from the front-end, disabling
the ability to execute arbitrary code. By default, voila runs with the
strip_source option, which strips out the input cells from the rendered
notebook. When using these default settings, the code powering the Jupyter
notebook is never sent to the front-end.

This package provides the python interface.

%package     -n jupyter-voila
Summary:        Plugin for serving read-only live Jupyter notebooksmacros
Requires:       python3-voila = %{version}

%description -n jupyter-voila
Voila serves live Jupyter notebook including Jupyter interactive widgets.

Unlike the usual HTML-converted notebooks, each user connecting to the Voila
tornado application gets a dedicated Jupyter kernel which can execute the
callbacks to changes in Jupyter interactive widgets.

By default, voila disallows execute requests from the front-end, disabling
the ability to execute arbitrary code. By default, voila runs with the
strip_source option, which strips out the input cells from the rendered
notebook. When using these default settings, the code powering the Jupyter
notebook is never sent to the front-end.

This package provides the jupyter components.

%prep
%autosetup -p1 -n voila-%{version}

%build
# Source1 wheel is pre-built (npm through hatchling jupyter-builder, not possible offline)

%if !%{with test}
%install
%pyproject_install %{SOURCE1}
%python_clone -a %{buildroot}%{_bindir}/voila
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
%endif

%if %{with test}
%check
export JUPYTER_PATH=%{_jupyter_prefix}:$PWD/tests/test_template/share/jupyter:$PWD/tests/skip_template/share/jupyter/
export VOILA_TEST_DEBUG=1
# very flaky in obs environments
donttest="test_kernel_death or test_request_with_query"
%pytest tests -k "not ($donttest)"  --reruns 2 --reruns-delay 1
%endif

%if !%{with test}
%pre
%python_libalternatives_reset_alternative voila

%post
%python_install_alternative voila

%postun
%python_uninstall_alternative voila

%files %{python_files}
%license LICENSE
%{python_sitelib}/voila-%{version}*-info
%{python_sitelib}/voila/
%python_alternative %{_bindir}/voila

%files -n jupyter-voila
%license LICENSE
%doc README.md
%{?_jupyter_config} %{_jupyter_servextension_confdir}/voila.json
%{?_jupyter_config} %{_jupyter_server_confdir}/voila.json
%{?_jupyter_config} %{_jupyter_nb_notebook_confdir}/voila.json
%{_jupyter_nbextension_dir}/voila/
%dir %{_jupyter_labextensions_dir3}/@voila-dashboards/
%{_jupyter_labextensions_dir3}/@voila-dashboards/jupyterlab-preview
%{_jupyter_prefix}/voila/
%endif

%changelog
