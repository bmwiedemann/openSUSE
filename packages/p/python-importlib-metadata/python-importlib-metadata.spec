#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-importlib-metadata%{psuffix}
Version:        5.1.0
Release:        0
Summary:        Read metadata from Python packages
License:        Apache-2.0
URL:            http://importlib-metadata.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/i/importlib_metadata/importlib_metadata-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zipp >= 0.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zipp >= 0.5
%if %{python_version_nodots} < 38
Requires:       python-typing_extensions >= 3.6.4
%endif
Provides:       python-importlib_metadata = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module importlib_resources >= 1.3 if %python-base < 3.9}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pep517}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module typing_extensions >= 3.6.4 if %python-base < 3.8}
%endif
%python_subpackages

%description
This package supplies third-party access to the functionality of
importlib.metadata including improvements added to subsequent Python versions.

%prep
%autosetup -p1 -n importlib_metadata-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# no pytest_perf available
%pytest --ignore exercises.py
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/importlib_metadata
%{python_sitelib}/importlib_metadata-%{version}*-info
%endif

%changelog
