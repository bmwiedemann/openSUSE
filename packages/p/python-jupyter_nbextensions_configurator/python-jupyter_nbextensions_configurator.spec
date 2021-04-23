#
# spec file for package python-jupyter_nbextensions_configurator
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter_nbextensions_configurator
Version:        0.4.1
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
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module traitlets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-jupyter_contrib_core >= 0.3.3
Requires:       python-jupyter_core
Requires:       python-notebook >= 4.0
Requires:       python-tornado
Requires:       python-traitlets
Recommends:     jupyter-jupyter_nbextensions_configurator = %{version}
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
Requires:       jupyter-notebook >= 4.0
Requires:       python3-jupyter_nbextensions_configurator = %{version}

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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/jupyter-nbextensions_configurator enable --user

for f in ~/.jupyter/nbconfig/*.json ; do
    tdir=$( basename -s .json ${f} )
    install -Dm 644 ${f} %{buildroot}%{_jupyter_nb_confdir}/${tdir}.d/nbextensions_configurator.json
done

%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{_jupyter_confdir}}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jupyter_nbextensions_configurator-%{version}-py*.egg-info
%{python_sitelib}/jupyter_nbextensions_configurator/

%files -n jupyter-jupyter_nbextensions_configurator
%license LICENSE.txt
%{_bindir}/jupyter-nbextensions_configurator
%config %{_jupyter_nb_notebook_confdir}/nbextensions_configurator.json
%config %{_jupyter_nb_tree_confdir}/nbextensions_configurator.json

%changelog
