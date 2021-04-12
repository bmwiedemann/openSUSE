#
# spec file for package python-dash-renderer
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dash-renderer
Version:        1.9.1
Release:        0
Summary:        Front-end component renderer for Dash
License:        MIT
URL:            https://github.com/plotly/dash/tree/dev/dash-renderer
Source:         https://files.pythonhosted.org/packages/source/d/dash_renderer/dash_renderer-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/plotly/dash/dev/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Front-end component renderer for Dash.

%prep
%setup -q -n dash_renderer-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no python tests available, js testing is hard.
# %%check

%files %{python_files}
%license LICENSE
%{python_sitelib}/dash_renderer
%{python_sitelib}/dash_renderer-%{version}-py*.egg-info

%changelog
