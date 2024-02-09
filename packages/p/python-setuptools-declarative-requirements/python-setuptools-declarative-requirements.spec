#
# spec file for package python-setuptools-declarative-requirements
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-setuptools-declarative-requirements%{psuffix}
Version:        1.3.0
Release:        0
Summary:        File support for setuptools declarative setup.cfg
License:        Apache-2.0
URL:            https://github.com/s0undt3ch/setuptools-declarative-requirements
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-declarative-requirements/setuptools-declarative-requirements-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-toml
Requires:       python-wheel
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pypiserver}
BuildRequires:  %{python_module pytest-shell-utilities}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module virtualenv}
%endif
# /SECTION
%python_subpackages

%description
File support for setuptools declarative setup.cfg.

%prep
%setup -q -n setuptools-declarative-requirements-%{version}
sed -i 's/"setuptools>=[0-9]*"/"setuptools"/g' tests/conftest.py

%build
%pyproject_wheel

%if %{with test}
%check
# sdist test tries to contact pypi.org
%pytest -k 'not sdist'
%else

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/declarative_requirements
%{python_sitelib}/setuptools_declarative_requirements-%{version}.dist-info
%endif

%changelog
