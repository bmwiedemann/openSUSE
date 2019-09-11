#
# spec file for package jupyter-jupyterlab_github
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


Name:           jupyter-jupyterlab_github
Version:        0.7.0
Release:        0
Summary:        Notebook server extension for GitHub API requests
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab-github
Source:         https://files.pythonhosted.org/packages/py3/j/jupyterlab_github/jupyterlab_github-%{version}-py3-none-any.whl
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab >= 0.32
BuildRequires:  jupyter-notebook
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-traitlets
Requires:       jupyter-jupyterlab >= 0.32
Requires:       jupyter-notebook
Requires:       python3-traitlets
Provides:       python3-jupyter_jupyterlab_github = %{version}
Obsoletes:      python3-jupyter_jupyterlab_github <= %{version}
Provides:       python3-jupyterlab_github = %{version}
BuildArch:      noarch

%description
A Jupyter Notebook server extension which acts
as a proxy for GitHub API requests

%prep
%setup -q -T -c

%build
# Not Needed

%install
pip%{python3_bin_suffix} install --root=%{buildroot} %{SOURCE0}

%{jupyter_move_config}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%files
%{python3_sitelib}/jupyterlab_github-%{version}.dist-info
%license %{python3_sitelib}/jupyterlab_github-%{version}.dist-info/LICENSE.txt
%{python3_sitelib}/jupyterlab_github/
%config %{_jupyter_servextension_confdir}/jupyterlab_github.json

%changelog
