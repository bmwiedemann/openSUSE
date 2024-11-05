#
# spec file for package python-sphinx-design
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
Name:           python-sphinx-design
Version:        0.6.1
Release:        0
Summary:        A sphinx extension for designing beautiful, view size responsive web components
License:        MIT
URL:            https://github.com/executablebooks/sphinx-design
Source:         https://github.com/executablebooks/sphinx-design/archive/refs/tags/v%{version}.tar.gz#/sphinx-design-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 6}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module myst-parser >= 2}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx >= 6
Suggests:       python-myst-parser >= 2
Suggests:       python-defusedxml
Suggests:       python-furo >= 2024.7.18
Suggests:       python-pydata-sphinx-theme >= 0.15.2
Suggests:       python-sphinx-rtd-theme >= 2.0
Suggests:       python-sphinx-book-theme >= 1.1
Suggests:       python-sphinx-immaterial >= 0.12.2
BuildArch:      noarch
%python_subpackages

%description
A sphinx extension for designing beautiful, view size responsive web components.

Created with inspiration from Bootstrap (v5), Material Design and Material-UI design frameworks.

%prep
%autosetup -p1 -n sphinx-design-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/sphinx_design
%{python_sitelib}/sphinx_design-%{version}.dist-info

%changelog
