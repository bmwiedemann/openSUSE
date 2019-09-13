#
# spec file for package jupyter-jupyterlab
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jupyter-jupyterlab
Version:        1.0.9
Release:        0
Summary:        The JupyterLab notebook server extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab
Source0:        https://files.pythonhosted.org/packages/py2.py3/j/jupyterlab/jupyterlab-%{version}-py2.py3-none-any.whl
Source99:       jupyter-jupyterlab-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-jupyterlab-server >= 1.0.0
BuildRequires:  jupyter-notebook >= 4.3.1
BuildRequires:  nodejs
BuildRequires:  npm >= 5
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.5
BuildRequires:  python3-pip
BuildRequires:  python3-tornado
BuildConflicts: python3-tornado >= 6
Requires:       jupyter-jupyter_core
Requires:       jupyter-jupyterlab-filesystem
Requires:       jupyter-jupyterlab-server >= 1.0.0
Requires:       jupyter-notebook >= 4.3.1
Requires:       nodejs
Requires:       npm >= 5
Requires:       python3-base >= 3.5
Requires:       python3-Jinja2 >= 2.10
Requires:       python3-tornado
Conflicts:      python3-tornado >= 6
Provides:       python3-jupyter_jupyterlab = %{version}
Obsoletes:      python3-jupyter_jupyterlab < %{version}
Provides:       python3-jupyterlab = %{version}
Provides:       jupyter-jupyterlab-discovery = 6
Obsoletes:      jupyter-jupyterlab-discovery < 6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-check-links
BuildRequires:  python3-requests
# /SECTION

%description
An extensible environment for interactive and reproducible computing,
based on the Jupyter Notebook and Architecture.

JupyterLab is a user interface for Project Jupyter.
It offers familiar building blocks of the classic Jupyter
Notebook like notebook, terminal, text editor, file browser, rich outputs,
etc. in a flexible user inteface that can be extended
through third party extensions.

JupyterLab is currently in beta.

%prep
%setup -q -c -T

%build
# not needed

%install
pip%{python3_bin_suffix} install --no-deps --root=%{buildroot} %{SOURCE0}

%{jupyter_move_config}
sed -i -e 's|^#!/usr/bin/env node|#!%{_bindir}/node|' %{buildroot}%{python3_sitelib}/jupyterlab/node-version-check.js
sed -i -e 's|^#!/usr/bin/env node|#!%{_bindir}/node|' %{buildroot}%{python3_sitelib}/jupyterlab/staging/yarn.js
chmod a+x %{buildroot}%{python3_sitelib}/jupyterlab/node-version-check.js
chmod a+x %{buildroot}%{python3_sitelib}/jupyterlab/staging/yarn.js
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%check
export PYTHONDONTWRITEBYTECODE=1
# Disable build checks that pull in remote resources with npm
pytest-%{python3_bin_suffix} %{buildroot}%{python3_sitelib}/jupyterlab/ -k \
    'not (test_build or test_clear or test_build_check or test_build_custom or test_uninstall_core_extension)'

%files
%license %{python3_sitelib}/jupyterlab-%{version}.dist-info/LICENSE
%{_bindir}/jlpm
%{_bindir}/jupyter-lab
%{_bindir}/jupyter-labextension
%{_bindir}/jupyter-labhub
%config %{_jupyter_servextension_confdir}/jupyterlab.json
%{_jupyter_lab_dir}
%{python3_sitelib}/jupyterlab/
%{python3_sitelib}/jupyterlab-%{version}.dist-info

%changelog
