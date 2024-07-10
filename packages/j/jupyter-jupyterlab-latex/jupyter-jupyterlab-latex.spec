#
# spec file for package jupyter-jupyterlab-latex
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


%define pythons python3
Name:           jupyter-jupyterlab-latex
Version:        4.0.0
Release:        0
Summary:        Jupyter Notebook server extension which acts as an endpoint for LaTeX
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab-latex
# >= 3.1 not on PyPI gh#jupyterlab/jupyterlab-latex#218
#Source:         https://files.pythonhosted.org/packages/py3/j/jupyterlab_latex/jupyterlab_latex-%%{version}-py3-none-any.whl
Source0:        https://github.com/jupyterlab/jupyterlab-latex/archive/refs/tags/v%{version}.tar.gz#/jupyterlab_latex-%{version}-gh.tar.gz
# package-lock.json file generated with command:
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source2:        package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source3:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
Source99:       jupyter-jupyterlab-latex-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.8
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  texlive-latex-bin
BuildRequires:  (python3-jupyter-packaging >= 0.12 with python3-jupyter-packaging < 2)
BuildRequires:  (python3-jupyter-server >= 2 with python3-jupyter-server < 3)
BuildRequires:  (python3-jupyterlab >= 4 with python3-jupyterlab < 5)
Requires:       texlive-latex-bin
Requires:       (python3-jupyter-server >= 2 with python3-jupyter-server < 3)
Requires:       (python3-jupyterlab >= 4 with python3-jupyterlab < 5)
Provides:       python3-jupyter_jupyterlab_latex = %{version}-%{release}
Obsoletes:      python3-jupyter_jupyterlab_latex < %{version}-%{release}
Provides:       python3-jupyterlab-latex = %{version}-%{release}
BuildArch:      noarch

%description
An extension for JupyterLab which allows for live-editing of LaTeX documents.

%prep
%autosetup -p1 -n jupyterlab-latex-%{version}
local-npm-registry %{_sourcedir} install --also=dev
sed -i "s/jlpm/npm/" pyproject.toml
sed -i "s/jlpm/npm run/g" package.json

%build
%pyproject_wheel

%install
%pyproject_install

%{jupyter_move_config}
%fdupes %{buildroot}%{_jupyter_prefix}
%fdupes %{buildroot}%{python3_sitelib}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
cp -r %{buildroot}%{_jupyter_confdir} myconfig
export JUPYTER_CONFIG_DIR=myconfig
export PYTHONPATH=%{buildroot}%{python3_sitelib}
jupyter server extension list 2>&1 | grep -ie "jupyterlab_latex.*OK"
jupyter labextension list 2>&1 | grep -ie "@jupyterlab/latex.*OK"
python3 -c 'import jupyterlab_latex'

%files
%license %{python3_sitelib}/jupyterlab_latex-*.dist-info/LICENSE
%{python3_sitelib}/jupyterlab_latex-%{version}*.dist-info
%{python3_sitelib}/jupyterlab_latex/
%dir %_jupyter_labextensions_dir3/@jupyterlab
%_jupyter_labextensions_dir3/@jupyterlab/latex
%_jupyter_config %{_jupyter_servextension_confdir}/jupyterlab_latex.json
%_jupyter_config %{_jupyter_server_confdir}/jupyterlab_latex.json

%changelog
