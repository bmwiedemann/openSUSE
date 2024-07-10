#
# spec file for package python-dash
#
# Copyright (c) 2022 SUSE LLC
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


# We can't test currenty, see below.
%bcond_with test
%define skip_python39 1
%define distver 2.16.1
Name:           python-dash
Version:        2.16.1
Release:        0
Summary:        Python framework for building reactive web-apps
License:        MIT
URL:            https://github.com/plotly/dash
# PyPI package does not contain unit tests. GitHub does, but we don't test right now
Source:         https://files.pythonhosted.org/packages/source/d/dash/dash-%{version}.tar.gz
Source99:       python-dash.rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module Flask >= 1.0.4}
BuildRequires:  %{python_module dash-core-components = 2.0.0}
BuildRequires:  %{python_module dash-html-components = 2.0.0}
BuildRequires:  %{python_module dash-table = 5.0.0}
BuildRequires:  %{python_module percy}
BuildRequires:  %{python_module plotly >= 5.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module typing-extensions >= 4.1.1}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module retrying}
BuildRequires:  %{python_module nest-asyncio}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  jupyter-rpm-macros
Requires:       python-Flask >= 1.0.4
Requires:       python-Werkzeug
Requires:       python-importlib-metadata
Requires:       python-typing-extensions >= 4.1.1
Requires:       python-requests
Requires:       python-retrying
Requires:       python-nest-asyncio
Requires:       python-setuptools
Requires:       python-dash-core-components = 2.0.0
Requires:       python-dash-html-components = 2.0.0
Requires:       python-dash-table = 5.0.0
Requires:       python-plotly >= 5.0.0
Requires:       jupyter-dash = %{version}-%{release}
# SECTION testing extras
# dash/testing/dash_page.py
Requires:       python-beautifulsoup4
# needed for dash/testing/browser.py
Requires:       python-percy
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-sugar}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module waitress}
BuildRequires:  nodejs
%endif
%python_subpackages

%description
Dash is a Python framework for building analytical web applications.
No JavaScript required.

Build on top of Plotly.js, React, and Flask, Dash ties modern UI
elements like dropdowns, sliders, and graphs directly to your
analytical python code.

%package -n jupyter-dash
Summary: Jupyter configuration for python-dash
Requires: python3dist(dash) = %{distver}
Suggests: python3-dash

%description -n jupyter-dash

Dash is a Python framework for building analytical web applications.

This package provides the jupyter notebook and jupyterlab configuration
for python-dash


%prep
%setup -q -n dash-%{version}
sed -i -e '/^#!\//, 1d' dash/extract-meta.js
chmod -x dash/extract-meta.js
find . -name .gitkeep -delete

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/renderer
%python_clone -a %{buildroot}%{_bindir}/dash-generate-components
%python_clone -a %{buildroot}%{_bindir}/dash-update-components
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
# Testing needs npm install from network and packages (e.g. flask_talisman) which we don't have.
%pytest
%endif

%post
%python_install_alternative renderer
%python_install_alternative dash-generate-components
%python_install_alternative dash-update-components

%postun
%python_uninstall_alternative renderer
%python_uninstall_alternative dash-generate-components
%python_uninstall_alternative dash-update-components

%files -n jupyter-dash
%doc README.md
%license LICENSE
%{?_jupyter_config} %{_jupyter_nb_notebook_confdir}/dash.json
%{_jupyter_labextensions_dir}/dash-jupyterlab.tgz
%{_jupyter_nbextension_dir}/dash/

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/dash-generate-components
%python_alternative %{_bindir}/dash-update-components
%python_alternative %{_bindir}/renderer
%{python_sitelib}/dash
%{python_sitelib}/dash-%{version}*-info

%changelog
