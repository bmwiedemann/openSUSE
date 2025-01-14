#
# spec file for package python-ipyevents
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python39 1
Name:           python-ipyevents
Version:        2.0.2
Release:        0
Summary:        A custom ipython widget for returning mouse and keyboard events
License:        BSD-3-Clause
URL:            https://github.com/mwcraig/ipyevents
# The Github archive has the test file, but does not bundle the extensions
Source0:        https://github.com/mwcraig/ipyevents/archive/%{version}.tar.gz#/ipyevents-%{version}-gh.tar.gz
# Only the (pure) wheel bundles both extensions
Source1:        https://files.pythonhosted.org/packages/py3/i/ipyevents/ipyevents-%{version}-py3-none-any.whl
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyevents = %{version}
Requires:       python-ipywidgets >= 7.6.0
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
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipyevents) = %{version}
Suggests:       python3-ipyevents

%description -n jupyter-ipyevents
ipyevents provides a custom widget for returning mouse and keyboard
events to Python. Use it to:

  * add keyboard shortcuts to an existing widget.
  * react to the user clicking on an image.
  * install callbacks on arbitrary mouse and keyboard events.

This package provides the tools and jupyter notebook extension.

%package     -n jupyter-ipyevents-jupyterlab
Summary:        A custom ipython widget for returning mouse and keyboard events
Requires:       jupyter-jupyterlab
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipyevents) = %{version}
Suggests:       python3-ipyevents

%description -n jupyter-ipyevents-jupyterlab
ipyevents provides a custom widget for returning mouse and keyboard
events to Python. Use it to:

  * add keyboard shortcuts to an existing widget.
  * react to the user clicking on an image.
  * install callbacks on arbitrary mouse and keyboard events.

This package provides the JupyterLab extension.

%prep
%setup -q -n ipyevents-%{version}

%build
# we install the (pure) wheel directly...

%install
%pyproject_install %{SOURCE1}

%{jupyter_move_config}
%python_expand find %{buildroot}%{$python_sitelib}/ipyevents/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
find %{buildroot}%{_prefix} -path ipyevents-%{version}.dist-info/LICENSE.md -exec cp {} . ';' -quit

%check
%pytest

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/ipyevents-%{version}*-info/
%{python_sitelib}/ipyevents/

%files -n jupyter-ipyevents
%license LICENSE.md
%_jupyter_config %{_jupyter_nb_notebook_confdir}/ipyevents.json

%files -n jupyter-ipyevents-jupyterlab
%license LICENSE.md
%{_jupyter_labextensions_dir3}/ipyevents

%changelog
