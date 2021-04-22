#
# spec file for package python-ipywebrtc
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-ipywebrtc
Version:        0.6.0
Release:        0
License:        MIT
Summary:        WebRTC for Jupyter notebook/lab
URL:            https://github.com/maartenbreddels/ipywebrtc
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/ipywebrtc/ipywebrtc-%{version}.tar.gz
BuildRequires:  %{python_module ipywidgets >= 7.4.0}
BuildRequires:  %{python_module jupyter-packaging >= 0.7.9}
BuildRequires:  %{python_module jupyterlab >= 3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  npm
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipywebrtc = %{version}
Requires:       python-ipywidgets >= 7.4.0
BuildArch:      noarch

%python_subpackages

%description
WebRTC and MediaStream API exposed in the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipywebrtc
Summary:        WebRTC for Jupyter notebook/lab
Requires:       jupyter-ipywidgets >= 7.4.0
Requires:       jupyter-jupyterlab
Requires:       jupyter-notebook
Requires:       python3-ipywebrtc = %{version}

%description -n jupyter-ipywebrtc
WebRTC and MediaStream API exposed in the Jupyter notebook.

This package provides the jupyter notebook and jupyterlab
extensions.

%prep
%setup -q -n ipywebrtc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# there are no python tests, only js in the github repo,
# which we cannot test offline with npm.
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_DIR=%{buildroot}%{_jupyter_confdir}
%{python_expand  # Just check that we installed the extensions
export PYTHONPATH=%{buildroot}%{$python_sitelib}
jupyter-%{$python_bin_suffix} nbextension list 2>&1 | grep -ie "jupyter-webrtc/extension.*enabled"
jupyter-%{$python_bin_suffix} labextension list 2>&1 | grep -ie "jupyter-webrtc.*enabled.*ok"
}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipywebrtc-%{version}*-info
%{python_sitelib}/ipywebrtc/

%files -n jupyter-ipywebrtc
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/jupyter-webrtc.json
%{_jupyter_nbextension_dir}/jupyter-webrtc/
%dir %{_jupyter_prefix}/labextensions/
%{_jupyter_prefix}/labextensions/jupyter-webrtc/

%changelog
