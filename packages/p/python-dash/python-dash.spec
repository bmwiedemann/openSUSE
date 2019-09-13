#
# spec file for package python-dash
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-dash
Version:        0.21.1
Release:        0
# For the license file
%define tag     ff93d2c4331a576b445be87bb3b77576f18b030a
Summary:        Python framework for building reactive web-apps
License:        MIT
Group:          Development/Languages/Python
Url:            https://plot.ly/dash
Source:         https://files.pythonhosted.org/packages/source/d/dash/dash-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/plotly/dash/%{tag}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 0.12}
BuildRequires:  %{python_module Flask-Compress}
BuildRequires:  %{python_module plotly}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Flask >= 0.12
Requires:       python-Flask-Compress
Requires:       python-plotly
BuildArch:      noarch

%python_subpackages

%description
Dash is a Python framework for building analytical web applications.
No JavaScript required.

Build on top of Plotly.js, React, and Flask, Dash ties modern UI
elements like dropdowns, sliders, and graphs directly to your
analytical python code.

%prep
%setup -q -n dash-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
