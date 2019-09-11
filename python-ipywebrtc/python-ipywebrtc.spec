#
# spec file for package python-ipywebrtc
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-ipywebrtc
Version:        0.5.0
Release:        0
License:        MIT
Summary:        WebRTC extension for the Jupyter notebook/lab
Url:            https://github.com/maartenbreddels/ipywebrtc
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/ipywebrtc/ipywebrtc-%{version}.tar.gz
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module bqplot}
BuildRequires:  %{python_module ipywidgets >= 7.4.0}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-ipywidgets >= 7.4.0
Requires:       python-notebook
Requires:       jupyter-ipywebrtc = %{version}
BuildArch:      noarch

%python_subpackages

%description
WebRTC and MediaStream API exposed in the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipywebrtc
Summary:        WebRTC extension for the Jupyter notebook
Requires:       jupyter-ipywidgets >= 7.4.0
Requires:       jupyter-notebook
Requires:       python3-ipywebrtc = %{version}

%description -n jupyter-ipywebrtc
WebRTC and MediaStream API exposed in the Jupyter notebook.

This package provides the jupyter notebook extension.

%prep
%setup -q -n ipywebrtc-%{version}

%build
%python_build

%install
%python_install
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipywebrtc-%{version}-py*.egg-info
%{python_sitelib}/ipywebrtc/

%files -n jupyter-ipywebrtc
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/ipywebrtc.json
%{_jupyter_nbextension_dir}/jupyter-webrtc/

%changelog
