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


%bcond_with     test
Name:           jupyter-jupyterlab
Version:        0.35.6
Release:        0
Summary:        The JupyterLab notebook server extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab
Source0:        https://files.pythonhosted.org/packages/py3/j/jupyterlab/jupyterlab-%{version}-py3-none-any.whl
Source99:       jupyter-jupyterlab-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-jupyterlab-launcher >= 0.13.1
BuildRequires:  jupyter-jupyterlab-server < 0.3.0
BuildRequires:  jupyter-jupyterlab-server >= 0.2.0
BuildRequires:  jupyter-notebook >= 5.3
BuildRequires:  npm >= 5
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.5
BuildRequires:  python3-certifi
BuildRequires:  python3-ipython_genutils
BuildRequires:  python3-pip
BuildRequires:  python3-requests
Requires:       jupyter-jupyterlab-filesystem
Requires:       jupyter-jupyterlab-launcher >= 0.13.1
Requires:       jupyter-jupyterlab-server < 0.3.0
Requires:       jupyter-jupyterlab-server >= 0.2.0
Requires:       jupyter-notebook >= 5.3
Requires:       npm >= 5
Requires:       python3-ipython_genutils
Recommends:     python3-Sphinx
Recommends:     python3-recommonmark
Recommends:     python3-requests
Recommends:     python3-sphinx_rtd_theme
Provides:       python3-jupyter_jupyterlab = %{version}
Obsoletes:      python3-jupyter_jupyterlab < %{version}
Provides:       python3-jupyterlab = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  python3-pytest
%endif

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
pip%{python3_bin_suffix} install --root=%{buildroot} %{SOURCE0}

%{jupyter_move_config}

%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%if %{with test}
%check
rm -r build
rm -r _build.*
%pytest
%endif

%files
%license %{python3_sitelib}/jupyterlab-%{version}.dist-info/LICENSE.txt
%{_bindir}/jlpm
%{_bindir}/jupyter-lab
%{_bindir}/jupyter-labextension
%{_bindir}/jupyter-labhub
%config %{_jupyter_servextension_confdir}/jupyterlab.json
%{_jupyter_lab_dir}
%{python3_sitelib}/jupyterlab
%{python3_sitelib}/jupyterlab-%{version}.dist-info

%changelog
