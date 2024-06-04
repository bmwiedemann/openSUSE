#
# spec file for package python-pydantic
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
Name:           python-pydantic%{psuffix}
Version:        2.7.1
Release:        0
Summary:        Data validation and settings management using python type hinting
License:        MIT
URL:            https://github.com/pydantic/pydantic
Source:         https://github.com/pydantic/pydantic/archive/v%{version}.tar.gz#/pydantic-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pydantic/pydantic#9527
Patch0:         support-pytest-8.patch
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module email-validator >= 2.0}
BuildRequires:  %{python_module pydantic == %{version}}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-examples}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv >= 0.10.4}
%endif
Requires:       python-annotated-types >= 0.4.0
%if 0%{?python_version_nodots} < 310
Requires:       python-eval-type-backport
%endif
Requires:       python-pydantic-core == 2.18.2
Requires:       python-typing_extensions >= 4.6.1
Suggests:       python-email-validator >= 2.0
BuildArch:      noarch
%python_subpackages

%description
Data validation and settings management using Python type hinting.

%prep
%autosetup -p1 -n pydantic-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md HISTORY.md
%{python_sitelib}/pydantic
%{python_sitelib}/pydantic-%{version}.dist-info
%endif

%changelog
