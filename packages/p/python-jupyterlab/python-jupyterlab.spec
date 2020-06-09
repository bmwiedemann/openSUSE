#
# spec file for package python-jupyterlab
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyterlab
Version:        2.1.4
Release:        0
Summary:        Environment for interactive and reproducible computing
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab
Source0:        https://files.pythonhosted.org/packages/py3/j/jupyterlab/jupyterlab-%{version}-py3-none-any.whl
Source99:       python-jupyterlab-rpmlintrc
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module jupyterlab-server >= 1.1.4}
BuildRequires:  %{python_module notebook >= 4.3.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  nodejs >= 10
BuildRequires:  npm >= 10
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab = %{version}
Requires:       python-Jinja2 >= 2.10
Requires:       python-base >= 3.5
Requires:       python-jupyter-core
Requires:       python-jupyterlab-server >= 1.1.4
Requires:       python-notebook >= 4.3.1
Requires:       python-tornado
Provides:       python-jupyter_jupyterlab = %{version}
Obsoletes:      python-jupyter_jupyterlab < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module pytest-check-links}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
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
Requires:       jupyter-jupyter-core
Requires:       jupyter-jupyterlab-filesystem
Requires:       jupyter-jupyterlab-server >= 1.0.0
Requires:       jupyter-notebook >= 4.3.1
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
cp -a %{SOURCE0} .
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
export PYTHONDONTWRITEBYTECODE=1
# Disable build checks that pull in remote resources with npm
%{pytest %{buildroot}%{$python_sitelib}/jupyterlab/ -k \
    'not (test_build or test_clear or test_build_check or test_build_custom or test_uninstall_core_extension or test_install_and_uninstall_pinned or test_install_and_uninstall_pinned_folder or test_install_extension)'
}

%files %{python_files}
%license %{python_sitelib}/jupyterlab-%{version}.dist-info/LICENSE
%{python_sitelib}/jupyterlab/
%{python_sitelib}/jupyterlab-%{version}.dist-info/

%files -n jupyter-jupyterlab
%license LICENSE
%{_bindir}/jlpm
%{_bindir}/jupyter-lab
%{_bindir}/jupyter-labextension
%config %{_jupyter_servextension_confdir}/jupyterlab.json
%{_jupyter_lab_dir}

%changelog
