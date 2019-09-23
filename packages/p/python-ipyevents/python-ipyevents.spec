#
# spec file for package python-ipyevents
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
%define mainver 0.6.3
%define labver  1.6.3
Name:           python-ipyevents
Version:        %{mainver}
Release:        0
License:        BSD-3-Clause
Summary:        A custom ipython widget for returning mouse and keyboard events
Url:            https://github.com/mwcraig/ipyevents
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/py2.py3/i/ipyevents/ipyevents-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  zip
Requires:       python-ipywidgets >= 7.0.0
Requires:       jupyter-ipyevents = %{mainver}
BuildArch:      noarch

%python_subpackages

%description
ipyevents provides a custom widget for returning mouse and keyboard 
events to Python. Use it to:

  * add keyboard shortcuts to an existing widget.
  * react to the user clicking on an image.
  * install callbacks on arbitrary mouse and keyboard events.

This package provides the python interface.

%package     -n jupyter-ipyevents
Summary:        A custom ipython widget for returning mouse and keyboard events
Requires:       jupyter-notebook
Requires:       python3-ipyevents = %{mainver}

%description -n jupyter-ipyevents
ipyevents provides a custom widget for returning mouse and keyboard 
events to Python. Use it to:

  * add keyboard shortcuts to an existing widget.
  * react to the user clicking on an image.
  * install callbacks on arbitrary mouse and keyboard events.

This package provides the tools and jupyter notebook extension.

%package     -n jupyter-ipyevents-jupyterlab
Version:        %{labver}
Summary:        A custom ipython widget for returning mouse and keyboard events
Requires:       jupyter-jupyterlab
Requires:       python3-ipyevents = %{mainver}

%description -n jupyter-ipyevents-jupyterlab
ipyevents provides a custom widget for returning mouse and keyboard 
events to Python. Use it to:

  * add keyboard shortcuts to an existing widget.
  * react to the user clicking on an image.
  * install callbacks on arbitrary mouse and keyboard events.

This package provides the JupyterLab extension.

%prep
%setup -q -c -T
unzip %{SOURCE0} 'ipyevents/*'
find ipyevents/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
zip -r %{SOURCE0} ipyevents
rm -rf ipyevents

%build
# Not Needed

%install
pip%{python3_bin_suffix} install --root=%{buildroot} %{SOURCE0}

%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix} 
cp %{buildroot}%{python3_sitelib}/ipyevents-%{mainver}.dist-info/LICENSE.md .

%files %{python_files}
%license %{python3_sitelib}/ipyevents-%{mainver}.dist-info/LICENSE.md
%{python3_sitelib}/ipyevents-%{mainver}.dist-info/
%{python3_sitelib}/ipyevents/

%files -n jupyter-ipyevents
%license LICENSE.md
%config %{_jupyter_nb_notebook_confdir}/ipyevents.json
%{_jupyter_nbextension_dir}/ipyevents/

%files -n jupyter-ipyevents-jupyterlab
%license LICENSE.md
%{_jupyter_labextensions_dir}/ipyevents-%{labver}.tgz

%changelog
