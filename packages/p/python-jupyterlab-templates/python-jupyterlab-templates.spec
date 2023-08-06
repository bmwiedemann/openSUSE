#
# spec file for package python-jupyterlab-templates
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


%define anypython python3dist
%define pyver 0.5.0
%define distver 0.5
Name:           python-jupyterlab-templates
Version:        %{pyver}
Release:        0
Summary:        Templates for notebooks in JupyterLab
License:        Apache-2.0
URL:            https://github.com/finos/jupyterlab_templates
Source:         https://files.pythonhosted.org/packages/py3/j/jupyterlab_templates/jupyterlab_templates-%{version}-py3-none-any.whl
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jupyterlab >= 4.0.0}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab-templates = %{version}
Requires:       python-jupyterlab >= 4.0
Requires:       (python-notebook if python-jupyterlab >= 4)
Conflicts:      jupyter-jupyterlab_templates < %{version}
Provides:       python-jupyter_jupyterlab_templates = %{version}
Obsoletes:      python-jupyter_jupyterlab_templates < %{version}
BuildArch:      noarch
%python_subpackages

%description
Support for jupyter notebook templates in jupyterlab.

%package     -n jupyter-jupyterlab-templates
Summary:        Templates for notebooks in JupyterLab
Requires:       jupyter-jupyterlab >= 4.0.0
Requires:       %anypython(jupyterlab-templates) = %{distver}
Provides:       jupyter-jupyterlab_templates = %{version}
Obsoletes:      jupyter-jupyterlab_templates < %{version}

%description -n jupyter-jupyterlab-templates
Support for jupyter notebook templates in jupyterlab.

%prep
%setup -q -c -T

%build
%{python_expand mkdir build/; cp -a %{SOURCE0} build/}

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
find  %{buildroot} -path '*/jupyterlab_templates-%{version}.dist-info/licenses' -exec cp -r {} ./ ';' -quit

%check
%pytest --pyargs jupyterlab_templates

%files %{python_files}
%license licenses/*
%{python_sitelib}/jupyterlab_templates-%{version}.dist-info/
%{python_sitelib}/jupyterlab_templates/

%files -n jupyter-jupyterlab-templates
%license licenses/*
%{_jupyter_config} %{_jupyter_server_confdir}/jupyterlab_templates.json
%{_jupyter_prefix}/labextensions/jupyterlab_templates
%dir %{_jupyter_prefix}/notebook
%{_jupyter_prefix}/notebook/jupyterlab_templates

%changelog
