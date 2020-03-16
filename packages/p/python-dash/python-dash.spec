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
Version:        1.9.1
Release:        0
Summary:        Python framework for building reactive web-apps
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/plotly/dash
Source:         https://files.pythonhosted.org/packages/source/d/dash/dash-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.12
Requires:       python-Flask-Compress
Requires:       python-plotly
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 0.12}
BuildRequires:  %{python_module Flask-Compress}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/dash-generate-components
%python3_only %{_bindir}/renderer
%{python_sitelib}/dash
%{python_sitelib}/dash-%{version}-py*.egg-info

%changelog
