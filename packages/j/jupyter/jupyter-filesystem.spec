#
# spec file for package jupyter-filesystem
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
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           jupyter-filesystem
Url:            https://jupyter.org/
Version:        20190823
%define tar_ver 1.0.0
Release:        0
Summary:        Common directories shared by Jupyter packages
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter/jupyter-%{tar_ver}.tar.gz
Source10:       macros.jupyter_core
Source11:       macros.jupyter_notebook
Source12:       macros.jupyterlab
License:        BSD-3-Clause
Group:          System/Fhs

%description
This package provides common directories and macros used by many 
jupyter packages.

%package     -n jupyter-jupyter_core-filesystem
Summary:        Common directories shared by Jupyter packages
Provides:       jupyter-jupyter_core-macros-devel = %{version}
Provides:       %{python_module jupyter_core-filesystem = %{version}}
Provides:       %{python_module jupyter_core-macros-devel = %{version}}

%description -n jupyter-jupyter_core-filesystem
This package provides common directories and macros used by many 
packages that depend on jupyter_core.

It also provides macros for building packages that depend on
jupyter_core.

%define _jupyter_prefix          %{_datadir}/jupyter/
%define _jupyter_kernel_dir      %{_jupyter_prefix}/kernels/
%define _jupyter_confdir         %{_sysconfdir}/jupyter/

%package     -n jupyter-notebook-filesystem
Summary:        Common directories shared by Jupyter notebook packages
Requires:       jupyter-jupyter_core-filesystem = %{version}
Requires:       python-rpm-macros
Provides:       jupyter-notebook-macros-devel = %{version}
Provides:       %{python_module notebook-filesystem = %{version}}
Provides:       %{python_module notebook-macros-devel = %{version}}

%description -n jupyter-notebook-filesystem
This package provides common directories and macros used by many 
packages that depend on the Jupyter notebook.

It also provides macros for building packages that depend on
the Jupyter notebook.

%define _jupyter_nbextension_dir        %{_jupyter_prefix}/nbextensions/
%define _jupyter_nb_confdir             %{_jupyter_confdir}/nbconfig/
%define _jupyter_nbextension_confdir    %{_jupyter_nb_confdir}/nbextensions/
%define _jupyter_servextension_confdir  %{_jupyter_confdir}/jupyter_notebook_config.d/
%define _jupyter_server_confdir         %{_jupyter_confdir}/jupyter_server_config.d/

%define _jupyter_nb_auth_confdir        %{_jupyter_nb_confdir}/auth.d
%define _jupyter_nb_base_confdir        %{_jupyter_nb_confdir}/base.d
%define _jupyter_nb_bidi_confdir        %{_jupyter_nb_confdir}/bidi.d
%define _jupyter_nb_custom_confdir      %{_jupyter_nb_confdir}/custom.d
%define _jupyter_nb_edit_confdir        %{_jupyter_nb_confdir}/edit.d
%define _jupyter_nb_notebook_confdir    %{_jupyter_nb_confdir}/notebook.d
%define _jupyter_nb_services_confdir    %{_jupyter_nb_confdir}/services.d
%define _jupyter_nb_style_confdir       %{_jupyter_nb_confdir}/style.d
%define _jupyter_nb_terminal_confdir    %{_jupyter_nb_confdir}/terminal.d
%define _jupyter_nb_tree_confdir        %{_jupyter_nb_confdir}/tree.d

%package     -n jupyter-jupyterlab-filesystem
Summary:        Common directories shared by JupyterLab packages
Requires:       jupyter-jupyter_core-filesystem = %{version}
Provides:       jupyter-jupyterlab-macros-devel = %{version}
Provides:       %{python_module jupyterlab-filesystem = %{version}}
Provides:       %{python_module jupyterlab-macros-devel = %{version}}
# jupyterlab-widgets is no longer available as a python package
Provides:       jupyter-jupyterlab-widgets = 0.7
Obsoletes:      jupyter-jupyterlab-widgets < 0.7

%description -n jupyter-jupyterlab-filesystem
This package provides common directories and macros used by many 
packages that depend on JupyterLab.

It also provides macros for building packages that depend on
JupyterLab.

%define _jupyter_lab_dir            %{_jupyter_prefix}/lab/
%define _jupyter_labextensions_dir  %{_jupyter_lab_dir}/extensions/

%prep
%setup -q -n jupyter-%{tar_ver}

%build
# Not needed

%install
# macros
install -D -m644 %{SOURCE10} %{buildroot}%{_rpmmacrodir}/macros.jupyter_core
install -D -m644 %{SOURCE11} %{buildroot}%{_rpmmacrodir}/macros.jupyter_notebook
install -D -m644 %{SOURCE12} %{buildroot}%{_rpmmacrodir}/macros.jupyterlab

# jupyter_core directories
mkdir -p %{buildroot}%{_jupyter_prefix}
mkdir -p %{buildroot}%{_jupyter_kernel_dir}
mkdir -p %{buildroot}%{_jupyter_confdir}

# notebook directories
mkdir -p %{buildroot}%{_jupyter_nbextension_dir}
mkdir -p %{buildroot}%{_jupyter_nb_confdir}
mkdir -p %{buildroot}%{_jupyter_nbextension_confdir}
mkdir -p %{buildroot}%{_jupyter_servextension_confdir}
mkdir -p %{buildroot}%{_jupyter_server_confdir}

mkdir -p %{buildroot}%{_jupyter_nb_auth_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_base_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_bidi_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_custom_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_edit_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_notebook_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_services_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_style_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_terminal_confdir}
mkdir -p %{buildroot}%{_jupyter_nb_tree_confdir}

# jupyterlab directories
mkdir -p %{buildroot}%{_jupyter_lab_dir}
mkdir -p %{buildroot}%{_jupyter_labextensions_dir}


%files -n jupyter-jupyter_core-filesystem
%license LICENSE
%{_rpmmacrodir}/macros.jupyter_core
%dir %{_jupyter_prefix}
%dir %{_jupyter_kernel_dir}
%dir %{_jupyter_confdir}

%files -n jupyter-notebook-filesystem
%license LICENSE
%{_rpmmacrodir}/macros.jupyter_notebook
%dir %{_jupyter_nbextension_dir}
%dir %{_jupyter_nb_confdir}
%dir %{_jupyter_nbextension_confdir}
%dir %{_jupyter_servextension_confdir}
%dir %{_jupyter_server_confdir}
%dir %{_jupyter_nb_auth_confdir}
%dir %{_jupyter_nb_base_confdir}
%dir %{_jupyter_nb_bidi_confdir}
%dir %{_jupyter_nb_custom_confdir}
%dir %{_jupyter_nb_edit_confdir}
%dir %{_jupyter_nb_notebook_confdir}
%dir %{_jupyter_nb_services_confdir}
%dir %{_jupyter_nb_style_confdir}
%dir %{_jupyter_nb_terminal_confdir}
%dir %{_jupyter_nb_tree_confdir}

%files -n jupyter-jupyterlab-filesystem
%license LICENSE
%{_rpmmacrodir}/macros.jupyterlab
%dir %{_jupyter_lab_dir}
%dir %{_jupyter_labextensions_dir}

%changelog
