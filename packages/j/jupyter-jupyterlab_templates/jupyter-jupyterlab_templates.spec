#
# spec file for package jupyter-jupyterlab_templates
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


Name:           jupyter-jupyterlab_templates
Version:        0.2.0
Release:        0
Summary:        Templates for notebooks in JupyterLab
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/timkpaine/jupyterlab_templates
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_templates/jupyterlab_templates-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-jupyterlab >= 1.0.0
Provides:       python3-jupyter_jupyterlab_templates = %{version}
Obsoletes:      python3-jupyter_jupyterlab_templates < %{version}
Provides:       python3-jupyterlab_templates = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  jupyter-jupyterlab >= 1.0.0
# /SECTION

%description
Support for jupyter notebook templates in jupyterlab.

%prep
%setup -q -n jupyterlab_templates-%{version}
rm -rf jupyterlab_templates/templates/.ipynb_checkpoints

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%post
%{jupyter_serverextension_enable jupyterlab_templates}

%preun
%{jupyter_serverextension_disable jupyterlab_templates}

%files
%doc README.md
%{python3_sitelib}/jupyterlab_templates-*-py*.egg-info
%{python3_sitelib}/jupyterlab_templates/

%changelog
