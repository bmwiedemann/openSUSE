#
# spec file for package python-importlib-metadata
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
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-importlib-metadata%{psuffix}
Version:        8.5.0
Release:        0
Summary:        Read metadata from Python packages
License:        Apache-2.0
URL:            https://importlib-metadata.readthedocs.io/
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
Provides:       python-importlib_metadata = %{version}
BuildArch:      noarch
Requires:       (python-typing_extensions >= 3.6.4 if python-base < 3.8)
%if %{with test}
BuildRequires:  %{python_module importlib_resources >= 1.3 if %python-base < 3.9}
BuildRequires:  %{python_module jaraco.test}
BuildRequires:  %{python_module packaging}
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
# no pytest_perf available (gh#python/importlib_metadata#490)
# skipping tests because of gh#python/importlib_metadata#509
skip_tests="test_packages_distributions_example or test_packages_distributions_example2"
skip_tests+=" or test_case_insensitive or test_files or test_missing_metadata"
skip_tests+=" or test_one_distribution or test_zip_entry_points or test_zip_version"
skip_tests+=" or test_case_insensitive or test_files or test_missing_metadata"
skip_tests+=" or test_normalized_name or test_one_distribution or test_zip_entry_points"
skip_tests+=" or test_zip_version"
%pytest --ignore exercises.py -k "not (${skip_tests})"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/importlib_metadata
%{python_sitelib}/importlib_metadata-%{version}*-info
%endif

%changelog
