#
# spec file for package python-dash
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


# We can't test currenty, see below.
%bcond_with test

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-dash
Version:        1.20.0
Release:        0
Summary:        Python framework for building reactive web-apps
License:        MIT
URL:            https://github.com/plotly/dash
# PyPI package does not contain unit tests. GitHub does, but we don't test right now
Source:         https://files.pythonhosted.org/packages/source/d/dash/dash-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 1.0.4}
BuildRequires:  %{python_module Flask-Compress}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module dash-core-components >= 1.16.0}
BuildRequires:  %{python_module dash-html-components >= 1.1.3}
BuildRequires:  %{python_module dash-renderer >= 1.9.1}
BuildRequires:  %{python_module dash-table >= 4.11.3}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module percy}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0.4
Requires:       python-Flask-Compress
# dash/testing/dash_page.py
Requires:       python-beautifulsoup4
Requires:       python-dash-core-components >= 1.16.0
Requires:       python-dash-html-components >= 1.1.3
Requires:       python-dash-renderer >= 1.9.1
Requires:       python-dash-table >= 4.11.3
Requires:       python-future
# needed for dash/testing/browser.py
Requires:       python-percy
Requires:       python-plotly
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-sugar}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
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

%prep
%setup -q -n dash-%{version}
sed -i -e '/^#!\//, 1d' dash/extract-meta.js
# no hardcoded versions
sed -i -e 's:==:>=:g' requires-*txt

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/renderer
%python_clone -a %{buildroot}%{_bindir}/dash-generate-components
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative renderer
%python_install_alternative dash-generate-components

%postun
%python_uninstall_alternative renderer
%python_uninstall_alternative dash-generate-components

%if %{with test}
%check
# Testing needs npm install from network and packages (e.g. flask_talisman) which we don't have.
%pytest
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/dash-generate-components
%python_alternative %{_bindir}/renderer
%{python_sitelib}/dash
%{python_sitelib}/dash-%{version}-py*.egg-info

%changelog
