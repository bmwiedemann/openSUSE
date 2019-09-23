#
# spec file for package python-jupyter-contrib-nbextensions
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
Name:           python-jupyter-contrib-nbextensions
Version:        0.5.1
Release:        0
Summary:        A collection of Jupyter nbextensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython-contrib/jupyter_contrib_nbextensions
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_contrib_nbextensions/jupyter_contrib_nbextensions-%{version}.tar.gz
BuildRequires:  %{python_module nbconvert >= 4.2}
BuildRequires:  %{python_module notebook >= 4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jupyter_nbextensions_configurator >= 0.2.8
Requires:       python-jupyter_contrib_core >= 0.3.3
Requires:       python-jupyter_core
Requires:       python-jupyter_highlight_selected_word >= 0.2
Requires:       python-jupyter_latex_envs >= 1.3.8
Requires:       python-nbconvert >= 4.2
Requires:       python-notebook >= 4.0
Requires:       python-PyYAML
Requires:       python-ipython_genutils
Requires:       python-lxml >= 3.8.0
Requires:       python-tornado
Requires:       python-traitlets >= 4.1
Recommends:     python-nbformat
Recommends:     python-requests
Provides:       python-jupyter_contrib_nbextensions = %{version}
Obsoletes:      python-jupyter_contrib_nbextensions < %{version}
Requires:       jupyter-jupyter-contrib-nbextensions = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyter_contrib_core >= 0.3.3}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module jupyter_highlight_selected_word >= 0.2}
BuildRequires:  %{python_module jupyter_latex_envs >= 1.3.8}
BuildRequires:  %{python_module jupyter_nbextensions_configurator >= 0.2.8}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module lxml >= 3.8.0}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module traitlets >= 4.1}
%endif

%python_subpackages

%description
Contains a collection of extensions that add functionality to the Jupyter
notebook. These extensions are mostly written in Javascript, and are loaded
locally in the browser.

Please Note: Because a large number of extensions are provided, extensions
are not enabled automatically. Please use the nbextensions_configurator
extension to enable or disable them individually. It is pulled in as a
dependency of this package

This package provides the python interface.

%package     -n jupyter-jupyter-contrib-nbextensions
Summary:        Libraries and Languages for Jupyter
Group:          Development/Languages/Python
Requires:       jupyter-jupyter_contrib_core >= 0.3.3
Requires:       jupyter-jupyter_highlight_selected_word >= 0.2
Requires:       jupyter-jupyter_latex_envs >= 1.3.8
Requires:       jupyter-jupyter_nbextensions_configurator >= 0.2.8
Requires:       jupyter-jupyter_core
Requires:       jupyter-notebook >= 4.0
Requires:       python3-jupyter-contrib-nbextensions = %{version}

%description -n jupyter-jupyter-contrib-nbextensions
Contains a collection of extensions that add functionality to the Jupyter
notebook. These extensions are mostly written in Javascript, and are loaded
locally in the browser.

Please Note: Because a large number of extensions are provided, extensions
are not enabled automatically. Please use the nbextensions_configurator
extension to enable or disable them individually. It is pulled in as a
dependency of this package

This package provides the jupyter components.

%prep
%setup -q -n jupyter_contrib_nbextensions-%{version}

%build
%python_build

%install
%python_install
find %{buildroot} -name '*.js' -exec chmod a-x {} \;
find %{buildroot} -name '*.css' -exec chmod a-x {} \;
find %{buildroot} -name '*.tpl' -exec chmod a-x {} \;
%python_expand %fdupes %{buildroot}%{$python_sitelib}

PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/jupyter-contrib-nbextension install --nbextensions=%{buildroot}%{_jupyter_nbextension_dir} --only-files

# These are provided by separate packages
rm -r %{buildroot}%{_jupyter_nbextension_dir}/highlight_selected_word/
rm -r %{buildroot}%{_jupyter_nbextension_dir}/latex_envs/

%fdupes %{buildroot}%{_jupyter_nbextension_dir}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc CHANGELOG.md README.md
%license COPYING.rst
%{python_sitelib}/jupyter_contrib_nbextensions/
%{python_sitelib}/jupyter_contrib_nbextensions-%{version}-py*.egg-info

%files -n jupyter-jupyter-contrib-nbextensions
%license COPYING.rst
%{_bindir}/jupyter-contrib-nbextension
%{_jupyter_nbextension_dir}/*/

%changelog
