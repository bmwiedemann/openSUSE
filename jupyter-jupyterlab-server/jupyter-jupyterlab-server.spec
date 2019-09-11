#
# spec file for package jupyter-jupyterlab-server
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


Name:           jupyter-jupyterlab-server
# Do not update to 0.3.0 until jupyter-jupyterlab supports it (probably version 1.0)
Version:        0.2.0
Release:        0
Summary:        Server components for JupyterLab and JupyterLab-like applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://jupyter.org
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_server/jupyterlab_server-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook >= 4.2.0
Requires:       python3-jsonschema >= 2.6.0
Requires:       python3-tornado
Requires:       python3-traitlets
Provides:       python3-jupyter_jupyterlab_server = %{version}
Obsoletes:      python3-jupyter_jupyterlab_server <= %{version}
# Factory has a newer, unsupported version due to a packaging mistake
Obsoletes:      python3-jupyter_jupyterlab_server <= 0.3.0
Provides:       python3-jupyterlab-server = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  jupyter-notebook >= 4.2.0
BuildRequires:  python3-jsonschema >= 2.6.0
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-traitlets
# /SECTION

%description
This package is used to launch an application built using JupyterLab.

%prep
%setup -q -n jupyterlab_server-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/jupyterlab_server/
%{python3_sitelib}/jupyterlab_server-%{version}-py*.egg-info/

%changelog
