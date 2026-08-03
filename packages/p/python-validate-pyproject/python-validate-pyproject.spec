#
# spec file for package python-validate-pyproject
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-validate-pyproject
Version:        0.25
Release:        0
Summary:        Validation library and CLI tool for checking on 'pyprojecttoml'
License:        BSD-3-Clause AND MIT AND MPL-2.0
URL:            https://github.com/abravalheri/validate-pyproject/
Source:         https://files.pythonhosted.org/packages/source/v/validate-pyproject/validate_pyproject-%{version}.tar.gz
BuildRequires:  %{python_module fastjsonschema >= 2.16.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 7.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-fastjsonschema >= 2.16.2
Provides:       python-validate_pyproject = %{version}-%{release}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  %{python_module importlib-resources if %python-base < 3.7}
BuildRequires:  %{python_module packaging >= 24.2}
BuildRequires:  %{python_module pytest >= 8.3.3}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module tomli >= 1.2.1 if %python-base < 3.11}
BuildRequires:  %{python_module trove-classifiers >= 2021.10.20}
# /SECTION
%python_subpackages

%description
Validation library and CLI tool for checking on 'pyproject.toml' files using JSON Schema

%prep
%setup -q -n validate_pyproject-%{version}
sed -i '/--cov --cov-report term-missing/d' setup.cfg

%build
# have to use PEP517: gh#abravalheri/validate-pyproject#52
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/validate-pyproject
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignore test_pre_compile and test_examples because they require
# network access to download JSON schemas.
# test_cache_open_url also requires network access
donttest="test_cache_open_url or downloaded"
%pytest --ignore tests/test_pre_compile.py --ignore tests/test_examples.py -k "not ($donttest)"

%post
%python_install_alternative validate-pyproject

%postun
%python_uninstall_alternative validate-pyproject

%pre
%python_libalternatives_reset_alternative validate-pyproject

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/validate-pyproject
%{python_sitelib}/validate_pyproject
%{python_sitelib}/validate_pyproject-%{version}.dist-info

%changelog
