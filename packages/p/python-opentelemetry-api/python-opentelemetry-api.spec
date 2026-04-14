#
# spec file for package python-opentelemetry-api
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-opentelemetry-api%{?psuffix}
Version:        1.41.0
Release:        0
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/master/opentelemetry-api
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-api/opentelemetry_api-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module importlib-metadata >= 6.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing-extensions >= 4.5.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-importlib-metadata >= 6.0
Requires:       python-typing-extensions >= 4.5.0
%if %{with test}
BuildRequires:  %{python_module opentelemetry-api = %{version}}
BuildRequires:  %{python_module opentelemetry-test-utils = 0.62b0}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
OpenTelemetry Python API

%prep
%setup -q -n opentelemetry_api-%{version}

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
%doc README.rst
%license LICENSE
%{python_sitelib}/opentelemetry
%{python_sitelib}/opentelemetry_api-%{version}*-info
%endif

%changelog
