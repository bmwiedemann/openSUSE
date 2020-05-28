#
# spec file for package python-dash
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
Name:           python-dash
Version:        1.11.0
Release:        0
Summary:        Python framework for building reactive web-apps
License:        MIT
URL:            https://github.com/plotly/dash
Source:         https://files.pythonhosted.org/packages/source/d/dash/dash-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0.2
Requires:       python-Flask-Compress
# dash/testing/dash_page.py
Requires:       python-beautifulsoup4
Requires:       python-dash-core-components >= 1.9.1
Requires:       python-dash-html-components >= 1.0.3
Requires:       python-dash-renderer >= 1.4.0
Requires:       python-dash-table >= 4.6.2
Requires:       python-future
# needed for dash/testing/browser.py
Requires:       python-percy
Requires:       python-plotly
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 1.0.2}
BuildRequires:  %{python_module Flask-Compress}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module dash-core-components >= 1.9.1}
BuildRequires:  %{python_module dash-html-components >= 1.0.3}
BuildRequires:  %{python_module dash-renderer >= 1.4.0}
BuildRequires:  %{python_module dash-table >= 4.6.2}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module percy}
BuildRequires:  %{python_module plotly}
# /SECTION
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

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/dash-generate-components
%python_alternative %{_bindir}/renderer
%{python_sitelib}/dash
%{python_sitelib}/dash-%{version}-py*.egg-info

%changelog
