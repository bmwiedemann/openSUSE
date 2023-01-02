#
# spec file for package python-jupyterlab
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


Name:           python-jupyterlab
Version:        3.5.2
Release:        0
Summary:        Environment for interactive and reproducible computing
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab
# install from wheel with all the bundled nodejs stuff
Source0:        https://files.pythonhosted.org/packages/py3/j/jupyterlab/jupyterlab-%{version}-py3-none-any.whl
Source99:       python-jupyterlab-rpmlintrc
BuildRequires:  %{python_module Jinja2 >= 2.1}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module jupyter_server >= 1.16 with %python-jupyter_server < 3}
BuildRequires:  %{python_module jupyterlab-server >= 2.10}
BuildRequires:  %{python_module nbclassic}
BuildRequires:  %{python_module notebook < 7}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tornado >= 6.1}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab = %{version}
Requires:       python-Jinja2 >= 2.1
Requires:       python-ipython
Requires:       python-jupyter_core
Requires:       python-jupyterlab-server >= 2.10
Requires:       python-nbclassic
Requires:       python-notebook < 7
Requires:       python-packaging
Requires:       python-tornado >= 6.1
Requires:       (python-jupyter_server >= 1.16 with python-jupyter_server < 3)
Provides:       python-jupyter_jupyterlab = %{version}
Obsoletes:      python-jupyter_jupyterlab < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jupyterlab-server-test}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-check-links}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-jupyter >= 0.6}
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
%pyproject_install %{SOURCE0}
%{python_expand #
for f in %{buildroot}%{$python_sitelib}/jupyterlab/{node-version-check.js,staging/yarn.js}; do
  sed -i -e 's|^#!%{_bindir}/env node|#!%{_bindir}/node|' $f
  chmod a+x $f
done
%fdupes %{buildroot}%{$python_sitelib}
}
%fdupes %{buildroot}%{_jupyter_prefix}
# Find any one installed LICENSE and get if for the rpm tagged file
find %{buildroot}%{_prefix}/lib/python3.* -path '*/jupyterlab-%{version}.dist-info/LICENSE' -exec cp {} . ';' -quit

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
# don't have the fixtures
donttest="$donttest or (TestBuildAPI and (test_get_status or test_build))"
donttest="$donttest or test_load_extension"

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
%{_jupyter_config} %{_jupyter_servextension_confdir}/jupyterlab.json
%{_jupyter_config} %{_jupyter_server_confdir}/jupyterlab.json
%{_jupyter_lab_dir}

%changelog
