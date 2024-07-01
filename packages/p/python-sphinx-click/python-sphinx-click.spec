#
# spec file for package python-sphinx-click
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-sphinx-click
Version:        6.0.0
Release:        0
Summary:        Sphinx extension that automatically documents click applications
License:        MIT
URL:            https://github.com/stephenfin/sphinx-click
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_click/sphinx_click-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
BuildRequires:  python-rpm-generators
%{?python_enable_dependency_generator}
%python_subpackages

%description
A Sphinx plugin that allows to automatically extract documentation from click-based applications and include it in documentation.

%prep
%autosetup -p1 -n sphinx_click-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/sphinx_click
%{python_sitelib}/sphinx_click-%{version}.dist-info

%changelog
