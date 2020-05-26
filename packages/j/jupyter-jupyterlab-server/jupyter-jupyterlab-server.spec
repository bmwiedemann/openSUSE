#
# spec file for package jupyter-jupyterlab-server
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


Name:           jupyter-jupyterlab-server
Version:        1.1.5
Release:        0
Summary:        Server components for JupyterLab and JupyterLab-like applications
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyterlab_server
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_server/jupyterlab_server-%{version}.tar.gz
Source100:      jupyter-jupyterlab-server-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       jupyter-notebook >= 4.2.0
Requires:       python3-Jinja2 >= 2.10
Requires:       python3-base >= 3.5
Requires:       python3-json5
Requires:       python3-jsonschema >= 3.0.1
Requires:       python3-requests
Provides:       python3-jupyter_jupyterlab_server = %{version}
Obsoletes:      python3-jupyter_jupyterlab_server < %{version}
Provides:       jupyter-jupyterlab-launcher = %{version}
Provides:       python3-jupyterlab-server = %{version}
Obsoletes:      jupyter-jupyterlab-launcher < %{version}
Provides:       python3-jupyter_jupyterlab_launcher = %{version}
Obsoletes:      python3-jupyter_jupyterlab_launcher < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  jupyter-notebook >= 4.2.0
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-base >= 3.5
BuildRequires:  python3-json5
BuildRequires:  python3-jsonschema >= 3.0.1
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
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

%check
export PYTHONDONTWRITEBYTECODE=1
pytest-%{python3_bin_suffix} -v .

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/jupyterlab_server/
%{python3_sitelib}/jupyterlab_server-%{version}-py*.egg-info/

%changelog
