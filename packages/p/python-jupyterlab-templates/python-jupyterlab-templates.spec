#
# spec file for package python-jupyterlab-templates
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
Name:           python-jupyterlab-templates
Version:        0.2.3
Release:        0
Summary:        Templates for notebooks in JupyterLab
License:        Apache-2.0
URL:            https://github.com/timkpaine/jupyterlab_templates
Source:         https://files.pythonhosted.org/packages/py2.py3/j/jupyterlab-templates/jupyterlab_templates-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab-templates = %{version}
Requires:       python-jupyterlab >= 1.0.0
Conflicts:      jupyter-jupyterlab_templates < %{version}
Provides:       python-jupyter_jupyterlab_templates = %{version}
Obsoletes:      python-jupyter_jupyterlab_templates < %{version}
BuildArch:      noarch
%python_subpackages

%description
Support for jupyter notebook templates in jupyterlab.

%package     -n jupyter-jupyterlab-templates
Summary:        Templates for notebooks in JupyterLab
Requires:       jupyter-jupyterlab >= 1.0.0
Requires:       python3-jupyterlab-templates = %{version}
Provides:       jupyter-jupyterlab_templates = %{version}
Obsoletes:      jupyter-jupyterlab_templates < %{version}

%description -n jupyter-jupyterlab-templates
Support for jupyter notebook templates in jupyterlab.

%prep
%setup -q -c -T

%build
# not needed

%install
cp -a %{SOURCE0} .
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

cp %{buildroot}%{python3_sitelib}/jupyterlab_templates-%{version}.dist-info/LICENSE .

%files %{python_files}
%license %{python_sitelib}/jupyterlab_templates-%{version}.dist-info/LICENSE
%{python_sitelib}/jupyterlab_templates-%{version}.dist-info/
%{python_sitelib}/jupyterlab_templates/

%files -n jupyter-jupyterlab-templates
%license LICENSE
%{_jupyter_servextension_confdir}/jupyterlab_templates.json
%{_jupyter_labextensions_dir}/jupyterlab_templates-%{version}.tgz

%changelog
