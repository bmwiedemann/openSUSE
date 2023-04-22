#
# spec file for package python-validate-pyproject
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


%{?sle15_python_module_pythons}
Name:           python-validate-pyproject
Version:        0.9
Release:        0
Summary:        Validation library and CLI tool for checking on 'pyprojecttoml'
License:        MPL-2.0 and MIT and BSD-3-Clause
URL:            https://github.com/abravalheri/validate-pyproject/
Source:         https://files.pythonhosted.org/packages/source/v/validate-pyproject/validate-pyproject-0.9.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
%if 0%{python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
%if 0%{python_version_nodots} < 37
Requires:       python-importlib-resources
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-validate_pyproject = %{version}-%{release}
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli >= 1.2.1 if %python-base < 3.11}
BuildRequires:  %{python_module packaging >= 20.4}
BuildRequires:  %{python_module trove-classifiers >= 2021.10.20}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  %{python_module importlib-resources if %python-base < 3.7}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Validation library and CLI tool for checking on 'pyproject.toml' files using JSON Schema

%prep
%setup -q -n validate-pyproject-%{version}
sed -i '/--cov/d' setup.cfg

%build
# have to use PEP517: gh#abravalheri/validate-pyproject#52
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/validate-pyproject
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not downloaded"

%post
%python_install_alternative validate-pyproject

%postun
%python_uninstall_alternative validate-pyproject


%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/validate-pyproject
%{python_sitelib}/validate_pyproject
%{python_sitelib}/validate_pyproject-%{version}*-info

%changelog
