#
# spec file for package python-anywidget
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define distver 0.9.21
Name:           python-anywidget
Version:        0.9.21
Release:        0
Summary:        Custom jupyter widgets made easy
License:        MIT
URL:            https://github.com/manzt/anywidget
Source:         https://files.pythonhosted.org/packages/source/a/anywidget/anywidget-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.6.0}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module msgspec}
BuildRequires:  %{python_module psygnal >= 0.8.1}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 4.2.0}
BuildRequires:  %{python_module watchfiles}
# /SECTION
BuildRequires:  fdupes
Requires:       python-ipywidgets >= 7.6.0
Requires:       python-psygnal >= 0.8.1
Requires:       python-typing-extensions >= 4.2.0
Suggests:       python-comm >= 0.1.0
Suggests:       python-watchfiles >= 0.18.0
Provides:       python-anywidget = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Custom jupyter widgets made easy

- create widgets **without complicated cookiecutter templates**
- **publish to PyPI** like any other Python package
- prototype **within** `.ipynb` or `.py` files
- run in **Jupyter**, **JupyterLab**, **Google Colab**, **VSCode**, and more
- develop with **instant HMR**, like modern web frameworks

%package     -n jupyter-anywidget
Summary:        Custom jupyter widgets made easy
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       (jupyter-notebook or jupyter-nbclassic)
Requires:       python3dist(anywidget) >= %{distver}
Suggests:       python3-anywidget

%description -n jupyter-anywidget
- create widgets **without complicated cookiecutter templates**
- **publish to PyPI** like any other Python package
- prototype **within** `.ipynb` or `.py` files
- run in **Jupyter**, **JupyterLab**, **Google Colab**, **VSCode**, and more
- develop with **instant HMR**, like modern web frameworks

This package provides the jupyter notebook extensions.

%prep
%autosetup -p1 -n anywidget-%{version}
# Different layout in sdist than in repository
sed -i "s|../packages/anywidget/|../anywidget/labextension/|" tests/test_widget.py

%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/anywidget
%{python_sitelib}/anywidget-%{version}.dist-info

%files -n jupyter-anywidget
%doc README.md
%license LICENSE
%{_jupyter_prefix}/labextensions/anywidget
%{_jupyter_nbextension_dir}/anywidget
%_jupyter_config %{_jupyter_nb_notebook_confdir}/anywidget.json

%changelog
