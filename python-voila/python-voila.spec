#
# spec file for package python-voila
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
Name:           python-voila
Version:        0.1.9
Release:        0
License:        BSD-3-Clause
Summary:        Plugin for serving read-only live Jupyter notebooks
Url:            https://github.com/QuantStack/voila
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/v/voila/voila-%{version}.tar.gz
BuildRequires:  %{python_module Pygments >= 2.4.1}
BuildRequires:  %{python_module jupyter-server >= 0.1.0}
BuildRequires:  %{python_module jupyterlab-pygments >= 0.1.0}
BuildRequires:  %{python_module nbconvert >= 5.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       python-Pygments >= 2.4.1
Requires:       python-jupyter-server >= 0.1.0
Requires:       python-nbconvert >= 5.5
Requires:       python-jupyterlab-pygments >= 0.1.0
Requires:       python-notebook
Requires:       jupyter-voila = %{version}
BuildArch:      noarch

%python_subpackages

%description
Voila serves live Jupyter notebook including Jupyter interactive widgets.

Unlike the usual HTML-converted notebooks, each user connecting to the Voila
tornado application gets a dedicated Jupyter kernel which can execute the
callbacks to changes in Jupyter interactive widgets.

By default, voila disallows execute requests from the front-end, disabling
the ability to execute arbitrary code. By default, voila runs with the
strip_source option, which strips out the input cells from the rendered
notebook. When using these default settings, the code powering the Jupyter
notebook is never sent to the front-end.

This package provides the python interface.

%package     -n jupyter-voila
Summary:        Plugin for serving read-only live Jupyter notebooksmacros
Requires:       jupyter-jupyter-server >= 0.0.3
Requires:       jupyter-nbconvert >= 5.4
Requires:       jupyter-notebook
Requires:       python3-voila = %{version}

%description -n jupyter-voila
Voila serves live Jupyter notebook including Jupyter interactive widgets.

Unlike the usual HTML-converted notebooks, each user connecting to the Voila
tornado application gets a dedicated Jupyter kernel which can execute the
callbacks to changes in Jupyter interactive widgets.

By default, voila disallows execute requests from the front-end, disabling
the ability to execute arbitrary code. By default, voila runs with the
strip_source option, which strips out the input cells from the rendered
notebook. When using these default settings, the code powering the Jupyter
notebook is never sent to the front-end.

This package provides the jupyter components.


%prep
%setup -q -n voila-%{version}

%build
%python_build

%install
%python_install
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/voila-%{version}-py*.egg-info
%{python_sitelib}/voila/

%files -n jupyter-voila
%license LICENSE
%doc README.md
%{_bindir}/voila
%config %{_jupyter_servextension_confdir}/voila.json
%config %{_jupyter_server_confdir}/voila.json
%config %{_jupyter_nb_notebook_confdir}/voila.json
%{_jupyter_nbextension_dir}/voila/
%{_jupyter_prefix}/voila/

%changelog
