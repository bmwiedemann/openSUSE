#
# spec file for package python-jupyter_nbextensions_configurator
#
# Copyright (c) 2023 SUSE LLC
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


%define         skip_python2 1
Name:           python-jupyter_nbextensions_configurator
Version:        0.6.1
Release:        0
Summary:        Configuration interfaces for nbextensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-contrib/jupyter_nbextensions_configurator
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_nbextensions_configurator/jupyter_nbextensions_configurator-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove_nose.patch bsc#[0-9]+ mcepl@suse.com
# port the test suite to pytest (from nose)
Patch0:         remove_nose.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module jupyter_contrib_core >= 0.3.3}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module notebook >= 6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module traitlets}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyter_nbextensions_configurator = %{version}
Requires:       python-PyYAML
Requires:       python-jupyter_contrib_core >= 0.3.3
Requires:       python-jupyter_core
Requires:       python-notebook >= 6
Requires:       python-tornado
Requires:       python-traitlets
BuildArch:      noarch

%python_subpackages

%description
The jupyter_nbextensions_configurator jupyter server extension provides
graphical user interfaces for configuring which nbextensions are enabled (load
automatically for every notebook), and display their readme files.
In addition, for extensions which include an appropriate yaml descriptor file,
the interface also provides controls to configure the extensions' options.

This package provides the python interface.

%package     -n jupyter-jupyter_nbextensions_configurator
Summary:        Configuration interfaces for nbextensions
Group:          Development/Languages/Python
Requires:       jupyter-jupyter_contrib_core >= 0.3.3
Requires:       jupyter-jupyter_core
Requires:       jupyter-notebook >= 6
# any flavor is okay
Requires:       (%(echo "%{python_module jupyter_nbextensions_configurator = %{version}@or@}" | sed "s/@or@/ or /g" | sed 's/ or\s*$//'))

%description -n jupyter-jupyter_nbextensions_configurator
The jupyter_nbextensions_configurator jupyter server extension provides
graphical user interfaces for configuring which nbextensions are enabled (load
automatically for every notebook), and display their readme files.
In addition, for extensions which include an appropriate yaml descriptor file,
the interface also provides controls to configure the extensions' options.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_nbextensions_configurator-%{version}
%autopatch -p1

sed -i 's/\r$//' LICENSE.txt
sed -i 's/\r$//' LICENSE.txt
sed -i 's|/usr/bin/env python|%{__python3}|' scripts/jupyter-nbextensions_configurator

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
# no geckodriver for selenium tests, no jupyterhub
%pytest --ignore tests/test_nbextensions_configurator.py --ignore tests/test_jupyterhub.py

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jupyter_nbextensions_configurator-%{version}.dist-info
%{python_sitelib}/jupyter_nbextensions_configurator/

%files -n jupyter-jupyter_nbextensions_configurator
%license LICENSE.txt
%{_bindir}/jupyter-nbextensions_configurator
%_jupyter_config %{_jupyter_servextension_confdir}/jupyter_nbextensions_configurator.json
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyter_nbextensions_configurator.json
%_jupyter_config %{_jupyter_nb_tree_confdir}/jupyter_nbextensions_configurator.json

%changelog
