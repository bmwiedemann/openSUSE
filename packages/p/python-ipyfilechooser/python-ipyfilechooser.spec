#
# spec file for package python-ipyfilechooser
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-ipyfilechooser
Version:        0.6.0
Release:        0
Summary:        File chooser widget for use in Jupyter/IPython
License:        MIT
URL:            https://github.com/crahan/ipyfilechooser
Source:         https://files.pythonhosted.org/packages/source/i/ipyfilechooser/ipyfilechooser-%{version}.tar.gz
Source1:        https://github.com/crahan/ipyfilechooser/raw/v%{version}/ipyfilechooser_examples.ipynb
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-ipywidgets
BuildArch:      noarch
%python_subpackages

%description
Python file chooser widget for use in Jupyter/IPython in conjunction with ipywidgets

%prep
%setup -q -n ipyfilechooser-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Cell 6 has a custom path
%pytest --nbval %{SOURCE1} -k "not 6"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipyfilechooser
%{python_sitelib}/ipyfilechooser-%{version}*-info

%changelog
