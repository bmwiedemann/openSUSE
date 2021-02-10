#
# spec file for package python-jupyterlab
#
# Copyright (c) 2021 SUSE LLC
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


%define _buildshell /bin/bash
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyterlab
Version:        3.0.7
Release:        0
Summary:        Environment for interactive and reproducible computing
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab
# install from wheel with all the bundled nodejs stuff
Source0:        https://files.pythonhosted.org/packages/py3/j/jupyterlab/jupyterlab-%{version}-py3-none-any.whl
Source99:       python-jupyterlab-rpmlintrc
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module jupyter_server >= 1.2}
BuildRequires:  %{python_module jupyterlab-server >= 2.0}
BuildRequires:  %{python_module nbclassic >= 0.2}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tornado >= 6.1}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab = %{version}
Requires:       python-Jinja2 >= 2.10
Requires:       python-ipython
Requires:       python-jupyter_core
Requires:       python-jupyter_server >= 1.2
Requires:       python-jupyterlab-server >= 2.0
Requires:       python-nbclassic >= 0.2
Requires:       python-packaging
Requires:       python-tornado >= 6.1
Provides:       python-jupyter_jupyterlab = %{version}
Obsoletes:      python-jupyter_jupyterlab < %{version}
BuildArch:      noarch
# SECTION test requirements including jupyterlab_server[test] and jupyter_server[test]
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-check-links}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module strict-rfc3339}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  %{python_module wheel}
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
Requires:       python3-jupyterlab = %{version}
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
%setup -q -c -T

%build
# not needed

%install
%{python_expand mkdir build; cp -a %{SOURCE0} build/}
%pyproject_install
%jupyter_move_config
%python_expand sed -i -e 's|^#!%{_bindir}/env node|#!%{_bindir}/node|' %{buildroot}%{$python_sitelib}/jupyterlab/node-version-check.js
%python_expand sed -i -e 's|^#!%{_bindir}/env node|#!%{_bindir}/node|' %{buildroot}%{$python_sitelib}/jupyterlab/staging/yarn.js
%python_expand chmod a+x %{buildroot}%{$python_sitelib}/jupyterlab/node-version-check.js
%python_expand chmod a+x %{buildroot}%{$python_sitelib}/jupyterlab/staging/yarn.js
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
cp %{buildroot}%{python3_sitelib}/jupyterlab-%{version}.dist-info/LICENSE .

%check
# This is only a rudimentary set of tests which we can run offline using pytest directly. The full test
# suite would use jlpm which needs online connection through npm:
# https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html#build-and-run-the-tests
# Disable build checks that pull in remote resources with npm
donttest+=" or (TestExtension and test_app_dir)"
donttest+=" or (TestExtension and test_build)"
donttest+=" or (TestExtension and test_disable_extension)"
donttest+=" or (TestExtension and test_enable_extension)"
donttest+=" or (TestExtension and test_list_extension)"
donttest+=" or (TestExtension and test_link)"
donttest+=" or (TestExtension and test_unlink)"
donttest+=" or (TestExtension and test_install)"
donttest+=" or (TestExtension and test_uninstall)"
donttest+=" or (TestExtension and test_update)"
donttest+=" or (TestAppHandlerRegistry and test_get_registry)"
donttest+=" or (TestAppHandlerRegistry and test_populate_staging)"
donttest+=" or (TestAppHandlerRegistry and test_yarn_config)"
# don't have the fixtures
donttest+=" or (TestBuildAPI and (test_get_status or test_build))"
donttest+=" or test_load_extension"

%pytest --pyargs jupyterlab -k "not (${donttest:4})"

%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyterlab/
%{python_sitelib}/jupyterlab-%{version}.dist-info/

%files -n jupyter-jupyterlab
%license LICENSE
%{_bindir}/jlpm
%{_bindir}/jupyter-lab
%{_bindir}/jupyter-labextension
%{_bindir}/jupyter-labhub
%config %{_jupyter_servextension_confdir}/jupyterlab.json
%config %{_jupyter_server_confdir}/jupyterlab.json
%{_jupyter_lab_dir}

%changelog
