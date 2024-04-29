#
# spec file for package python-trio-typing
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
Name:           python-trio-typing
Version:        0.10.0
Release:        0
Summary:        Static type checking support for Trio and related projects
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/trio-typing
Source:         https://files.pythonhosted.org/packages/source/t/trio-typing/trio-typing-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module mypy_extensions >= 0.4.2}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module trio >= 0.16.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-async_generator
Requires:       python-importlib-metadata
Requires:       python-mypy_extensions >= 0.4.2
Requires:       python-packaging
Requires:       python-trio >= 0.16.0
Requires:       python-typing_extensions >= 3.7.4
Suggests:       python-mypy >= 1.0
BuildArch:      noarch
%python_subpackages

%description
Static type checking support for Trio and related projects

%prep
%autosetup -p1 -n trio-typing-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -p trio_typing._tests.datadriven --pyargs trio_typing

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/trio_typing
%{python_sitelib}/trio_typing-%{version}.dist-info
%{python_sitelib}/async_generator-stubs
%{python_sitelib}/outcome-stubs
%{python_sitelib}/trio-stubs

%changelog
