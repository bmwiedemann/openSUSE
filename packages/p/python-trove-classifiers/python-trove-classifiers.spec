#
# spec file for package python-trove-classifiers
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
Name:           python-trove-classifiers%{?psuffix}
Version:        2024.10.21.16
Release:        0
Summary:        Canonical source for classifiers on PyPI
License:        Apache-2.0
URL:            https://github.com/pypa/trove-classifiers
Source:         https://files.pythonhosted.org/packages/source/t/trove-classifiers/trove_classifiers-%{version}.tar.gz
BuildRequires:  %{python_module calver}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
Classifiers categorize projects per PEP 301. Use this package to validate classifiers in packages for PyPI upload or download.

%prep
%setup -q -n trove_classifiers-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/trove_classifiers
%{python_sitelib}/trove_classifiers-%{version}.dist-info
%endif

%changelog
