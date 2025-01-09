#
# spec file for package python-opentelemetry-instrumentation-fastapi
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-opentelemetry-instrumentation-fastapi%{?psuffix}
Version:        0.50b0
Release:        0
Summary:        OpenTelemetry FastAPI Instrumentation
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-fastapi
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry_instrumentation_fastapi/opentelemetry_instrumentation_fastapi-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module fastapi >= 0.58}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module opentelemetry-instrumentation-fastapi == %{version}}
BuildRequires:  %{python_module opentelemetry-test-utils == %{version}}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-api >= 1.12}
BuildRequires:  %{python_module opentelemetry-instrumentation == %{version}}
BuildRequires:  fdupes
Requires:       python-opentelemetry-api >= 1.12
Requires:       python-opentelemetry-instrumentation == %{version}
Requires:       python-opentelemetry-instrumentation-asgi == %{version}
Requires:       python-opentelemetry-semantic-conventions == %{version}
Requires:       python-opentelemetry-util-http == %{version}
BuildArch:      noarch
%python_subpackages

%description
This library provides automatic and manual instrumentation of FastAPI web frameworks,
instrumenting http requests served by applications utilizing the framework.

Auto-instrumentation using the opentelemetry-instrumentation package is also supported.

%prep
%setup -q -n opentelemetry_instrumentation_fastapi-%{version}

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
%{python_sitelib}/opentelemetry/instrumentation/fastapi
%{python_sitelib}/opentelemetry_instrumentation_fastapi-%{version}.dist-info
%endif

%changelog
